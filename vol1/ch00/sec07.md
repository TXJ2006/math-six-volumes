# 0.7 集合的并与交

## 二元并交的定义与性质、逻辑对应、Venn 图直觉与证明方法

上一节讨论了子集、相等与幂集——它们刻画的是集合之间的"谁包含谁""谁等于谁""一个集合有多少种可能的部分"。现在进入集合论真正开始"运算"的地方：并与交。Halmos 把 union 与 intersection 放在朴素集合论最前面的基本操作中；Hammack 在 *Book of Proof* 里把它们与 Venn 图、差集、补集一起讲，强调这是"把逻辑语言转成集合语言的第一步"；Velleman 则特别突出它们与命题联结词 or / and 的对应关系；Tao 在分析与集合基础叙述中更关心这些运算如何自然推广到更大族的集合。经典教材虽然写法不同，但共同的主线非常清楚：并与交不是两个孤立记号，而是集合论里"合并条件"和"同时满足条件"的基本机制。

但要把这两个概念真正理解透，需要超出教材的标准叙述。Boole 在 1854 年的 *The Laws of Thought* 中最早把逻辑运算（$\lor, \land$）与类的运算（并、交）系统对应起来，建立了"逻辑就是集合代数"的基本图景。Cantor 在创立集合论时虽然更关注无穷集的比较，但他处理"Vereinigung"（并）和"Durchschnitt"（交）的方式已经蕴含了现代定义的核心——通过成员资格条件来组合集合。Dedekind 在 *Was sind und was sollen die Zahlen?* 中独立引入了"Gemeinheit"（公共部分，即交）的概念。Peano 在 1888-1895 年间发明了后来成为标准的 $\cup$ 和 $\cap$ 符号——这不是偶然的记号选择，而是为了在形式语言层面精确对应逻辑联结词。Hausdorff 在 *Grundzüge der Mengenlehre*（1914）中则首次系统整理了并交的代数性质（交换律、结合律、分配律、吸收律），把它们组织成一个完整的运算体系。

从本科生的视角看，并与交表面上只是"放在一起"和"共同部分"，似乎非常直观。但真正进入严格数学后，这两个概念的重要性远远超过图形直观。它们的本质不在于图画上两块区域如何重叠，而在于**成员资格怎样通过逻辑联结词组合起来**。集合论中的并与交，本质上是逻辑中的"或"与"且"在对象层面的实现。这个认识一旦建立，后面几乎所有集合恒等式都会变得透明：你不再是在记公式，而是在读逻辑。

---

### 一、并集的定义

> **定义（并集）.** 设 $A, B$ 为集合。$A$ 与 $B$ 的**并集（union）**记作 $A \cup B$，定义为
>
> $$
> A \cup B = \{x : x \in A \;\text{或}\; x \in B\}.
> $$
>
> 用量词语言写出来就是
>
> $$
> x \in A \cup B \;\;\iff\;\; x \in A \;\lor\; x \in B.
> $$

Velleman 在其集合章节中正是这样给出定义的：一个元素属于并集，当且仅当它**至少**属于两个集合中的一个。这里的"或"在数学中默认是**包含式或（inclusive or）**——若一个元素同时属于 $A$ 和 $B$，它当然也属于 $A \cup B$。这一点必须说透，因为日常语言里的"或"常常带有"二选一"的暗示，而数学中的并集绝不把重合部分排除在外。

> **例 1.** 设 $A = \{1, 2, 3\}$，$B = \{3, 4, 5\}$。则
>
> $$
> A \cup B = \{1, 2, 3, 4, 5\}.
> $$
>
> 元素 $3$ 虽然在两个集合中都出现，但在并集中只算一个元素，因为集合不计重复。

这说明并集不是"把两张列表拼接起来"，而是"把两个成员资格条件用逻辑或合并起来"。

> **例 2.** 设 $A = \{x \in \mathbb{R} : x > 0\}$，$B = \{x \in \mathbb{R} : x < 1\}$。则
>
> $$
> A \cup B = \{x \in \mathbb{R} : x > 0 \;\lor\; x < 1\} = \mathbb{R}.
> $$
>
> **理由.** 任取 $x \in \mathbb{R}$。若 $x \geq 1$，则 $x > 0$，故 $x \in A$。若 $x < 1$，则 $x \in B$。无论哪种情况，$x \in A \cup B$。反向显然（$A \cup B \subseteq \mathbb{R}$）。$\square$

