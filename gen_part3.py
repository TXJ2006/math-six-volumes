# -*- coding: utf-8 -*-
import os

BASE = r"F:\github主页与个人博客\math-six-volumes"
VOL_CN = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六"}

volumes = [
  (5, "实分析、泛函分析与概率统计", [
    (41, "测度论基础", [
      "集合代数与σ-代数","测度的定义","外测度的构造","Carathéodory延拓定理",
      "Lebesgue外测度","Lebesgue可测集","Lebesgue测度的性质","Borel集",
      "可测集的正则性","不可测集——Vitali集","Banach-Tarski悖论简介",
      "可测函数","简单函数的逼近","几乎处处性质","依测度收敛",
      "Egorov定理","Lusin定理","乘积测度","Fubini定理(测度论版)",
      "Tonelli定理","符号测度","Hahn分解与Jordan分解","Radon-Nikodym定理",
      "测度论在概率论中的地位","本章总结与习题选讲"]),
    (42, "Lebesgue积分", [
      "Lebesgue积分——非负简单函数","Lebesgue积分——非负可测函数",
      "一般可测函数的积分","单调收敛定理","Fatou引理","Lebesgue控制收敛定理",
      "收敛定理的应用","积分与极限交换","Riemann积分与Lebesgue积分的关系",
      "Lebesgue可积的充要条件","逐项积分定理","含参积分的连续性",
      "含参积分的可微性","Lebesgue微分定理","有界变差函数","绝对连续函数",
      "微积分基本定理的推广","积分换元公式","卷积","磨光算子与正则化",
      "Lebesgue-Stieltjes积分","积分不等式综合","Lebesgue积分在Fourier分析中的应用",
      "积分论的完备化视角","本章总结与习题选讲"]),
    (43, "Lp空间与Banach空间", [
      "Lp空间的定义","Hölder不等式","Minkowski不等式","Lp空间的完备性",
      "Lp空间的可分性","稠密子集","L1空间","L2空间的Hilbert结构",
      "L∞空间","Lp的对偶空间","Riesz表示定理(Lp对偶)","赋范空间",
      "Banach空间的定义","完备化","Hahn-Banach定理——解析形式",
      "Hahn-Banach定理——几何形式","开映射定理","闭图像定理",
      "一致有界性原理(Banach-Steinhaus)","弱收敛与弱*收敛","Banach-Alaoglu定理",
      "自反空间","Eberlein-Šmulian定理","Banach空间在PDE中的应用",
      "本章总结与习题选讲"]),
    (44, "Hilbert空间", [
      "内积空间回顾","Hilbert空间的定义","平行四边形恒等式","投影定理",
      "正交分解","正交补","Riesz表示定理","正交系与Bessel不等式",
      "标准正交基","Parseval恒等式","Hilbert空间中的Fourier分析",
      "Gram-Schmidt正交化(无穷维)","可分Hilbert空间的结构","正交投影算子",
      "投影算子的性质","Hilbert空间的直和","弱收敛","紧算子",
      "Hilbert-Schmidt算子","迹类算子","自伴算子的谱定理","正算子与平方根",
      "极分解","Hilbert空间在量子力学中的框架","本章总结与习题选讲"]),
    (45, "有界线性算子与谱理论", [
      "有界线性算子","算子范数","算子空间B(X,Y)","Banach代数初步",
      "可逆算子与Neumann级数","谱与预解集","谱的基本性质","谱半径公式",
      "紧算子的谱","Fredholm替代定理","Riesz-Schauder理论","自伴算子的谱",
      "正规算子的谱","谱定理——紧自伴算子","谱定理——一般自伴算子",
      "谱测度","函数演算","无界算子","闭算子与图",
      "自伴延拓与Friedrichs延拓","本性谱与离散谱","Schrödinger算子",
      "半群与生成元","谱理论的应用","本章总结与习题选讲"]),
    (46, "广义函数与Sobolev空间", [
      "测试函数空间D(Ω)","广义函数(分布)的定义","正则分布","Dirac δ函数",
      "分布的导数","分布导数的例子","分布的卷积","基本解",
      "Schwartz空间S","Fourier变换在S上","缓增分布的Fourier变换",
      "Sobolev空间H^s的定义","Sobolev连续嵌入","Rellich紧嵌入定理",
      "迹定理","Poincaré不等式","椭圆正则性","Lax-Milgram在Sobolev空间中",
      "Sobolev空间的插值","Gagliardo-Nirenberg不等式","Sobolev空间与PDE",
      "分数阶Sobolev空间","Besov空间简介","广义函数在物理中的应用",
      "本章总结与习题选讲"]),
    (47, "概率空间与随机变量", [
      "概率的古典定义","Kolmogorov公理","σ-代数与事件空间","概率测度的性质",
      "条件概率","独立性","全概率与Bayes公式","随机变量的定义",
      "分布函数","离散分布","连续分布与密度","常见连续分布",
      "随机变量的函数","联合分布与边际分布","条件分布与条件期望","数学期望",
      "方差与高阶矩","矩母函数与特征函数","多维随机变量","协方差与相关系数",
      "多维正态分布","条件期望的性质","随机变量的独立性判定",
      "概率论的测度论基础","本章总结与习题选讲"]),
    (48, "极限定理与收敛性", [
      "依概率收敛","几乎必然收敛","Lp收敛","依分布收敛",
      "四种收敛的关系","弱大数律","强大数律(Kolmogorov)","大数律的应用",
      "Borel-Cantelli引理","Kolmogorov零一律","中心极限定理——iid情形",
      "Lindeberg-Lévy定理","Lindeberg-Feller条件","Berry-Esseen定理",
      "CLT的应用","特征函数证明CLT","收敛速度","大偏差原理",
      "Cramér定理","Markov与Chebyshev不等式","Chernoff界","Hoeffding不等式",
      "集中不等式","极限理论的现代发展","本章总结与习题选讲"]),
    (49, "随机过程", [
      "随机过程的定义","有限维分布","平稳过程","离散时间Markov链",
      "转移概率矩阵","常返与暂态","遍历定理","平稳分布",
      "吸收态与吸收时间","连续时间Markov链","生灭过程","Poisson过程",
      "Poisson过程的推广","Brown运动的定义","Brown运动的性质",
      "Brown运动的路径——连续但几乎处处不可微","离散时间鞅","鞅收敛定理",
      "停时与任选停时定理","连续时间鞅","Itô积分","Itô公式",
      "随机微分方程","Feynman-Kac公式","本章总结与习题选讲"]),
    (50, "数理统计", [
      "统计模型与统计量","充分统计量","完备统计量","矩估计法",
      "最大似然估计(MLE)","MLE的渐近性质","Rao-Blackwell定理","Cramér-Rao下界",
      "有效估计","置信区间","枢轴量法","假设检验框架",
      "似然比检验","Neyman-Pearson引理","均匀最优势检验","卡方检验",
      "t检验","F检验与方差分析","非参数统计——秩检验","Kolmogorov-Smirnov检验",
      "贝叶斯统计","先验与后验","共轭先验","统计决策理论",
      "本章总结与习题选讲"]),
  ]),
  (6, "代数、几何与拓扑", [
    (51, "群论", [
      "群的定义与基本例子","子群","循环群","置换群与对称群Sn",
      "群同态与同构","Lagrange定理","陪集与指数","正规子群",
      "商群","同构定理","群的直积","群在集合上的作用",
      "轨道-稳定子定理","Burnside引理","Sylow定理","Sylow定理的应用",
      "有限群的结构","可解群与幂零群","单群","Abel群的结构定理",
      "自由群与生成元关系","群的表示引论","群论在化学中的应用",
      "群论在物理中的应用","本章总结与习题选讲"]),
    (52, "环与域", [
      "环的定义与基本例子","子环与理想","商环","环同态定理",
      "整环","主理想整环(PID)","唯一分解整环(UFD)","Euclid整环",
      "多项式环","多项式的因式分解","Eisenstein判别法","高斯引理",
      "分式域","域的定义与基本性质","域扩张","代数扩张与超越扩张",
      "有限域GF(p^n)","域的特征","分裂域","代数闭域",
      "代数基本定理(代数证明)","有限域的结构","有限域在编码中的应用",
      "环论在数论中的应用","本章总结与习题选讲"]),
    (53, "Galois理论", [
      "域扩张回顾","自同构与Galois群","不变子域","正规扩张",
      "可分扩张","Galois扩张的定义","Galois基本定理","Galois对应",
      "Galois基本定理的证明","有限域的Galois理论","循环扩张",
      "根式可解性","S5的不可解性","Abel-Ruffini定理","尺规作图问题",
      "三等分角的不可能性","倍立方的不可能性","正n边形的可作图性",
      "Galois群的计算","分圆域与分圆多项式","Kummer理论",
      "可解方程与可解群","逆Galois问题","Galois理论在数论中的应用",
      "本章总结与习题选讲"]),
    (54, "点集拓扑", [
      "拓扑空间的定义","开集与闭集","基与子基","内部、闭包与边界",
      "连续映射","同胚","子空间拓扑","乘积拓扑",
      "商拓扑","度量空间回顾","Urysohn度量化定理","Hausdorff分离公理",
      "正则空间与正规空间","Urysohn引理","Tietze延拓定理","紧性",
      "紧性的等价条件","Tychonoff定理","局部紧Hausdorff空间","一点紧化",
      "连通性","道路连通与局部连通","连通分支",
      "Baire纲定理","本章总结与习题选讲"]),
    (55, "代数拓扑", [
      "拓扑不变量的思想","基本群的定义","道路同伦","基本群的计算——S1",
      "覆叠空间","提升定理","覆叠空间的分类","覆叠空间与基本群",
      "Van Kampen定理","自由积","Van Kampen定理的应用","单纯复形",
      "三角剖分","单纯同调","奇异同调","同调群的计算",
      "Euler示性数","同调的长正合列","Mayer-Vietoris序列","上同调初步",
      "de Rham上同调","Brouwer不动点定理","同伦型与同伦等价",
      "高阶同伦群","本章总结与习题选讲"]),
    (56, "微分流形", [
      "微分流形的定义","坐标卡与图册","光滑映射","切空间",
      "切映射","余切空间","切丛与余切丛","向量场",
      "Lie括号","光滑函数环","浸入与嵌入","子流形",
      "Whitney嵌入定理","分布与Frobenius定理","微分形式","外微分",
      "拉回映射","流形上的积分","Stokes定理(流形版)","de Rham上同调",
      "de Rham定理","Poincaré对偶","流形上的定向",
      "流形与物理——相空间","本章总结与习题选讲"]),
    (57, "微分几何", [
      "曲线论与Frenet公式","平面曲线的曲率","空间曲线的曲率与挠率",
      "第一基本形式","第二基本形式","Gauss曲率与平均曲率","测地线",
      "Gauss绝妙定理","Gauss-Bonnet定理","Riemann度量",
      "Levi-Civita联络","平行移动","曲率张量","Ricci曲率与数量曲率",
      "截面曲率","测地线方程","指数映射","Hopf-Rinow定理",
      "Jacobi场","Rauch比较定理","Bonnet-Myers定理","Hadamard定理",
      "极小曲面","微分几何在广义相对论中的应用","本章总结与习题选讲"]),
    (58, "李群与李代数", [
      "李群的定义","矩阵李群","李群的连通性","左不变向量场",
      "李代数的定义","李括号","李群的李代数","指数映射",
      "单参数子群","BCH公式","伴随表示Ad与ad","Killing形式",
      "半单李代数","Cartan子代数","根系","Dynkin图",
      "李代数的Cartan分类","李群的表示","不可约表示","最高权理论",
      "Weyl特征公式","Peter-Weyl定理","李群在粒子物理中的应用",
      "李群在微分方程中的应用","本章总结与习题选讲"]),
    (59, "代数几何初步", [
      "仿射代数集","Hilbert零点定理","Zariski拓扑","仿射簇",
      "坐标环","射影空间","射影簇","齐次坐标环",
      "代数曲线","曲线的奇点","Bézout定理","除子与线丛",
      "Riemann-Roch定理应用","椭圆曲线","椭圆曲线的群结构","层的定义",
      "层上同调","概形——Spec","概形的态射","光滑性与正则性",
      "纤维积与基变换","吹胀与奇点解消","代数几何在数论中的应用",
      "代数几何在密码学中的应用","本章总结与习题选讲"]),
    (60, "范畴论与数学统一视角", [
      "范畴的定义","函子","自然变换","等价范畴",
      "泛性质","极限与余极限","伴随函子","Yoneda引理",
      "可表函子","Abel范畴","正合函子与导出函子","链复形",
      "上同调的范畴论观点","Tor与Ext函子","谱序列简介",
      "单子与Kleisli范畴","Topos理论简介","范畴论在代数拓扑中的角色",
      "范畴论在代数几何中的角色","Curry-Howard对应","高阶范畴论简介",
      "数学结构的统一视角","从分析到代数的桥梁","数学的统一性与多样性",
      "数学六卷的终章"]),
  ]),
]

