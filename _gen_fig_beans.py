# -*- coding: utf-8 -*-
"""
_gen_fig_beans.py — 生成第 1 章「挑豆子」题图（300 粒豆子示意图）

设计意图（贴合题目设定）：
  - 绿豆是「少数派」，红豆是「多数派」—— 这正是本题的关键：
    直接数绿豆要一颗颗挑；反过来挑出红豆，剩下的就是绿豆，更省事。
  - 画面须让人一眼看出「混在一起、数量不少」，但不必真去数。

输出：_assets/fig_ch1_beans.png（1267x557 左右的宽幅，适配卡片宽度）
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '_assets', 'fig_ch1_beans.png')

W, H = 1400, 640
BG_TOP = (255, 251, 240)
BG_BOTTOM = (255, 243, 224)

# 豆子配色
GREEN = [(74, 152, 78), (96, 172, 92), (60, 133, 68), (112, 183, 105)]
RED = [(190, 62, 54), (211, 84, 71), (166, 48, 44), (224, 110, 92)]

GREEN_TOTAL = 300          # 题目说「三百粒豆子」
GREEN_RATIO = 0.22         # 绿豆占少数（约 66 粒）


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def load_font(size):
    """尽力找一个可用中文字体；找不到就用默认（英文）字体。"""
    candidates = [
        r'C:\Windows\Fonts\msyhbd.ttc',
        r'C:\Windows\Fonts\msyh.ttc',
        r'C:\Windows\Fonts\simhei.ttf',
        r'C:\Windows\Fonts\Deng.ttf',
    ]
    for p in candidates:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_bean(draw, cx, cy, rx, ry, angle, color, hi_alpha=90):
    """画一颗豆子：椭圆 + 高光点。"""
    box = [cx - rx, cy - ry, cx + rx, cy + ry]
    draw.ellipse(box, fill=color)
    # 沿长轴内侧的高光（用更亮的同色系叠加，模拟球面反光）
    hx = cx - rx * 0.32
    hy = cy - ry * 0.30
    draw.ellipse(
        [hx - rx * 0.30, hy - ry * 0.28, hx + rx * 0.30, hy + ry * 0.28],
        fill=lerp(color, (255, 255, 255), 0.42),
    )
    # 描边让豆子在密集排布中仍能分辨
    draw.ellipse(box, outline=lerp(color, (0, 0, 0), 0.30), width=2)


def main():
    img = Image.new('RGB', (W, H), BG_TOP)
    d = ImageDraw.Draw(img)

    # 背景：淡黄→淡橙的横向渐变
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOTTOM, t))

    # ---- 木碗（一个大的椭圆碗底）----
    bowl_w, bowl_h = 1200, 452
    bx0 = (W - bowl_w) // 2
    by0 = 130
    bowl_box = [bx0, by0, bx0 + bowl_w, by0 + bowl_h]

    d.ellipse(bowl_box, fill=(226, 197, 156), outline=(176, 138, 92), width=5)
    inner = [bx0 + 26, by0 + 22, bx0 + bowl_w - 26, by0 + bowl_h - 26]
    d.ellipse(inner, fill=(244, 231, 208), outline=(196, 162, 118), width=3)

    # ---- 撒豆子（在碗内椭圆里均匀铺开）----
    random.seed(20260921)
    cx = (inner[0] + inner[2]) / 2
    cy = (inner[1] + inner[3]) / 2
    ax = (inner[2] - inner[0]) / 2 - 14
    ay = (inner[3] - inner[1]) / 2 - 14

    n_green = int(GREEN_TOTAL * GREEN_RATIO)
    n_red = GREEN_TOTAL - n_green

    # 生成候选位置（拒绝采样保证不重叠）
    beans = []           # (x, y, rx, ry, angle)
    attempts = 0
    target = GREEN_TOTAL
    while len(beans) < target and attempts < 60000:
        attempts += 1
        # 均匀撒在椭圆内
        u = math.sqrt(random.random())
        th = random.random() * 2 * math.pi
        x = cx + ax * u * math.cos(th)
        y = cy + ay * u * math.sin(th)
        rx = random.uniform(11.5, 15.0)
        ry = rx * random.uniform(0.62, 0.72)
        ang = random.uniform(0, 180)
        ok = True
        for (px, py, prx, pry, _a) in beans:
            dx = x - px
            dy = y - py
            if math.hypot(dx, dy) < (rx + prx) * 0.78:
                ok = False
                break
        if ok:
            beans.append((x, y, rx, ry, ang))

    # 决定哪些是绿豆：随机挑出少数，其余为红豆
    idx = list(range(len(beans)))
    random.shuffle(idx)
    green_idx = set(idx[:n_green])

    # 按 y 排序绘制，制造自然的堆叠感
    order = sorted(range(len(beans)), key=lambda i: beans[i][1])
    for i in order:
        x, y, rx, ry, ang = beans[i]
        color = random.choice(GREEN if i in green_idx else RED)
        # 轻微阴影
        d.ellipse([x - rx + 2, y - ry + 3, x + rx + 2, y + ry + 3],
                  fill=(214, 199, 176))
        draw_bean(d, x, y, rx, ry, ang, color)

    img = img.filter(ImageFilter.SMOOTH)

    # ---- 文案标注 ----
    d = ImageDraw.Draw(img)
    f_leg = load_font(25)

    # 左上角标题小卡
    d.rounded_rectangle([40, 32, 400, 94], radius=12, fill=(255, 255, 255),
                        outline=(245, 158, 11), width=3)
    d.text((62, 47), '约 300 粒豆子混在一起', font=load_font(29), fill=(146, 64, 14))

    # 右上角图例（宽度算足，避免被裁）
    leg_w = 372
    lx = W - 40 - leg_w
    ly = 32
    d.rounded_rectangle([lx, ly, W - 40, ly + 62], radius=12,
                        fill=(255, 255, 255), outline=(252, 211, 77), width=3)
    cy_dot = ly + 31
    d.ellipse([lx + 20, cy_dot - 11, lx + 42, cy_dot + 11],
              fill=GREEN[1], outline=lerp(GREEN[1], (0, 0, 0), 0.3), width=2)
    d.text((lx + 52, cy_dot - 16), '绿豆（少数）', font=f_leg, fill=(55, 65, 81))
    d.ellipse([lx + 208, cy_dot - 11, lx + 230, cy_dot + 11],
              fill=RED[1], outline=lerp(RED[1], (0, 0, 0), 0.3), width=2)
    d.text((lx + 240, cy_dot - 16), '红豆（多数）', font=f_leg, fill=(55, 65, 81))

    # 底部提示（两行，避免超宽）
    tips = [
        '绿豆只有一小把，红豆是绝大多数。',
        '想数清绿豆，也可以反过来想：把红豆挑走，剩下的是什么？',
    ]
    box_top = H - 124
    d.rounded_rectangle([40, box_top, W - 40, H - 26], radius=12,
                        fill=(255, 255, 255), outline=(252, 211, 77), width=3)
    f_tip = load_font(30)
    d.text((66, box_top + 16), tips[0], font=f_tip, fill=(120, 53, 15))
    d.text((66, box_top + 58), tips[1], font=f_tip, fill=(120, 53, 15))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, 'PNG', optimize=True)
    print('已生成：', OUT)
    print('豆子总数：', len(beans), '（绿豆约', n_green, '，红子约', n_red, '）')
    print('尺寸：%dx%d' % img.size)


if __name__ == '__main__':
    main()