> **例 3.** 设 $A = \{n \in \mathbb{Z} : 2 \mid n\}$（偶数集），$B = \{n \in \mathbb{Z} : 2 \nmid n\}$（奇数集）。则 $A \cup B = \mathbb{Z}$。
>
> **证明.** 任取 $n \in \mathbb{Z}$。$n$ 被 $2$ 除的余数为 $0$ 或 $1$。若余数为 $0$，则 $2 \mid n$，故 $n \in A$。若余数为 $1$，则 $2 \nmid n$，故 $n \in B$。因此 $n \in A \cup B$。反向由 $A, B \subseteq \mathbb{Z}$ 显然。$\square$

---

### 二、交集的定义

> **定义（交集）.** 设 $A, B$ 为集合。$A$ 与 $B$ 的**交集（intersection）**记作 $A \cap B$，定义为
>
> $$
> A \cap B = \{x : x \in A \;\text{且}\; x \in B\}.
> $$
>
> 用量词语言写出来就是
>
> $$
> x \in A \cap B \;\;\iff\;\; x \in A \;\land\; x \in B.
> $$

一个元素属于交集，当且仅当它**同时满足**两个集合的成员条件。Velleman 与 Hammack 都把这一点讲得非常清楚：交集的定义关键不在"重合区域"的图像，而在"同时满足"的逻辑强度。

**并集对应放宽条件：满足其一即可。交集对应加严条件：必须同时满足。** 这是贯穿本节的核心对比。

> **例 4.** 设 $A = \{1, 2, 3\}$，$B = \{3, 4, 5\}$。则
>
> $$
> A \cap B = \{3\}.
> $$
>
> 因为 $3$ 是唯一同时属于 $A$ 与 $B$ 的元素。

> **例 5.** 设 $A = \{x \in \mathbb{R} : x > 0\}$，$B = \{x \in \mathbb{R} : x < 1\}$。则
>
> $$
> A \cap B = \{x \in \mathbb{R} : 0 < x < 1\} = (0, 1).
> $$
>
> **证明.** $x \in A \cap B$ 当且仅当 $x > 0$ 且 $x < 1$，即 $0 < x < 1$。$\square$

这个例子值得注意：同样的两个集合 $A, B$，并集是 $\mathbb{R}$（极度扩张），交集是 $(0, 1)$（大幅收缩）。并与交对条件范围的相反效果在此一目了然。

> **例 6.** 设 $A = \{n \in \mathbb{Z} : 4 \mid n\}$，$B = \{n \in \mathbb{Z} : 6 \mid n\}$。证明 $A \cap B = \{n \in \mathbb{Z} : 12 \mid n\}$。
>
> **证明.** 设 $C = \{n \in \mathbb{Z} : 12 \mid n\}$。
>
> **($A \cap B \subseteq C$)** 设 $n \in A \cap B$，则 $4 \mid n$ 且 $6 \mid n$。因 $\text{lcm}(4, 6) = 12$，由最小公倍数的定义得 $12 \mid n$，故 $n \in C$。
>
> **($C \subseteq A \cap B$)** 设 $n \in C$，则 $12 \mid n$。因 $4 \mid 12$ 且 $6 \mid 12$，由整除的传递性得 $4 \mid n$ 且 $6 \mid n$，故 $n \in A \cap B$。
>
> 综合两个方向，$A \cap B = C$。$\square$

---

### 三、并交与逻辑联结词的结构对应

这里是本节最关键的思想。用命题函数来描述集合，设

$$
A = \{x : P(x)\}, \qquad B = \{x : Q(x)\},
$$

那么

$$
A \cup B = \{x : P(x) \lor Q(x)\}, \qquad A \cap B = \{x : P(x) \land Q(x)\}.
$$

这正是 Velleman 一类教材反复强调的**结构对应**：集合语言与命题逻辑并不是两套平行体系，而是同一结构的两种表达。Boole 在 *The Laws of Thought* 中通过代数记号把这种对应首次形式化，Schröder 在 *Vorlesungen über die Algebra der Logik*（1890-1905）中将其发展为系统的**关系代数**。Stone 的表示定理（1936）最终证明了这种对应不是巧合：**每个布尔代数都同构于某个集合域上的集合运算代数**。

从方法论的角度看，这个对应带来一条极其实用的原则：

> **集合恒等式的逻辑翻译原则.** 要判断或证明一个集合恒等式，可以先把所有集合运算翻译成逻辑联结词，然后检验对应的逻辑恒等式是否成立。

这就是为什么 0.5 节关于"描述法与逻辑对应"的讨论如此重要——它提供的不只是语言翻译，而是一整套从逻辑到集合的**证明迁移机制**。

