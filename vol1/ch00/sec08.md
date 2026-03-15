# 0.8 补集与 De Morgan 律

## 全集与补集、De Morgan 对偶定律的证明与应用

在上一节里，我们学习了并集与交集。它们分别对应逻辑中的"或"与"且"，于是集合的语言第一次露出了它与命题逻辑之间的深层同构："属于 $A \cup B$"等价于"属于 $A$ 或属于 $B$"；"属于 $A \cap B$"等价于"属于 $A$ 且属于 $B$"。

那么，一个自然的问题立刻出现：如果并与交分别对应"或"与"且"，那么逻辑中的"非"在集合世界里对应什么？

答案就是：**补集**。

从逻辑的角度看，补集是集合语言中的否定；从几何的角度看，补集是"这个区域之外"的全部空间；从分析的角度看，补集则是"偏离某个邻域""不满足某个约束"的精确载体。很多学生最初觉得补集只是一个附属记号，好像只是"全集减去这个集合"。但真正进入分析、概率或拓扑之后才会发现：补集不是边角料，而是把"正面条件"翻译成"反面条件"的核心机制。De Morgan 律之所以重要，也正因为它说明了：**否定穿过并与交时，会把并变成交，把交变成并。**

这不是记忆技巧，而是结构事实。它既是命题逻辑中

$$
\neg(P \lor Q) \equiv (\neg P) \land (\neg Q), \qquad \neg(P \land Q) \equiv (\neg P) \lor (\neg Q)
$$

的集合版本，也是以后分析学里写定义的否定、写不连续、不收敛、非紧、非有界等命题时反复使用的底层模板。

从历史上看，De Morgan 在 1847 年的 *Formal Logic* 中首次系统表述了这两条对偶律，但他的表述仍停留在自然语言和三段论的框架中。真正把 De Morgan 律纳入符号逻辑体系的是 Boole——在 1854 年的 *The Laws of Thought* 中，De Morgan 律获得了代数化的精确表达。Peirce 在 1880 年代进一步把它推广到关系逻辑中，Schröder 在 *Vorlesungen über die Algebra der Logik*（1890-1905）中则系统地在集合代数语境下讨论了对偶律的全部推论。Hausdorff 在 *Grundzüge der Mengenlehre*（1914）中把 De Morgan 律作为集合运算体系的标准组成部分写入教材，此后它成为每一本集合论和分析学教科书的基本内容。

这一节，我们从补集本身讲起，严格证明它的每一条基本性质，然后证明 De Morgan 律，再讨论它在数学写作和分析语言中的实际作用。

---

### 一、补集为什么必须依赖全集

给定一个全集 $U$ 和它的子集 $A \subseteq U$，集合 $A$ 的**补集（complement）**定义为

$$
A^c := U \setminus A = \{x \in U : x \notin A\}.
$$

读作"$A$ 的补集"或"$A$ 的余集"。它表示：**在全集 $U$ 中，一切不属于 $A$ 的元素所组成的集合。**

这一句话里最重要的词，不是"$A$"而是"在全集 $U$ 中"。很多初学者第一次学补集时，容易把"补集"理解成一个绝对概念，好像一个集合天然自带一个补集。其实不是。**补集从来不是绝对的，它总是相对于某个给定的全集而言。**

Halmos 在 *Naive Set Theory* 中用简洁的语言点明了这一点：complement 这个词本身就暗示了"相对于什么"。没有全集作为背景，$A^c$ 这个记号就没有确定的含义。Velleman 在 *How to Prove It* 中也特别提醒学生：在使用补集之前，务必先声明或确认全集是什么。

> **例 1.** 设
>
> $$
> A = (0, 1).
> $$
>
> 若全集取为 $U = \mathbb{R}$，则
>
> $$
> A^c = \mathbb{R} \setminus (0, 1) = (-\infty, 0] \cup [1, +\infty).
> $$
>
> 但若全集取为 $U = [0, 2]$，则
>
> $$
> A^c = [0, 2] \setminus (0, 1) = \{0\} \cup [1, 2].
> $$
>
> 同一个集合 $A = (0, 1)$，因为全集不同，补集完全不同。

> **例 2.** 设 $A = \mathbb{Q}$（全体有理数）。
>
> 若全集是 $U = \mathbb{R}$，则 $A^c$ 是全体无理数：
>
> $$
> \mathbb{Q}^c = \mathbb{R} \setminus \mathbb{Q}.
> $$
>
> 但若全集是 $U = [0, 1]$，则 $A^c$ 不是"所有无理数"，而只是区间 $[0, 1]$ 中的全体无理数：
>
> $$
> [0, 1] \setminus \mathbb{Q}.
> $$

这说明补集并不是"世界上所有不在 $A$ 里的东西"，而是"在当前讨论范围内，不在 $A$ 里的东西"。

这一点看似技术细节，实则根本。因为数学推理永远发生在一个语境中。逻辑里，命题的否定必须相对于同一论域来理解；集合里，补集也必须相对于同一全集来理解。你若偷偷换了全集，其实就相当于偷偷换了命题的讨论范围，整个陈述都会变味。

Zermelo 在 1908 年建立 ZF 公理系统时，没有设立"全集公理"——事实上 Russell 悖论已经表明，不加限制的"所有集合的集合"是不存在的。因此在严格的公理化集合论中，补集只能相对于某个已经存在的集合来定义，这通过**分离公理模式（Axiom Schema of Separation）**来保证：如果 $A$ 是集合，$P(x)$ 是性质，那么 $\{x \in A : P(x)\}$ 是集合。补集 $A^c = \{x \in U : x \notin A\}$ 正是分离公理的一个实例。Fraenkel 和 Skolem 在完善公理系统时进一步明确了这一点。

因此，在学习阶段，最好养成一个严格习惯：**一旦使用补集符号 $A^c$，脑中立刻同时浮现出全集 $U$。** 这会帮你避开大量后续错误。

---

### 二、补集的直观含义：集合论中的"非"

从定义出发，补集最基本的成员判别式就是：

$$
x \in A^c \;\;\iff\;\; x \notin A.
$$

这里有一个隐含的前提：$x \in U$。完整写出来是

$$
x \in A^c \;\;\iff\;\; x \in U \;\land\; x \notin A.
$$

这几乎就是补集的一切本质。它表明补集在集合世界中所做的事，正是逻辑否定所做的事——把"属于 $A$"翻转成"不属于 $A$"。

因此，若把"$x \in A$"视为一个关于 $x$ 的命题 $P(x)$，那么"$x \in A^c$"就是它的否定。也就是说：

$$
x \in A^c \;\;\iff\;\; \neg(x \in A).
$$

这正是集合与逻辑之间最重要的桥梁之一。0.5 节我们讲过：一个性质 $P(x)$ 对应一个集合 $\{x \in U : P(x)\}$。那么，否定性质 $\neg P(x)$ 所对应的集合，就是原集合的补集：

$$
\{x \in U : \neg P(x)\} = U \setminus \{x \in U : P(x)\}.
$$

从这个角度看，补集不是"额外运算"，而是把逻辑的"非"翻译成集合语言的标准方式。以后你看到一个集合定义，就要逐渐养成这种反应：这个集合刻画的是"满足某性质"的对象；它的补集刻画的是"该性质不成立"的对象。

