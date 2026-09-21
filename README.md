# 《思维学习理念复习》微课

面向 **VIPTHINK 国内线上少儿数学思维班主任（LP）** 的互动式复习微课。
帮助学员掌握核心思维理论，并能清晰、有说服力地向家长说明思维学习的重要性。

线上地址：https://ruanqiaoyun0-a11y.github.io/cn-lp-thinking-course/

---

## 课程结构（5 章）

| 章 | 主题 | 互动 |
|---|---|---|
| 1 | 什么是数学思维（思维定义 / 数学重要性 / 16 种数学方法 / 枚举法案例） | 3 道测验 |
| 2 | 学习数学思维的好处（五大好处） | 3 道测验 |
| 3 | 为什么必须重视思维培养（政策风向 / 国家战略 / 关键期） | 3 道测验 |
| 4 | 3-12 岁儿童思维发展特点（皮亚杰四阶段 / 幼儿与小学生特点） | 3 道测验 + 阶段速查库 |
| 5 | 家长沟通实战与终极考核（四大说明角度 / 表达示例） | 情境应答演练 4 个 + 填空题 3 道 + AI 家长自由对话 |

素材来源：《思维学习理念》.pptx（25 页 · 益智国内新人训）

## 终极考核

1. **家长说明填空（3 题）**：关键要点关键词作答，答错可重填、不泄题
2. **情境应答演练（4 个场景）**：家长提问 → 学员用自己的话组织回应 → 关键词自检（不给标准答案）
3. **AI 家长自由对话**：与「小宇妈妈」对话 ≥4 轮，AI 从四维综合评分（理论准确性 30 / 说服力 30 / 服务亲和力 25 / 家长视角 15）

## 学习者 UI 红线

- 不显示任何阈值线 / 分数线，但展示实际得分
- 选择题答错可重新作答，且不展示正确答案
- 填空题答错只给知识点提示，不泄题
- 情境演练只给关键词命中提示与复习指引，**不给满分参考答案**
- AI 不可用时自动降级为脚本模拟回复，不报错、不崩页

## 工程结构

```
index.html        单文件交付物（含混淆密钥）
_content.py       单一内容源（章节正文 / 题库 / AI 提示词 / 评分维度）
_build.py         组装 + 校验（章节数、题数、DOM 模板、维度标签、明文密钥扫描）
_build.js         MiMo 密钥 XOR+hex 混淆注入（幂等、--check、不打印）
_server.js        本地静态服务（CDP 测试用）
_cdp_test.js      headless Chrome 全链路 E2E（100 项断言）
_cdp_ai_smoke.js  AI 通路冒烟测试
_run_e2e.sh       一体化 E2E（起服务 → 起 Chrome → 跑测试）
_worker/          Cloudflare Worker 代理（B 档：前端零密钥）
```

## 构建与验证

```bash
python _build.py                 # 组装 index.html + 校验
node _build.js                   # 注入 MiMo 密钥（XOR+hex 混淆）
node _build.js --check           # 检查注入状态
bash _run_e2e.sh                 # 一体化 E2E（100 项断言）
```

## AI 后端

小米 MiMo `mimo-v2.5-pro`，`https://api.xiaomimimo.com/v1/chat/completions`。
- 必带 `thinking: {type:'disabled'}`（否则 content 为空）
- 参数名 `max_completion_tokens`（不是 `max_tokens`）
- 对话 `temperature: 0.75`，评分 `temperature: 0.3`
- 域名白名单 + 100 次/小时限流
