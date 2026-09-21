# -*- coding: utf-8 -*-
"""
《思维学习理念复习》微课 · 单一内容源
面向：线上少儿数学思维 班主任（LP）｜ 简体中文 · 大陆用语

素材来源：
  《思维学习理念》.pptx（25 页 · 益智国内新人训）
    PART 01 什么是数学思维（Slide 1-9）
    PART 02 学习数学思维的好处 & 重要性（Slide 10-18）
    PART 03 3-12 岁儿童思维发展特点（Slide 19-24）

课程定位：班主任「思维学习理念」复习与家长沟通实战课。
目标：① 梳理核心思维理论要点；② 掌握向家长说明思维学习重要性的关键角度与表达；
      ③ 能在真实沟通场景中把这些理念说得清楚、有说服力。
终极考核：家长说明综合选择题（3 题） + 情境应答演练（4 个场景） 。
"""

COURSE_TITLE = '思维学习理念复习'
LS_PREFIX = 'cn_lp_thinking'
ORG_NAME = 'VIPTHINK'

# ============================================================
# 第一章：什么是数学思维
# ============================================================
CH1 = '''
<div class="section-header">
  <span class="section-badge">第 1 章</span>
  <h1>什么是数学思维</h1>
  <p class="duration">⏱ 学习时长：10-12 分钟 ｜ 📝 含 3 道章节测验</p>
</div>

<div class="activate-box">
  <span class="at">🔎 先做一道题，找找感觉</span>
  看下面这张图——碗里有三百粒豆子，想知道里面有多少<strong>绿豆</strong>，你会选择哪种方案？<br>
  <strong>方案一：挑出绿豆。方案二：挑出红豆。</strong><br>
  想一想再往下看——你会选哪个，为什么？
  <figure class="q-figure">{{FIG_BEANS}}</figure>
</div>

<div class="card">
  <h2 class="card-title">🧠 先看清楚：「思维」到底是什么</h2>
  <p style="margin-bottom:14px;">很多家长以为「思维」是个虚词，其实它有严格的定义。我们先把它说清楚——这也是你跟家长沟通时的底气来源。</p>
  <div class="def-card">
    <div class="def-q">思维：是人类认识活动的最高形式。</div>
    <div class="def-a">
      它让我们的认知不再停留在「眼睛看到什么就是什么」，而是能够<strong>反映出事物之间的内在联系</strong>。<br><br>
      它是通过对事物的<strong>分析、比较、综合、抽象和概括</strong>来进行的——是一种用<strong>推理或判断</strong>，间接反映事物本质的认识活动；也是凭记忆、想象去处理抽象事物，从而理解其意义的过程。
    </div>
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>关键词</th><th>通俗解释</th><th>家长能听懂的说法</th></tr></thead>
      <tbody>
        <tr><td><strong>最高形式</strong></td><td>比「感觉」「记忆」更高一级的认知活动</td><td>不只是记住，而是会想、会判断</td></tr>
        <tr><td><strong>内在联系</strong></td><td>看到现象背后的规律与因果</td><td>能看出「为什么会这样」，而不只是「就是这样」</td></tr>
        <tr><td><strong>间接反映</strong></td><td>不靠直接看到，靠推理得出</td><td>不是套公式，是能自己推出来</td></tr>
        <tr class="tr-hot"><td><strong>概括与抽象</strong></td><td>把同类问题的共性提炼出来</td><td>会举一反三，而不是做一题会一题</td></tr>
      </tbody>
    </table>
  </div>
  <div class="tips-box">💡 <strong>记住一句话：</strong>思维不是「知识」，而是「处理知识的能力」。同样学一个知识点，有思维的孩子能迁移、能拓展；没思维的孩子只能靠重复记忆。</div>
</div>

<div class="card">
  <h2 class="card-title">🔍 回到刚才那道题：逆向思维为什么更快</h2>
  <div class="choice-demo">
    <div class="cd-item">
      <span class="cd-tag">方案一</span>
      <div class="cd-h">挑出绿豆</div>
      <div class="cd-d">绿豆数量多，要一粒一粒挑出来，耗时长、易出错。<br><br>这是顺着「要什么就找什么」的<strong>正向思路</strong>。</div>
    </div>
    <div class="cd-item cd-best">
      <span class="cd-tag">✅ 最优解</span>
      <div class="cd-h">挑出红豆</div>
      <div class="cd-d">红豆数量远小于绿豆，挑完红豆，剩下的就是绿豆，又快又准。<br><br>这是调转方向的<strong>逆向思维</strong>。</div>
    </div>
  </div>
  <p>两种方案都能得到答案，但<strong>好的思维能让「更少的功夫」换「同样甚至更好的结果」</strong>。这就是思维训练真正的价值——不是让孩子做更多题，而是让他找到更聪明的路径。</p>
  <div class="reflect-box">
    <span class="rt">📣 这段可以直接讲给家长听</span>
    「同样是算一道题，有的孩子埋头硬算，有的孩子先想一步用更巧的办法——这个差别，就是思维训练的差别。我们教的不是多做几道题，而是让孩子遇到问题时<strong>先找更聪明的路</strong>。」
  </div>
</div>

<div class="card">
  <h2 class="card-title">👀 家长会怎么想数学？两种截然不同的认知</h2>
  <p style="margin-bottom:14px;">在跟家长谈思维学习之前，你要先知道家长脑子里对「数学」的印象是什么。多数家长的第一反应其实是这样的：</p>
  <div class="say-compare">
    <div class="say-col say-bad">
      <div class="sc-h">❌ 大多数家长对数学的印象</div>
      <ul>
        <li>数学就是「数字」和「加减乘除计算」</li>
        <li>学好数学的办法就是做题、做题、做题</li>
        <li>需要记住大量公式，靠重复才能记住</li>
        <li>数学很难，想考高分更是难上加难</li>
      </ul>
    </div>
    <div class="say-col say-good">
      <div class="sc-h">✅ 数学真正的样子</div>
      <ul>
        <li>数字、计算，也包含<strong>几何、推理、概率</strong></li>
        <li>核心是<strong>数学方法</strong>，不只是结果</li>
        <li>靠的是<strong>想明白</strong>，而不是背下来</li>
        <li>难在「没有方法」，而不是「题目本身」</li>
      </ul>
    </div>
  </div>
  <div class="tips-box">💡 <strong>这个认知差，就是你的切入点。</strong>家长之所以觉得「多刷题就行」，正是因为他把数学等同于计算。你要做的，是把「数学＝计算」这个印象，升级成「数学＝思考问题的方法」。</div>
</div>

<div class="card">
  <h2 class="card-title">⭐ 数学为什么重要（讲给家长的四个理由）</h2>
  <div class="reason-cards">
    <div class="reason-card rc-a">
      <span class="rc-tag">理由一</span>
      <div class="rc-h">数学是认知世界的基础工具</div>
      <div class="rc-b">数学是各个学科的基础，有着非常重要的地位。生活中解决很多现实问题都要用到数学——简单的如计算、分类，复杂一点的如小的统计、推理。</div>
    </div>
    <div class="reason-card rc-b">
      <span class="rc-tag">理由二</span>
      <div class="rc-h">数学提供解决问题的场景</div>
      <div class="rc-b">数学中的大量问题在生活中都能找到对应场景，从而提供培养<strong>解决问题的能力和方法</strong>的契机。</div>
    </div>
    <div class="reason-card rc-c">
      <span class="rc-tag">理由三</span>
      <div class="rc-h">数学知识本身包含思维方法</div>
      <div class="rc-b">思维方法是通过具体的数学题目体现出来的——所以在数学题目的训练中，可以很好地锻炼孩子各方面的思维能力。</div>
    </div>
  </div>
  <div class="table-wrap" style="margin-top:18px;">
    <table>
      <thead><tr><th>理由四 · 不可替代性</th><th>它意味着什么</th></tr></thead>
      <tbody>
        <tr><td>数学在<strong>几何直观能力、运算能力、逻辑推理能力、数据处理能力</strong>等方面，是其它学科不可替代的</td><td>这些能力不是「顺便学到」的，只有数学这条路能系统训练。<strong>换个科目补不上来</strong>——这是你跟家长强调「必要性」时最有力的一句。</td></tr>
      </tbody>
    </table>
  </div>
  <div class="reflect-box">
    <span class="rt">📣 沟通转化：把「学科价值」说成「孩子的能力」</span>
    家长对「数学是基础学科」这句话往往是无感的。你要把它翻译成：<br>
    「孩子以后学物理、化学，要靠<strong>逻辑推理</strong>；看图表、比数据，要靠<strong>数据处理</strong>；搭模型、看立体图，要靠<strong>几何直观</strong>。这些能力，别的科目练不了，只有数学能练——而且练得越早越扎实。」
  </div>
</div>

<div class="card">
  <h2 class="card-title">🧰 什么是数学思维：16 种数学方法</h2>
  <p style="margin-bottom:12px;">「数学思维就是用数学的方法去思考问题和解决问题的能力。」这句话里最关键的词是<strong>数学方法</strong>。家长最常问「你们到底教什么」，你把下面这张方法表亮出来，他立刻就明白了。</p>
  <div class="method-grid">
    <span class="method-chip">整体代换</span>
    <span class="method-chip hot">逆向思维</span>
    <span class="method-chip hot">分类讨论</span>
    <span class="method-chip">类比推理</span>
    <span class="method-chip">比较</span>
    <span class="method-chip">特值</span>
    <span class="method-chip hot">枚举</span>
    <span class="method-chip">假设</span>
    <span class="method-chip">划归</span>
    <span class="method-chip">对应</span>
    <span class="method-chip">联想</span>
    <span class="method-chip">排除</span>
    <span class="method-chip hot">建模分析</span>
    <span class="method-chip">发散</span>
    <span class="method-chip">转换</span>
    <span class="method-chip">数形分析</span>
  </div>
  <div class="def-card" style="margin-top:18px;">
    <div class="def-q">📌 重点方法：枚举法（穷举法）</div>
    <div class="def-a">
      在研究问题时，把<strong>所有可能发生的情况一一列举</strong>加以研究的方法，叫做枚举法。<br><br>
      它的价值在于：训练孩子<strong>「不重不漏」</strong>的思维习惯——这恰恰是很多孩子做难题时最大的短板（漏情况、重复算）。
    </div>
  </div>
  <p style="margin-top:14px;"><strong>两个课堂案例（家长常举给孩子的「难题」，正是这样解出来的）：</strong></p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>案例</th><th>题目</th><th>思维切入点</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>案例 1</strong></td>
          <td>有 5 角和 1 角硬币若干枚，凑出 2 元 6 角，共有多少种不同的凑法？</td>
          <td>按 5 角硬币的枚数<strong>分类</strong>，从多到少逐一枚举，保证不重不漏</td>
        </tr>
        <tr class="tr-hot">
          <td><strong>案例 2</strong></td>
          <td>将 0-9 这十个数分别填入圆圈中，且每个正方形顶点上的四个数之和都是 18，求 A 和 B 的和。</td>
          <td>不硬填，先算总量：<br>数和 0+1+…+9 = <strong>45</strong>；三个正方形顶点数之和 = 18×3 = <strong>54</strong>；<br>重叠部分即 <strong>A+B = 54−45 = 9</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="tips-box">💡 <strong>案例 2 是最好的沟通素材：</strong>孩子硬填要试几十次，会方法的孩子两步就出来了。这就是「思维」和「刷题」的差距——你可以用这个例子，让家长亲眼看到思维的价值。</div>
  <div id="ch1-reflect"></div>
</div>

<div class="reflect-box">
  <span class="rt">📝 本章小结 · 三句话记住第 1 章</span>
  ① 思维是认识活动的最高形式，核心是<strong>推理与概括</strong>，不是记忆。<br>
  ② 数学的重要性在于它<strong>不可替代</strong>地训练逻辑推理、几何直观、数据处理能力。<br>
  ③ 数学思维 ＝ 用<strong>数学方法</strong>（逆向、分类、枚举、建模…）去思考和解决问题的能力。
</div>
'''