> **例 3.** 设
>
> $$
> A = \{x \in \mathbb{R} : |x - a| < \varepsilon\}.
> $$
>
> 这表示"距离 $a$ 小于 $\varepsilon$"的全体实数，也就是 $a$ 的一个 $\varepsilon$-邻域 $(a - \varepsilon,\; a + \varepsilon)$。
>
> 则它在 $\mathbb{R}$ 中的补集是
>
> $$
> A^c = \{x \in \mathbb{R} : |x - a| \geq \varepsilon\}.
> $$
>
> **推导.** "$x \notin A$"等价于"$\neg(|x - a| < \varepsilon)$"，即"$|x - a| \geq \varepsilon$"。这里用到的是实数中严格不等号的否定：$\neg(a < b) \iff a \geq b$。$\square$

这个例子在分析中几乎每天都会用到。邻域的补集，正是"离中心至少有 $\varepsilon$ 远"的点集。以后写"某数列不收敛到 $a$"时，本质上说的就是：存在某个 $\varepsilon > 0$，使得数列项会无限次落在这个补集里。

---

### 三、补集的基本性质

由定义可以推出一系列最重要的基本恒等式。下面逐条严格证明。

#### 性质 1：互补性

> **命题.** 对任意集合 $A \subseteq U$，
>
> $$
> A \cap A^c = \varnothing, \qquad A \cup A^c = U.
> $$

> **证明.**
>
> **第一条.** 用反证法。假设 $A \cap A^c \neq \varnothing$，则存在 $x \in A \cap A^c$。由交集的定义，$x \in A$ 且 $x \in A^c$。但 $x \in A^c$ 意味着 $x \notin A$。于是同时有 $x \in A$ 与 $x \notin A$，矛盾。因此 $A \cap A^c = \varnothing$。
>
> **第二条.** 任取 $x \in U$。根据排中律（$P \lor \neg P$ 恒真），$x \in A$ 或 $x \notin A$。若 $x \in A$，则 $x \in A \cup A^c$。若 $x \notin A$，则 $x \in A^c$，故也有 $x \in A \cup A^c$。无论哪种情况，$x \in A \cup A^c$。因此 $U \subseteq A \cup A^c$。反向 $A \cup A^c \subseteq U$ 由 $A, A^c \subseteq U$ 显然。$\square$

这两条公式正是命题逻辑中**无矛盾律**与**排中律**的集合版本。$A \cap A^c = \varnothing$ 对应"一个命题不可能同时为真又为假"（$\neg(P \land \neg P)$）；$A \cup A^c = U$ 对应"一个命题要么真，要么假"（$P \lor \neg P$）。

从代数结构的角度看，这两条性质正是布尔代数中**补元（complement）**的定义条件。Huntington 在 1904 年给出的布尔代数公理系统中，明确把"对每个元素 $a$ 存在元素 $a'$ 使得 $a \lor a' = 1$ 且 $a \land a' = 0$"列为核心公理。在集合语境中，$U$ 扮演 $1$（最大元），$\varnothing$ 扮演 $0$（最小元），补集 $A^c$ 正是 $A$ 的补元。

值得注意的是，Brouwer 的直觉主义数学对排中律持保留态度——在直觉主义逻辑中，$P \lor \neg P$ 不是公理。对应地，在 Heyting 代数（直觉主义逻辑的代数模型）中，补元不一定存在，$A \cup A^c = U$ 不一定成立。换言之，经典集合论中的互补性依赖排中律这一逻辑前提。这个区分在通常的本科数学中可以暂时搁置，但值得了解：**补集的"完备性"（$A \cup A^c = U$）不是无条件的，它建立在经典逻辑之上。**

#### 性质 2：双重补集

> **命题.** 对任意集合 $A \subseteq U$，
>
> $$
> (A^c)^c = A.
> $$

> **证明.** 对任意 $x \in U$，
>
> $$
> x \in (A^c)^c \;\;\iff\;\; x \notin A^c \;\;\iff\;\; \neg(x \notin A) \;\;\iff\;\; x \in A.
> $$
>
> 第一个 $\iff$ 是补集的定义（$x$ 不属于 $A^c$）。第二个 $\iff$ 是补集定义的展开（$x \in A^c$ 等价于 $x \notin A$，取否定）。第三个 $\iff$ 是双重否定律（$\neg \neg P \equiv P$）。
>
> 因此两个集合有完全相同的元素，故 $(A^c)^c = A$。$\square$

这就是命题逻辑里的双重否定律 $\neg(\neg P) \equiv P$ 的集合版本。它告诉我们：取两次补集回到原来。补集运算是自身的逆运算——在群论的语言中，补集是一个**对合（involution）**。

#### 性质 3：空集与全集互为补集

> **命题.**
>
> $$
> \varnothing^c = U, \qquad U^c = \varnothing.
> $$

> **证明.**
>
> **第一条.** 任取 $x \in U$。$x \in \varnothing^c$ 当且仅当 $x \notin \varnothing$。由于空集没有任何元素，$x \notin \varnothing$ 对所有 $x$ 都成立。因此 $U \subseteq \varnothing^c$。反向 $\varnothing^c \subseteq U$ 由定义显然。故 $\varnothing^c = U$。
>
> **第二条.** 任取 $x$。$x \in U^c$ 当且仅当 $x \in U$ 且 $x \notin U$，这是矛盾式，不可能成立。因此 $U^c$ 没有任何元素，即 $U^c = \varnothing$。$\square$

也可以从性质 2 直接得到：由 $\varnothing^c = U$ 两边取补得 $(\varnothing^c)^c = U^c$，左边由双重补集律等于 $\varnothing$，故 $U^c = \varnothing$。这展示了基本性质之间的**内在联系**——它们不是一堆独立事实，而是一个代数系统的不同侧面。

#### 性质 4：补集反转包含关系

> **命题.** 对任意集合 $A, B \subseteq U$，
>
> $$
> A \subseteq B \;\;\iff\;\; B^c \subseteq A^c.
> $$

> **证明.**
>
> **($\Rightarrow$)** 设 $A \subseteq B$。任取 $x \in B^c$，则 $x \notin B$。若 $x \in A$，由 $A \subseteq B$ 得 $x \in B$，与 $x \notin B$ 矛盾。因此 $x \notin A$，即 $x \in A^c$。故 $B^c \subseteq A^c$。
>
> **($\Leftarrow$)** 设 $B^c \subseteq A^c$。任取 $x \in A$，则 $x \notin A^c$（否则 $x \in A$ 且 $x \notin A$，矛盾）。由 $B^c \subseteq A^c$，若 $x \in B^c$ 则 $x \in A^c$，对逆否命题即：若 $x \notin A^c$ 则 $x \notin B^c$。因此 $x \notin B^c$，即 $x \in B$。故 $A \subseteq B$。$\square$

这条性质初看有些"方向反了"，但正因为方向反了，它才值得记住。集合越大，它的补集越小；集合越小，它的补集越大。这像不等式取相反数时方向翻转（若 $a \leq b$ 则 $-a \geq -b$），也像条件命题取逆否形式时前后互换（$P \to Q$ 等价于 $\neg Q \to \neg P$）。

从逻辑角度看，$(\Rightarrow)$ 的证明本质上就是在构造逆否命题：$x \in A \to x \in B$ 的逆否是 $x \notin B \to x \notin A$，即 $x \in B^c \to x \in A^c$。Tarski 在其逻辑教科书 *Introduction to Logic* 中称这种包含关系的翻转为"补集的反变性（contravariance）"——这个术语后来在范畴论中被 Eilenberg 和 Mac Lane 赋予了更一般的含义：补集是从偏序 $(\mathcal{P}(U), \subseteq)$ 到其自身的一个**反变函子（contravariant functor）**，它在保持结构的同时反转所有箭头的方向。