sidebar_lines = []
for vol_num, vol_title, chapters in volumes:
    sidebar_lines.append(f'\n* **第{VOL_CN[vol_num]}卷：{vol_title}**')
    sidebar_lines.append(f'  * [导论](vol{vol_num}/README.md)')
    for ch_num, ch_title, sections in chapters:
        sidebar_lines.append(f'  * 第{ch_num}章 {ch_title}')
        ch_dir = os.path.join(BASE, f"vol{vol_num}", f"ch{ch_num:02d}")
        os.makedirs(ch_dir, exist_ok=True)
        for i, sec_title in enumerate(sections, 1):
            sidebar_lines.append(f'    * [{ch_num}.{i} {sec_title}](vol{vol_num}/ch{ch_num:02d}/sec{i:02d}.md)')
            fp = os.path.join(ch_dir, f"sec{i:02d}.md")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(f"# {ch_num}.{i} {sec_title}\n\n> 待撰写\n")

with open(os.path.join(BASE, "sidebar_part3.txt"), "w", encoding="utf-8") as f:
    f.write('\n'.join(sidebar_lines))

count = sum(len(secs) for _, _, chs in volumes for _, _, secs in chs)
print(f"Part 3 完成: 第五卷+第六卷, 共 {count} 节, 20 章")