| 集合运算 | 逻辑联结词 | 含义 |
|---|---|---|
| $x \in A \cup B$ | $P(x) \lor Q(x)$ | 至少满足一个条件 |
| $x \in A \cap B$ | $P(x) \land Q(x)$ | 同时满足两个条件 |
| $x \in A^c$ | $\neg P(x)$ | 不满足该条件 |
| $A \subseteq B$ | $\forall\, x,\; P(x) \to Q(x)$ | 一个条件蕴含另一个 |
| $A = B$ | $\forall\, x,\; P(x) \iff Q(x)$ | 两个条件等价 |

Pólya 在 *How to Solve It* 中所说的"Can you restate the problem?"在这里获得了精确的数学实现：把集合问题重新陈述为逻辑问题，往往就是解题的第一步。

---

### 四、交换律

一旦看清并交与逻辑的对应，基本性质就不再是需要死记的"运算律"，而是逻辑联结词性质的外化。

> **命题（交换律）.** 对任意集合 $A, B$，
>
> $$
> A \cup B = B \cup A, \qquad A \cap B = B \cap A.
> $$

> **证明（以并集为例）.**
>
> **($A \cup B \subseteq B \cup A$)** 任取 $x \in A \cup B$，则 $x \in A$ 或 $x \in B$。无论哪种情况，$x \in B$ 或 $x \in A$，即 $x \in B \cup A$。
>
> **($B \cup A \subseteq A \cup B$)** 同理。
>
> 因此 $A \cup B = B \cup A$。$\square$

这个证明虽然短，但它体现了集合相等的核心方法论：不是看式子长得对称，而是看元素资格在两个方向上是否一致。交换律之所以成立，根本原因是逻辑上

$$
P \lor Q \equiv Q \lor P, \qquad P \land Q \equiv Q \land P.
$$

把集合重新翻译成成员资格条件，这两个等价式就立刻给出结论。

---

### 五、结合律

> **命题（结合律）.** 对任意集合 $A, B, C$，
>
> $$
> (A \cup B) \cup C = A \cup (B \cup C), \qquad (A \cap B) \cap C = A \cap (B \cap C).
> $$

> **证明（以交集为例）.** 任取 $x$。
>
> $$
> x \in (A \cap B) \cap C \;\;\iff\;\; (x \in A \;\land\; x \in B) \;\land\; x \in C \;\;\iff\;\; x \in A \;\land\; (x \in B \;\land\; x \in C) \;\;\iff\;\; x \in A \cap (B \cap C).
> $$
>
> 中间一步用的是逻辑合取的结合律 $(P \land Q) \land R \equiv P \land (Q \land R)$。$\square$

结合律的深层意义在于，它允许我们把二元运算平滑推广到有限多个集合。

$$
A_1 \cup A_2 \cup \cdots \cup A_n
$$

不必纠结先并哪两个，最终结果一致。这不是书写方便的小事——Birkhoff 在 *Lattice Theory* 中指出，结合律是使二元运算能够自然扩展为 $n$ 元运算的必要条件。对本科生来说，这一点初看似乎只是书写方便，但事实上它在告诉你：并与交具有真正的代数结构，它们不是临时发明的图形操作，而是稳定的二元运算。

> **例 7.** 设 $A = \{1, 2\}$，$B = \{2, 3\}$，$C = \{3, 4\}$。验证结合律：
>
> - $(A \cup B) \cup C = \{1, 2, 3\} \cup \{3, 4\} = \{1, 2, 3, 4\}$
> - $A \cup (B \cup C) = \{1, 2\} \cup \{2, 3, 4\} = \{1, 2, 3, 4\}$
>
> 两者相等。$\square$

---

### 六、分配律

交换律和结合律说的是并和交各自的内部规则。分配律说的是并与交**之间**的互动。

> **命题（分配律）.** 对任意集合 $A, B, C$，
>
> $$
> A \cap (B \cup C) = (A \cap B) \cup (A \cap C),
> $$
>
> $$
> A \cup (B \cap C) = (A \cup B) \cap (A \cup C).
> $$