---

### 四、相对补与差集

补集是相对于全集 $U$ 定义的。但在实际计算中，我们常常不想"从整个全集里去掉 $A$"，而是想"从某个集合 $B$ 里去掉 $A$"。这就引出**差集（set difference）**，也叫**相对补（relative complement）**。

> **定义.** 给定两个集合 $A, B$，定义
>
> $$
> A \setminus B := \{x : x \in A \;\text{且}\; x \notin B\}.
> $$
>
> 读作"$A$ 去掉 $B$"或"$A$ 与 $B$ 的差集"。

从逻辑结构上看：

$$
x \in A \setminus B \;\;\iff\;\; x \in A \;\land\; \neg(x \in B).
$$

因此，差集与补集的关系是：

> **命题.** $A \setminus B = A \cap B^c$。

> **证明.** 对任意 $x$，
>
> $$
> x \in A \setminus B \;\;\iff\;\; x \in A \;\land\; x \notin B \;\;\iff\;\; x \in A \;\land\; x \in B^c \;\;\iff\;\; x \in A \cap B^c.
> $$
>
> $\square$

这条公式非常重要，因为它告诉我们：**差集不是一种全新的运算，而是交集与补集的组合。** 这意味着所有关于差集的恒等式，都可以翻译成关于交集和补集的恒等式，然后用已知的代数规则来处理。

> **例 4.** 在 $U = \mathbb{R}$ 中，
>
> $$
> [0, 3] \setminus (1, 2) = \{x \in [0, 3] : x \notin (1, 2)\} = [0, 1] \cup [2, 3].
> $$
>
> **验证.** $x \in [0, 3]$ 且 $x \notin (1, 2)$ 等价于 $0 \leq x \leq 3$ 且 $\neg(1 < x < 2)$，即 $0 \leq x \leq 3$ 且 $(x \leq 1 \lor x \geq 2)$。分配合取到析取上：$(0 \leq x \leq 1) \lor (2 \leq x \leq 3)$，即 $x \in [0, 1] \cup [2, 3]$。$\square$

> **例 5.** 设 $E = \{n \in \mathbb{N} : n \text{ 是偶数}\}$，$M = \{n \in \mathbb{N} : 3 \mid n\}$。则
>
> $$
> E \setminus M = \{n \in \mathbb{N} : n \text{ 是偶数且 } 3 \nmid n\} = \{2, 4, 8, 10, 14, 16, 20, \ldots\}.
> $$
>
> 这些是偶数中去掉 $6$ 的倍数后剩下的部分。因为 $E \cap M = \{n \in \mathbb{N} : 6 \mid n\}$（偶数且是 $3$ 的倍数等价于 $6$ 的倍数），所以 $E \setminus M = E \setminus (E \cap M)$，恰好把 $6$ 的所有倍数从偶数集中剔除。

差集在分析和代数中无处不在："定义域去掉奇点""区间去掉端点""集合去掉零测集"……每一次"去掉"，背后都是补集在局部全集中的应用。

差集还有两条基本性质值得一并记录：

> **命题.** 对任意集合 $A, B$，
>
> (a) $A \setminus B \subseteq A$。
>
> (b) $A \setminus B$ 与 $B$ 不相交，即 $(A \setminus B) \cap B = \varnothing$。
>
> (c) $A = (A \cap B) \cup (A \setminus B)$，且 $A \cap B$ 与 $A \setminus B$ 不相交。

> **证明.**
>
> (a) 若 $x \in A \setminus B$，则 $x \in A$ 且 $x \notin B$。由第一个条件直接得 $x \in A$。
>
> (b) 若 $x \in (A \setminus B) \cap B$，则 $x \in A \setminus B$ 且 $x \in B$。但 $x \in A \setminus B$ 意味着 $x \notin B$，与 $x \in B$ 矛盾。故交集为空。
>
> (c) **($\supseteq$)** 若 $x \in A \cap B$，则 $x \in A$；若 $x \in A \setminus B$，则也有 $x \in A$。因此 $(A \cap B) \cup (A \setminus B) \subseteq A$。
>
> **($\subseteq$)** 任取 $x \in A$。若 $x \in B$，则 $x \in A \cap B$。若 $x \notin B$，则 $x \in A \setminus B$。无论哪种情况，$x \in (A \cap B) \cup (A \setminus B)$。
>
> 不相交性：若 $x \in (A \cap B) \cap (A \setminus B)$，则 $x \in B$（由 $x \in A \cap B$）且 $x \notin B$（由 $x \in A \setminus B$），矛盾。$\square$

性质 (c) 特别重要——它说明 $A \cap B$ 和 $A \setminus B$ 构成 $A$ 的一个**分拆（partition into two disjoint parts）**。这个分拆在概率论中对应**全概率公式**的最简情形：$P(A) = P(A \cap B) + P(A \setminus B)$。Kolmogorov 在 1933 年的概率公理化中，正是利用差集的不相交分解来推导基本的概率加法规则。

---

### 五、De Morgan 律：否定如何穿过并与交

现在来到本节的中心定理。

> **定理（De Morgan 律）.** 对任意两个集合 $A, B \subseteq U$，
>
> $$
> (A \cup B)^c = A^c \cap B^c,
> $$
>
> $$
> (A \cap B)^c = A^c \cup B^c.
> $$

这两条公式分别读作：

- "并集的补集 = 补集的交集"
- "交集的补集 = 补集的并集"

很多学生最初把它们当作公式来背。但如果从逻辑角度看，它们根本不神秘。因为对任意元素 $x \in U$，有：

$$
x \in A \cup B \;\;\iff\;\; (x \in A) \lor (x \in B),
$$

$$
x \in A \cap B \;\;\iff\;\; (x \in A) \land (x \in B).
$$

对这两条分别取否定，由命题逻辑中的 De Morgan 律立刻得到集合版本。下面把证明完整写出。

> **证明（第一条）.** 需证 $(A \cup B)^c = A^c \cap B^c$，即证两个集合互相包含。
>
> **($\subseteq$)** 任取 $x \in (A \cup B)^c$。由补集定义，$x \in U$ 且 $x \notin A \cup B$。
>
> "$x \notin A \cup B$"意味着"$\neg(x \in A \lor x \in B)$"。
>
> 由命题逻辑的 De Morgan 律（0.1 节），$\neg(P \lor Q) \equiv \neg P \;\land\; \neg Q$，得
>
> $$
> \neg(x \in A) \;\land\; \neg(x \in B),
> $$
>
> 即 $x \notin A$ 且 $x \notin B$，即 $x \in A^c$ 且 $x \in B^c$，即 $x \in A^c \cap B^c$。
>
> **($\supseteq$)** 任取 $x \in A^c \cap B^c$。则 $x \in A^c$ 且 $x \in B^c$，即 $x \notin A$ 且 $x \notin B$。
>
> 由 $\neg P \;\land\; \neg Q \;\equiv\; \neg(P \lor Q)$，得 $\neg(x \in A \lor x \in B)$，即 $x \notin A \cup B$，即 $x \in (A \cup B)^c$。
>
> 由双向包含，$(A \cup B)^c = A^c \cap B^c$。$\square$

