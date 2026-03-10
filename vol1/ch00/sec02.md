# 0.2 量词与命题函数

## 分析学语言的真正起点

上一节建立了命题逻辑的基本框架：命题、联结词、真值表、推理规则。但我们在最后坦承了命题逻辑的边界——它无法处理"对所有""存在"这类核心数学表达。数学中几乎所有深刻的定理，从极限到连续到收敛到可导，都不是关于一个固定命题的真假判断，而是关于**一族依赖于变量的命题**在某种量化范围下是否成立的声明。处理这种结构，需要两个新工具：**命题函数**与**量词**。

从数学家的视角来看，量词是分析学语言的底层机制。Tao 在 *Analysis I* 中反复强调，学生在极限和连续定义上犯的错误，绝大多数不是计算失误，而是量词误读——要么读反了全称与存在的顺序，要么在否定时只翻转了一层量词而遗漏了更深层的结构。Velleman 在 *How to Prove It* 中把量词视为"证明发现的指南"：全称量词告诉你要假设什么是任意的，存在量词告诉你要构造什么。Hammack 的做法则是把量词与证明策略直接绑定：看到 $\forall$ 就"设一个任意的"，看到 $\exists$ 就"找一个具体的"。

我们这一节要做的，是把这三种视角融合在一起，同时将量词语法与分析学的核心定义紧密对接，使读者在学到极限之前就已经具备精确读写量词表达式的能力。

---

### 一、从命题到命题函数：变量如何改变真假

在命题逻辑中，$P$ 是一个确定为真或假的陈述。但考虑如下表达：

$$
x^2 - 4 = 0.
$$

这既不是真也不是假——它的真假依赖于 $x$ 的取值。当 $x = 2$ 或 $x = -2$ 时它为真，否则为假。这种含有**自由变量**的表达式，在逻辑中称为**命题函数（propositional function）**，也常称为**谓词（predicate）**或**开句（open sentence）**。

> **定义.** 设 $D$ 是一个非空集合（称为**论域**或**全集**，universe of discourse）。一个**命题函数**是一个映射
>
> $$
> P: D \to \{T, F\},
> $$
>
> 它给 $D$ 中的每一个元素 $x$ 赋予一个确定的真值 $P(x)$。换言之，$P(x)$ 是一个含自由变量 $x$ 的表达式，当 $x$ 被指定为 $D$ 中某个具体元素时，$P(x)$ 变成一个命题。

> **例 1.** 设论域 $D = \mathbb{R}$，$P(x): x^2 \geq 0$。
>
> 对任何实数 $x$，$x^2 \geq 0$ 都成立，所以 $P(x)$ 对所有 $x \in \mathbb{R}$ 为真。

> **例 2.** 设 $D = \mathbb{R}$，$Q(x): x^2 - 3x + 2 = 0$。
>
> $Q(1) = T$（因为 $1 - 3 + 2 = 0$），$Q(2) = T$（因为 $4 - 6 + 2 = 0$），但 $Q(3) = F$（因为 $9 - 9 + 2 = 2 \neq 0$）。也就是说，$Q$ 只在 $x = 1$ 和 $x = 2$ 处为真。

> **例 3.** 命题函数可以有多个变量。设 $D = \mathbb{R} \times \mathbb{R}$，$R(x, y): x + y = 5$。
>
> $R(2, 3) = T$，$R(1, 1) = F$，$R(0, 5) = T$。这里 $R$ 是一个**二元谓词**。

命题函数是命题逻辑通往分析学的桥梁。分析学中的几乎每一条定义和定理，都在操作命题函数而非固定命题。例如"$|a_n - a| < \varepsilon$"本身不是命题——它的真假取决于 $n$、$\varepsilon$、数列 $\{a_n\}$ 和极限值 $a$。只有在量词把这些变量的范围和顺序规定清楚之后，它才变成一个可以被判定真假的完整命题。

从深层看，命题函数的本质是**把一个集合按照某种性质划分为"真"和"假"两部分**。集合 $\{x \in D : P(x)\}$ 就是所有使 $P(x)$ 为真的元素组成的子集。这将在 0.5 节（集合概念）中正式出现，那里我们会看到，集合的构造性定义正依赖命题函数。

---

### 二、全称量词（$\forall$）：普遍性声明

命题函数 $P(x)$ 本身没有确定真值，但一旦我们宣布"$P(x)$ 对 $D$ 中**所有**元素都成立"，就得到了一个完整的命题。这种"对所有"的宣称，由**全称量词（universal quantifier）**来表达。

> **定义.** 设 $P(x)$ 是论域 $D$ 上的命题函数。**全称量化命题**
>
> $$
> \forall x \in D,\; P(x)
> $$
>
> 读作"对所有 $x \in D$，$P(x)$ 成立"。它是一个命题：当且仅当 $D$ 中的每一个 $x$ 都使 $P(x)$ 为真时，它为真；只要存在哪怕一个 $x \in D$ 使 $P(x)$ 为假，它就为假。