> **证明（第一条）.** 任取 $x$。
>
> **($\subseteq$)** 设 $x \in A \cap (B \cup C)$。则 $x \in A$ 且 $x \in B \cup C$。后者意味着 $x \in B$ 或 $x \in C$。
>
> - 若 $x \in B$，则 $x \in A$ 且 $x \in B$，故 $x \in A \cap B$，从而 $x \in (A \cap B) \cup (A \cap C)$。
> - 若 $x \in C$，则 $x \in A$ 且 $x \in C$，故 $x \in A \cap C$，从而 $x \in (A \cap B) \cup (A \cap C)$。
>
> **($\supseteq$)** 设 $x \in (A \cap B) \cup (A \cap C)$。则 $x \in A \cap B$ 或 $x \in A \cap C$。
>
> - 若 $x \in A \cap B$，则 $x \in A$ 且 $x \in B$，故 $x \in B \cup C$，从而 $x \in A \cap (B \cup C)$。
> - 若 $x \in A \cap C$，则 $x \in A$ 且 $x \in C$，故 $x \in B \cup C$，从而 $x \in A \cap (B \cup C)$。
>
> 由双向包含，等式成立。$\square$

从逻辑角度看，第一条分配律恰好就是命题逻辑中的

$$
P \land (Q \lor R) \iff (P \land Q) \lor (P \land R)
$$

在集合层面的实现。第二条同理对应

$$
P \lor (Q \land R) \iff (P \lor Q) \land (P \lor R).
$$

这两条分配律值得与数的运算做一个对比。在实数算术中，乘法对加法满足分配律（$a \cdot (b + c) = ab + ac$），但加法对乘法**不**满足分配律（$a + bc \neq (a+b)(a+c)$ 一般而言）。然而在集合论中，**并对交和交对并都满足分配律**——这是一个完美的对称性。Birkhoff 在格论中把这种双向分配律称为**分配格（distributive lattice）**的标志性性质。幂集 $\mathcal{P}(X)$ 关于 $\cup, \cap$ 构成分配格，而一般的格不一定满足分配律——这说明集合运算的代数结构比许多抽象代数结构更"好"。

> **例 8.** 设 $A = \{1, 2, 3\}$，$B = \{2, 4\}$，$C = \{3, 5\}$。验证第一条分配律。
>
> - 左边：$B \cup C = \{2, 3, 4, 5\}$，$A \cap (B \cup C) = \{2, 3\}$。
> - 右边：$A \cap B = \{2\}$，$A \cap C = \{3\}$，$(A \cap B) \cup (A \cap C) = \{2, 3\}$。
>
> 两边相等。$\square$

---

### 七、幂等律与吸收律

并与交还满足两条揭示集合本性的律则。

> **命题（幂等律）.** 对任意集合 $A$，
>
> $$
> A \cup A = A, \qquad A \cap A = A.
> $$

> **证明.** $x \in A \cup A \iff x \in A \lor x \in A \iff x \in A$。交集同理。$\square$

幂等律揭示了集合与列表（或多重集）的根本差别。对一个列表来说，把元素"重复加入"会产生不同结果；对集合来说不会。集合的世界不记录重复，因此幂等律是其本性，而不是附加规则。这也是集合运算与数的算术的根本差异之一——实数中 $a + a = 2a \neq a$（$a \neq 0$ 时），但集合中 $A \cup A = A$ 恒成立。

> **命题（吸收律）.** 对任意集合 $A, B$，
>
> $$
> A \cup (A \cap B) = A, \qquad A \cap (A \cup B) = A.
> $$

> **证明（第一条）.**
>
> **($\supseteq$)** 任取 $x \in A$。由 $A \subseteq A \cup (A \cap B)$ 显然。
>
> **($\subseteq$)** 任取 $x \in A \cup (A \cap B)$。则 $x \in A$ 或 $x \in A \cap B$。若 $x \in A$，结论已成立。若 $x \in A \cap B$，则 $x \in A$。无论哪种情况，$x \in A$。
>
> 因此 $A \cup (A \cap B) = A$。$\square$

吸收律在逻辑上对应 $P \lor (P \land Q) \equiv P$ 和 $P \land (P \lor Q) \equiv P$。它的直觉含义是：若某元素已经在 $A$ 中，那么把 $A$ 的一部分（$A \cap B$）再并进去，不会增加新元素；反过来，若某元素必须在 $A$ 中，那么再要求它同时属于含有 $A$ 的大集合（$A \cup B$），也不会缩小范围。

吸收律在代数中有独特地位。Whitehead 和 Huntington 在 20 世纪初研究布尔代数和格的公理系统时，发现**吸收律是区分格与环的关键**——环满足分配律但不满足吸收律，格满足吸收律但其加法不满足消去律。Dedekind 最早在 1900 年的论文中研究了满足吸收律的代数结构（他称之为"Dualgruppe"），这正是后来格论的萌芽。

---

### 八、并交的基本性质汇总

把前面证明的律则与子集关系的若干基本事实汇总如下，它们构成集合运算的完整代数骨架。

**与子集的关系：**