> **证明（第二条）.** 需证 $(A \cap B)^c = A^c \cup B^c$。
>
> **($\subseteq$)** 任取 $x \in (A \cap B)^c$。则 $x \in U$ 且 $x \notin A \cap B$。
>
> "$x \notin A \cap B$"意味着"$\neg(x \in A \;\land\; x \in B)$"。
>
> 由命题逻辑的 De Morgan 律，$\neg(P \land Q) \equiv \neg P \;\lor\; \neg Q$，得
>
> $$
> \neg(x \in A) \;\lor\; \neg(x \in B),
> $$
>
> 即 $x \notin A$ 或 $x \notin B$，即 $x \in A^c$ 或 $x \in B^c$，即 $x \in A^c \cup B^c$。
>
> **($\supseteq$)** 任取 $x \in A^c \cup B^c$。则 $x \in A^c$ 或 $x \in B^c$。
>
> - 若 $x \in A^c$，则 $x \notin A$，故 $\neg(x \in A \;\land\; x \in B)$（因为合取的第一个分量为假），即 $x \notin A \cap B$，故 $x \in (A \cap B)^c$。
> - 若 $x \in B^c$，则 $x \notin B$，故 $\neg(x \in A \;\land\; x \in B)$（因为合取的第二个分量为假），即 $x \notin A \cap B$，故 $x \in (A \cap B)^c$。
>
> 无论哪种情况，$x \in (A \cap B)^c$。
>
> 由双向包含，$(A \cap B)^c = A^c \cup B^c$。$\square$

这两个证明极其典型。它们体现了集合论最重要的证明方法之一：**逐元素证明（element-chasing）**。你不需要画图，不需要靠直觉想象两个区域怎么翻来翻去；你只需要抓住一个任意元素 $x$，一步步把"属于左边"改写成"属于右边"。这类证明之所以稳健，正因为它几乎完全受逻辑驱动——每一步都有明确的逻辑律作为依据。

Gentzen 的自然演绎观点在这里再次有用：第一条证明的 $(\subseteq)$ 方向本质上是 $\lor$-消去规则的逆向使用（从否定一个析取推出否定两个分量），$(\supseteq)$ 方向则是 $\lor$-引入的逆向。第二条的 $(\supseteq)$ 方向中的分情况讨论，正是 $\lor$-消去规则的标准应用。

---

### 六、De Morgan 律的深层含义：对偶性

De Morgan 律真正深刻的地方，不在于它能帮你算题，而在于它揭示了集合运算中的一种**对偶（duality）**：

- 补集会把"并"变成"交"；
- 补集会把"交"变成"并"；
- 补集会把"全集"变成"空集"；
- 补集会把"空集"变成"全集"。

也就是说，补集像一个"翻转器"，把集合语言中的大部分基本运算都成对交换。若从更高的代数观点看，这正是布尔代数的核心结构之一。

例如，上一节学过：

$$
A \cup B = B \cup A, \qquad A \cap B = B \cap A.
$$

这是并与交的交换律——它们本身就互为对偶。De Morgan 律则提供了从一条到另一条的**桥梁**：如果你知道某个关于 $\cup$ 的恒等式，只要对所有集合取补、把 $\cup$ 换成 $\cap$、把 $\cap$ 换成 $\cup$、把 $\varnothing$ 换成 $U$、把 $U$ 换成 $\varnothing$，就得到一条对偶恒等式，而且它自动成立。

> **对偶原理.** 在 $(\mathcal{P}(U), \cup, \cap, {}^c, \varnothing, U)$ 这个布尔代数中，若一个关于 $\cup, \cap, \varnothing, U$ 的恒等式成立，则把 $\cup \leftrightarrow \cap$，$\varnothing \leftrightarrow U$ 互换后得到的恒等式也成立。

这条原理不需要逐个验证——它是 De Morgan 律和互补性的系统推论。Halmos 在 *Lectures on Boolean Algebras* 中把对偶原理称为布尔代数的"免费定理生产机"：每证一条恒等式，就自动得到另一条。

下面用几个例子展示这种对偶性。

| 恒等式                                             | 对偶恒等式                                         |
| -------------------------------------------------- | -------------------------------------------------- |
| $A \cup \varnothing = A$                         | $A \cap U = A$                                   |
| $A \cup U = U$                                   | $A \cap \varnothing = \varnothing$               |
| $A \cup A^c = U$                                 | $A \cap A^c = \varnothing$                       |
| $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| $(A \cup B)^c = A^c \cap B^c$                    | $(A \cap B)^c = A^c \cup B^c$                    |

Birkhoff 在 *Lattice Theory* 中系统研究了对偶原理在格结构中的推广。在一般的格中，对偶性不需要补集——只要交换 join 与 meet、交换最大元与最小元即可。但在布尔代数中，补集运算本身就是连接对偶双方的桥梁。Stone 在 1936 年的表示定理中证明，每个布尔代数都同构于某个拓扑空间（Stone 空间）的 clopen 集构成的集合代数——这个同构精确地保持了对偶结构。

---

### 七、De Morgan 律的直接推论

De Morgan 律一旦成立，很多常见恒等式都可以迅速得到。

#### 推论 1：差集对并与交的分配

> **命题.** 对任意集合 $A, B, C$，
>
> $$
> A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C),
> $$
>
> $$
> A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C).
> $$

> **证明（第一条）.** 利用 $A \setminus X = A \cap X^c$ 把差集转化为交集与补集：
>
> $$
> A \setminus (B \cup C) = A \cap (B \cup C)^c.
> $$
>
> 由 De Morgan 律（第一条），$(B \cup C)^c = B^c \cap C^c$，代入得
>
> $$
> A \cap (B^c \cap C^c).
> $$
>
> 由交集的结合律，
>
> $$
> A \cap (B^c \cap C^c) = (A \cap B^c) \cap (A \cap C^c) \quad \text{？}
> $$
>
> 等一下——这一步需要仔细验证。$A \cap (B^c \cap C^c)$ 是否等于 $(A \cap B^c) \cap (A \cap C^c)$？
>
> 设 $x \in A \cap (B^c \cap C^c)$，则 $x \in A$，$x \in B^c$，$x \in C^c$。于是 $x \in A \cap B^c$ 且 $x \in A \cap C^c$，故 $x \in (A \cap B^c) \cap (A \cap C^c)$。
>
> 反过来，设 $x \in (A \cap B^c) \cap (A \cap C^c)$，则 $x \in A \cap B^c$ 且 $x \in A \cap C^c$，从而 $x \in A$，$x \in B^c$，$x \in C^c$，故 $x \in A \cap (B^c \cap C^c)$。
>
> 因此
>
> $$
> A \cap (B^c \cap C^c) = (A \cap B^c) \cap (A \cap C^c) = (A \setminus B) \cap (A \setminus C).
> $$
>
> $\square$

> **证明（第二条）.** 同样地，
>
> $$
> A \setminus (B \cap C) = A \cap (B \cap C)^c = A \cap (B^c \cup C^c),
> $$
>
> 其中第二步用了 De Morgan 律（第二条）。再由交对并的分配律（0.7 节），
>
> $$
> A \cap (B^c \cup C^c) = (A \cap B^c) \cup (A \cap C^c) = (A \setminus B) \cup (A \setminus C).
> $$
>
> $\square$

这两条公式在集合计算中非常常见。前者说：从 $A$ 中去掉"$B$ 或 $C$"的元素，就等于**同时去掉 $B$ 和 $C$**——两刀都要砍。后者说：从 $A$ 中去掉"既在 $B$ 又在 $C$"的元素，等于**去掉 $B$ 或去掉 $C$ 中的一部分**——只须砍一刀即可。直觉上，"去掉并集"要求更严格（两个都得去），"去掉交集"要求更宽松（去其一即可），因此前者用 $\cap$，后者用 $\cup$。