# ============================================================
# 第二章：学习数学思维的好处
# ============================================================
CH2 = '''
<div class="section-header">
  <span class="section-badge">第 2 章</span>
  <h1>学习数学思维的好处</h1>
  <p class="duration">⏱ 学习时长：10-12 分钟 ｜ 📝 含 3 道章节测验</p>
</div>

<div class="activate-box">
  <span class="at">🔎 家长最常问的一句话</span>
  「学这个思维，到底对孩子有什么用？」<br>
  <strong>这一章给你五个答案，每一句都能直接讲给家长听。</strong>
</div>

<div class="benefit-grid">
  <div class="benefit-card">
    <div class="bc-ico">🏗️</div>
    <div class="bc-h">为其他学科打好基础</div>
    <div class="bc-b">数理化的底层能力，语文英语的理解分析能力，都由此而来。</div>
  </div>
  <div class="benefit-card">
    <div class="bc-ico">💡</div>
    <div class="bc-h">开拓解题思路</div>
    <div class="bc-b">从「套公式」升级为「分析判断、逻辑推理」，越往高年级越明显。</div>
  </div>
  <div class="benefit-card">
    <div class="bc-ico">⚡</div>
    <div class="bc-h">高效率解决问题</div>
    <div class="bc-b">条理性分析、抓住关键点，同样时间做更多、更准。</div>
  </div>
  <div class="benefit-card">
    <div class="bc-ico">🌟</div>
    <div class="bc-h">意志品质的锻炼</div>
    <div class="bc-b">难度递增时坚持钻研，养成受用一生的思维品质。</div>
  </div>
  <div class="benefit-card">
    <div class="bc-ico">😊</div>
    <div class="bc-h">增强自信心</div>
    <div class="bc-b">做事有条理、有办法，形成良性循环，孩子更有底气。</div>
  </div>
</div>

<div class="why-block">
  <div class="wb-head"><div class="wb-ico">🏗️</div><div class="wb-h">好处一 · 为其他学科打好基础</div></div>
  <div class="wb-b">
    从小培养和锻炼孩子的数学思维能力，对孩子的每个阶段学习和成长都是有益的。数学思维的学习，可以为数学这门学科打下良好的基础，同时还能培养<strong>空间想象能力、抽象思维能力</strong>等。<br><br>
    我们都知道，等孩子上了初中、高中，每门课程难度都在加大，尤其是数理化。如果孩子在小学阶段通过锻炼数学思维，让思维能力得以提高增强，孩子<strong>头脑灵活、逻辑思维强</strong>，那后期学好数理化课程都能轻松应对。<br><br>
    同时，学习数学思维还能锻炼孩子的<strong>理解分析能力</strong>，这又能对学习语文、英语等也有很大的帮助。
  </div>
</div>

<div class="why-block">
  <div class="wb-head"><div class="wb-ico">💡</div><div class="wb-h">好处二 · 开拓解题思路（最关键的一条）</div></div>
  <div class="wb-b">
    孩子在小学阶段所学的数学知识，主要还是以<strong>感性认识和形象思维</strong>为主。说得通俗点：对于小学 3 年级以前，绝大多数数学题只要记住定义和公式，一般都能求解出来——注重的是一个<strong>「套」</strong>字。<br><br>
    但<strong>四年级以后</strong>要想学得好，就要有学习方法了。如果不对孩子进行数学思维训练，那么进入初高中之后，课程难度陡增，孩子解题方式却依然停留在初级阶段，成绩自然会一落千丈。<br><br>
    因此学习数学思维、运用数学思维解题，经过<strong>分析判断、逻辑推理</strong>等方法「抽丝剥茧」，提升逻辑推理和抽象思维能力，才能开拓解题思路、取得更好的成绩。
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>阶段</th><th>题目特点</th><th>需要的能力</th><th>没学思维会怎样</th></tr></thead>
      <tbody>
        <tr><td><strong>三年级以前</strong></td><td>记住定义和公式基本就能解</td><td>记性 + 「套」</td><td>成绩看不出差别，家长容易误以为「够用」</td></tr>
        <tr class="tr-hot"><td><strong>四年级以后</strong></td><td>需要分析、推理、多步思考</td><td>逻辑推理 + 抽象思维</td><td>解题方式还停在初级阶段，<strong>成绩一落千丈</strong></td></tr>
        <tr><td><strong>初高中</strong></td><td>数理化难度陡增</td><td>系统化的思维能力</td><td>越学越吃力，越补越被动</td></tr>
      </tbody>
    </table>
  </div>
  <div class="tips-box">💡 <strong>这是最有说服力的一条：</strong>家长常说「我家孩子现在成绩挺好的，不需要」。你要回应——<strong>三年级以前看不出差别，恰恰是最危险的信号</strong>。等到四年级现出原形，思维习惯已经基本定型，补起来要花好几倍力气。</div>
</div>

<div class="why-block">
  <div class="wb-head"><div class="wb-ico">⚡</div><div class="wb-h">好处三 · 高效率解决问题</div></div>
  <div class="wb-b">
    一谈到数学学习，大家首先想到的就是「会解题」。确实，解决数学问题是数学学习的重要方面，新课标也要求「学生在学习基础知识和掌握基本技能的同时，不断积累解决数学问题的活动经验，获取分析问题和解决问题的能力」。<br><br>
    培养孩子有效的<strong>思维活动方法</strong>，建立相对全面的<strong>数学思维模型</strong>，条理性分析、找出问题的异同与关键点进行解答，从而提高解决问题的能力和效率。
  </div>
</div>

<div class="why-block">
  <div class="wb-head"><div class="wb-ico">🌟</div><div class="wb-h">好处四 · 意志品质的锻炼</div></div>
  <div class="wb-b">
    抓住幼儿的<strong>数学敏感期</strong>——大部分孩子刚学数学时都是兴趣盎然、信心十足的，但随着课程深入、难度越来越大，这时候对孩子的意志力是一种考验。<br><br>
    少部分孩子凭借天分钻研进去、通过努力得到了一定成效；大多数孩子则需要在家长的陪伴、引导下才能完成学习。<br><br>
    但不论学得如何，<strong>贵在坚持</strong>——这个过程培养的是孩子对数学思维锻炼的兴趣度和<strong>钻研精神</strong>，而这种思维品质对于今后孩子在数学学习方面、面对困难挫折方面，都有着至关重要的作用。
  </div>
</div>

<div class="why-block">
  <div class="wb-head"><div class="wb-ico">😊</div><div class="wb-h">好处五 · 增强自信心</div></div>
  <div class="wb-b">
    数学思维跟我们的生活息息相关。比如<strong>有序思考</strong>，能让你做事分清主次、提高时间管理能力；<strong>正向与逆向思考</strong>能提高解决问题的能力，让自己更有办法；<strong>发散思考</strong>能让你变得更有创意；<strong>逻辑思考</strong>能提高办事效率以及语言表达能力……<br><br>
    这就是数学思维带给我们的益处——让我们能够多角度地观察事物，跳出思维的局限性，用创造性思维去解决问题。一件事，当你能够通过不一样的思路去看待时，你就能够发现不一样的解决方法。<br><br>
    当孩子做任何事情都有条有理、思路清晰，形成<strong>良性循环</strong>，做起事情来也会事半功倍、更有信心。
  </div>
</div>

<div class="card">
  <h2 class="card-title">📋 五大好处速查表（沟通时随手可用）</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>好处</th><th>一句家长听得懂的话</th></tr></thead>
      <tbody>
        <tr><td><strong>打好学科基础</strong></td><td>「数理化靠逻辑推理，语文英语靠理解分析，这些底子都是思维给的。」</td></tr>
        <tr class="tr-hot"><td><strong>开拓解题思路</strong></td><td>「三年级以前靠记，四年级以后靠想——不早点练思维，越往后越吃力。」</td></tr>
        <tr><td><strong>高效解决问题</strong></td><td>「会思维的孩子，用更少的功夫拿同样的结果。」</td></tr>
        <tr><td><strong>锻炼意志品质</strong></td><td>「难度上来时能不能坚持钻研，靠的是这几年养成的习惯。」</td></tr>
        <tr><td><strong>增强自信心</strong></td><td>「孩子做事有条理、有办法，自然越来越有底气。」</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="reflect-box">
  <span class="rt">📝 本章小结 · 一句话记住第 2 章</span>
  学数学思维不是为了一门课，而是为孩子装上一套<strong>「怎么想问题」的底层系统</strong>——它同时喂养学科成绩、学习方法、抗挫能力和自信心。
</div>
'''