> **命题.** 对任意集合 $A, B$，
>
> (a) $A \subseteq A \cup B$，$B \subseteq A \cup B$。
>
> (b) $A \cap B \subseteq A$，$A \cap B \subseteq B$。
>
> (c) $A \subseteq B \;\;\iff\;\; A \cup B = B \;\;\iff\;\; A \cap B = A$。

> **证明.**
>
> (a) 若 $x \in A$，则 $x \in A$ 或 $x \in B$，故 $x \in A \cup B$。另一半同理。
>
> (b) 若 $x \in A \cap B$，则 $x \in A$ 且 $x \in B$，故 $x \in A$。另一半同理。
>
> (c) 先证 $A \subseteq B \Rightarrow A \cup B = B$：由 $B \subseteq A \cup B$ 已知一个方向；若 $x \in A \cup B$，则 $x \in A$ 或 $x \in B$，但 $A \subseteq B$ 保证第一种情况也有 $x \in B$，故 $A \cup B \subseteq B$。再证 $A \cup B = B \Rightarrow A \subseteq B$：由 $A \subseteq A \cup B = B$。最后 $A \subseteq B \iff A \cap B = A$ 同理可得。$\square$

性质 (c) 特别重要——它提供了子集关系的**三种等价刻画**。在实际证明中，有时直接证 $A \subseteq B$ 不便，转而证 $A \cup B = B$ 或 $A \cap B = A$ 反而更方便。Halmos 在 *Naive Set Theory* 中正是利用这种灵活性来简化许多后续证明的。

---

### 九、不相交集合

> **定义（不相交）.** 若 $A \cap B = \varnothing$，则称 $A$ 与 $B$ **不相交（disjoint）**。

$A \cap B = \varnothing$ 的含义是：不存在任何元素同时属于 $A$ 和 $B$。用量词语言表述：$\forall\, x,\; \neg(x \in A \land x \in B)$，等价于 $\forall\, x,\; x \in A \to x \notin B$。

> **例 9.** $\{1, 2\}$ 与 $\{3, 4\}$ 不相交。$\{n \in \mathbb{Z} : 2 \mid n\}$ 与 $\{n \in \mathbb{Z} : 2 \nmid n\}$ 不相交。

> **例 10.** 证明：对任意集合 $A$，$A$ 与 $\varnothing$ 不相交。
>
> **证明.** $A \cap \varnothing = \{x : x \in A \land x \in \varnothing\}$。由于 $x \in \varnothing$ 永远为假，合取 $x \in A \land x \in \varnothing$ 亦永远为假，故 $A \cap \varnothing = \varnothing$。$\square$

这个结论也可以从更一般的角度看：$\varnothing$ 是并运算的**单位元**（$A \cup \varnothing = A$），同时也是交运算的**零元**（$A \cap \varnothing = \varnothing$）。如果存在全集 $U$，则 $U$ 是交运算的单位元（$A \cap U = A$），也是并运算的零元（$A \cup U = U$）。这种对偶结构将在 0.8 节 De Morgan 律中得到系统展现。

---

### 十、Venn 图：直觉工具与操作边界

Hammack 在 *Book of Proof* 中专门把 Venn diagrams 单列出来，因为它们在入门阶段非常有效。核心思想是：把全集 $U$ 画成大矩形，把集合画成内部的封闭区域，于是并集对应两个区域的覆盖总和，交集对应两块区域重叠的部分。

**两个集合 $A, B$ 的 Venn 图分区.** 两个集合把全集 $U$ 分成四个互不相交的区域：

$$
A \cap B, \qquad A \setminus B, \qquad B \setminus A, \qquad U \setminus (A \cup B).
$$

其中 $A \setminus B = \{x \in A : x \notin B\}$ 是差集（0.8 节详述）。在 Venn 图中：

- $A \cup B$ 对应前三个区域的合并。
- $A \cap B$ 对应中间重叠区域。
- 四个区域的并等于 $U$，且两两不相交。

这就解释了为什么 Venn 图直觉上有效——它把成员资格的逻辑分类变成了平面上的区域分类。

> **例 11.** 设 $U = \{1, 2, 3, 4, 5, 6, 7, 8\}$，$A = \{1, 2, 3, 4, 5\}$，$B = \{4, 5, 6, 7\}$。在 Venn 图的四个区域中填入元素：
>
> - $A \cap B = \{4, 5\}$
> - $A \setminus B = \{1, 2, 3\}$
> - $B \setminus A = \{6, 7\}$
> - $U \setminus (A \cup B) = \{8\}$