> **例 4.** $\forall x \in \mathbb{R},\; x^2 \geq 0$。这是真命题：每个实数的平方都非负。

> **例 5.** $\forall x \in \mathbb{R},\; x^2 > 0$。这是假命题：$x = 0$ 是反例。

> **例 6.** $\forall n \in \mathbb{N},\; n(n+1) \text{ 是偶数}$。这是真命题。证明：$n$ 与 $n+1$ 中必有一个偶数，因此乘积为偶数。

全称量词在数学中的出现频率极高，但很多时候它是**隐含的**。训练量词敏感性的第一步，就是学会识别自然语言中的隐含全称量词。

> **例 7（隐含全称量词的识别）.** 以下三种写法在数学中含义相同：
>
> - "实数的平方非负。"
> - "任何实数的平方都不小于零。"
> - "$\forall x \in \mathbb{R},\; x^2 \geq 0$。"
>
> 第一种写法最接近日常表达，但其中"实数的平方"已经隐含了"任取一个实数 $x$"——这就是一个未写出的 $\forall$。

从证明的角度看，全称量词告诉你：**你不能挑选一个特殊的 $x$，而必须对任意的 $x$ 进行论证。** Velleman 把这表述为一条操作准则：要证 $\forall x \in D,\; P(x)$，你应当"设 $x$ 为 $D$ 中任意一个元素"，然后在不对 $x$ 做任何特殊假设的前提下证明 $P(x)$ 成立。

> **要推翻** $\forall x \in D,\; P(x)$，只需找到**一个反例**——某个具体的 $x_0 \in D$ 使得 $P(x_0)$ 为假。这呼应了上一节关于条件命题的讨论：全称命题被"击穿"只需一个反例。

> **例 8.** 推翻"$\forall x \in \mathbb{R},\; |x| = x$"：取 $x = -1$，则 $|{-1}| = 1 \neq -1$。一个反例足矣。

---

### 三、存在量词（$\exists$）：存在性保证

与全称量词对称的是**存在量词（existential quantifier）**。它宣称命题函数**至少有一个**成立的实例。

> **定义.** 设 $P(x)$ 是论域 $D$ 上的命题函数。**存在量化命题**
>
> $$
> \exists x \in D,\; P(x)
> $$
>
> 读作"存在 $x \in D$，使得 $P(x)$ 成立"。它是一个命题：当且仅当 $D$ 中至少有一个 $x$ 使 $P(x)$ 为真时，它为真；当 $D$ 中没有任何 $x$ 使 $P(x)$ 为真时，它为假。

> **例 9.** $\exists x \in \mathbb{R},\; x^2 = 2$。这是真命题：$x = \sqrt{2}$ 即满足。

> **例 10.** $\exists n \in \mathbb{N},\; 2n + 1 = 6$。这是假命题：$n = 5/2 \notin \mathbb{N}$。

从证明角度看，存在量词告诉你：**你必须构造出一个具体对象，或者间接地证明它的存在。** Velleman 称之为"existential instantiation"——一旦你需要证明 $\exists x,\; P(x)$，你必须展示一个见证者（witness）。

> **例 11.** 证明 $\exists x \in \mathbb{R},\; x^3 + x - 1 = 0$。
>
> 设 $f(x) = x^3 + x - 1$。$f(0) = -1 < 0$，$f(1) = 1 > 0$。由连续函数的介值定理，$f$ 在 $(0, 1)$ 内至少有一个零点。因此满足条件的 $x$ 存在。$\square$
>
> 这里我们并没有写出 $x$ 的精确值，但通过介值定理间接保证了存在性——这在分析学中极其常见。

要**推翻** $\exists x \in D,\; P(x)$，必须证明对 $D$ 中**所有**的 $x$，$P(x)$ 都不成立——这等价于证 $\forall x \in D,\; \neg P(x)$，工作量远大于推翻全称命题。

---

### 四、约束域：量词的精确范围

量词的含义完全依赖于它的**约束域**。同一个命题函数在不同论域下的量化结果可能完全不同。

> **例 12.**
>
> - $\forall x \in \mathbb{R},\; x^2 \geq 0$ 为真。
> - $\forall x \in \mathbb{C},\; x^2 \geq 0$ 无意义，因为复数没有全序关系，"$\geq 0$"不能直接定义（除非限制在实部或模的意义上）。
>
> 论域从 $\mathbb{R}$ 换到 $\mathbb{C}$，整个命题的意义就变了。

> **例 13.**
>
> - $\exists x \in \mathbb{Q},\; x^2 = 2$ 为假（$\sqrt{2}$ 不是有理数）。
> - $\exists x \in \mathbb{R},\; x^2 = 2$ 为真（$\sqrt{2} \in \mathbb{R}$）。
>
> 同一个方程，在有理数内无解、在实数内有解——仅因为论域不同。