#### 推论 2：子集关系的补集刻画

> **命题.** 对任意集合 $A, B \subseteq U$，
>
> $$
> A \subseteq B \;\;\iff\;\; A \cap B^c = \varnothing.
> $$

> **证明.**
>
> **($\Rightarrow$)** 设 $A \subseteq B$。若存在 $x \in A \cap B^c$，则 $x \in A$ 且 $x \notin B$。但由 $A \subseteq B$，$x \in A$ 蕴含 $x \in B$，矛盾。故 $A \cap B^c = \varnothing$。
>
> **($\Leftarrow$)** 设 $A \cap B^c = \varnothing$。任取 $x \in A$。若 $x \notin B$，则 $x \in B^c$，故 $x \in A \cap B^c$，与 $A \cap B^c = \varnothing$ 矛盾。因此 $x \in B$。故 $A \subseteq B$。$\square$

这条等价关系在分析证明中常被隐式使用。要证明"$A$ 的每个元素都在 $B$ 中"，等价于证明"$A$ 中没有不在 $B$ 中的元素"，即 $A \cap B^c = \varnothing$。从逻辑上看，这对应着 $\forall x,\; (x \in A \to x \in B)$ 与 $\neg \exists x,\; (x \in A \land x \notin B)$ 的等价。

#### 推论 3：覆盖与不相交的对偶

> **命题.** 对任意集合 $A, B \subseteq U$，
>
> (a) 若 $A \cup B = U$，则 $A^c \cap B^c = \varnothing$。
>
> (b) 若 $A \cap B = \varnothing$，则 $A^c \cup B^c = U$。

> **证明.** (a) 对 $A \cup B = U$ 两边取补：$(A \cup B)^c = U^c = \varnothing$。左边由 De Morgan 律等于 $A^c \cap B^c$。
>
> (b) 对 $A \cap B = \varnothing$ 两边取补：$(A \cap B)^c = \varnothing^c = U$。左边由 De Morgan 律等于 $A^c \cup B^c$。$\square$

这两条表明："覆盖整个全集"与"补集没有公共部分"是同一件事的两种说法；"没有交"与"补集联合覆盖"也是同一结构的两种说法。

---

### 八、区间与不等式中的 De Morgan 律

对于初学者来说，De Morgan 律最容易真正"落地"的地方，是区间与不等式。

> **例 6.** 在 $\mathbb{R}$ 中，求 $(0, 1)^c$。
>
> **解.** $x \in (0, 1)$ 等价于 $0 < x < 1$，即
>
> $$
> (x > 0) \;\land\; (x < 1).
> $$
>
> 对这个合取取否定，由 De Morgan 律得
>
> $$
> \neg(x > 0) \;\lor\; \neg(x < 1),
> $$
>
> 即
>
> $$
> (x \leq 0) \;\lor\; (x \geq 1).
> $$
>
> 因此
>
> $$
> (0, 1)^c = (-\infty, 0] \cup [1, +\infty).
> $$
>
> 注意端点带等号——因为 $\neg(x > 0) \iff x \leq 0$，不等号的否定会把严格变为非严格。$\square$

> **例 7.** 设 $A = \{x \in \mathbb{R} : |x - a| < \varepsilon\} = (a - \varepsilon,\; a + \varepsilon)$。求 $A^c$。
>
> **解.** $|x - a| < \varepsilon$ 等价于 $-\varepsilon < x - a < \varepsilon$，即
>
> $$
> (x > a - \varepsilon) \;\land\; (x < a + \varepsilon).
> $$
>
> 取否定：
>
> $$
> (x \leq a - \varepsilon) \;\lor\; (x \geq a + \varepsilon),
> $$
>
> 即 $|x - a| \geq \varepsilon$。因此
>
> $$
> A^c = (-\infty, a - \varepsilon] \cup [a + \varepsilon, +\infty) = \{x \in \mathbb{R} : |x - a| \geq \varepsilon\}.
> $$
>
> $\square$

> **例 8.** 求 $[a, b]^c$（在 $\mathbb{R}$ 中）。
>
> **解.** $x \in [a, b]$ 等价于 $(x \geq a) \land (x \leq b)$。取否定：
>
> $$
> (x < a) \;\lor\; (x > b).
> $$
>
> 因此
>
> $$
> [a, b]^c = (-\infty, a) \cup (b, +\infty).
> $$
>
> 这里**没有**等号——因为 $\neg(x \geq a) \iff x < a$，非严格不等号的否定变为严格。$\square$

端点是否带等号，完全由"否定时关系符号如何翻转"决定。规则只有一条：

$$
\neg(a < b) \iff a \geq b, \qquad \neg(a \leq b) \iff a > b.
$$

很多学生在区间补集上出错，本质上不是区间概念不熟，而是**否定没有做干净**。De Morgan 律是保证否定做干净的系统性工具——它告诉你，否定一个区间（合取条件）时，必须把"且"翻成"或"，然后对每个分量分别取否定。

---

### 九、分析学中的应用：定义的否定几乎都在用补集

补集与 De Morgan 律在分析学中最深的作用，不在于算集合，而在于**给定义取否定**。

0.2 节讨论过数列收敛的定义：

$$
\forall\, \varepsilon > 0,\;\; \exists\, N \in \mathbb{N},\;\; \forall\, n > N,\;\; |a_n - a| < \varepsilon.
$$

这里最内层的条件 $|a_n - a| < \varepsilon$ 对应邻域集合 $B_\varepsilon(a) = \{x \in \mathbb{R} : |x - a| < \varepsilon\}$。那么"不在这个邻域里"正是其补集：

$$
B_\varepsilon(a)^c = \{x \in \mathbb{R} : |x - a| \geq \varepsilon\}.
$$

于是"$\{a_n\}$ 不收敛到 $a$"的逻辑结构是：

$$
\exists\, \varepsilon > 0,\;\; \forall\, N \in \mathbb{N},\;\; \exists\, n > N,\;\; |a_n - a| \geq \varepsilon.
$$

仔细对比收敛的定义与不收敛的定义，发生了三件事：

1. $\forall\, \varepsilon$ 变成 $\exists\, \varepsilon$（全称变存在）。
2. $\exists\, N$ 变成 $\forall\, N$（存在变全称）。
3. $|a_n - a| < \varepsilon$ 变成 $|a_n - a| \geq \varepsilon$（邻域变补集）。

前两条是 0.2 节讲过的**量词否定律**（$\neg \forall \equiv \exists \neg$，$\neg \exists \equiv \forall \neg$）。第三条正是补集：从邻域 $B_\varepsilon(a)$ 翻转到 $B_\varepsilon(a)^c$。

同样的机制在函数连续性中也完全一致。$f$ 在 $x_0$ 处连续：

$$
\forall\, \varepsilon > 0,\;\; \exists\, \delta > 0,\;\; \forall\, x,\;\; |x - x_0| < \delta \;\Rightarrow\; |f(x) - f(x_0)| < \varepsilon.
$$

$f$ 在 $x_0$ 处**不**连续：

$$
\exists\, \varepsilon > 0,\;\; \forall\, \delta > 0,\;\; \exists\, x,\;\; |x - x_0| < \delta \;\land\; |f(x) - f(x_0)| \geq \varepsilon.
$$