但这里必须说清楚一个边界：**Venn 图是直觉工具，不是证明本身。** 它能帮你猜测交换律、结合律、分配律为何成立，却不能替代严格证明。因为 Venn 图本质上只展示有限个集合、有限层关系，且依赖视觉直觉；而严格的数学证明必须回到"任取元素"的成员资格论证，或者回到逻辑恒等式。经典教材在这一点上态度一致：图像可以辅助理解，但严格性来自定义。

John Venn 本人在 1880 年发表 *On the Diagrammatic and Mechanical Representation of Propositions and Reasonings* 时，明确把图表法定位为辅助工具（"merely illustrative"），而非逻辑推理的替代。Euler 在 18 世纪更早地使用了类似的圆形图（Euler diagrams），但 Euler 图的约定与 Venn 图不同——Euler 图只画实际存在的包含关系，而 Venn 图画出所有可能的区域。这个区别在处理三个以上集合时尤为重要。

从方法论角度看，Venn 图的真正价值在于提醒你：集合运算有两种等价视角。第一种是**逻辑视角**——并是"或"，交是"且"；第二种是**几何视角**——并是区域合并，交是区域重叠。成熟的数学学习者必须能在这两种视角之间自由切换。只会图像不够严谨，只会定义不够灵活。**图像帮助你猜结构，定义帮助你证结构。**

---

### 十一、并交的证明示范

掌握了定义后，关于并交的证明就有了统一的方法论。下面通过几个典型例题展示完整的论证过程。

> **例 12.** 证明：对任意集合 $A, B$，$A \setminus B \subseteq A$。
>
> **证明.** 设 $x \in A \setminus B$，则 $x \in A$ 且 $x \notin B$。由前一个条件立即得 $x \in A$。$\square$

> **例 13.** 证明：对任意集合 $A, B, C$，若 $A \subseteq C$ 且 $B \subseteq C$，则 $A \cup B \subseteq C$。
>
> **证明.** 设 $x \in A \cup B$，则 $x \in A$ 或 $x \in B$。
>
> - 若 $x \in A$，由 $A \subseteq C$ 得 $x \in C$。
> - 若 $x \in B$，由 $B \subseteq C$ 得 $x \in C$。
>
> 无论哪种情况，$x \in C$。$\square$

这个命题说明：$C$ 是 $A$ 和 $B$ 的公共超集，当且仅当 $A \cup B \subseteq C$。换言之，**$A \cup B$ 是包含 $A$ 和 $B$ 的最小集合**——它是 $A$ 和 $B$ 的所有公共超集的交。这正是 Birkhoff 格论中**最小上界（join）** 的定义。

> **例 14.** 证明：对任意集合 $A, B, C$，若 $C \subseteq A$ 且 $C \subseteq B$，则 $C \subseteq A \cap B$。
>
> **证明.** 设 $x \in C$。由 $C \subseteq A$ 得 $x \in A$；由 $C \subseteq B$ 得 $x \in B$。因此 $x \in A \land x \in B$，即 $x \in A \cap B$。$\square$

对称地，**$A \cap B$ 是同时包含于 $A$ 和 $B$ 的最大集合**——它是 $A$ 和 $B$ 的所有公共子集的并。这是格论中**最大下界（meet）** 的定义。

例 13 和例 14 合在一起揭示了一个深层结构：$\cup$ 是偏序 $(\mathcal{P}(U), \subseteq)$ 中的 join，$\cap$ 是 meet。这一视角在 Mac Lane 和 Birkhoff 的 *Algebra*（1967）中被系统阐述，成为统一理解格、布尔代数和拓扑的出发点。

> **例 15.** 证明：对任意集合 $A, B$，
>
> $$
> A \cup B = A \;\;\iff\;\; B \subseteq A.
> $$
>
> **证明.**
>
> **($\Rightarrow$)** 设 $A \cup B = A$。任取 $x \in B$，则 $x \in A \cup B = A$，故 $B \subseteq A$。
>
> **($\Leftarrow$)** 设 $B \subseteq A$。$A \subseteq A \cup B$ 显然。任取 $x \in A \cup B$，则 $x \in A$ 或 $x \in B$，后者由 $B \subseteq A$ 也有 $x \in A$。故 $A \cup B \subseteq A$。$\square$