这一点在分析学中至关重要。数列 $\{(-1)^n\}$ 在 $\mathbb{R}$ 中不收敛，但如果在离散度量意义下考虑某些子列，就可能有极限点。**写量词时必须明确约束域**，否则论证就没有基础。

在实际数学写作中，约束域有时从上下文推断。教材写"设 $\varepsilon > 0$"时，通常默认 $\varepsilon \in \mathbb{R}$；写"设 $n \in \mathbb{N}$"时约束域是自然数。但严格来说，省略约束域是一种简写，不是省略逻辑。在学习阶段，我们建议**始终显式写出量词的约束域**，直到这种习惯内化。

---

### 五、量词的否定：De Morgan 律的量词版本

这是本节最实用、也是初学者最容易出错的部分。

在命题逻辑中，De Morgan 律告诉我们否定如何在 $\land$ 和 $\lor$ 之间转换。量词的否定是它的自然推广：

> **定理（量词否定律）.**
>
> $$
> \neg\bigl(\forall x \in D,\; P(x)\bigr) \equiv \exists x \in D,\; \neg P(x),
> $$
>
> $$
> \neg\bigl(\exists x \in D,\; P(x)\bigr) \equiv \forall x \in D,\; \neg P(x).
> $$

第一条说："并非所有 $x$ 都满足 $P$"等价于"存在某个 $x$ 使 $P$ 不成立"。第二条说："不存在满足 $P$ 的 $x$"等价于"所有 $x$ 都不满足 $P$"。

这两条规则的直觉是清晰的：$\forall$ 相当于"无穷个合取"——$P(x_1) \land P(x_2) \land \cdots$，否定后变成"无穷个析取"的存在；$\exists$ 相当于"无穷个析取"——$P(x_1) \lor P(x_2) \lor \cdots$，否定后变成"无穷个合取"的全称。量词否定律正是 De Morgan 律从有限到无限的推广。

> **例 14.** 否定"所有素数都是奇数"，即
>
> $$
> \neg\bigl(\forall p \in \text{素数},\; p \text{ 是奇数}\bigr) \equiv \exists p \in \text{素数},\; p \text{ 不是奇数}.
> $$
>
> 而 $p = 2$ 恰好就是这个见证者：$2$ 是素数但不是奇数。所以原命题为假，因为它的否定为真。

> **例 15.** 否定"存在有理数 $x$ 使得 $x^2 = 2$"，即
>
> $$
> \neg\bigl(\exists x \in \mathbb{Q},\; x^2 = 2\bigr) \equiv \forall x \in \mathbb{Q},\; x^2 \neq 2.
> $$
>
> 这正是"$\sqrt{2}$ 不是有理数"的逻辑内容——没有任何有理数的平方等于 $2$。

> **例 16（为什么量词否定在分析中极其重要）.** 数列 $\{a_n\}$ 收敛到 $a$ 的定义：
>
> $$
> \forall \varepsilon > 0,\; \exists N \in \mathbb{N},\; \forall n > N,\; |a_n - a| < \varepsilon.
> $$
>
> 逐层否定：
>
> $$
> \exists \varepsilon > 0,\; \forall N \in \mathbb{N},\; \exists n > N,\; |a_n - a| \geq \varepsilon.
> $$
>
> 这就是"$\{a_n\}$ **不**收敛到 $a$"的精确含义：存在某个正的误差阈值 $\varepsilon$，（不管你选多大的 $N$），总能在 $N$ 之后找到一个项 $a_n$ 偏离 $a$ 至少 $\varepsilon$。
>
> 注意否定的机械操作：**每过一层量词就翻转（$\forall \leftrightarrow \exists$），最内层的不等式方向也翻转（$< \to \geq$）**。这是一个纯粹的逻辑操作，不需要任何分析知识，但它是证明"某个数列不收敛"的逻辑起点。

Tao 在 *Analysis I* 中反复练习这种逐层否定，并指出：**如果你无法写出一个分析定义的否定形式，那你实际上还没有真正理解这个定义。** 这个判断标准值得每一位学习分析的人铭记。

---

### 六、嵌套量词：分析学的核心语法

分析学的特征之一是量词的**深度嵌套**。一个极限定义至少有三层量词，一致连续定义也是三层，一致收敛定义还是三层。正确理解嵌套量词的含义——特别是**每一层量词所控制的范围**和**各层之间的依赖关系**——是掌握分析学的关键能力。