# ============================================================
# 第三章：为什么必须重视思维培养（三大理由）
# ============================================================
CH3 = '''
<div class="section-header">
  <span class="section-badge">第 3 章</span>
  <h1>为什么必须重视思维培养</h1>
  <p class="duration">⏱ 学习时长：10-12 分钟 ｜ 📝 含 3 道章节测验</p>
</div>

<div class="activate-box">
  <span class="at">🔎 家长最常说的拖延理由</span>
  「现在是小学，没那么急吧？等初中再说。」<br>
  <strong>这一章给你三个「不能等」的理由——政策在变、人才需求在变、孩子的时间窗口在关。</strong>
</div>

<div class="reason-cards">
  <div class="reason-card rc-a">
    <span class="rc-tag">理由一</span>
    <div class="rc-h">政策风向变了：国家直接喊停「填鸭式教育」</div>
    <div class="rc-b">新课标明确提出，数学核心素养的培养重点<strong>从单纯的计算能力，转向逻辑推理和抽象建模能力</strong>——这体现了教育理念的深刻变革。</div>
  </div>
  <div class="reason-card rc-b">
    <span class="rc-tag">理由二</span>
    <div class="rc-h">国家战略：科技人才缺口与数理思维的重要性</div>
    <div class="rc-b">目前我国面临科技人才的巨大缺口，<strong>预计到 2030 年将达到 600 万</strong>。数理思维作为人工智能时代的基础能力，对培养科技人才至关重要。</div>
  </div>
  <div class="reason-card rc-c">
    <span class="rc-tag">理由三</span>
    <div class="rc-h">关键期警示与脑科学依据</div>
    <div class="rc-b">脑科学研究表明，<strong>12 岁之前是孩子逻辑思维发展的黄金时期</strong>。一旦错过这个阶段，思维模式可能会逐渐固化，难以进行有效的调整和改变。</div>
  </div>
</div>

<div class="card">
  <h2 class="card-title">📜 理由一详解 · 政策风向：从「算得快」到「想得清」</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>变化方向</th><th>过去</th><th>现在（新课标）</th></tr></thead>
      <tbody>
        <tr><td><strong>数学核心素养</strong></td><td>重点考核单纯的计算能力</td><td>转向<strong>逻辑推理和抽象建模能力</strong></td></tr>
        <tr class="tr-hot"><td><strong>中高考命题趋势</strong></td><td>靠反复刷题、记题型可取高分</td><td>压轴题<strong>淘汰「伪学霸」</strong>，考察「概念关联分析」与「创新解题能力」</td></tr>
        <tr><td><strong>命题深度</strong></td><td>难在计算量</td><td>难度和区分度不断提高，旨在筛选出<strong>真正具备数学思维能力</strong>的学生</td></tr>
      </tbody>
    </table>
  </div>
  <div class="tips-box">💡 <strong>怎么说给家长听：</strong>「以前拼谁刷题多，现在拼谁真的会想。中高考压轴题就是在淘汰靠刷题堆出来的『伪学霸』——孩子如果只会套题型，越到高年级越吃亏。」</div>
</div>

<div class="card">
  <h2 class="card-title">🇨🇳 理由二详解 · 国家战略：人才缺口与职场预演</h2>
  <div class="stat-box">
    <div class="stat-item">
      <div class="st-n">600 万</div>
      <div class="st-l">预计到 2030 年<br>我国科技人才缺口</div>
    </div>
    <div class="stat-item">
      <div class="st-n">&lt; 30%</div>
      <div class="st-l">谷歌、华为等名企<br>逻辑推理测试的通过率</div>
    </div>
    <div class="stat-item">
      <div class="st-n">1 : 3</div>
      <div class="st-l">1 小时思维训练<br>≈ 3 小时无效刷题</div>
    </div>
  </div>
  <div class="why-block" style="margin-top:18px;">
    <div class="wb-head"><div class="wb-ico">🏢</div><div class="wb-h">职场预演：名企在招人时就考逻辑</div></div>
    <div class="wb-b">
      在职场中，许多知名企业如<strong>谷歌、华为</strong>等在招聘过程中都设置了<strong>逻辑推理测试</strong>，以此来筛选出具有优秀思维能力的人才。<br><br>
      然而数据显示，这些逻辑推理测试的<strong>通过率不足 30%</strong>——这说明在当前的教育体系中，学生的思维能力培养还存在很大的不足。
    </div>
  </div>
  <div class="why-block">
    <div class="wb-head"><div class="wb-ico">💰</div><div class="wb-h">投入产出比：1 小时思维训练 ＝ 3 小时无效刷题</div></div>
    <div class="wb-b">
      从教育投资的性价比来看，思维训练具有显著优势。研究表明，<strong>1 小时的思维训练相当于 3 小时的无效刷题</strong>。<br><br>
      这意味着通过系统的思维训练，学生可以在<strong>更短的时间内取得更好的学习效果</strong>，提高学习效率，为未来的发展奠定基础。
    </div>
  </div>
  <div class="reflect-box">
    <span class="rt">📣 沟通转化：把「国家大事」说成「你家孩子的账」</span>
    家长对「国家战略」往往无感，你要落到他自己的投入产出上：<br>
    「您给孩子报班，本质是买时间。同样的时间，<strong>练思维的孩子能得到 3 倍的效果</strong>——这不是我编的，是研究数据。您是想让孩子把时间花在『1 小时顶 1 小时』的重复刷题上，还是『1 小时顶 3 小时』的思维训练上？」
  </div>
</div>

<div class="card">
  <h2 class="card-title">🧠 理由三详解 · 关键期：为什么必须是 12 岁以前</h2>
  <div class="def-card">
    <div class="def-q">⏰ 12 岁之前，是孩子逻辑思维发展的黄金时期。</div>
    <div class="def-a">
      脑科学研究表明，这个阶段孩子的大脑可塑性最强、思维模式尚未定型。<strong>一旦错过这个阶段，思维模式可能会逐渐固化，难以进行有效的调整和改变。</strong><br><br>
      这就是为什么「等初中再说」是最危险的想法——等到初中，孩子的思维方式已经在小学阶段「长成」了，改起来事倍功半。
    </div>
  </div>
  <div class="say-compare">
    <div class="say-col say-bad">
      <div class="sc-h">❌ 家长常见的认知误区</div>
      <ul>
        <li>「小学成绩好就行，思维以后再说」</li>
        <li>「多刷题就能提分，报思维班没必要」</li>
        <li>「等初中难度上来了自然会重视」</li>
        <li>把思维培养当成「锦上添花」</li>
      </ul>
    </div>
    <div class="say-col say-good">
      <div class="sc-h">✅ 市场真相与正确认知</div>
      <ul>
        <li>当前市场上许多家长仍<strong>过度依赖刷题</strong>提升成绩</li>
        <li>由此<strong>忽视、错过了思维能力的黄金培养期</strong></li>
        <li>成绩是结果，思维才是原因——因上努力才有效</li>
        <li>思维培养是<strong>不可逆的投资窗口</strong>，过时不补</li>
      </ul>
    </div>
  </div>
  <div class="tips-box">💡 <strong>这句话要说得郑重：</strong>「我不是催您现在花钱，而是提醒您——有些窗口关上了就真的关上了。12 岁前思维还能『塑形』，12 岁后只能『修补』。您现在做的决定，是在孩子的黄金期里下注。」</div>
</div>

<div class="card">
  <h2 class="card-title">📋 三大理由速查表</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>维度</th><th>核心事实</th><th>对家长的一句话</th></tr></thead>
      <tbody>
        <tr><td><strong>政策风向</strong></td><td>新课标转向逻辑推理与抽象建模；中高考压轴题淘汰「伪学霸」</td><td>「拼刷题的时代过去了，现在拼真会想。」</td></tr>
        <tr><td><strong>国家战略</strong></td><td>2030 年科技人才缺口 600 万；名企逻辑测试通过率不足 30%；1 小时思维训练 = 3 小时刷题</td><td>「未来要的人才会想，不是会背。」</td></tr>
        <tr class="tr-hot"><td><strong>关键期</strong></td><td>12 岁前是逻辑思维黄金期，错过难调整</td><td>「黄金期不等人，错过了补起来要好几倍力气。」</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="reflect-box">
  <span class="rt">📝 本章小结 · 三个「不能等」</span>
  ① 政策<strong>不能等</strong>——评价标准已经变了。<br>
  ② 需求<strong>不能等</strong>——未来职场考的正是思维能力。<br>
  ③ 时间<strong>不能等</strong>——12 岁前的黄金期，过去了就不再回来。
</div>
'''