> **例 16.** 证明或反驳：对任意集合 $A, B, C$，若 $A \cup B = A \cup C$，则 $B = C$。
>
> **反驳.** 取 $A = \{1, 2, 3\}$，$B = \{1\}$，$C = \{2\}$。则
>
> $$
> A \cup B = \{1, 2, 3\} = A \cup C,
> $$
>
> 但 $B = \{1\} \neq \{2\} = C$。$\square$
>
> **分析.** 这说明并运算不满足消去律。原因在于 $A$ 已经"吞没"了 $B$ 和 $C$ 中的部分元素，导致 $B$ 和 $C$ 的差异被 $A$ 掩盖了。在代数术语中，$(\mathcal{P}(U), \cup)$ 不构成群——缺少逆元。

---

### 十二、并交的深层视角

把并与交理解透，需要看清它们在不同数学分支中承担的角色。

**实分析视角.** 开区间的并常常用来拼接更大的开放区域。一个关键定理是：$\mathbb{R}$ 中的每个开集都可以写成至多可数个不相交开区间的并。闭区间的交常常用来逐步压缩范围——区间套定理（Cantor 交定理）正是利用嵌套闭区间的交来定位极限点。

**概率论视角.** 事件的并对应"至少一个事件发生"，交对应"所有事件同时发生"。概率论中的容斥原理（inclusion-exclusion principle）

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

就是在定量修正并集运算中"重复计算"的部分。

**拓扑学视角.** 拓扑空间的公理要求开集族对**有限交**和**任意并**封闭——注意这里的不对称性：交只要求有限，并可以任意。这个不对称性不是人为规定，而是出于深层的数学必要性。Hausdorff 在建立拓扑学基础时清楚地意识到：无限个开集的交不一定是开集（例如 $\bigcap_{n=1}^{\infty}(-1/n, 1/n) = \{0\}$ 是单点集，不是开集），但无限个开集的并一定是开集。

**代数视角.** 子结构（子群、子环、子模、子空间）的交通常仍保留结构，而并则往往不保留。例如两个子群的交仍是子群，但两个子群的并一般不是子群。这说明交运算在代数结构中更"安全"——它保持封闭性。这正是为什么在代数中，生成子群、生成子空间的定义都用"包含某集合的所有子结构的**交**"来给出。Emmy Noether 的抽象代数方法论正是在这一背景下展开的。

**范畴论视角.** Mac Lane 在 *Categories for the Working Mathematician* 中把并与交推广为**余积（coproduct）** 与**积（product）** 的特殊情形。在集合范畴 $\mathbf{Set}$ 中，积是笛卡尔积，余积是不相交并。但在偏序范畴中，$\cup$ 就是余积，$\cap$ 就是积。这种统一视角解释了为什么并和交在完全不同的数学语境中反复出现——它们不是集合论的专有物，而是满足一个共同的范畴论性质（万有性质）的构造。

---

### 十三、集合运算的代数结构

把本节的所有律则放在一起，可以看到一个完整的代数图景。

幂集 $\mathcal{P}(U)$ 关于 $\cup, \cap$ 满足：
- **交换律**：$A \cup B = B \cup A$，$A \cap B = B \cap A$
- **结合律**：$(A \cup B) \cup C = A \cup (B \cup C)$，$(A \cap B) \cap C = A \cap (B \cap C)$
- **分配律**（双向）：$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$，$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
- **幂等律**：$A \cup A = A$，$A \cap A = A$
- **吸收律**：$A \cup (A \cap B) = A$，$A \cap (A \cup B) = A$
- **单位元与零元**：$A \cup \varnothing = A$，$A \cap U = A$，$A \cap \varnothing = \varnothing$，$A \cup U = U$

这些性质合在一起，恰好说明 $(\mathcal{P}(U), \cup, \cap)$ 构成一个**有界分配格（bounded distributive lattice）**。如果再加上补运算（0.8 节），则进一步成为**布尔代数（Boolean algebra）**——这正是 0.6 节提到的 Stone 表示定理的出发点。

从公理化方法论的角度看，这些律则不是一堆需要记忆的公式，而是一个代数结构的**公理骨架**。Huntington 在 1904 年给出了布尔代数的第一组独立公理系统，其中核心就是交换律、分配律和补余律。Birkhoff 随后证明，仅用吸收律就可以公理化格结构。这意味着上面列出的性质有着**内在的逻辑层次**——有些是更基本的，有些是从更基本的推出的。

---

### 十四、方法论总结：并交问题的思考框架

Pólya 在 *How to Solve It* 中强调，面对任何数学问题都应当先问三个问题：条件是什么？未知量是什么？你见过类似的问题吗？在并交问题中，这些问题可以具体化为：

**第一步：翻译.** 把集合语言翻译成逻辑语言。$\cup$ 变 $\lor$，$\cap$ 变 $\land$，$\subseteq$ 变 $\forall\, x,\; \to$，$=$ 变 $\forall\, x,\; \iff$。