> **例 17（极限定义的量词结构）.**
>
> $$
> \lim_{n \to \infty} a_n = a \;\;\overset{\text{def}}{\iff}\;\; \forall \varepsilon > 0,\; \exists N \in \mathbb{N},\; \forall n > N,\; |a_n - a| < \varepsilon.
> $$
>
> 三层量词的含义：
>
> - **第一层** $\forall \varepsilon > 0$：对手挑选任意精度要求（外部/挑战者控制）
> - **第二层** $\exists N \in \mathbb{N}$：我方找到一个足够大的起点（证明者控制，可依赖 $\varepsilon$）
> - **第三层** $\forall n > N$：该起点之后的所有项都满足（普遍验证）
>
> 注意第二层的 $N$ **可以依赖于** $\varepsilon$——这是嵌套结构允许的。$\varepsilon$ 越小，$N$ 通常越大。这种"外层量词的参数流入内层选择"的机制，是嵌套量词的本质。

> **例 18（连续性定义的量词结构）.** 函数 $f$ 在点 $x_0$ 处连续：
>
> $$
> \forall \varepsilon > 0,\; \exists \delta > 0,\; \forall x \in D,\; |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon.
> $$
>
> 同样三层：任意精度要求 $\varepsilon$ → 存在输入范围 $\delta$（可依赖 $\varepsilon$ 和 $x_0$）→ 范围内所有 $x$ 都满足输出精度。

> **例 19（一致连续的量词结构）.** 函数 $f$ 在 $D$ 上一致连续：
>
> $$
> \forall \varepsilon > 0,\; \exists \delta > 0,\; \forall x, y \in D,\; |x - y| < \delta \implies |f(x) - f(y)| < \varepsilon.
> $$
>
> 表面上与例 18 相似，但关键区别在于：这里 $\delta$ **只依赖于 $\varepsilon$**，不再依赖于具体的点 $x_0$。同一个 $\delta$ 要对所有 $x, y$ 都管用。逻辑上，这是因为 $\delta$ 出现在 $\forall x, y$ 之前（外层），而不是之后。

仅仅是 $\delta$ 的位置从"在 $x_0$ 之后"移到"在 $x, y$ 之前"，就把"逐点连续"变成了"一致连续"——一个更强的性质。这种区分完全来自量词的嵌套顺序。

---

### 七、量词顺序：为什么交换量词会改变一切

嵌套量词中最深刻的一点是：**$\forall$ 和 $\exists$ 的顺序不能随意交换。** 这是本节最核心的洞见，也是本科分析课上错误率最高的地方。

> **定理.** 一般地，
>
> $$
> \forall x,\; \exists y,\; P(x, y) \;\;\not\equiv\;\; \exists y,\; \forall x,\; P(x, y).
> $$
>
> 但有一个方向的蕴涵总是成立的：
>
> $$
> \bigl(\exists y,\; \forall x,\; P(x, y)\bigr) \;\;\implies\;\; \bigl(\forall x,\; \exists y,\; P(x, y)\bigr).
> $$

直觉上，"先存在一个 $y$ 对所有 $x$ 都管用"比"对每个 $x$ 分别找一个 $y$"要求更强。前者的 $y$ 是统一的，后者的 $y$ 可以随 $x$ 变化。所以前者蕴涵后者，但反过来不成立。

> **例 20.** 设论域 $D = \mathbb{R}$，$P(x, y): x + y = 0$。
>
> - $\forall x \in \mathbb{R},\; \exists y \in \mathbb{R},\; x + y = 0$。**真**：对每个 $x$，取 $y = -x$ 即可。
> - $\exists y \in \mathbb{R},\; \forall x \in \mathbb{R},\; x + y = 0$。**假**：没有一个固定的 $y$ 能让所有 $x$ 都满足 $x + y = 0$。
>
> 第一种，$y$ 依赖于 $x$（$y = -x$）；第二种要求 $y$ 独立于 $x$，不可能。

> **例 21（分析学中的经典实例）.** 对比"逐点连续"与"一致连续"：
>
> - **逐点连续**：$\forall x_0 \in D,\; \forall \varepsilon > 0,\; \exists \delta > 0,\; \cdots$
> - **一致连续**：$\forall \varepsilon > 0,\; \exists \delta > 0,\; \forall x, y \in D,\; \cdots$
>
> 逐点连续中 $\delta$ 可以同时依赖 $\varepsilon$ 和 $x_0$；一致连续中 $\delta$ 只依赖 $\varepsilon$。后者更强。$f(x) = x^2$ 在 $\mathbb{R}$ 上逐点连续但不一致连续，就是因为 $\delta$ 必须随 $x_0$ 的增大而缩小，无法找到统一的 $\delta$。

> **例 22（逐点收敛 vs 一致收敛）.** 函数列 $\{f_n\}$ 在 $D$ 上：
>
> - **逐点收敛**：$\forall x \in D,\; \forall \varepsilon > 0,\; \exists N,\; \forall n > N,\; |f_n(x) - f(x)| < \varepsilon$
> - **一致收敛**：$\forall \varepsilon > 0,\; \exists N,\; \forall n > N,\; \forall x \in D,\; |f_n(x) - f(x)| < \varepsilon$
>
> 逐点收敛中 $N$ 可以依赖 $x$ 和 $\varepsilon$；一致收敛中 $N$ 只依赖 $\varepsilon$。$f_n(x) = x^n$ 在 $[0, 1)$ 上逐点收敛到 $0$，但不一致收敛——因为越接近 $x = 1$，需要的 $N$ 越大。