# ============================================================
# 第四章：3-12 岁儿童思维发展特点
# ============================================================
CH4 = '''
<div class="section-header">
  <span class="section-badge">第 4 章</span>
  <h1>3-12 岁儿童思维发展特点</h1>
  <p class="duration">⏱ 学习时长：10-12 分钟 ｜ 📝 含 3 道章节测验</p>
</div>

<div class="activate-box">
  <span class="at">🔎 这一章解决一个高频沟通难题</span>
  家长问：「我家孩子这个年纪，学思维到底在学什么？会不会太早？」<br>
  <strong>懂发展阶段，你就能用「孩子现在在哪、下一步会变难在哪」两句话说清楚——这是最专业的回答。</strong>
</div>

<div class="card">
  <h2 class="card-title">🔬 皮亚杰认知发展四阶段</h2>
  <p style="margin-bottom:16px;">当代著名认知心理学家<strong>皮亚杰</strong>在多年的观察、研究基础上，提出了独特的儿童思维发展阶段理论，认为儿童的思维发展分为<strong>四个阶段</strong>。这是我们理解孩子「为什么现在学这个」的理论地基。</p>
  <div class="stage-axis">
    <div class="axis-node">
      <div class="an-age">0~2 岁</div>
      <div class="an-h">感知运动阶段</div>
      <div class="an-d">直觉行动思维</div>
    </div>
    <div class="axis-arrow">→</div>
    <div class="axis-node an-hot">
      <div class="an-age">2~6/7 岁</div>
      <div class="an-h">前运算阶段</div>
      <div class="an-d">具体形象思维</div>
    </div>
    <div class="axis-arrow">→</div>
    <div class="axis-node an-hot">
      <div class="an-age">6/7~11/12 岁</div>
      <div class="an-h">具体运算阶段</div>
      <div class="an-d">逻辑抽象思维萌芽</div>
    </div>
    <div class="axis-arrow">→</div>
    <div class="axis-node">
      <div class="an-age">11/12~14/15 岁</div>
      <div class="an-h">形式运算阶段</div>
      <div class="an-d">逻辑抽象思维</div>
    </div>
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>阶段</th><th>年龄</th><th>思维水平</th><th>典型特征</th></tr></thead>
      <tbody>
        <tr><td><strong>感知运动阶段</strong></td><td>0~2 岁</td><td>直觉行动思维</td><td>为了对付当前世界，婴儿组织天然的动作图式，如吮吸、抓握、打击等；在主观与客体交往中，逐渐实现感觉与动作的分化和精确化。</td></tr>
        <tr class="tr-hot"><td><strong>前运算阶段</strong></td><td>2~6/7 岁</td><td>具体形象思维</td><td>由于语言的参与，儿童学会了用符号和内部想象去思维，但其思维不够系统且不具备可逆性，有极强的「自我中心主义」。</td></tr>
        <tr class="tr-hot"><td><strong>具体运算阶段</strong></td><td>6/7~11/12 岁</td><td>逻辑抽象思维萌芽</td><td>儿童发展了有条不紊地思维的能力，可以进行简单抽象思维；守恒观念形成，但仅仅在能借助于具体对象与活动时才可能这样做。</td></tr>
        <tr><td><strong>形式运算阶段</strong></td><td>11/12~14/15 岁</td><td>逻辑抽象思维</td><td>能够根据逻辑推理、归纳或演绎方式来解决问题；能理解符号意义、隐喻和直喻，能做一定的概括；思维具有可逆性、补偿性和灵活性。</td></tr>
      </tbody>
    </table>
  </div>
  <div class="tips-box">💡 <strong>沟通要点：</strong>3-12 岁正好横跨<strong>前运算阶段</strong>与<strong>具体运算阶段</strong>——这是孩子从「具体形象思维」向「逻辑抽象思维」过渡的关键窗口。你教的每一个思维方法，都是在帮孩子完成这次跨越。</div>
</div>

<div class="card">
  <h2 class="card-title">🧒 幼儿思维发展特点（前运算阶段 · 以具体形象思维为主）</h2>
  <div class="trait-box" style="margin-top:0;">
    <ul class="trait-list">
      <li><span class="tl-k">单向思维</span><span>思维具有<strong>不可逆性</strong>——知道 3+2=5，但算不出 5−2。</span></li>
      <li><span class="tl-k">模仿思维</span><span>喜欢模仿，但只能<strong>简单模仿</strong>，还不会举一反三。</span></li>
      <li><span class="tl-k">具体思维</span><span>能够理解代表<strong>实际事物</strong>的概念，不能理解抽象概念。</span></li>
      <li><span class="tl-k">形象思维</span><span>依靠<strong>头脑、形状、声音</strong>进行思考。</span></li>
      <li><span class="tl-k">表象思维</span><span>只能看到事物的<strong>表面现象</strong>，不能看到本质特点。</span></li>
    </ul>
  </div>
  <div class="reflect-box">
    <span class="rt">📣 这段怎么讲给家长听</span>
    「这个阶段的孩子，你跟他讲道理他听不懂，但你给他看、给他摆、给他动手操作，他立刻就明白了——因为他的思维是<strong>看得见、摸得着</strong>的。所以我们上课都从具体情景和教具入手，让孩子在操作里把思维『长』出来。」
  </div>
</div>

<div class="card">
  <h2 class="card-title">🎒 小学生思维发展特点（具体运算阶段 · 以抽象逻辑思维萌芽为主）</h2>
  <div class="trait-box tb-b" style="margin-top:0;">
    <div class="tb-head">具体运算阶段以抽象逻辑思维萌芽为主</div>
    <div class="tb-sub">孩子开始能「在脑子里想」，但还需要具体事物撑腰</div>
    <ul class="trait-list">
      <li><span class="tl-k amber">接受与理解能力提高</span><span>能吸收更复杂的信息，听得懂推理过程。</span></li>
      <li><span class="tl-k amber">理解更有组织、有条理</span><span>思考从零散变得系统、更准确。</span></li>
      <li><span class="tl-k amber">思维独立性与发散性发展快</span><span>开始有自己的思路，能想出多种办法。</span></li>
    </ul>
  </div>
  <div class="two-trait">
    <div class="trait-box">
      <div class="tb-head">幼儿（前运算）</div>
      <div class="tb-sub">以具体形象思维为主</div>
      <ul class="trait-list">
        <li><span class="tl-k">教学方式</span><span>看得到、摆得出、动手做</span></li>
        <li><span class="tl-k">沟通话术</span><span>用实物和情景描述，少讲抽象概念</span></li>
      </ul>
    </div>
    <div class="trait-box tb-b">
      <div class="tb-head">小学生（具体运算）</div>
      <div class="tb-sub">以抽象逻辑思维萌芽为主</div>
      <ul class="trait-list">
        <li><span class="tl-k amber">教学方式</span><span>在具体支撑下，引入推理与抽象</span></li>
        <li><span class="tl-k amber">沟通话术</span><span>可以开始讲「方法」和「为什么」</span></li>
      </ul>
    </div>
  </div>
  <div class="tips-box">💡 <strong>一句话对比记忆：</strong>幼儿是「看见了才懂」，小学生是「想着也能懂，但还需要例子帮忙」。所以小学阶段的孩子，正是引入<strong>思维方法训练</strong>的最佳时机。</div>
</div>

<div class="card">
  <h2 class="card-title">🎓 落地到课堂：以学生为主体的引导式教学</h2>
  <p style="margin-bottom:14px;">知道了孩子的思维特点，教学方式就必须跟着变——不能灌，要引导。豌豆是这样培养孩子数学思维的：</p>
  <div class="teach-flow">
    <div class="teach-item">
      <div class="ti-n">1</div>
      <div class="ti-h">引导孩子多思考</div>
      <div class="ti-b">设置<strong>生活化场景</strong>，进行问题互动——比如「家用设施多维度分类」，让孩子在熟悉的场景里动脑。</div>
    </div>
    <div class="teach-item">
      <div class="ti-n">2</div>
      <div class="ti-h">综合应用</div>
      <div class="ti-b">在课程中孩子学到了知识，再碰到<strong>同样类型</strong>的问题时可以直接解决，做到<strong>举一反三</strong>。</div>
    </div>
    <div class="teach-item">
      <div class="ti-n">3</div>
      <div class="ti-h">善于总结，精准表达</div>
      <div class="ti-b">孩子要将所学所感，<strong>用自己的语言总结并表达</strong>出来，从侧面训练孩子的逻辑思维。</div>
    </div>
    <div class="teach-item">
      <div class="ti-n">4</div>
      <div class="ti-h">以学生为主体</div>
      <div class="ti-b">老师在课堂上会根据每个阶段孩子的特点进行引导，鼓励孩子<strong>自主探索、主动学习、做好总结</strong>。</div>
    </div>
  </div>
  <div class="reflect-box">
    <span class="rt">📣 这是最能体现专业度的一段</span>
    「我们不直接把答案讲给孩子，而是请他<strong>自己说一遍</strong>——孩子能把思路用自己的话讲清楚，才说明他真的懂了。这个『说出来』的过程，本身就是在训练逻辑思维。」
  </div>
</div>

<div class="card">
  <h2 class="card-title">📚 阶段速查库 · 家长问「这个年纪学什么」时的答案</h2>
  <p style="margin-bottom:8px;">点开对应阶段，看看「这一阶段能培养什么」和「下一阶段会变难在哪」——这两句连起来用，最有说服力。</p>
  <div id="levelLibrary"></div>
</div>

<div class="reflect-box">
  <span class="rt">📝 本章小结 · 一张图记住第 4 章</span>
  皮亚杰四阶段 = <strong>感知运动（0-2）→ 前运算（2-6/7）→ 具体运算（6/7-11/12）→ 形式运算（11/12-15）</strong>。<br>
  3-12 岁正好跨越中间两个阶段：幼儿靠<strong>具体形象</strong>，小学生<strong>抽象逻辑开始萌芽</strong>。教学要引导，不要灌输。
</div>
'''