核心改变仍然是三步：量词翻转、条件命题变合取否定（$\neg(P \to Q) \equiv P \land \neg Q$）、不等号从 $<$ 翻成 $\geq$（补集）。

Weierstrass 在 19 世纪 60 年代建立 $\varepsilon$-$\delta$ 语言时，虽然没有使用"补集"这个术语，但他写下的每一个"不连续"的判定标准，都在做同样的逻辑翻转。Heine 在 1872 年的序列收敛定义、Cantor 同年的实数完备性论证，也都隐含了相同的结构——从"落在邻域内"到"落在邻域外"的翻转，正是补集在起作用。

所以从某种意义上说，分析里的"不连续""不收敛""不一致连续""不一致收敛"，并不是全新的概念，而只是原有邻域条件被补集化之后再套上量词否定律的结果。**真正起翻转作用的核心结构，正是补集与 De Morgan 律。**

这也解释了为什么一个看似初等的集合公式，会在高等分析里频繁出现。因为分析虽然讨论极限、连续、可导这些"无限逼近"现象，但它的语言骨架仍然是逻辑与集合：性质对应集合，否定对应补集，并与交对应"或""且"，量词则控制这种结构在无限层面的嵌套方式。

---

### 十、广义 De Morgan 律：从两个集合到任意多个集合

对于两个集合的 De Morgan 律，我们已经证明完毕。事实上，它可以自然推广到任意族集合。

> **定理（广义 De Morgan 律）.** 设 $\{A_i\}_{i \in I}$ 是全集 $U$ 的一族子集，则
>
> $$
> \left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^c,
> $$
>
> $$
> \left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^c.
> $$

> **证明（第一条）.** 对任意 $x \in U$，
>
> $$
> x \in \left(\bigcup_{i \in I} A_i\right)^c \;\;\iff\;\; x \notin \bigcup_{i \in I} A_i \;\;\iff\;\; \neg\left(\exists\, i \in I,\; x \in A_i\right).
> $$
>
> 由量词否定律（$\neg \exists \equiv \forall \neg$），
>
> $$
> \iff\;\; \forall\, i \in I,\; x \notin A_i \;\;\iff\;\; \forall\, i \in I,\; x \in A_i^c \;\;\iff\;\; x \in \bigcap_{i \in I} A_i^c.
> $$
>
> $\square$

> **证明（第二条）.** 对任意 $x \in U$，
>
> $$
> x \in \left(\bigcap_{i \in I} A_i\right)^c \;\;\iff\;\; x \notin \bigcap_{i \in I} A_i \;\;\iff\;\; \neg\left(\forall\, i \in I,\; x \in A_i\right).
> $$
>
> 由量词否定律（$\neg \forall \equiv \exists \neg$），
>
> $$
> \iff\;\; \exists\, i \in I,\; x \notin A_i \;\;\iff\;\; \exists\, i \in I,\; x \in A_i^c \;\;\iff\;\; x \in \bigcup_{i \in I} A_i^c.
> $$
>
> $\square$

注意证明的关键一步：$\neg \exists \leftrightarrow \forall \neg$ 和 $\neg \forall \leftrightarrow \exists \neg$。这正是 0.2 节量词否定律的直接应用。广义 De Morgan 律把二元情形中"$\neg(\lor)$ 变 $\land$"推广为"$\neg(\exists)$ 变 $\forall$"——析取的无限推广就是存在量词，合取的无限推广就是全称量词。

> **例 9.** 设 $A_n = \left(-\frac{1}{n},\; \frac{1}{n}\right)$，$n = 1, 2, 3, \ldots$，全集 $U = \mathbb{R}$。
>
> 先算交集：$\bigcap_{n=1}^{\infty} A_n = \{0\}$（0.7 节曾提到的 Cantor 交定理的特例）。
>
> 对右边取补：$\{0\}^c = \mathbb{R} \setminus \{0\} = (-\infty, 0) \cup (0, +\infty)$。
>
> 再用广义 De Morgan 律验证：
>
> $$
> \left(\bigcap_{n=1}^{\infty} A_n\right)^c = \bigcup_{n=1}^{\infty} A_n^c.
> $$
>
> 而 $A_n^c = (-\infty, -\frac{1}{n}] \cup [\frac{1}{n}, +\infty)$。随着 $n$ 增大，$A_n^c$ 越来越"瘦"，但它们的并恰好覆盖 $\mathbb{R} \setminus \{0\}$ 的每一个点——对任意 $x \neq 0$，取 $n$ 充分大使得 $\frac{1}{n} \leq |x|$，则 $x \in A_n^c$。$\square$

这个例子说明广义 De Morgan 律不仅是形式推广，在处理无穷族集合时有实质应用。Lebesgue 在测度论中研究零测集时，Borel 在研究 $\sigma$-代数的闭合性时，以及 Sierpiński 在研究点集拓扑中的 $G_\delta$ 集和 $F_\sigma$ 集时，都反复依赖广义 De Morgan 律在可数并与可数交之间做翻转。

---

### 十一、对称差

在差集的基础上，还有一个自然的组合运算值得介绍。

> **定义（对称差）.** 给定集合 $A, B$，定义
>
> $$
> A \triangle B := (A \setminus B) \cup (B \setminus A).
> $$
>
> 读作"$A$ 与 $B$ 的**对称差（symmetric difference）**"。

$A \triangle B$ 收集的是"恰好属于 $A$ 和 $B$ 中的一个，但不同时属于两者"的元素。换言之：

$$
x \in A \triangle B \;\;\iff\;\; (x \in A \;\land\; x \notin B) \;\lor\; (x \in B \;\land\; x \notin A).
$$

这在逻辑上等价于**异或（exclusive or）**：$P \oplus Q \equiv (P \land \neg Q) \lor (\neg P \land Q)$。

> **例 10.** 设 $A = \{1, 2, 3, 4\}$，$B = \{3, 4, 5, 6\}$。则
>
> $$
> A \setminus B = \{1, 2\}, \quad B \setminus A = \{5, 6\}, \quad A \triangle B = \{1, 2, 5, 6\}.
> $$

对称差有一组整洁的代数性质：

> **命题.** 对任意集合 $A, B, C \subseteq U$，
>
> (a) $A \triangle B = B \triangle A$（交换律）。
>
> (b) $(A \triangle B) \triangle C = A \triangle (B \triangle C)$（结合律）。
>
> (c) $A \triangle \varnothing = A$（$\varnothing$ 是单位元）。
>
> (d) $A \triangle A = \varnothing$（每个元素是自己的逆元）。
>
> (e) $A \triangle B = (A \cup B) \setminus (A \cap B)$。