**第二步：选择策略.**
- 证集合相等：双向包含法。
- 证子集关系：任取元素，推出归属。
- 反驳相等或包含：找反例（区分元素）。
- 验证恒等式：先把两边翻译成逻辑式，检查是否为逻辑恒等式。

**第三步：执行.** 逐行写出论证，每步标明依据。并集的证明中，遇到 $x \in A \cup B$ 时，分 $x \in A$ 和 $x \in B$ 两种情况讨论（情形分析）。交集的证明中，$x \in A \cap B$ 同时给出两个条件，可以分别使用。

**第四步：回顾.** 证明完成后审视：（1）所用的是哪条逻辑律？（2）结论能否推广到三个以上集合？（3）是否有更简洁的证法（例如直接引用已知恒等式）？

---

### 十五、本节的核心结构

回顾本节内容，可以提炼出三层递进的认识。

**第一层：定义层.** 并集和交集的定义完全由成员资格决定——$\cup$ 对应 $\lor$，$\cap$ 对应 $\land$。不理解这一点，就只能靠 Venn 图的视觉记忆，遇到稍微抽象的集合就会失去方向。

**第二层：代数层.** 并与交满足交换律、结合律、分配律、幂等律、吸收律。这些性质不是独立事实，而是逻辑联结词对应性质在集合层面的表现。掌握了逻辑，就掌握了集合运算的全部代数规则。

**第三层：结构层.** 并与交揭示了集合论中最基本的两种组织方式。并是扩张——放宽准入门槛；交是收缩——提高准入门槛。数学中的分类、分解、逼近、限制，都是这两种机制的不同变形。从格论的角度看，$\cup$ 是 join，$\cap$ 是 meet；从范畴论的角度看，它们是万有构造的特殊实例。

用一句话收束本节：**并与交不是在"拼图"，而是在"组合条件"。** 一旦看清这一点，集合运算就不再是花括号之间的机械变形，而成为逻辑、几何与结构三者统一的语言。

---

### 十六、练习

**A 组（基本运算）**

1. 设 $A = \{1, 2, 3, 4\}$，$B = \{3, 4, 5, 6\}$，$C = \{5, 6, 7, 8\}$。分别计算 $A \cup B$，$A \cap B$，$(A \cup B) \cap C$，$A \cup (B \cap C)$。
2. 设 $A = \{x \in \mathbb{R} : x^2 \leq 4\}$，$B = \{x \in \mathbb{R} : x \geq 0\}$。用区间表示 $A \cup B$ 和 $A \cap B$。
3. 设 $A = \{n \in \mathbb{Z} : 3 \mid n\}$，$B = \{n \in \mathbb{Z} : 5 \mid n\}$。证明 $A \cap B = \{n \in \mathbb{Z} : 15 \mid n\}$。

**B 组（性质证明）**

4. 证明 $A \cup \varnothing = A$ 和 $A \cap \varnothing = \varnothing$。
5. 证明第二条分配律：$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$。
6. 证明第二条吸收律：$A \cap (A \cup B) = A$。
7. 证明：若 $A \cap B = A \cap C$ 且 $A \cup B = A \cup C$，则 $B = C$。

**C 组（集合等式与子集）**

8. 证明：$A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)$，然后说明反向包含也成立（从而给出分配律的另一种证法）。
9. 证明：$A \cap B = A \setminus (A \setminus B)$。（提示：展开差集的定义。）
10. 证明或反驳：$(A \cup B) \cap C = A \cup (B \cap C)$。
11. 证明：$A \subseteq B$ 当且仅当 $A \cup B = B$。

**D 组（不相交与分解）**

12. 设 $A, B$ 为集合。证明 $A = (A \cap B) \cup (A \setminus B)$，且 $A \cap B$ 与 $A \setminus B$ 不相交。
13. 设 $A \cap B = \varnothing$。证明 $A \cup B = A \triangle B$，其中 $A \triangle B = (A \setminus B) \cup (B \setminus A)$ 是对称差（0.8 节详述）。

**E 组（思考题）**

14. 证明：对任意集合 $A, B$，$\mathcal{P}(A) \cap \mathcal{P}(B) = \mathcal{P}(A \cap B)$。再问：$\mathcal{P}(A) \cup \mathcal{P}(B) = \mathcal{P}(A \cup B)$ 是否成立？若不成立，给出反例并说明哪个方向的包含失败。
15. 在拓扑学中，开集族要求对有限交和任意并封闭。举例说明为什么"任意交"不能替代"有限交"（即给出可数个开集，其交不是开集的例子）。