# ============================================================
# 第五章：家长沟通实战 + 终极考核
# ============================================================
CH5 = '''
<div class="section-header">
  <span class="section-badge">第 5 章</span>
  <h1>家长沟通实战 · 把理念说清楚、说到心里</h1>
  <p class="duration">⏱ 学习时长：18-22 分钟 ｜ 🏆 含终极考核（综合选择题 + 情境演练）</p>
</div>

<div class="activate-box">
  <span class="at">🔎 前三章你学的是「是什么」，这一章练的是「怎么说」</span>
  理论再扎实，说不进家长心里也没用。<br>
  <strong>这一章给你四个说明角度、一批可直接用的话术，以及四个真实场景的开口练习。</strong>
</div>

<div class="card">
  <h2 class="card-title">🎯 家长沟通四大说明角度（核心框架）</h2>
  <p style="margin-bottom:14px;">面对「学思维有什么用／要不要学／现在急不急」这类问题，你不需要背长篇大论，只要抓住下面四个角度中的<strong>一到两个</strong>，就能讲得清楚又有力。</p>
  <div class="angle-cards">
    <div class="angle-card ac-1">
      <div class="ac-h">① 能力价值角度</div>
      <div class="ac-core">核心：思维是不可替代的底层能力</div>
      <div class="ac-say">「数学的<strong>逻辑推理、几何直观、数据处理</strong>能力，是别的科目练不出来的。孩子现在练的不是一道题，是以后学数理化、看数据、解决实际问题的底层能力。」</div>
    </div>
    <div class="angle-card ac-2">
      <div class="ac-h">② 学习规律角度</div>
      <div class="ac-core">核心：四年级是分水岭，思维必须提前练</div>
      <div class="ac-say">「三年级以前靠记公式就能考好，<strong>四年级以后靠的是分析方法</strong>。如果思维没跟上，孩子解题方式还停在低年级，成绩就会一下子掉下来——这是很多家长的共同经历。」</div>
    </div>
    <div class="angle-card ac-3">
      <div class="ac-h">③ 时间窗口角度</div>
      <div class="ac-core">核心：12 岁前是黄金期，错过难补</div>
      <div class="ac-say">「脑科学表明，<strong>12 岁前是逻辑思维的黄金期</strong>。这时候思维还能塑形，过了这个阶段就基本定型了。我不是催您，是真心不希望孩子错过这个窗口。」</div>
    </div>
    <div class="angle-card ac-4">
      <div class="ac-h">④ 时代趋势角度</div>
      <div class="ac-core">核心：评价标准变了，拼的是会想</div>
      <div class="ac-say">「新课标已经把重点从『算得快』转到『<strong>想得清</strong>』，中高考压轴题专门淘汰只会刷题的孩子。连谷歌、华为招人都考逻辑推理——未来要的人才是会思考的，不是会背题的。」</div>
    </div>
  </div>
  <div class="tips-box">💡 <strong>使用要点：</strong>不要四个角度一次全倒给家长——那会像背课文。<strong>先共情，再挑最贴合的一个角度说透</strong>，剩下的等家长追问时再补。这才是「有说服力」的样子。</div>
</div>

<div class="card">
  <h2 class="card-title">🗣 表达示例 · 同一件事，换个说法效果差很多</h2>
  <p style="margin-bottom:14px;">沟通的分水岭往往不在「说什么」，而在「怎么说」。下面三组对照，左边是家长听不懂的版本，右边是能进心里的版本。</p>
  <div class="say-compare">
    <div class="say-col say-bad">
      <div class="sc-h">❌ 这样说，家长容易走神</div>
      <ul>
        <li>「我们培养的是孩子的数学思维能力。」</li>
        <li>「思维训练很重要，对孩子帮助很大。」</li>
        <li>「现在不学，以后就跟不上了。」</li>
      </ul>
    </div>
    <div class="say-col say-good">
      <div class="sc-h">✅ 这样说，家长听得进去</div>
      <ul>
        <li>「同样是算一道题，有的孩子埋头硬算，有的孩子先想一步用巧办法——这就是思维训练教的东西。」</li>
        <li>「三年级以前看不出来，四年级一上难度，孩子是『会想』还是『只会套』，差距一下子就拉开了。」</li>
        <li>「12 岁前思维还能塑形，过了这个阶段就只能修补了——趁现在还来得及。」</li>
      </ul>
    </div>
  </div>
  <div class="table-wrap" style="margin-top:18px;">
    <table>
      <thead><tr><th>沟通技巧</th><th>怎么做</th><th>为什么有效</th></tr></thead>
      <tbody>
        <tr><td><strong>先共情再讲理</strong></td><td>家长说「孩子成绩还行」，先接「能理解，孩子确实表现不错」，再引出「正因为不错，更要提前铺路」</td><td>不反驳、不争辩，家长才愿意听下去</td></tr>
        <tr><td><strong>用孩子举例</strong></td><td>把抽象理念落到「这孩子」身上的具体表现</td><td>从「泛泛而谈」变成「说的是我家孩子」</td></tr>
        <tr class="tr-hot"><td><strong>把道理翻成账</strong></td><td>「1 小时思维训练 ＝ 3 小时无效刷题」</td><td>家长关心投入产出，数字最有冲击力</td></tr>
        <tr><td><strong>讲窗口不讲恐惧</strong></td><td>说「现在还来得及」，不说「晚了就完了」</td><td>给动力，不给焦虑，家长才不会防御</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="card" style="border-top:4px solid var(--primary);">
  <div id="scenarioDrillContainer" class="drill-section"></div>
</div>

<div class="reflect-box">
  <span class="rt">📝 复习最后一遍</span>
  闭上眼把四个角度跑一遍：<strong>能力价值 → 学习规律 → 时间窗口 → 时代趋势</strong>。<br>
  再想想：如果家长说「我家孩子成绩挺好的，不用学这个」，你会先共情哪一句，再挑哪个角度说透？<strong>想清楚了，就回到上面的情境演练写下你的应答，再去完成下方的终极考核选择题。</strong>
</div>
'''