# === Assemble final _sidebar.md and README.md ===
parts = []
for i in range(1, 4):
    with open(os.path.join(BASE, f"sidebar_part{i}.txt"), "r", encoding="utf-8") as f:
        parts.append(f.read())

with open(os.path.join(BASE, "_sidebar.md"), "w", encoding="utf-8") as f:
    f.write('\n'.join(parts))

readme = """# 本科生的数学六卷

> **Six Volumes of Mathematics for Undergraduates**
>
> *作者：唐旭江 (Xujiang Tang)*

---

欢迎来到《本科生的数学六卷》。

本书试图为数学本科生提供一条 **贯穿核心数学思想的主干逻辑线**——从实数的完备性公理出发，经过分析、代数、方程、泛函，直达流形与李群。全书共 **60 章、1500 节**，覆盖本科与研究生阶段的全部核心数学知识。

## 七大核心思想

| # | 思想 | 一句话 |
|---|------|-------|
| 1 | **极限与逼近** | 用有限逼近无限 |
| 2 | **线性结构** | 一切从线性开始 |
| 3 | **对称与不变量** | 结构由对称性决定 |
| 4 | **局部与整体** | 微分是局部的，积分是整体的 |
| 5 | **对偶与变分** | 每个问题都有其对偶 |
| 6 | **算子与谱** | 无穷维的特征值问题 |
| 7 | **几何直觉** | 代数是语言，几何是直觉 |

## 六卷结构

| 卷 | 标题 | 章节 | 节数 |
|----|------|------|------|
| 第一卷 | 数学分析基础 | 第 1–10 章 | 250 节 |
| 第二卷 | 线性代数与解析几何 | 第 11–20 章 | 250 节 |
| 第三卷 | 常微分方程与动力系统 | 第 21–30 章 | 250 节 |
| 第四卷 | 复分析与偏微分方程 | 第 31–40 章 | 250 节 |
| 第五卷 | 实分析、泛函分析与概率统计 | 第 41–50 章 | 250 节 |
| 第六卷 | 代数、几何与拓扑 | 第 51–60 章 | 250 节 |

## 知识地图

```
实数完备性 ──→ 极限理论 ──→ 微积分 ──→ 级数 ──→ 多元分析
    │                                              │
    ↓                                              ↓
线性代数 ──→ 矩阵理论 ──→ 内积空间 ──→ 张量 ──→ 微分形式
    │                                              │
    ↓                                              ↓
常微分方程 ──→ 动力系统 ──→ 分岔混沌 ──→ 变分法 ──→ 最优控制
    │                                              │
    ↓                                              ↓
复分析 ──→ Cauchy理论 ──→ 留数 ──→ PDE ──→ 现代PDE方法
    │                                              │
    ↓                                              ↓
测度论 ──→ Lebesgue积分 ──→ 泛函分析 ──→ 概率论 ──→ 数理统计
    │                                              │
    ↓                                              ↓
群论 ──→ 环域 ──→ Galois ──→ 拓扑 ──→ 流形 ──→ 李群 ──→ 范畴论
```

---

*© 2026 Xujiang Tang. All rights reserved.*
"""