> **证明.**
>
> (a) 由定义直接得到：$(A \setminus B) \cup (B \setminus A) = (B \setminus A) \cup (A \setminus B)$，利用并集的交换律。
>
> (c) $A \triangle \varnothing = (A \setminus \varnothing) \cup (\varnothing \setminus A) = A \cup \varnothing = A$，因为 $A \setminus \varnothing = A$（没有元素需要去掉）且 $\varnothing \setminus A = \varnothing$。
>
> (d) $A \triangle A = (A \setminus A) \cup (A \setminus A) = \varnothing \cup \varnothing = \varnothing$，因为 $A \setminus A = \{x : x \in A \land x \notin A\} = \varnothing$。
>
> (e) 需证 $(A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$。
>
> 任取 $x \in (A \setminus B) \cup (B \setminus A)$。则 $x \in A \setminus B$ 或 $x \in B \setminus A$。
>
> 若 $x \in A \setminus B$，则 $x \in A$（故 $x \in A \cup B$）且 $x \notin B$（故 $x \notin A \cap B$，因为 $A \cap B$ 的元素必须同时在 $A$ 和 $B$ 中）。因此 $x \in (A \cup B) \setminus (A \cap B)$。
>
> 若 $x \in B \setminus A$，同理可得 $x \in (A \cup B) \setminus (A \cap B)$。
>
> 反过来，设 $x \in (A \cup B) \setminus (A \cap B)$。则 $x \in A \cup B$ 且 $x \notin A \cap B$。由 $x \in A \cup B$，$x \in A$ 或 $x \in B$。由 $x \notin A \cap B$，$x$ 不能同时属于 $A$ 和 $B$。因此要么 $x \in A$ 且 $x \notin B$（即 $x \in A \setminus B$），要么 $x \in B$ 且 $x \notin A$（即 $x \in B \setminus A$）。故 $x \in (A \setminus B) \cup (B \setminus A)$。
>
> (b) 的证明较为繁琐（需要逐元素展开三层差集），此处留作练习。关键技巧是利用 (e)，把对称差写成 $(A \cup B) \setminus (A \cap B)$ 的形式，再反复应用分配律和 De Morgan 律。$\square$

性质 (a)-(d) 合在一起说明：$(\mathcal{P}(U), \triangle)$ 构成一个**阿贝尔群（abelian group）**——交换律、结合律、单位元、逆元四条全部满足。这使得对称差在代数中有独特地位。如果再加上 $\cap$ 对 $\triangle$ 的分配律 $A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C)$，则 $(\mathcal{P}(U), \triangle, \cap)$ 构成一个**布尔环（Boolean ring）**。Stone 在 1936 年正是通过布尔环与布尔代数之间的对偶，建立了布尔代数的表示定理。von Neumann 在研究可测集的等价关系时也使用了对称差——两个集合的"距离"可以通过 $\mu(A \triangle B)$ 来度量（其中 $\mu$ 是某个测度），这成为后来度量化集合代数的基础工具。

---

### 十二、数学写作中的常见误区

本节的公式不多，但最常见的错误不在计算，而在逻辑感觉不够敏锐。下面列出几类最值得警惕的问题。

**误区 1：忘记补集依赖全集。**

写 $A^c$ 时若不先明确全集，表达其实是不完整的。尤其当同一个集合在不同语境中出现时，补集很可能不同。

**误区 2：把 De Morgan 律写反。**

$(A \cup B)^c$ 不是 $A^c \cup B^c$，而是 $A^c \cap B^c$。"补集穿过并号，要把并号翻成交号。"相应地，$(A \cap B)^c$ 要翻成 $A^c \cup B^c$。

一个有用的检验方法：De Morgan 律翻转的是运算符号（$\cup \leftrightarrow \cap$），而不是集合本身。如果你写出的结果中运算符号没有变化，几乎一定写错了。

**误区 3：区间补集的端点。**

$(0, 1)^c = (-\infty, 0] \cup [1, +\infty)$，**不是** $(-\infty, 0) \cup (1, +\infty)$。

$[a, b]^c = (-\infty, a) \cup (b, +\infty)$，**不是** $(-\infty, a] \cup [b, +\infty)$。

规则：开区间的补有闭端点，闭区间的补有开端点。这来自 $\neg(<) = \geq$ 和 $\neg(\leq) = >$。

**误区 4：混淆"不是都在"与"都不在"。**

$(A \cap B)^c = A^c \cup B^c$ 表达的是"至少有一个不在里面"，**不是**"两个都不在里面"。

$(A \cup B)^c = A^c \cap B^c$ 表达的是"两个都不在里面"。

这两个自然语言表述非常容易混淆。**一旦发觉自然语言不够清晰，就退回到逻辑符号——这是最可靠的做法。**

**误区 5：混淆 $A \setminus B$ 与 $B \setminus A$。**

差集不是对称的。$A \setminus B = \{x \in A : x \notin B\}$ 与 $B \setminus A = \{x \in B : x \notin A\}$ 一般不同。例如 $\{1, 2, 3\} \setminus \{2, 3, 4\} = \{1\}$，而 $\{2, 3, 4\} \setminus \{1, 2, 3\} = \{4\}$。

---

### 十三、补集与 De Morgan 律的深层视角

在不同数学分支中，补集与 De Morgan 律承担着各具特色的角色。

**拓扑学视角.** 拓扑空间中，开集的补是闭集，闭集的补是开集。De Morgan 律在这里直接给出：有限个开集的交的补 = 有限个闭集的并；任意多个开集的并的补 = 任意多个闭集的交。因此**开集公理的对偶就是闭集公理**——闭集族对有限并和任意交封闭。Kuratowski 在 1922 年从**闭包算子**出发等价地定义了拓扑结构，他的四条公理中 $\overline{A \cup B} = \overline{A} \cup \overline{B}$ 直接依赖补集与 De Morgan 律的配合。Alexandroff 和 Urysohn 在 1920 年代发展紧空间理论时，有限交性质与开覆盖的对偶——"$\{F_\alpha\}$ 的有限交非空当且仅当 $\{F_\alpha^c\}$ 没有有限子覆盖"——本质上也是 De Morgan 律的拓扑版本。

**测度论视角.** $\sigma$-代数要求对可数并和补集封闭。由广义 De Morgan 律，可数并封闭加补集封闭就自动蕴含可数交封闭——所以 $\sigma$-代数的定义中只需要写两条（补集 + 可数并），第三条是免费的。Lebesgue 在建立测度论时直觉地使用了这一点。Carathéodory 在 1914 年给出的外测度方法中，可测集的判定条件 $\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c)$ 显式依赖补集——这个条件本质上说的是：$A$ 和 $A^c$ 对 $E$ 的"分割"不会让测度"泄漏"。

**代数视角.** 在布尔代数中，补元的存在使得格结构从分配格升级为布尔代数。Stone 的表示定理（1936）证明每个布尔代数都同构于某个 Stone 空间的 clopen 集代数——而 clopen 集（既开又闭的集合）恰好是同时关于补集封闭的开集。Sikorski 在 1960 年代进一步发展了完备布尔代数理论，其中 De Morgan 律在无限运算意义下的推广起到核心作用。

**逻辑学视角.** Łukasiewicz 在 1920 年代建立多值逻辑时，发现经典 De Morgan 律在三值逻辑中仍然以修改形式成立。Heyting 代数（直觉主义逻辑的模型）中有"伪补"但不一定有真正的补，De Morgan 律的两条中只有一条单方向成立：$A^c \cup B^c \subseteq (A \cap B)^c$ 总是对的，但反向包含依赖排中律。这微妙的差异精确地反映了经典逻辑与直觉主义逻辑的分野。Gödel 在 1932 年证明直觉主义命题逻辑不能嵌入有限值逻辑，而这一结论的构造性证明中恰好利用了 De Morgan 律在直觉主义中的部分失效。

**概率论视角.** 事件 $A$ 的补事件 $A^c$ 是概率公理的基本组成部分。$P(A^c) = 1 - P(A)$ 这条最基本的关系，实质上来自 $A \cup A^c = U$ 与 $A \cap A^c = \varnothing$ 加上可加性。De Morgan 律在概率的语境中变成："$A$ 或 $B$ 都不发生"（$= (A \cup B)^c = A^c \cap B^c$）等价于"$A$ 不发生且 $B$ 不发生"。Rényi 称这种转换为"事件的对偶翻译"，它在可靠性理论和系统安全分析中有直接应用：系统失效（所有组件都坏）的概率可以通过每个组件的补事件的交来计算。