Tao 将这种"交换量词使命题变强"的现象概括为一条原则：**把存在量词往外推（使其出现在更多全称量词之前），命题变强；把存在量词往里推（使其出现在更多全称量词之后），命题变弱。** 这个原则贯穿整个分析课程。

---

### 八、唯一存在量词（$\exists!$）

数学中常需表达"恰好存在一个"满足条件的对象。这由**唯一存在量词**表达：

$$
\exists! x \in D,\; P(x),
$$

读作"存在唯一的 $x \in D$ 使得 $P(x)$ 成立"。

> **定义.** $\exists! x \in D,\; P(x)$ 是以下合取命题的缩写：
>
> **存在性**：$\exists x \in D,\; P(x)$；
>
> **唯一性**：$\forall x, y \in D,\; \bigl(P(x) \land P(y)\bigr) \to x = y$。

也就是说，至少有一个满足 $P$ 的 $x$（存在性），并且任何两个都满足 $P$ 的元素必须相等（唯一性）。

> **例 23.** $\exists! x \in \mathbb{R},\; x + 3 = 5$。存在性：$x = 2$ 满足。唯一性：若 $x + 3 = 5$ 且 $y + 3 = 5$，则 $x = 2 = y$。

> **例 24.** $\exists! x \in \mathbb{R},\; x^2 = 4$ 为假。存在性成立（$x = 2$ 或 $x = -2$），但唯一性不成立——有两个解。

在分析学中，唯一存在量词出现在许多关键定理中：极限的唯一性（若数列收敛，则极限唯一）、导数的唯一性、Picard 定理（初值问题解的唯一性）等。证明唯一性的标准策略是：**假设有两个都满足条件的对象，证明它们必须相等。**

> **例 25（极限的唯一性）.** 若 $\lim_{n \to \infty} a_n = a$ 且 $\lim_{n \to \infty} a_n = b$，则 $a = b$。
>
> **证明思路**：对任意 $\varepsilon > 0$，存在 $N_1$ 使得 $n > N_1 \implies |a_n - a| < \varepsilon/2$，存在 $N_2$ 使得 $n > N_2 \implies |a_n - b| < \varepsilon/2$。取 $N = \max(N_1, N_2)$，对 $n > N$：
>
> $$
> |a - b| \leq |a - a_n| + |a_n - b| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> $$
>
> 由于 $|a - b| < \varepsilon$ 对**任意** $\varepsilon > 0$ 成立，而 $|a - b|$ 是一个固定的非负实数，必有 $|a - b| = 0$，即 $a = b$。$\square$

这个证明之所以有效，关键在于最后一步的逻辑：一个非负实数如果小于所有正数，它只能是零。这是"$\forall \varepsilon > 0,\; |a - b| < \varepsilon$"蕴涵"$|a - b| = 0$"——一个全称量词命题的推论。

---

### 九、极限定义的量词解剖

极限是分析学的第一个核心概念，也是量词结构最密集的定义之一。在此做一次完整的"量词解剖"，为后续学习打下基础。

> **定义.** 数列 $\{a_n\}_{n=1}^{\infty}$ 收敛到实数 $a$，记作 $\lim_{n \to \infty} a_n = a$，是指：
>
> $$
> \forall \varepsilon > 0,\; \exists N \in \mathbb{N},\; \forall n \in \mathbb{N},\; n > N \implies |a_n - a| < \varepsilon.
> $$

**逐词逐量词解读：**

1. **$\forall \varepsilon > 0$**：给出任意正实数 $\varepsilon$ 作为精度标准。这里的"任意"意味着，你的论证不能对 $\varepsilon$ 做任何特殊假设（比如不能说"取 $\varepsilon = 1$"来完成证明）。$\varepsilon$ 仅受 $\varepsilon > 0$ 的约束。
2. **$\exists N \in \mathbb{N}$**：承诺可以找到一个自然数 $N$。这个 $N$ **可以依赖于 $\varepsilon$**——不同的精度要求可以对应不同的起点。$N$ 由证明者构造。
3. **$\forall n \in \mathbb{N},\; n > N$**：对 $N$ 之后的**所有**自然数 $n$（不只是某一个），下面的不等式都必须成立。
4. **$|a_n - a| < \varepsilon$**：数列第 $n$ 项与极限值 $a$ 的距离严格小于 $\varepsilon$。