with open(os.path.join(BASE, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

# Create volume READMEs for vol2-6 (vol1 already has content)
vol_intros = {
    2: ("线性代数与解析几何", "从一维到高维——本卷探讨线性结构的力量。向量空间、矩阵、特征值、内积、张量构成了现代数学与工程的基础语言。"),
    3: ("常微分方程与动力系统", "运动的数学语言——本卷从常微分方程出发，经过定性理论、稳定性、分岔与混沌，揭示确定性系统中的复杂行为。"),
    4: ("复分析与偏微分方程", "虚数的实在与物理的数学——本卷将复分析的优美理论与偏微分方程的强大框架统一呈现。"),
    5: ("实分析、泛函分析与概率统计", "无穷维的世界与随机的秩序——从测度论到泛函分析，从概率论到数理统计，本卷构建现代分析的完整框架。"),
    6: ("代数、几何与拓扑", "结构、对称与空间——本卷从群、环、域到拓扑、流形、李群，最终以范畴论统一所有数学结构。"),
}
for v, (title, intro) in vol_intros.items():
    fp = os.path.join(BASE, f"vol{v}", "README.md")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(f"# 第{VOL_CN[v]}卷：{title}\n\n{intro}\n")

# Clean up temp files
for i in range(1, 4):
    tp = os.path.join(BASE, f"sidebar_part{i}.txt")
    if os.path.exists(tp):
        os.remove(tp)

# Count total
total = 0
for v in range(1, 7):
    vdir = os.path.join(BASE, f"vol{v}")
    for d in os.listdir(vdir):
        dd = os.path.join(vdir, d)
        if os.path.isdir(dd) and d.startswith("ch"):
            total += len([f for f in os.listdir(dd) if f.endswith(".md")])
print(f"\n=== 全部完成 ===")
print(f"总计: {total} 个节文件, 60 章, 6 卷")
print(f"_sidebar.md 已生成")
print(f"README.md 已更新")