---

### 十四、方法论总结：补集与 De Morgan 律的思考框架

Pólya 在 *How to Solve It* 中反复强调"你能换一种方式表述这个问题吗？"（Can you restate the problem?）补集恰好是集合论中最强的"重新表述"工具——它把正面条件翻转为反面条件，有时候反面条件更容易处理。

**第一步：识别否定.** 当你在题目中看到"不属于""不满足""$A$ 以外""去掉"这类词时，立即想到补集或差集。把问题翻译成 $A^c$、$A \setminus B = A \cap B^c$ 的形式。

**第二步：决定是否使用 De Morgan 律.** 如果当前表达式中出现了"并集或交集的补集"，就使用 De Morgan 律把补集"推进去"。典型信号：$(A \cup B)^c$、$(A \cap B)^c$、$A \setminus (B \cup C)$、$A \setminus (B \cap C)$。

**第三步：逐元素执行.** 和 0.7 节一样，所有关于补集的证明最终都回到逐元素论证：任取 $x$，展开定义，利用逻辑律改写。每一步标注依据：

- 补集定义：$x \in A^c \iff x \notin A$。
- De Morgan 律：$\neg(P \lor Q) \equiv \neg P \land \neg Q$，$\neg(P \land Q) \equiv \neg P \lor \neg Q$。
- 双重否定：$\neg \neg P \equiv P$。
- 差集转化：$A \setminus B = A \cap B^c$。

**第四步：回顾.** 证明完成后问自己：（1）结论有对偶形式吗？如果有，写下来作为"免费的推论"。（2）能否推广到无限族？如果能，广义 De Morgan 律是否适用？（3）结论在区间、邻域或分析定义中有没有具体实例？

---

### 十五、本节的核心结构

回顾本节内容，可以提炼出三层递进的认识。

**第一层：定义层.** 补集 $A^c = \{x \in U : x \notin A\}$ 把逻辑否定嵌入集合语言。它必须相对于全集 $U$ 定义——没有全集就没有补集。差集是补集的局部版本：$A \setminus B = A \cap B^c$。

**第二层：定律层.** De Morgan 律说的是否定如何穿过并与交：

$$
(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c.
$$

它不是两条孤立公式，而是集合运算**对偶性**的核心表达。加上互补性（$A \cap A^c = \varnothing$，$A \cup A^c = U$）和双重补集律（$(A^c)^c = A$），补集使得 $(\mathcal{P}(U), \cup, \cap, {}^c, \varnothing, U)$ 从有界分配格升级为**布尔代数**。

**第三层：方法层.** 在分析学中，补集是"给定义取否定"的基本手段——从 $|x - a| < \varepsilon$ 到 $|x - a| \geq \varepsilon$，从"收敛"到"不收敛"，底层结构都是补集加量词否定律。De Morgan 律则保证否定穿越多层集合运算时方向不会搞乱。

用一句话收束本节：**补集不是"剩下的东西"，而是"否定的精确实现"。** 一旦把补集理解为逻辑否定的集合版本，De Morgan 律就不再是需要背诵的公式，而是逻辑运算法则的自然翻译。

---

### 十六、练习

**A 组（基本运算）**

1. 设 $U = \{1, 2, 3, 4, 5, 6, 7, 8\}$，$A = \{1, 2, 3, 4, 5\}$，$B = \{4, 5, 6, 7\}$。分别计算 $A^c$，$B^c$，$A^c \cap B^c$，$(A \cup B)^c$，并验证 De Morgan 律的第一条。

2. 在 $\mathbb{R}$ 中，计算以下补集（写成区间的并）：(a) $(-1, 2)^c$；(b) $[0, +\infty)^c$；(c) $(-\infty, 3]^c$；(d) $((-2, 0) \cup (1, 3))^c$。

3. 设 $A = \{n \in \mathbb{Z} : 2 \mid n\}$，$B = \{n \in \mathbb{Z} : 3 \mid n\}$。在 $U = \mathbb{Z}$ 中，描述 $A^c$，$B^c$，$A^c \cup B^c$，$(A \cap B)^c$，并验证 De Morgan 律的第二条。

**B 组（性质证明）**

4. 严格证明：$A \setminus (B \setminus C) = (A \setminus B) \cup (A \cap C)$。（提示：把所有差集化为 $\cap$ 和 ${}^c$。）

5. 证明：$(A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$。（即对称差的等价定义。）

6. 证明：对任意集合 $A, B$，$A \subseteq B$ 当且仅当 $A \setminus B = \varnothing$。

7. 证明：$A^c \setminus B^c = B \setminus A$。

**C 组（De Morgan 律的应用）**

8. 设 $A, B, C \subseteq U$。利用 De Morgan 律证明 $(A \cup B \cup C)^c = A^c \cap B^c \cap C^c$。然后推广到 $n$ 个集合的情形。

9. 证明：若 $A \cup B = U$ 且 $A \cap B = \varnothing$，则 $B = A^c$。（提示：利用互补性的唯一性。）

10. 证明：对任意集合 $A, B \subseteq U$，$A = (A \cap B) \cup (A \cap B^c)$。解释此等式的集合含义。

11. 设 $f: \mathbb{R} \to \mathbb{R}$ 是函数，$A, B \subseteq \mathbb{R}$。利用 De Morgan 律证明 $f^{-1}(A^c) = (f^{-1}(A))^c$。（这里 $f^{-1}(S) = \{x : f(x) \in S\}$ 是原像。）

**D 组（分析应用）**

12. 写出"数列 $\{a_n\}$ 不是 Cauchy 列"的严格否定形式。（Cauchy 列的定义：$\forall\, \varepsilon > 0,\; \exists\, N,\; \forall\, m, n > N,\; |a_m - a_n| < \varepsilon$。）

13. 写出"函数 $f$ 在 $[a, b]$ 上**不**一致连续"的严格否定形式。（一致连续的定义：$\forall\, \varepsilon > 0,\; \exists\, \delta > 0,\; \forall\, x, y \in [a, b],\; |x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon$。）

14. 设 $\{E_n\}_{n=1}^{\infty}$ 是 $\mathbb{R}$ 的一列子集。利用广义 De Morgan 律证明

$$
\left(\bigcup_{n=1}^{\infty} E_n\right)^c = \bigcap_{n=1}^{\infty} E_n^c,
$$

并利用此恒等式证明：若每个 $E_n$ 是开集，则 $\bigcap_{n=1}^{\infty} E_n^c$ 是 $G_\delta$ 集的补集（即 $F_\sigma$ 集）。

**E 组（思考题）**

15. 证明对称差的结合律：$(A \triangle B) \triangle C = A \triangle (B \triangle C)$。（提示：展开定义，或利用 $A \triangle B = (A \cup B) \setminus (A \cap B)$ 配合分配律。也可以用逻辑方法——证明异或的结合律 $(P \oplus Q) \oplus R \equiv P \oplus (Q \oplus R)$，然后翻译到集合层面。）

16. 证明：$(\mathcal{P}(U), \triangle, \cap)$ 构成一个交换环，其中 $\triangle$ 是加法，$\cap$ 是乘法。具体地，验证 $\cap$ 对 $\triangle$ 的分配律 $A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C)$，并说明这个环的加法单位元和乘法单位元分别是什么。