> **例 26.** 证明 $\lim_{n \to \infty} \frac{1}{n} = 0$。
>
> **证明.** 设 $\varepsilon > 0$（这一步对应 $\forall \varepsilon > 0$：我们假设 $\varepsilon$ 任意给定但固定）。由 Archimedes 性质，存在 $N \in \mathbb{N}$ 使得 $N > \frac{1}{\varepsilon}$（这一步对应 $\exists N$：我们构造了 $N$，它依赖于 $\varepsilon$）。则对所有 $n > N$（这一步对应 $\forall n > N$），有
>
> $$
> \left|\frac{1}{n} - 0\right| = \frac{1}{n} < \frac{1}{N} < \varepsilon.
> $$
>
> 因此 $\lim_{n \to \infty} \frac{1}{n} = 0$。$\square$

**否定形式**："$\{a_n\}$ 不收敛到 $a$"的精确含义：

$$
\exists \varepsilon > 0,\; \forall N \in \mathbb{N},\; \exists n > N,\; |a_n - a| \geq \varepsilon.
$$

读作：存在一个正的误差标准 $\varepsilon$，使得无论你选多大的起点 $N$，总能在 $N$ 之后找到至少一个项偏离 $a$ 达到 $\varepsilon$。

> **例 27.** 证明 $\{(-1)^n\}$ 不收敛到 $0$。
>
> **证明.** 取 $\varepsilon = 1$（这对应 $\exists \varepsilon > 0$：我们展示了一个具体的 $\varepsilon$）。对任意 $N \in \mathbb{N}$（这对应 $\forall N$），取 $n = N + 1$（或任何大于 $N$ 的自然数），则
>
> $$
> |(-1)^n - 0| = 1 \geq 1 = \varepsilon.
> $$
>
> 因此 $\{(-1)^n\}$ 不收敛到 $0$。$\square$

---

### 十、连续性定义的量词解剖

> **定义.** 函数 $f: D \to \mathbb{R}$ 在点 $x_0 \in D$ 处连续，是指：
>
> $$
> \forall \varepsilon > 0,\; \exists \delta > 0,\; \forall x \in D,\; |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon.
> $$

**逐层解读：**

- **第 1 层** $\forall \varepsilon > 0$：任意输出精度（无依赖）
- **第 2 层** $\exists \delta > 0$：存在输入范围（$\delta$ 可依赖 $\varepsilon$ 和 $x_0$）
- **第 3 层** $\forall x \in D$：范围内所有点（无依赖）

**否定形式**——"$f$ 在 $x_0$ 处不连续"：

$$
\exists \varepsilon > 0,\; \forall \delta > 0,\; \exists x \in D,\; |x - x_0| < \delta \;\land\; |f(x) - f(x_0)| \geq \varepsilon.
$$

读作：存在某个精度要求 $\varepsilon$，使得无论输入范围 $\delta$ 取多小，总能找到一个在 $\delta$ 范围内的点 $x$，其函数值偏离 $f(x_0)$ 至少 $\varepsilon$。

> **例 28.** 设 $f: \mathbb{R} \to \mathbb{R}$ 定义为
>
> $$
> f(x) = \begin{cases} 1, & x \geq 0, \\ 0, & x < 0. \end{cases}
> $$
>
> 证明 $f$ 在 $x_0 = 0$ 处不连续。
>
> **证明.** 取 $\varepsilon = \frac{1}{2}$。对任意 $\delta > 0$，取 $x = -\frac{\delta}{2}$，则 $|x - 0| = \frac{\delta}{2} < \delta$，但 $|f(x) - f(0)| = |0 - 1| = 1 \geq \frac{1}{2} = \varepsilon$。因此 $f$ 在 $0$ 处不连续。$\square$

---

### 十一、量词与证明策略：如何读、如何写

Velleman 提出了一套系统的"量词-证明策略"对应规则。理解它们，是从"能看懂定义"到"能写出证明"的关键一步。

> **策略表.**
>
> - **要证** $\forall x \in D,\; P(x)$（$\forall$）→ 设 $x$ 为 $D$ 中**任意**元素，证明 $P(x)$
> - **要证** $\exists x \in D,\; P(x)$（$\exists$）→ **构造**一个具体的 $x_0 \in D$，验证 $P(x_0)$
> - **已知** $\forall x \in D,\; P(x)$（$\forall$）→ 对任何你需要的特定 $x_0 \in D$，直接**代入**得到 $P(x_0)$
> - **已知** $\exists x \in D,\; P(x)$（$\exists$）→ 引入一个满足 $P$ 的元素（**设**存在这样的 $x_0$ 使得 $P(x_0)$）

