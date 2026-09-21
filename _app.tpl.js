// ============================================================
// 《思维学习理念复习》微课 · 应用逻辑
// 数据从 #appDataJson 读取（JSON），避免转义问题
// ============================================================
const APP = JSON.parse(document.getElementById('appDataJson').textContent);
const courseData = { title: APP.title, sections: APP.sections };
const chapterQuizzes = APP.chapterQuizzes;

// ---------------- 状态 ----------------
const LS_PREFIX = APP.lsPrefix;
let currentSection = 0;
let completedSections = new Set();
let chapterQuizDone = new Array(chapterQuizzes.length).fill(false);
let chapterQuizAnswers = {};   // { 'chIdx_qi': { selected, isCorrect } }

let studySeconds = 0; let timerInterval = null;

// ---------------- 工具函数 ----------------
function escapeHtml(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// ============================================================
// 初始化
// ============================================================
function init() {
  renderSidebar();
  renderSections();
  renderLevelLibrary();
  renderScenarioDrills(); // 第 5 章情境应答演练
  loadProgress();
  startTimer();
  loadNotes();
}

function renderSidebar() {
  const nav = document.getElementById('sidebarNav');
  nav.innerHTML = courseData.sections.map((s, i) =>
    '<div class="nav-section" data-index="' + i + '" onclick="navigateTo(' + i + ')">' +
    '<div class="nav-icon">' + s.icon + '</div>' +
    '<div class="nav-info"><div class="nav-label">' + escapeHtml(s.title) + '</div>' +
    '<div class="nav-sub">⏱ ' + s.duration + '</div></div></div>').join('');
  updateSidebarLocks();
}

function updateSidebarLocks() {
  document.querySelectorAll('.nav-section').forEach((el, i) => {
    const check = canNavigateTo(i);
    if (!check.ok && i !== currentSection) el.classList.add('locked');
    else el.classList.remove('locked');
  });
}

function renderSections() {
  const main = document.getElementById('mainContent');
  main.innerHTML = courseData.sections.map((s, i) =>
    '<div class="section" data-section="' + i + '">' +
      s.content +
      quizBlockFor(i, s) +
      '<div class="section-nav-buttons">' +
        '<div>' + (i > 0 ? '<button class="btn btn-outline" onclick="navigateTo(' + (i - 1) + ')">← 上一章</button>' : '') + '</div>' +
        '<div>' + (i < courseData.sections.length - 1
          ? '<button class="btn" onclick="markComplete(' + i + ');navigateTo(' + (i + 1) + ')">下一章 →</button>'
          : '<button class="btn btn-success" id="completeCourseBtn" onclick="tryCompleteCourse(' + i + ')">✓ 完成课程</button>') +
        '</div>' +
      '</div>' +
    '</div>').join('');
}

// 章节测验区块：带 content_quiz 类型的章节渲染对应章的选择题
// 第 1-4 章为章节测验；第 5 章同为 content_quiz，渲染的是终极考核综合选择题。
function quizBlockFor(i, s) {
  let h = '';
  const hasQuiz = (s.type === 'content_quiz' || s.type === 'content_quiz_fill')
    && chapterQuizzes[i] && chapterQuizzes[i].length > 0;
  if (hasQuiz) h += renderChapterQuiz(i);
  return h;
}

// ============================================================
// 章节测验（串行锁定：答对上一题才解锁下一题）
// ============================================================
function renderChapterQuiz(chIdx) {
  const qs = chapterQuizzes[chIdx];
  if (!qs || qs.length === 0) return '';
  const isFinal = finalChapterIndex() === chIdx;
  const title = isFinal
    ? '🏆 终极考核 · 综合选择题（共 ' + qs.length + ' 题，全部答对才算通过）'
    : '📝 ' + (chIdx + 1) + ' 章测验（共 ' + qs.length + ' 题，全部答对后解锁下一章）';
  return '<div class="card" style="border-top:4px solid var(--primary);" id="chquizwrap-' + chIdx + '">' +
    '<h2 style="margin-bottom:8px;">' + title + '</h2>' +
    '<p style="margin:0 0 12px 0;font-size:13px;color:var(--text-secondary);background:#FFF7ED;border-left:3px solid #F59E0B;padding:8px 12px;border-radius:4px">🔒 串行作答：第 1 题答对后才能解锁第 2 题，以此类推。答错的题可以点「重新作答」再做一次。</p>' +
    qs.map((q, qi) =>
      '<div class="quiz-card' + (qi > 0 && !isPreviousQuestionCorrect(chIdx, qi) ? ' locked' : '') + '" id="chquiz-' + chIdx + '-' + qi + '" data-answered="false">' +
        '<div class="quiz-question">第 ' + (qi + 1) + ' 题：' + escapeHtml(q.q) + '</div>' +
        '<div class="quiz-options">' + q.opts.map((opt, oi) =>
          '<div class="quiz-option" data-option="' + oi + '" onclick="selectChQuizOption(this,' + oi + ',' + chIdx + ',' + qi + ')">' +
          '<span class="quiz-option-label">' + String.fromCharCode(65 + oi) + '</span><span>' + escapeHtml(opt) + '</span></div>').join('') +
        '</div>' +
        '<div class="quiz-feedback" id="feedback-chquiz-' + chIdx + '-' + qi + '"></div>' +
        '<div class="quiz-locked-hint"><span>🔒 请先答对上一题，本题才会解锁</span></div>' +
      '</div>').join('') +
    '<div id="chquizstatus-' + chIdx + '" style="text-align:center;margin-top:8px;padding:12px;border-radius:8px;font-size:14px;background:' +
      (chapterQuizDone[chIdx] ? '#ECFDF5' : '#F8FAFC') + ';">' +
      chapterQuizStatusHtml(chIdx) +
    '</div></div>';
}

// 末章（终极考核）与常规章节的状态文案略有不同
function finalChapterIndex() { return courseData.sections.length - 1; }

function chapterQuizStatusHtml(chIdx) {
  if (!chapterQuizDone[chIdx]) {
    return '<span style="color:#64748B;">📋 请按顺序答完所有题目</span>';
  }
  return finalChapterIndex() === chIdx
    ? '<span style="color:#065F46;font-weight:600;">✅ 终极考核选择题已全部答对！</span>'
    : '<span style="color:#065F46;font-weight:600;">✅ 本章测验已全部通过！</span>';
}

function isPreviousQuestionCorrect(chIdx, qi) {
  if (qi === 0) return true;
  const prev = document.getElementById('chquiz-' + chIdx + '-' + (qi - 1));
  if (!prev) return false;
  return prev.dataset.answered === 'true' && !prev.querySelector('.quiz-option.wrong');
}

function updateChapterQuizLockState(chIdx) {
  const qs = chapterQuizzes[chIdx] || [];
  const done = chapterQuizDone[chIdx];
  qs.forEach((q, qi) => {
    const card = document.getElementById('chquiz-' + chIdx + '-' + qi);
    if (!card) return;
    // 本章已全部答对 → 清除所有锁定（否则刷新后会残留「锁定」外观）
    if (done || isPreviousQuestionCorrect(chIdx, qi)) card.classList.remove('locked');
    else card.classList.add('locked');
  });
}

function selectChQuizOption(el, oi, chIdx, qi) {
  const card = document.getElementById('chquiz-' + chIdx + '-' + qi);
  if (!card || card.dataset.answered === 'true') return;
  if (card.classList.contains('locked')) { showToast('🔒 请先答对上一题', 'warning'); return; }
  const q = chapterQuizzes[chIdx][qi];
  const isCorrect = (oi === q.correct);
  card.querySelectorAll('.quiz-option').forEach(b => {
    const optIdx = parseInt(b.dataset.option, 10);
    b.style.pointerEvents = 'none';
    if (isCorrect && optIdx === q.correct) b.classList.add('correct');
    else if (!isCorrect && optIdx === oi) b.classList.add('wrong');
    else b.classList.add('disabled');
  });
  const fb = document.getElementById('feedback-chquiz-' + chIdx + '-' + qi);
  if (isCorrect) {
    fb.innerHTML = '✅ 回答正确！';
    fb.classList.add('show', 'correct');
    card.style.borderColor = 'var(--success)';
  } else {
    // 学习者红线：不展示正确答案，只提示错误并允许重做
    fb.innerHTML = '❌ 这个选项还不对。再想一想第 ' + (qi + 1) + ' 题考的是哪个知识点，点「重新作答」再试一次。' +
      '<div class="quiz-retry"><button class="btn btn-outline btn-sm" onclick="resetChapterQuiz(' + chIdx + ',' + qi + ')">重新作答</button></div>';
    fb.classList.add('show', 'wrong');
    card.style.borderColor = 'var(--danger)';
  }
  card.dataset.answered = 'true';
  chapterQuizAnswers[chIdx + '_' + qi] = { selected: oi, isCorrect: isCorrect };
  updateChapterQuizLockState(chIdx);
  checkChapterQuizComplete(chIdx);
  saveProgress();
}

function resetChapterQuiz(chIdx, qi) {
  const card = document.getElementById('chquiz-' + chIdx + '-' + qi);
  if (!card) return;
  card.dataset.answered = 'false';
  card.querySelectorAll('.quiz-option').forEach(b => {
    b.classList.remove('correct', 'wrong', 'disabled');
    b.style.pointerEvents = '';
  });
  card.style.borderColor = '';
  const fb = document.getElementById('feedback-chquiz-' + chIdx + '-' + qi);
  fb.classList.remove('show', 'correct', 'wrong');
  fb.innerHTML = '';
  delete chapterQuizAnswers[chIdx + '_' + qi];
  updateChapterQuizLockState(chIdx);
  saveProgress();
}

function checkChapterQuizComplete(chIdx) {
  if (chapterQuizDone[chIdx]) return;
  const qs = chapterQuizzes[chIdx] || [];
  if (qs.length === 0) return;
  const allCorrect = qs.every((q, qi) => {
    const card = document.getElementById('chquiz-' + chIdx + '-' + qi);
    return card && card.dataset.answered === 'true' && !card.querySelector('.quiz-option.wrong');
  });
  if (!allCorrect) return;
  chapterQuizDone[chIdx] = true;
  refreshChapterQuizStatus(chIdx);
  showToast(finalChapterIndex() === chIdx
    ? '🎉 终极考核选择题全部答对！'
    : '🎉 第 ' + (chIdx + 1) + ' 章测验全部通过！', 'success');
  updateSidebarLocks();
  saveProgress();
}

// 刷新某章测验的底部状态条（首次渲染 / 答题完成 / 进度恢复 共用）
function refreshChapterQuizStatus(chIdx) {
  const el = document.getElementById('chquizstatus-' + chIdx);
  if (!el) return;
  const done = !!chapterQuizDone[chIdx];
  el.style.background = done ? '#ECFDF5' : '#F8FAFC';
  el.innerHTML = chapterQuizStatusHtml(chIdx);
}

// ============================================================
// 文本归一化工具（情景演练关键词匹配共用；终极考核原作答题型已改为选择题）
// ============================================================
function normFill(s) {
  return String(s === undefined || s === null ? '' : s)
    .toLowerCase()
    .replace(/[\s\u3000]+/g, '')
    .replace(/[，。、；：！？,.;:!?"'“”‘’（）()【】\[\]《》<>·—－-]/g, '')
    .replace(/％/g, '%');
}

// ============================================================
// 第 4 章 · 3-12 岁思维发展阶段速查库（折叠卡片，具体运算/前运算为热点）
// ============================================================
function renderLevelLibrary() {
  const box = document.getElementById('levelLibrary');
  const levels = APP.levelLibrary || [];
  if (!box || !levels.length) return;
  // position 字段来自课程内容（可信本地数据），保留少量行内标签用于强调；其余字段一律转义
  const richText = (s) => escapeHtml(s).replace(/&lt;(\/?)(strong|em|b|br)\s*\/?&gt;/g, '<$1$2>');
  const stuckHtml = (l) => (l.stuck || []).map(s =>
    '<div class="lv-stuck"><b>阶段性表现：' + escapeHtml(s[0]) + '</b><br>' +
    '👀 课堂／作业里的样子：' + escapeHtml(s[1]) + '<br>' +
    '<span class="lv-fix">🛠 沟通时可这样说：' + escapeHtml(s[2]) + '</span></div>').join('');
  box.innerHTML = '<div class="level-grid">' + levels.map((l, i) =>
    '<div class="level-card' + (l.hot ? ' is-hot' : '') + '" id="levelcard-' + i + '">' +
      '<div class="level-card-h" onclick="toggleLevelCard(' + i + ')">' +
        '<div class="lv-badge">' + escapeHtml(l.level) + '</div>' +
        '<div class="lv-title"><b>' + escapeHtml(l.grade || '') + (l.hot ? ' · 关键培养期' : '') + '</b>' +
          '<span>' + richText(l.position || '') + '</span></div>' +
        '<div class="lv-caret">▼</div>' +
      '</div>' +
      '<div class="level-card-body">' +
        '<div class="lv-sec"><div class="lv-sec-h">🧭 阶段表现与沟通口径</div>' + stuckHtml(l) + '</div>' +
        '<div class="lv-sec"><div class="lv-sec-h">📐 这一阶段可以培养什么</div><ul>' +
          (l.build || []).map(x => '<li>' + richText(x) + '</li>').join('') + '</ul></div>' +
        '<div class="lv-sec"><div class="lv-sec-h">🔄 进入下一阶段的变化</div><ul>' +
          (l.change || []).map(x => '<li>' + richText(x) + '</li>').join('') + '</ul></div>' +
        '<div class="lv-tip">💡 用法：家长问「我家孩子现在这个年纪，学思维到底是在学什么」时，先定位孩子所处阶段，再用「这一阶段能培养什么」和「下一阶段会变难在哪」两句话把必要性讲清楚。</div>' +
      '</div>' +
    '</div>').join('') + '</div>';
}

function toggleLevelCard(i) {
  const card = document.getElementById('levelcard-' + i);
  if (card) card.classList.toggle('open');
}

// ============================================================
// 第 5 章 · 情境应答演练（家长提问 → 学员用自己的话回答 → 关键词自检）
// 红线：不展示「满分参考答案」，只做关键词命中提示 + 知识点回顾指引
// ============================================================
let drillAnswers = {};   // { id: { text, hit, passed } }

function renderScenarioDrills() {
  const box = document.getElementById('scenarioDrillContainer');
  const drills = APP.scenarioDrills || [];
  if (!box || !drills.length) return;
  box.innerHTML =
    '<h2 style="margin-bottom:8px;">🎯 情境应答演练（共 ' + drills.length + ' 个场景）</h2>' +
    '<p style="margin:0 0 14px 0;font-size:13px;color:var(--text-secondary);background:#EEF2FF;border-left:3px solid var(--primary);padding:8px 12px;border-radius:4px">家长抛出一个问题，你用<strong>自己的话</strong>组织一段回应。系统会检查你的回答里有没有踩到关键说明角度，并给出补强方向——<strong>不会给标准答案</strong>。答不完整可以反复重写。</p>' +
    drills.map((d, i) => {
      const rec = drillAnswers[d.id];
      const passed = rec && rec.passed;
      return '<div class="drill-card" id="drill-' + d.id + '" data-passed="' + (passed ? 'true' : 'false') + '">' +
        '<div class="dc-h"><span class="dc-n">' + (i + 1) + '</span>' + escapeHtml(d.title) + '</div>' +
        '<div class="drill-parent">' + escapeHtml(d.parent) + '</div>' +
        '<textarea class="drill-textarea" id="drillInput-' + d.id + '" placeholder="写下你会怎么回答这位家长（尽量口语化，像真的在沟通）..."' +
          (passed ? ' disabled' : '') + '>' + (passed && rec ? escapeHtml(rec.text) : '') + '</textarea>' +
        '<div class="drill-actions">' +
          (passed ? '' :
            '<button class="btn" id="drillBtn-' + d.id + '" onclick="submitDrill(\'' + d.id + '\')">提交自检</button>' +
            '<button class="btn btn-outline" onclick="clearDrill(\'' + d.id + '\')">清空重写</button>') +
        '</div>' +
        '<div class="drill-feedback' + (rec && rec.show ? ' show ' + (passed ? 'good' : 'refer') : '') + '" id="drillFeedback-' + d.id + '">' +
          (rec && rec.show ? drillFeedbackHtml(d, rec) : '') +
        '</div>' +
      '</div>';
    }).join('') +
    '<div class="drill-progress" id="drillProgress">' + drillProgressText() + '</div>';
}

function drillFeedbackHtml(d, rec) {
  const total = d.angles.length;
  const hit = rec.hit || [];
  if (rec.passed) {
    return '<div class="df-h">✅ 说得不错！</div>' +
      '你的回答覆盖了 ' + hit.length + '/' + total + ' 个关键说明角度：' + hit.map(h => '「' + escapeHtml(h) + '」').join(' ') + '。<br>' +
      '可以再想一想：同样的内容，换一个更贴近家长原话的说法会不会更自然？';
  }
  return '<div class="df-h">📝 还可以再补一补</div>' +
    '你目前踩到了 ' + hit.length + '/' + total + ' 个关键说明角度' +
    (hit.length ? '：' + hit.map(h => '「' + escapeHtml(h) + '」').join(' ') : '') + '。<br>' +
    '这个场景里，一个有说服力的回应通常要照顾到下面这些角度，看看还差哪个：<br>' +
    '<strong>' + d.angles.map(a => escapeHtml(a)).join(' ／ ') + '</strong>' +
    '<div class="df-ref">🧭 复习指引：' + d.hint + '</div>';
}

function drillProgressText() {
  const drills = APP.scenarioDrills || [];
  const done = drills.filter(d => drillAnswers[d.id] && drillAnswers[d.id].passed).length;
  return done >= drills.length
    ? '<span style="color:#065F46;font-weight:600;">✅ 情境演练已全部通过！</span>'
    : '📋 已通过 ' + done + ' / ' + drills.length + ' 个情境演练';
}

function submitDrill(id) {
  const drills = APP.scenarioDrills || [];
  const d = drills.filter(x => x.id === id)[0];
  const card = document.getElementById('drill-' + id);
  const input = document.getElementById('drillInput-' + id);
  const fb = document.getElementById('drillFeedback-' + id);
  if (!d || !card || !input || card.dataset.passed === 'true') return;
  const text = (input.value || '').trim();
  if (text.length < 15) {
    showToast('请先多写一点你的回应（至少一两句话）', 'warning');
    input.focus();
    return;
  }
  const normalized = normFill(text);
  const hit = d.angles.filter(angle => {
    const kws = d.keywords[angle] || [];
    return kws.some(k => normalized.indexOf(normFill(k)) !== -1);
  });
  // 通过条件：命中至少一半角度（向上取整），且回答有一定长度
  const need = Math.ceil(d.angles.length / 2);
  const passed = hit.length >= need && text.length >= 30;
  drillAnswers[id] = { text: text, hit: hit, passed: passed, show: true };
  if (passed) {
    card.dataset.passed = 'true';
    input.disabled = true;
    const btn = document.getElementById('drillBtn-' + id);
    if (btn) btn.remove();
    showToast('✅ 情境演练通过', 'success');
  }
  fb.className = 'drill-feedback show ' + (passed ? 'good' : 'refer');
  fb.innerHTML = drillFeedbackHtml(d, drillAnswers[id]);
  const pg = document.getElementById('drillProgress');
  if (pg) pg.innerHTML = drillProgressText();
  saveProgress();
}

function clearDrill(id) {
  const card = document.getElementById('drill-' + id);
  if (!card || card.dataset.passed === 'true') return;
  const input = document.getElementById('drillInput-' + id);
  if (input) { input.value = ''; input.focus(); }
  const fb = document.getElementById('drillFeedback-' + id);
  if (fb) { fb.className = 'drill-feedback'; fb.innerHTML = ''; }
  delete drillAnswers[id];
  saveProgress();
}

function restoreDrillUI() {
  const drills = APP.scenarioDrills || [];
  drills.forEach(d => {
    const rec = drillAnswers[d.id];
    if (!rec || !rec.show) return;
    const card = document.getElementById('drill-' + d.id);
    const input = document.getElementById('drillInput-' + d.id);
    const fb = document.getElementById('drillFeedback-' + d.id);
    if (rec.passed) {
      if (card) card.dataset.passed = 'true';
      if (input) { input.value = rec.text; input.disabled = true; }
      const btn = document.getElementById('drillBtn-' + d.id);
      if (btn) btn.remove();
    }
    if (fb) {
      fb.className = 'drill-feedback show ' + (rec.passed ? 'good' : 'refer');
      fb.innerHTML = drillFeedbackHtml(d, rec);
    }
  });
  const pg = document.getElementById('drillProgress');
  if (pg) pg.innerHTML = drillProgressText();
}

// ============================================================
// 导航与解锁
// ============================================================
function canNavigateTo(index) {
  if (index === 0) return { ok: true };
  // 章序：0 什么是数学思维 → 1 学思维的好处 → 2 必须重视的理由 → 3 3-12岁发展特点 → 4 家长沟通实战+终极考核
  if (index >= 1 && !chapterQuizDone[0]) return { ok: false, msg: '请先完成第 1 章的所有测验题（全部答对）' };
  if (index >= 2 && !chapterQuizDone[1]) return { ok: false, msg: '请先完成第 2 章的所有测验题（全部答对）' };
  if (index >= 3 && !chapterQuizDone[2]) return { ok: false, msg: '请先完成第 3 章的所有测验题（全部答对）' };
  if (index >= 4 && !chapterQuizDone[3]) return { ok: false, msg: '请先完成第 4 章的所有测验题（全部答对）' };
  return { ok: true };
}

function navigateTo(index) {
  const check = canNavigateTo(index);
  if (!check.ok) { showToast('🔒 ' + check.msg, 'warning'); return; }
  currentSection = index;
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-section').forEach(n => n.classList.remove('active'));
  const section = document.querySelector('.section[data-section="' + index + '"]');
  if (section) section.classList.add('active');
  const navItem = document.querySelector('.nav-section[data-index="' + index + '"]');
  if (navItem) navItem.classList.add('active');
  updateProgress(); updateNotesForSection(index); saveProgress();
  window.scrollTo({ top: 0, behavior: 'smooth' });
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('sidebarOverlay').classList.remove('show');
  const mhTitle = document.getElementById('mhTitle');
  if (mhTitle) mhTitle.textContent = courseData.sections[index].title;
}

function markComplete(index) {
  completedSections.add(index);
  updateProgress(); saveProgress();
  showToast('「' + courseData.sections[index].title + '」已完成 ✓', 'success');
  checkCertificate();
}

// 终极考核 = 第 5 章综合选择题（家长沟通要点） + 情境应答演练
// 说明：本课为「复习」定位，不设 AI 家长对练。
//      选择题共 15 道：第 1-4 章各 3 道（全部答对即解锁下一章），
//      第 5 章 3 道为终极考核部分。
//      第 5 章：3 道选择题全对 + 4 个情境演练全过 → 可完成课程。
function finalMcqDone() {
  const last = finalChapterIndex();
  const qs = chapterQuizzes[last] || [];
  return qs.length === 0 || !!chapterQuizDone[last];
}

function drillAllDone() {
  const drills = APP.scenarioDrills || [];
  return drills.length === 0 || drills.every(d => drillAnswers[d.id] && drillAnswers[d.id].passed);
}
function finalDrillsDone() { return drillAllDone(); }

function tryCompleteCourse(index) {
  if (!finalMcqDone()) { showToast('请先完成第 5 章的终极考核选择题（全部答对）', 'warning'); return; }
  if (!finalDrillsDone()) { showToast('请先完成全部情境应答演练', 'warning'); return; }
  markComplete(index);
}

function updateProgress() {
  const total = courseData.sections.length;
  const viewed = new Set([...completedSections, currentSection]);
  const pct = Math.round((viewed.size / total) * 100);
  document.getElementById('progressPercent').textContent = pct + '%';
  document.getElementById('progressFill').style.width = pct + '%';
  document.querySelectorAll('.nav-section').forEach((el, i) => {
    if (completedSections.has(i)) el.classList.add('completed');
  });
}


// ============================================================
// 计时器 / 标签页 / 笔记
// ============================================================
function startTimer() {
  const saved = localStorage.getItem(LS_PREFIX + '_study_seconds');
  if (saved) studySeconds = parseInt(saved, 10);
  updateTimerDisplay();
  timerInterval = setInterval(() => {
    studySeconds++;
    updateTimerDisplay();
    if (studySeconds % 10 === 0) localStorage.setItem(LS_PREFIX + '_study_seconds', studySeconds);
  }, 1000);
}
function updateTimerDisplay() {
  const mins = Math.floor(studySeconds / 60), secs = studySeconds % 60;
  const ts = String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
  const el = document.getElementById('timerDisplay'); if (el) el.textContent = ts;
  const mt = document.getElementById('mhTimer'); if (mt) mt.textContent = '⏱ ' + ts;
}

function switchTab(btn, panelId) {
  const wrap = btn.closest('.card') || document;
  wrap.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  wrap.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  const panel = document.getElementById(panelId);
  if (panel) panel.classList.add('active');
}

function toggleNotes() { document.getElementById('notesPanel').classList.toggle('open'); }
function updateNotesForSection(index) {
  document.getElementById('notesChapterLabel').textContent = courseData.sections[index].title;
  const saved = JSON.parse(localStorage.getItem(LS_PREFIX + '_notes') || '{}');
  document.getElementById('notesTextarea').value = saved[index] || '';
}
function loadNotes() {
  const saved = JSON.parse(localStorage.getItem(LS_PREFIX + '_notes') || '{}');
  const ta = document.getElementById('notesTextarea');
  if (!ta) return;
  ta.value = saved[currentSection] || '';
  ta.addEventListener('input', function () {
    const all = JSON.parse(localStorage.getItem(LS_PREFIX + '_notes') || '{}');
    all[currentSection] = this.value;
    localStorage.setItem(LS_PREFIX + '_notes', JSON.stringify(all));
  });
}

// ============================================================
// 进度持久化
// ============================================================
function restoreChapterQuizUI() {
  Object.keys(chapterQuizAnswers).forEach(key => {
    const parts = key.split('_').map(Number);
    const chIdx = parts[0], qi = parts[1];
    if (isNaN(chIdx) || isNaN(qi)) return;
    const ans = chapterQuizAnswers[key];
    if (!ans) return;
    const card = document.getElementById('chquiz-' + chIdx + '-' + qi);
    if (!card) return;
    card.dataset.answered = 'true';
    card.querySelectorAll('.quiz-option').forEach(b => {
      const oi = parseInt(b.dataset.option, 10);
      b.style.pointerEvents = 'none';
      if (ans.isCorrect && oi === (chapterQuizzes[chIdx][qi] || {}).correct) b.classList.add('correct');
      else if (!ans.isCorrect && oi === ans.selected) b.classList.add('wrong');
      else b.classList.add('disabled');
    });
    const fb = document.getElementById('feedback-chquiz-' + chIdx + '-' + qi);
    if (fb) {
      if (ans.isCorrect) {
        fb.innerHTML = '✅ 回答正确！';
        fb.classList.add('show', 'correct');
        card.style.borderColor = 'var(--success)';
      } else {
        fb.innerHTML = '❌ 这个选项还不对。点「重新作答」再试一次。' +
          '<div class="quiz-retry"><button class="btn btn-outline btn-sm" onclick="resetChapterQuiz(' + chIdx + ',' + qi + ')">重新作答</button></div>';
        fb.classList.add('show', 'wrong');
        card.style.borderColor = 'var(--danger)';
      }
    }
  });
}

function saveProgress() {
  const state = {
    completedSections: [...completedSections],
    chapterQuizDone: chapterQuizDone,
    chapterQuizAnswers: chapterQuizAnswers,
    drillAnswers: drillAnswers,
    currentSection: currentSection
  };
  try { localStorage.setItem(LS_PREFIX + '_progress', JSON.stringify(state)); } catch (e) {}
}

function loadProgress() {
  try {
    const saved = JSON.parse(localStorage.getItem(LS_PREFIX + '_progress'));
    if (saved) {
      completedSections = new Set(saved.completedSections || []);
      chapterQuizDone = saved.chapterQuizDone || new Array(chapterQuizzes.length).fill(false);
      if (chapterQuizDone.length !== chapterQuizzes.length) chapterQuizDone = new Array(chapterQuizzes.length).fill(false);
      chapterQuizAnswers = saved.chapterQuizAnswers || {};
      drillAnswers = saved.drillAnswers || {};
      currentSection = saved.currentSection || 0;
      // 兼容旧数据：有完成标记但没有答题记录 → 重置测验状态
      const hasDoneButNoAnswers = chapterQuizDone.some(d => d) && Object.keys(chapterQuizAnswers).length === 0;
      if (hasDoneButNoAnswers) chapterQuizDone = new Array(chapterQuizzes.length).fill(false);
      if (!canNavigateTo(currentSection).ok) currentSection = 0;
      updateProgress();
      updateSidebarLocks();
      restoreChapterQuizUI();
      for (let i = 0; i < chapterQuizzes.length; i++) {
        if (chapterQuizzes[i] && chapterQuizzes[i].length > 0) {
          updateChapterQuizLockState(i);
          refreshChapterQuizStatus(i);
        }
      }
      restoreDrillUI();
      document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
      const section = document.querySelector('.section[data-section="' + currentSection + '"]');
      if (section) section.classList.add('active');
      const navItem = document.querySelector('.nav-section[data-index="' + currentSection + '"]');
      if (navItem) navItem.classList.add('active');
      const mhTitle = document.getElementById('mhTitle');
      if (mhTitle) mhTitle.textContent = courseData.sections[currentSection].title;
    } else {
      navigateTo(0);
    }
  } catch (e) {
    navigateTo(0);
  }
}

// ============================================================
// 结业证书
// ============================================================
function checkCertificate() {
  const allDone = completedSections.size >= courseData.sections.length && finalMcqDone() && finalDrillsDone();
  if (!allDone) return;
  setTimeout(() => {
    showToast('🏆 恭喜完成全部课程！点击领取结业证书', 'success');
    // 证书口径：选择题（15 题，含终极考核 3 题）+ 情境演练（4 个）
    const mcqTotal = chapterQuizzes.reduce((n, qs) => n + (qs ? qs.length : 0), 0);
    const drills = APP.scenarioDrills || [];
    const drillN = drills.filter(d => drillAnswers[d.id] && drillAnswers[d.id].passed).length;
    document.getElementById('certScore').textContent =
      '综合评定：通过（选择题 ' + mcqTotal + '/' + mcqTotal + '）';
    document.getElementById('certFinalScore').textContent = '情境应答演练：已通过 ' + drillN + '/' + drills.length + ' 个场景';
    document.getElementById('certDate').textContent = new Date().toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' });
    const savedName = localStorage.getItem(LS_PREFIX + '_student_name');
    if (savedName) {
      document.getElementById('certStudentName').textContent = savedName;
      document.getElementById('certNameEdit').style.display = 'none';
    } else {
      document.getElementById('certNameEdit').style.display = 'block';
      document.getElementById('certNameInput').focus();
    }
    document.getElementById('certOverlay').style.display = 'flex';
  }, 800);
}
function saveCertName() {
  const input = document.getElementById('certNameInput');
  const name = (input.value || '').trim();
  if (!name) { showToast('请输入姓名后再确认', 'warning'); input.focus(); return; }
  localStorage.setItem(LS_PREFIX + '_student_name', name);
  document.getElementById('certStudentName').textContent = name;
  document.getElementById('certNameEdit').style.display = 'none';
  showToast('✅ 姓名已保存', 'success');
}
function closeCertificate() { document.getElementById('certOverlay').style.display = 'none'; }
function printCertificate() {
  const name = document.getElementById('certStudentName').textContent;
  if (!name || name === '请填写姓名') { showToast('请先确认姓名后再打印证书', 'warning'); return; }
  const cert = document.getElementById('certPaper');
  const win = window.open('', '_blank', 'width=750,height=600');
  win.document.write('<html><head><meta charset="UTF-8"><title>结业证书</title><style>');
  win.document.write('body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#f1f5f9;}');
  win.document.write('.cert{background:#fff;width:700px;padding:48px 36px;text-align:center;border:2px solid #e2e8f0;border-radius:12px;}');
  win.document.write('.cert h1{font-size:28px;color:#3730A3;margin-bottom:4px;}');
  win.document.write('.cert .sub{font-size:12px;color:#64748b;letter-spacing:0.1em;margin-bottom:24px;}');
  win.document.write('.cert .body{font-size:15px;line-height:2;color:#1e293b;}');
  win.document.write('.cert .name{display:inline-block;border-bottom:2px solid #4F46E5;min-width:120px;padding:4px 12px;margin:0 4px;}');
  win.document.write('.cert .course{font-weight:700;color:#3730A3;margin:8px 0;}');
  win.document.write('.cert .score{margin:20px 0 4px;font-size:16px;font-weight:600;color:#10b981;}');
  win.document.write('.cert .final-score{margin:4px 0 20px;font-size:14px;font-weight:600;color:#3730A3;}');
  win.document.write('.cert .footer{display:flex;justify-content:space-between;font-size:12px;color:#64748b;margin-top:32px;border-top:1px solid #e2e8f0;padding-top:16px;}');
  win.document.write('</style></head><body><div class="cert">');
  win.document.write(cert.innerHTML.replace(/<button[^>]*>[\s\S]*?<\/button>/g, '').replace(/<div class="cert-name-edit"[\s\S]*?<\/div><\/div>/g, ''));
  win.document.write('</div></body></html>');
  win.document.close(); setTimeout(() => win.print(), 500);
}

// ============================================================
// Toast / 侧边栏
// ============================================================
function showToast(msg, type) {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();
  const toast = document.createElement('div');
  toast.className = 'toast ' + type;
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2500);
}
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
  document.getElementById('sidebarOverlay').classList.toggle('show');
}

// ---------------- 题图放大预览 ----------------
function zoomFigure(img) {
  if (!img) return;
  const ov = document.getElementById('figZoomOverlay');
  if (!ov) return;
  const big = document.createElement('img');
  big.src = img.getAttribute('src');
  big.alt = img.getAttribute('alt') || '';
  // 清掉上一张（保留关闭按钮）
  ov.querySelectorAll('img').forEach(el => el.remove());
  ov.appendChild(big);
  ov.classList.add('show');
}
function closeZoomFigure() {
  const ov = document.getElementById('figZoomOverlay');
  if (ov) ov.classList.remove('show');
}
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') closeZoomFigure();
});

document.addEventListener('DOMContentLoaded', init);
