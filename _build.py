# -*- coding: utf-8 -*-
"""
_build.py — 组装 index.html
用法：python _build.py [--check]
  --check  只校验，不写文件
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import _content as C  # noqa: E402

OUT = os.path.join(HERE, 'index.html')
CHECK_ONLY = '--check' in sys.argv


def read(name):
    with open(os.path.join(HERE, name), 'r', encoding='utf-8') as f:
        return f.read()


def build_app_data():
    return {
        'title': C.COURSE_TITLE,
        'lsPrefix': C.LS_PREFIX,
        'orgName': C.ORG_NAME,
        'sections': C.SECTIONS,
        'chapterQuizzes': C.CHAPTER_QUIZZES,
        'finalFills': C.CH5_FILLS,
        'levelLibrary': C.STAGE_LIBRARY,
        'scenarioDrills': C.SCENARIO_DRILLS,
    }


HEAD = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="面向线上少儿数学思维班主任（LP）的《续费全流程实战》互动微课">
<title>{title} · 班主任微课</title>
<style>
{css}
</style>
</head>
'''


def main():
    css = read('_shell.css') + '\n' + read('_additions.css')
    shell = read('_shell.html')
    js = read('_app.tpl.js')
    app = build_app_data()

    # 关键断言：JSON 里若含 </script 会截断 script 标签
    data_json = json.dumps(app, ensure_ascii=False, separators=(',', ':'))
    assert '</script' not in data_json.lower(), 'JSON 中包含 </script，需转义处理'

    html = (
        HEAD.format(title=C.COURSE_TITLE, css=css)
        + shell
        + '\n<!-- ===== 课程数据（JSON） ===== -->\n'
        + '<script id="appDataJson" type="application/json">' + data_json + '</script>\n'
        + '\n<!-- ===== 应用逻辑 ===== -->\n'
        + '<script>\n' + js + '\n</script>\n'
        + '</body>\n</html>\n'
    )

    # ---------- 校验 ----------
    problems = []
    if re.search(r'\{\{[A-Z_]+\}\}', html):
        problems.append('存在未替换的 {{PLACEHOLDER}} 占位符')
    if '<script' not in html or '</script>' not in html:
        problems.append('script 标签缺失')
    if 'quiz-locked-hint' not in html:
        problems.append('缺少串行锁定样式/提示')
    if 'fillQuizContainer5' not in html:
        problems.append('缺少第 5 章填空题挂载点 #fillQuizContainer5')
    if 'levelLibrary' not in html:
        problems.append('缺少第 4 章阶段速查库挂载点 #levelLibrary')
    if 'scenarioDrillContainer' not in html:
        problems.append('缺少情境应答演练挂载点 #scenarioDrillContainer')
    if 'placeholder="MIMO_API_KEY"' in html:
        problems.append('异常：出现密钥占位串')
    if '__MIMO_API_KEY__' in html or 'MIMO_API_KEY' in html:
        problems.append('异常：本课程无 AI 对练，不应出现密钥占位符')
    # 复习课不含 AI 对练，须确认相关挂载点已彻底移除
    for stale_id in ('roleplayContainer', 'finalDialogue', 'finalStartBtn', 'finalMessages', 'finalSystemPrompt', 'scoringPrompt', 'fallbackReplies', 'topicTags'):
        if stale_id in html:
            problems.append('残留 AI 对练相关代码：%s' % stale_id)
    # 章节 / 题目数量：题目 DOM 由 JS 运行时生成，校验生成模板与数据条数
    if "chquiz-' + chIdx + '-' + qi" not in js:
        problems.append('缺少题目 DOM 生成模板')
    if "feedback-chquiz-' + chIdx + '-' + qi" not in js:
        problems.append('缺少题目反馈 DOM 生成模板')
    for i, qs in enumerate(C.CHAPTER_QUIZZES):
        if not isinstance(qs, list):
            problems.append('第 %d 章测验数据格式错误' % (i + 1))
        for qi, q in enumerate(qs):
            if not all(k in q for k in ('q', 'opts', 'correct')):
                problems.append('第 %d 章第 %d 题字段缺失' % (i + 1, qi + 1))
            elif not (0 <= q['correct'] < len(q['opts'])):
                problems.append('第 %d 章第 %d 题 correct 越界' % (i + 1, qi + 1))
    # 填空题校验
    if not C.CH5_FILLS:
        problems.append('缺少第 5 章填空题数据')
    for fi, f in enumerate(C.CH5_FILLS):
        if not all(k in f for k in ('q', 'answer', 'hint')):
            problems.append('第 %d 道填空字段缺失' % (fi + 1))
        elif not f['answer']:
            problems.append('第 %d 道填空没有可接受答案' % (fi + 1))
    # 阶段速查库校验（皮亚杰四阶段）
    if len(C.STAGE_LIBRARY) != 4:
        problems.append('阶段速查库阶段数不为 4（当前 %d）' % len(C.STAGE_LIBRARY))
    for lv in C.STAGE_LIBRARY:
        if not all(k in lv for k in ('level', 'grade', 'position', 'stuck', 'build', 'change')):
            problems.append('速查库 %s 字段缺失' % lv.get('level', '?'))
    # 情境应答演练校验
    if not C.SCENARIO_DRILLS:
        problems.append('缺少情境应答演练数据')
    for di, d in enumerate(C.SCENARIO_DRILLS):
        if not all(k in d for k in ('id', 'title', 'parent', 'angles', 'keywords', 'hint')):
            problems.append('第 %d 个情境演练字段缺失' % (di + 1))
        elif not d['angles']:
            problems.append('第 %d 个情境演练没有说明角度' % (di + 1))
    if 'level-card' not in js:
        problems.append('缺少速查库折叠卡片渲染模板')
    if 'renderScenarioDrills' not in js:
        problems.append('缺少情境应答演练渲染函数')
    if 'submitDrill' not in js:
        problems.append('缺少情境应答演练提交处理函数')
    if 'fillInput-' not in js:
        problems.append('缺少填空题 DOM 生成模板')
    if 'submitFill' not in js:
        problems.append('缺少填空题提交处理函数')
    # 终评维度标签：本课无 AI 对练，须确认旧课的四维评分标签已彻底移除
    for stale in ('流程规范性', '信息准确性', '话题覆盖度', '理论准确性', '服务亲和力'):
        if stale in js:
            problems.append('残留旧课终评维度标签：%s' % stale)
    # 明文密钥
    if re.search(r'sk-[A-Za-z0-9]{20,}', html):
        problems.append('严重：index.html 中出现明文密钥 sk-...')

    print('章节数：', len(C.SECTIONS))
    print('选择题总数：', sum(len(x) for x in C.CHAPTER_QUIZZES))
    print('填空题总数（第 5 章）：', len(C.CH5_FILLS))
    print('阶段速查库：', len(C.STAGE_LIBRARY), '阶段（皮亚杰四阶段）')
    print('情境应答演练：', len(C.SCENARIO_DRILLS), '个场景')
    print('index.html 字节数：', len(html.encode('utf-8')))
    if problems:
        print('\n❌ 校验未通过：')
        for p in problems:
            print('  -', p)
        sys.exit(1)
    print('✅ 校验通过')

    if CHECK_ONLY:
        print('（--check 模式，未写文件）')
        return
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    print('已写出：', OUT)


if __name__ == '__main__':
    main()