> **例 29（策略应用）.** 证明：若 $\{a_n\}$ 收敛到 $a$ 且 $\{b_n\}$ 收敛到 $b$，则 $\{a_n + b_n\}$ 收敛到 $a + b$。
>
> **证明框架的量词分析：**
>
> 目标：$\forall \varepsilon > 0,\; \exists N,\; \forall n > N,\; |(a_n + b_n) - (a + b)| < \varepsilon$。
>
> 第一层（$\forall \varepsilon > 0$）→ 策略：设 $\varepsilon > 0$ 任意。
>
> 已知 $\{a_n\} \to a$：代入 $\varepsilon/2$（这是"使用已知的 $\forall$"策略——选一个对我们有利的特定值），得到 $\exists N_1,\; \forall n > N_1,\; |a_n - a| < \varepsilon/2$。
>
> 已知 $\{b_n\} \to b$：同理得 $\exists N_2,\; \forall n > N_2,\; |b_n - b| < \varepsilon/2$。
>
> 第二层（$\exists N$）→ 策略：构造。取 $N = \max(N_1, N_2)$。
>
> 第三层（$\forall n > N$）→ 策略：设 $n > N$ 任意，则 $n > N_1$ 且 $n > N_2$，于是
>
> $$
> |(a_n + b_n) - (a + b)| \leq |a_n - a| + |b_n - b| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> $$
>
> $\square$

注意证明的每一步都精确对应一层量词。这不是巧合，而是系统方法：**量词结构 = 证明骨架**。掌握了这一点，写分析证明就不再是"灵光一现"，而是"逐层响应量词的指令"。

---

### 十二、自由变量与约束变量

在量词表达式中，变量有两种身份：**自由的**和**约束的**。区分它们对于正确理解表达式的含义至关重要。

> **定义.** 在一个含量词的表达式中：
>
> - **约束变量（bound variable）**：出现在某个量词作用域内的变量。它的名字可以替换为任何其他字母而不改变表达式的含义。
> - **自由变量（free variable）**：不在任何量词作用域内的变量。它的取值直接影响表达式的真假。

> **例 30.** 在 $\forall x \in \mathbb{R},\; x^2 + y \geq 0$ 中：
>
> - $x$ 是约束变量（被 $\forall$ 约束），可以换成 $t$：$\forall t \in \mathbb{R},\; t^2 + y \geq 0$，含义不变。
> - $y$ 是自由变量——表达式的真假取决于 $y$ 的值。当 $y \geq 0$ 时命题为真，当 $y < 0$ 时命题为假（例如 $y = -1$，取 $x = 0$ 则 $0 + (-1) = -1 < 0$）。

> **例 31.** 在 $\exists N \in \mathbb{N},\; \forall n > N,\; |a_n - a| < \varepsilon$ 中：
>
> - $N$ 和 $n$ 是约束变量。
> - $\varepsilon$、$a$ 以及数列 $\{a_n\}$ 是自由的——它们的值需要从上下文确定。
>
> 这就解释了为什么极限定义的最外层还需要 $\forall \varepsilon > 0$：只有把 $\varepsilon$ 也约束了，整个表达式才没有自由变量，才成为一个完整的命题。

判断标准：**一个表达式是命题（具有确定真值），当且仅当它没有自由变量。** 如果还有自由变量，它就是命题函数。量词的作用，正是把命题函数中的自由变量逐个约束掉，最终变成命题。

---

### 十三、多层量词否定的系统方法

对于多层嵌套量词的否定，我们给出一个**机械化的操作规程**，使得否定过程变得可靠且不容易出错。

> **操作规程.** 否定一个含 $k$ 层量词的命题，按以下步骤进行：
>
> 1. 从最外层开始，逐层翻转量词：$\forall \leftrightarrow \exists$。
> 2. 量词后面的约束域和变量名保持不变。
> 3. 到达最内层的谓词时，对谓词取否定（$< \to \geq$，$= \to \neq$，$\in \to \notin$，等等）。
> 4. 如果最内层谓词本身是一个蕴涵 $A \implies B$，其否定为 $A \land \neg B$（前件保持，后件否定）。

> **例 32.** 否定一致连续的定义：
>
> 原命题：$\forall \varepsilon > 0,\; \exists \delta > 0,\; \forall x, y \in D,\; |x - y| < \delta \implies |f(x) - f(y)| < \varepsilon$。
>
> 逐层翻转：
>
> $$
> \exists \varepsilon > 0,\; \forall \delta > 0,\; \exists x, y \in D,\; |x - y| < \delta \;\land\; |f(x) - f(y)| \geq \varepsilon.
> $$
>
> 这就是"$f$ 在 $D$ 上不一致连续"的精确含义：存在某个正精度 $\varepsilon$，使得不管 $\delta$ 多小，总能找到两个点在 $\delta$ 以内但函数值之差不小于 $\varepsilon$。

> **例 33.** 否定"函数列 $\{f_n\}$ 在 $D$ 上一致收敛到 $f$"：
>
> 原命题：$\forall \varepsilon > 0,\; \exists N,\; \forall n > N,\; \forall x \in D,\; |f_n(x) - f(x)| < \varepsilon$。
>
> 否定（四层量词逐层翻转）：
>
> $$
> \exists \varepsilon > 0,\; \forall N,\; \exists n > N,\; \exists x \in D,\; |f_n(x) - f(x)| \geq \varepsilon.
> $$