# ============================================================
# 选择题（12 题，分布在第 1-4 章，每章 3 题）
# ============================================================
CH1_Q = [
    {
        'q': '关于「思维」的定义，下列说法最准确的是？',
        'opts': [
            '思维就是记住知识点的能力，记得越牢思维越强',
            '思维是人类认识活动的最高形式，通过对事物的分析、比较、综合、抽象和概括，间接反映事物本质',
            '思维就是反应速度，谁算得快谁思维好',
            '思维是天生的，后天无法培养'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。思维是认识活动的最高形式，核心在于「分析、比较、综合、抽象、概括」这一系列过程，是一种间接反映事物本质的认识活动。记住定义不等于有思维——这正是你要跟家长区分开的一点。',
        'feedback_wrong': '❌ 再想想思维的定义。思维不是「记得牢」，也不是「算得快」，更不是天生的。它是在分析、比较、综合、抽象、概括中，间接反映事物本质的认识活动。建议回顾第 1 章「思维是什么」。'
    },
    {
        'q': '关于「数学的重要性」，下列哪一项是 PPT 中特别强调、且其它学科不可替代的？',
        'opts': [
            '数学能提高孩子的记忆力',
            '数学是考试分值最高的科目',
            '数学在几何直观能力、运算能力、逻辑推理能力、数据处理能力等方面是其它学科不可替代的',
            '数学能让孩子变得更细心'
        ],
        'correct': 2,
        'feedback_correct': '✅ 对。数学在几何直观、运算、逻辑推理、数据处理这几方面的训练作用不可替代——这是你跟家长强调「必要性」时最有力的一句：这些能力换个科目补不上来。',
        'feedback_wrong': '❌ 注意题干在问「其它学科不可替代」的能力。分值高、能提记忆力、让人更细心都不是数学独有的。数学独有的是几何直观、运算、逻辑推理、数据处理能力。建议回顾第 1 章「数学为什么重要」。'
    },
    {
        'q': '「数学思维」的正确定义是？',
        'opts': [
            '快速完成计算题的能力',
            '把公式背熟并套用的能力',
            '用数学的方法去思考问题和解决问题的能力',
            '对数字特别敏感的天赋'
        ],
        'correct': 2,
        'feedback_correct': '✅ 对。数学思维 ＝ 用数学的方法（逆向、分类讨论、枚举、建模分析等）去思考问题和解决问题的能力。定义里的关键词是「数学方法」，而不是「计算速度」。',
        'feedback_wrong': '❌ 数学思维不等于「算得快」或「背得熟」。它的定义是：用数学的方法去思考问题和解决问题的能力——重点是「方法」二字。建议回顾第 1 章「什么是数学思维」。'
    },
]

CH2_Q = [
    {
        'q': '家长问「学这个思维到底有什么用」，下列哪一组是 PPT 中提到的「学习数学思维的好处」？',
        'opts': [
            '提高记忆力、缩短做题时间、增加考试分数',
            '为其他学科打好基础、开拓解题思路、高效率解决问题、增强自信心、意志品质的锻炼',
            '让孩子变安静、更听话、更爱学习',
            '提前学完高年级课程、跳级、拿竞赛奖'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。五大好处是：为其他学科打好基础、开拓解题思路、高效率解决问题、增强自信心、意志品质的锻炼。回答家长时按需挑一两条说透即可，不要一次全倒。',
        'feedback_wrong': '❌ 注意区分「功利的短期结果」和 PPT 里真正强调的五大好处。正确答案是：为其他学科打好基础、开拓解题思路、高效率解决问题、增强自信心、意志品质的锻炼。建议回顾第 2 章。'
    },
    {
        'q': '关于「开拓解题思路」这一好处，PPT 的核心论证是什么？',
        'opts': [
            '小学三年级以前靠记住定义和公式就能解题（重在一个「套」字），四年级以后必须有学习方法，否则进入初高中难度陡增时成绩会一落千丈',
            '只要多做题，解题思路自然就开阔了',
            '数学思维能让孩子考试时更冷静',
            '思维能力强的孩子不用写作业'
        ],
        'correct': 0,
        'feedback_correct': '✅ 对。关键论证是「三年级以前靠套，四年级以后靠想」。不进行思维训练，进入初高中后课程难度陡增，孩子解题方式却停留在初级阶段，成绩自然一落千丈——这是说服家长「提前练」最有力的论据。',
        'feedback_wrong': '❌ 再想想这条好处的论证逻辑。核心是「三年级以前靠套公式，四年级以后必须有方法」，否则初高中难度上来后成绩会一落千丈。多做题并不等于开拓思路。建议回顾第 2 章「开拓解题思路」。'
    },
    {
        'q': '关于「意志品质的锻炼」这一好处，下列说法正确的是？',
        'opts': [
            '孩子学数学必须靠天分，努力没用',
            '大部分孩子刚学数学时兴趣盎然、信心十足，随着难度增大对意志力是考验；贵在坚持，这个过程培养的兴趣度和钻研精神对今后面对困难挫折都至关重要',
            '只要孩子学得好，意志品质自然就强',
            '学了数学思维，孩子就不会怕困难了'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。大部分孩子一开始都是兴趣盎然的，难度上来后考验的是意志力。多数孩子需要在家长陪伴引导下完成学习——贵在坚持，而这过程养成的钻研精神，是受用一生的思维品质。',
        'feedback_wrong': '❌ 注意「天分」和「意志品质」的区别。PPT 强调的是：难度递增时对意志力是考验，多数孩子需要家长陪伴引导才能坚持，而这个过程养成的钻研精神对今后面对困难挫折至关重要。建议回顾第 2 章「意志品质的锻炼」。'
    },
]

CH3_Q = [
    {
        'q': '关于「政策风向变了」，新课标提出的数学核心素养培养重点发生了什么变化？',
        'opts': [
            '从计算能力转向逻辑推理和抽象建模能力',
            '从应用题转向口算题',
            '从逻辑能力转向计算速度',
            '没有变化，只是增加了考试科目'
        ],
        'correct': 0,
        'feedback_correct': '✅ 对。新课标明确提出，数学核心素养的培养重点从单纯的计算能力转向逻辑推理和抽象建模能力。配套的中高考趋势是：压轴题专门淘汰「伪学霸」，考察「概念关联分析」与「创新解题能力」。',
        'feedback_wrong': '❌ 方向反了。新课标的变化是「从单纯的计算能力 → 转向逻辑推理和抽象建模能力」。这跟你跟家长说的「拼刷题的时代过去了，现在拼真会想」是同一件事。建议回顾第 3 章「政策风向」。'
    },
    {
        'q': '关于「国家战略」这一理由，下列哪组数据是 PPT 中提到的？',
        'opts': [
            '科技人才缺口预计到 2030 年达 600 万；名企逻辑推理测试通过率不足 30%；1 小时思维训练相当于 3 小时无效刷题',
            '科技人才缺口预计达 60 万；名企测试通过率不足 50%；1 小时训练相当于 2 小时刷题',
            '未来只需要会计算的工人',
            '数学能力对未来职场没有影响'
        ],
        'correct': 0,
        'feedback_correct': '✅ 对。三组关键数据：① 2030 年科技人才缺口 600 万；② 谷歌、华为等名企逻辑推理测试通过率不足 30%；③ 1 小时思维训练 ≈ 3 小时无效刷题。第三组是家长最买账的「投入产出比」。',
        'feedback_wrong': '❌ 数据记错啦。正确的是：2030 年科技人才缺口<strong>600 万</strong>、名企逻辑推理测试通过率<strong>不足 30%</strong>、1 小时思维训练 ≈ <strong>3 小时</strong>无效刷题。建议回顾第 3 章「国家战略」。'
    },
    {
        'q': '关于「关键期警示」，脑科学研究指出的黄金期和依据是？',
        'opts': [
            '18 岁之前都是黄金期，什么时候开始都来得及',
            '12 岁之前是孩子逻辑思维发展的黄金时期，一旦错过思维模式可能逐渐固化，难以有效调整',
            '6 岁之前必须学完所有思维方法',
            '黄金期这个说法没有科学依据'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。脑科学研究表明，12 岁之前是逻辑思维发展的黄金时期。一旦错过，思维模式可能逐渐固化、难以有效调整——所以「等初中再说」是最危险的想法。',
        'feedback_wrong': '❌ 黄金期的界定是「12 岁之前」。脑科学研究表明，这个阶段思维还能塑形，错过之后可能逐渐固化、难以有效调整。建议回顾第 3 章「关键期警示与脑科学依据」。'
    },
]

CH4_Q = [
    {
        'q': '皮亚杰将儿童思维发展分为四个阶段，正确顺序是？',
        'opts': [
            '具体运算 → 前运算 → 感知运动 → 形式运算',
            '感知运动（0~2岁）→ 前运算（2~6/7岁）→ 具体运算（6/7~11/12岁）→ 形式运算（11/12~14/15岁）',
            '前运算 → 感知运动 → 形式运算 → 具体运算',
            '形式运算 → 具体运算 → 前运算 → 感知运动'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。顺序是：感知运动（0~2岁）→ 前运算（2~6/7岁）→ 具体运算（6/7~11/12岁）→ 形式运算（11/12~14/15岁）。3-12 岁正好横跨前运算与具体运算两个阶段，这是思维培养的关键窗口。',
        'feedback_wrong': '❌ 顺序记反了。正确顺序：感知运动（0~2岁）→ 前运算（2~6/7岁）→ 具体运算（6/7~11/12岁）→ 形式运算（11/12~14/15岁）。建议回顾第 4 章「皮亚杰认知发展四阶段」。'
    },
    {
        'q': '关于「幼儿思维发展特点（前运算阶段）」，下列哪一项不属于 PPT 提到的特点？',
        'opts': [
            '单向思维：思维具有不可逆性',
            '具体思维：能够理解代表实际事物的概念，不能理解抽象概念',
            '抽象思维：已经能熟练进行逻辑演绎推理',
            '表象思维：只能看到事物的表面现象，不能看到本质特点'
        ],
        'correct': 2,
        'feedback_correct': '✅ 对。逻辑演绎推理是<strong>形式运算阶段（11/12 岁以后）</strong>才具备的能力。前运算阶段的幼儿是：单向思维、模仿思维、具体思维、形象思维、表象思维——以具体形象思维为主。',
        'feedback_wrong': '❌ 「抽象思维：能熟练进行逻辑演绎推理」是形式运算阶段（11/12 岁以后）的能力，不属于前运算阶段的幼儿特点。幼儿的五大特点是：单向、模仿、具体、形象、表象思维。建议回顾第 4 章「幼儿思维发展特点」。'
    },
    {
        'q': '关于「小学生思维发展特点（具体运算阶段）」，下列表述正确的是？',
        'opts': [
            '思维完全定型，无法再发展',
            '以抽象逻辑思维萌芽为主；接受和理解能力提高，理解更有组织、有条理，思维独立性和发散性发展快速',
            '只能进行具体形象思维，无法理解任何抽象概念',
            '这个阶段的孩子只能模仿，不能独立思考'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。具体运算阶段以抽象逻辑思维萌芽为主：接受和理解能力提高；理解更有组织、有条理、更准确；思维的独立性和发散性发展快速。所以小学阶段正是引入思维方法训练的最佳时机。',
        'feedback_wrong': '❌ 注意「萌芽」二字。小学生不是「无法抽象」，而是「抽象逻辑思维开始萌芽」——接受理解能力提高、理解更有条理、独立性与发散性发展快。建议回顾第 4 章「小学生思维发展特点」。'
    },
]

# ============================================================
# 第 5 章 · 终极考核综合选择题（3 题）
# 说明：原为填空题，因复习定位改为选择题 —— 与第 1-4 章共用同一套
#       串行锁定选择题机制（renderChapterQuiz / selectChQuizOption）。
#       知识点不变：数学四项能力 / 四年级分水岭 / 12 岁黄金期。
CH5_Q = [
    {
        'q': '向家长说明「数学为什么不可替代」时，PPT 里指出数学特别能训练、且其它学科替代不了的是哪四项能力？',
        'opts': [
            '记忆力、专注力、表达力、创造力',
            '几何直观能力、运算能力、逻辑推理能力、数据处理能力',
            '阅读能力、写作能力、听说能力、书写能力',
            '观察能力、模仿能力、应试能力、竞争能力'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。几何直观、运算、逻辑推理、数据处理这四项，是 PPT 里明确点出的「其它学科不可替代」。跟家长说的时候别停留在「数学很重要」，把这四项摊开讲，说服力立刻不一样。',
        'feedback_wrong': '❌ 还不是这一项。回顾第 1 章「数学为什么重要」——PPT 点名的四项都是能练出来、且可迁移到其它科目的硬能力，不是「记忆力、专注力」这类通用素质。回去再认一遍那四个词，就能选对。'
    },
    {
        'q': '家长说「孩子小学成绩挺好的，没必要学思维」，用「学习规律」角度回应时，最关键要讲清楚哪一句？',
        'opts': [
            '现在不报名，以后就再也补不回来了，过了这个村没这个店',
            '三年级以前靠记公式就能考好，四年级以后比的是分析方法，这往往是孩子成绩拉开的分水岭',
            '成绩好说明孩子已经掌握方法了，完全可以再等等，到初中再说也来得及',
            '小学成绩都是假的，不代表任何东西，必须用思维班重新打基础'
        ],
        'correct': 1,
        'feedback_correct': '✅ 对。这是「学习规律」角度的标准打开方式：先承认成绩好是真的，再点出「四年级以后靠方法」的规律。关键在于讲规律，而不是吓唬家长。',
        'feedback_wrong': '❌ 再想想第 2 章「开拓解题思路」和第 5 章的沟通红线。正确说法聚焦在「三年级以前靠套公式、四年级以后靠方法」的分水岭；「现在不报就完了」属于贩卖恐惧，PPT 明确要求「讲窗口不讲恐惧」；把家长的成绩观察全盘否定也会直接激起防御。'
    },
    {
        'q': '向家长强调「时间窗口」时，下面哪种说法既准确、又符合 PPT 强调的沟通分寸？',
        'opts': [
            '12 岁前是逻辑思维发展的黄金期，这时候思维还能塑形，趁现在开始完全来得及',
            '错过 12 岁就彻底没救了，以后再学一点用都没有',
            '思维要到 12 岁以后才开始定型，所以现在完全不用着急',
            '您家孩子已经过了关键期了，现在只能尽量补，效果不好别怪我们没提前说'
        ],
        'correct': 0,
        'feedback_correct': '✅ 对。既讲清了「12 岁前是黄金期」的事实，又落到「现在还来得及」的行动建议上——这正是 PPT 里「讲窗口不讲恐惧」的要求：给动力，不给焦虑。',
        'feedback_wrong': '❌ 再回顾第 3 章「关键期警示与脑科学依据」。判断这道题要同时满足两个条件：一是年龄窗口说得准，二是符合 PPT 强调的「讲窗口不讲恐惧」——既不能把窗口说成绝望，也不能把事实说反。'
    },
]

# ============================================================
# 第 5 章 · 情境应答演练（4 个场景，关键词自检，不给标准答案）
# ============================================================
SCENARIO_DRILLS = [
    {
        'id': 'd1',
        'title': '家长说：「小学成绩挺好的，没必要学思维吧？」',
        'parent': '孩子现在考试都能考九十多分，我看成绩挺好的呀，学这个思维……是不是没必要？',
        'angles': ['共情承接', '学习规律（四年级分水岭）', '能力价值'],
        'keywords': {
            '共情承接': ['理解', '能理解', '是的', '确实', '看得出来', '恭喜', '高兴', '先', '明白您'],
            '学习规律（四年级分水岭）': ['四年级', '三年级', '分水岭', '套公式', '靠方法', '难度', '以后', '初高中', '拉开'],
            '能力价值': ['思维', '逻辑', '推理', '能力', '举一反三', '方法', '想'],
        },
        'hint': '回顾第 2 章「开拓解题思路」和第 5 章角度②学习规律。先肯定家长（成绩好是好事），再点出「三年级以前靠套公式、四年级以后靠方法」的分水岭，最后落到思维能力本身。',
    },
    {
        'id': 'd2',
        'title': '家长问：「你们说的数学思维，到底教的是什么？」',
        'parent': '我听你们老说数学思维数学思维，可我还是不太明白，这跟平时上课做题有什么区别？',
        'angles': ['给出定义（用数学方法解决问题）', '举具体例子', '对比刷题'],
        'keywords': {
            '给出定义（用数学方法解决问题）': ['数学方法', '方法', '思考', '解决问题', '能力'],
            '举具体例子': ['比如', '例如', '举例', '逆向', '分类', '枚举', '一道题', '硬币', '凑', '圆圈'],
            '对比刷题': ['刷题', '多做', '不一样', '区别', '举一反三', '换个问法', '同样'],
        },
        'hint': '回顾第 1 章「什么是数学思维」和第 5 章角度①能力价值。先用一句话给定义，再举 PPT 里的枚举法案例（如凑硬币、填数字），最后用「同样一道题，会方法的孩子两步就出来了」对比刷题。',
    },
    {
        'id': 'd3',
        'title': '家长问：「孩子才一年级，学思维是不是太早了？」',
        'parent': '我家孩子才一年级，是不是大一点再学更合适？现在学会不会太早、跟不上？',
        'angles': ['阶段特点解释', '时间窗口（12岁前）', '早期培养的价值'],
        'keywords': {
            '阶段特点解释': ['一年级', '这个年纪', '阶段', '具体', '形象', '看得见', '操作', '动手', '特点', '启蒙'],
            '时间窗口（12岁前）': ['12岁', '黄金', '关键期', '窗口', '塑形', '定型', '越早', '脑'],
            '早期培养的价值': ['基础', '习惯', '兴趣', '提前', '打基础', '慢慢', '衔接', '现在'],
        },
        'hint': '回顾第 4 章「幼儿思维发展特点」和第 3 章「关键期警示」。先说明一年级孩子正处于具体形象思维阶段、正好适合用形象化方式启蒙；再点出 12 岁前是黄金期；最后讲现在打基础的价值。',
    },
    {
        'id': 'd4',
        'title': '家长说：「我们作业都写不完，多刷点题不就行了？」',
        'parent': '说实话我觉得多做题最实在。学校作业本来就多，再报个思维班，不如让他多刷两套卷子。',
        'angles': ['共情承接', '投入产出比（1小时=3小时）', '学习规律'],
        'keywords': {
            '共情承接': ['理解', '能理解', '确实', '辛苦', '压力', '都希望', '明白'],
            '投入产出比（1小时=3小时）': ['效率', '3倍', '三倍', '1小时', '一小时', '投入', '产出', '更少', '性价比', '划算'],
            '学习规律': ['方法', '会想', '思路', '四年级', '难题', '举一反三', '刷不完', '越刷', '瓶颈'],
        },
        'hint': '回顾第 3 章「投入产出比」和第 5 章「把道理翻成账」。先共情作业压力，再用「1 小时思维训练 = 3 小时无效刷题」把道理翻成账，最后说明「刷题刷不出方法，到高年级会卡住」。',
    },
]

# ============================================================
# 皮亚杰四阶段速查库（第 4 章折叠卡片）
# ============================================================
STAGE_LIBRARY = [
    {
        'level': '0~2 岁',
        'grade': '感知运动阶段',
        'position': '直觉行动思维 · 靠动作认识世界',
        'hot': False,
        'stuck': [
            ['通过动作认识世界',
             '让婴儿组织天然的动作图式，如吮吸、抓握、打击等',
             '这一阶段还谈不上「学思维」，重点是丰富感官与动作体验，家长不必焦虑。'],
        ],
        'build': [
            '在主观与客体的交往中，逐步实现<strong>感觉与动作的分化与精确化</strong>',
            '建立对物体恒存性的初步认知',
        ],
        'change': [
            '进入前运算阶段后，<strong>语言参与进来</strong>，孩子开始用符号和内部想象思考',
        ],
    },
    {
        'level': '2~6/7 岁',
        'grade': '前运算阶段',
        'position': '具体形象思维 · 以符号与想象思考',
        'hot': True,
        'stuck': [
            ['思维不可逆（单向思维）',
             '知道 3+2=5，但算不出 5−2；只能顺着想，不能倒回去',
             '用「看得见的实物」把过程演示一遍，帮孩子建立可逆的意识。'],
            ['自我中心主义较强',
             '只从自己的角度看问题，不容易理解别人的想法',
             '多用生活场景互动，让孩子在具体情境里体会「换个角度想」。'],
            ['依赖表象、看表面',
             '只看事物的表面现象，抓不住本质特点',
             '通过动手操作与提问，引导孩子说出「为什么」，从表象走向本质。'],
        ],
        'build': [
            '<strong>具体形象思维</strong>：依靠头脑、形状、声音进行思考',
            '能理解代表<strong>实际事物</strong>的概念（尚不能理解抽象概念）',
            '喜欢模仿，为后续思维习惯打下基础',
        ],
        'change': [
            '进入具体运算阶段后，开始发展<strong>有条不紊的思维能力</strong>，可以借助具体对象进行简单抽象思维',
            '守恒观念开始形成',
        ],
    },
    {
        'level': '6/7~11/12 岁',
        'grade': '具体运算阶段',
        'position': '逻辑抽象思维萌芽 · 思维开始成体系',
        'hot': True,
        'stuck': [
            ['抽象还需要具体事物撑着',
             '能推理，但一旦脱离具体对象就容易卡住',
             '课堂上先用具体例子搭桥，再逐步撤掉「拐杖」，练抽象。'],
            ['思维独立性和发散性刚起步',
             '开始有自己的思路，但想到多种办法还不熟练',
             '多给「一题多解」的练习，鼓励孩子说出不同思路。'],
        ],
        'build': [
            '发展<strong>有条不紊的思维能力</strong>，可进行简单抽象思维',
            '<strong>守恒观念</strong>形成（在能借助具体对象与活动时）',
            '接受与理解能力提高，理解更有组织、有条理、更准确',
            '思维的<strong>独立性和发散性</strong>发展快速',
        ],
        'change': [
            '进入形式运算阶段后，思维具备<strong>可逆性、补偿性和灵活性</strong>，能进行完整的逻辑演绎',
        ],
    },
    {
        'level': '11/12~14/15 岁',
        'grade': '形式运算阶段',
        'position': '逻辑抽象思维 · 能演绎与概括',
        'hot': False,
        'stuck': [
            ['前两阶段基础不牢，此时会很吃力',
             '需要抽象推理时，仍习惯退回具体层面想办法',
             '这正是「小学思维没练好、初中掉队」的原因——所以黄金期必须在 12 岁前抓住。'],
        ],
        'build': [
            '能够根据<strong>逻辑推理、归纳或演绎方式</strong>解决问题',
            '能理解符号意义、隐喻和直喻，能做一定的概括',
            '思维具有<strong>可逆性、补偿性和灵活性</strong>',
        ],
        'change': [
            '这一阶段的思维模式是小学阶段逐步「长成」的结果——<strong>此时已很难重塑</strong>',
        ],
    },
]

# ============================================================
# 章节数据
# ============================================================
SECTIONS = [
    {'id': 's1', 'title': '什么是数学思维', 'duration': '10-12分钟', 'icon': '1', 'type': 'content_quiz', 'content': CH1},
    {'id': 's2', 'title': '学习数学思维的好处', 'duration': '10-12分钟', 'icon': '2', 'type': 'content_quiz', 'content': CH2},
    {'id': 's3', 'title': '为什么必须重视思维培养', 'duration': '10-12分钟', 'icon': '3', 'type': 'content_quiz', 'content': CH3},
    {'id': 's4', 'title': '3-12 岁儿童思维发展特点', 'duration': '10-12分钟', 'icon': '4', 'type': 'content_quiz', 'content': CH4},
    {'id': 's5', 'title': '家长沟通实战与终极考核', 'duration': '18-22分钟', 'icon': '🏆', 'type': 'content_quiz', 'content': CH5},
]

CHAPTER_QUIZZES = [CH1_Q, CH2_Q, CH3_Q, CH4_Q, CH5_Q]