> **例 34.** 否定 Cauchy 列定义：
>
> 原命题：$\forall \varepsilon > 0,\; \exists N,\; \forall m, n > N,\; |a_m - a_n| < \varepsilon$。
>
> 否定：
>
> $$
> \exists \varepsilon > 0,\; \forall N,\; \exists m, n > N,\; |a_m - a_n| \geq \varepsilon.
> $$

熟练掌握这套机械化方法后，否定任何分析定义都不再需要"灵感"，只需要"操作"。这正是形式逻辑训练带来的技术红利。

---

### 十四、从量词到集合论语言的过渡

量词与集合论语言有天然的对应关系。理解这一对应，是从逻辑走向分析学的最后铺垫。

> **对应表.**
>
> - $\forall x \in D,\; P(x)$ $\;\;\Longleftrightarrow\;\;$ $\{x \in D : P(x)\} = D$
> - $\exists x \in D,\; P(x)$ $\;\;\Longleftrightarrow\;\;$ $\{x \in D : P(x)\} \neq \varnothing$
> - $\neg\exists x \in D,\; P(x)$ $\;\;\Longleftrightarrow\;\;$ $\{x \in D : P(x)\} = \varnothing$

也就是说，$\forall$ 对应"使命题为真的元素组成的集合等于整个论域"，$\exists$ 对应"使命题为真的元素组成的集合非空"。

> **例 35.** "$\forall x \in \mathbb{R},\; x^2 \geq 0$"等价于"$\{x \in \mathbb{R} : x^2 \geq 0\} = \mathbb{R}$"——所有实数都满足这个不等式。

> **例 36.** "$\exists x \in \mathbb{R},\; x^2 = 2$"等价于"$\{x \in \mathbb{R} : x^2 = 2\} \neq \varnothing$"——满足 $x^2 = 2$ 的实数集非空。

这种对应在后续几节（0.5 集合概念、0.6 子集与幂集）中会变得更加清晰。实际上，集合的构造性定义 $\{x \in D : P(x)\}$ 本身就依赖命题函数 $P$：先有谓词，后有集合。

此外，量词与集合运算的关系也值得注意：

$$
\forall x \in A \cup B,\; P(x) \;\;\iff\;\; \bigl(\forall x \in A,\; P(x)\bigr) \land \bigl(\forall x \in B,\; P(x)\bigr),
$$

$$
\exists x \in A \cup B,\; P(x) \;\;\iff\;\; \bigl(\exists x \in A,\; P(x)\bigr) \lor \bigl(\exists x \in B,\; P(x)\bigr).
$$

这说明全称量词对并集的分解对应合取，存在量词对并集的分解对应析取——再次印证了 $\forall$ 与 $\land$、$\exists$ 与 $\lor$ 之间的深层对偶。

---

### 十五、本节小结

本节的核心，不在于记住几条量词符号的定义，而在于建立一种对**量化结构的敏感和操控能力**。分析学的整套语言——极限、连续、可导、积分——都建立在量词的精确嵌套之上。

我们建立了以下认识：

1. **命题函数**是含自由变量的真值表达式，量词把自由变量约束为确定命题。
2. **全称量词** $\forall$ 声明普遍性——对证明者意味着"设任意的"；对反驳者意味着"只需一个反例"。
3. **存在量词** $\exists$ 声明存在性——对证明者意味着"构造或找到"；对反驳者意味着"证明全部不满足"。
4. **量词否定律**是 De Morgan 律的无限推广：$\neg\forall \equiv \exists\neg$，$\neg\exists \equiv \forall\neg$。
5. **嵌套量词的顺序决定含义**：$\forall x\;\exists y$ 与 $\exists y\;\forall x$ 完全不同，后者严格强于前者。逐点连续 vs 一致连续、逐点收敛 vs 一致收敛，本质上就是量词顺序之别。
6. **唯一存在** $\exists!$ 是存在性与唯一性的合取。
7. **量词结构 = 证明骨架**：$\forall$ 的目标对应"设任意"，$\exists$ 的目标对应"构造"，$\forall$ 的已知对应"代入"，$\exists$ 的已知对应"引入见证者"。
8. **量词与集合论互译**：$\forall$ 对应"真集 = 全集"，$\exists$ 对应"真集非空"。

从更高的观点看，量词与命题函数的结合，把数学从"有限个案的验证"推进到"无限情况的逻辑控制"。这是分析学之所以能严格处理极限、收敛和连续的根本原因——它不是靠直觉画图，而是靠量词语法把"无限逼近"翻译成可操作的有限步骤逻辑。正是 Cauchy、Weierstrass 一代人完成了这场翻译，使分析学从"能算"变成"能证"。

下一节（0.3 直接证明与反证法）将在量词语法的基础上，系统讨论数学证明的方法论。
