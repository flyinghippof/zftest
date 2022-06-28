---
title: latex
date: 2020-12-8
tags:
mathjax: true

---



注释前言

前边为刘海洋哔哩哔哩视频讲解，已经下载ppt

···

<!-- more -->

- 背景：
  - 高德纳为了写书发明了tex
  - Leslie Lamport为了写自己的书，写了一个基于tex的宏，latex
- tex的发行版软件
  - texlive miktex （for windows）
  - https://www.overleaf.com （在线）
- texlive下载网站：tug.org
- texwork是一个文字编辑器，装texlive后会自动装上，也可以用vscode或者记事本这类的文本编辑器





- \documentclass{ctexart}  中文类

- 编译（.tex文件--.pdf文件）：
  - pdflatex（英文推荐）
  - xelatex（中文推荐）
  - lualatex（未广泛使用）

- latex的语法结构被限制为相对固定的形式

- 命令：参数总在后面花括号表示，用中括号表示可选参数。

  ```latex
    \cmd[opt]{arg1}{arg2}
  ```

- 环境

  ~~~latex
  \begin{env}
    ``````
  \end{env}
  ~~~

- 注释：以%开头，该行在%后边的部分





- 用空格分开单词。一个换行符等同于一个空格，多个空格的效果与一个相同。
- 自然段分段是空一行。
- 一些符号被latex宏语言占用，需要以命令形式输入。比如：# $ % & 等，需要反斜杠\进行转义
- 反斜杠\输入：\textbackslash
- 键盘上没有的符号可以用命令输出出来，具体看符号字体包。symbols文档。





数学公式模式

- 数学模式下字体、符号、间距与正文都不同，一切数学公式（包括单个符号）都要在数学模式下输入。
- 行内（inline）公式：使用一对符号$ $ 来标示。如$a+b=c$。
- 显示（display）公式。
  - 简单的不编号公式用命令\\[ 和\\] 标示。（不要使用双美元符号$$  $$）
  - 基本的编号的公式用equation 环境。
  - 更复杂的结构，使用amsmath 宏包提供的专门的数学环境。（不要使用eqnarray 环境）

- 上标与下标：用^ 和_ 表示。
- 上下画线与花括号：\overline, \underline, \overbrace,\underbrace
- 分式：\frac{分子}{分母}
- 根式：\sqrt[次数]{根号下}
- 矩阵：使用amsmath 宏包提供的专门的矩阵环境matrix,pmatrix, bmatrix 等。特别复杂的矩阵（如带线条）使用array环境作为表格画出。

- 数学字母a, b,  Δ，数学字体\mathbb（R）、\mathcal（P）等
- 普通符号：如\infty, \angle
- 二元运算符：a + b
- 二元关系符：a = b
- 括号：⟨a , b⟩，使用\left, \right 放大
- 标点：逗号、分号（\colon）



- 数学公式一般总是要用amsmath这个宏包
- amsmath 是基本的数学工具包，在包含数学公式的文档中几乎无处不在。mathtools 则对amsmath 做了一些补充和增强。

- siunitx：数字单位的一揽子解决方案
- mhchem 宏包是在TEX 中定义新语法规则的典范。它让化学反应式的书写比数学式还要容易，绝大部分功能只需要\ce 一条命令

- 列表环境：
  - enumerate 编号
  - itemize 不编号
  - description 有标题

- 定理类环境：

  - \newtheorem 定义定理类环境，如\newtheorem{thm}{定理}[section]

  - ```latex
    \begin{thm}
    一个定理
    \end{thm}
    ```

- 抄录代码:

  - \verb 命令

    ```latex
    代码
    \verb|#include <stdio.h>|
    ```

  - verbatim

    ```latex
    \begin{verbatim}
    #include <stdio>
    main() {
    puts("hello world.");
    }
    \end{verbatim}
    ```

- 算法结构：

  - clrscode宏包（算法导论）
  - algorithm2e宏包
  - algorithmmicx宏包的algpseudocode

- 画表格：使用tabular 环境。

  - [https://www.tablesgenerator.com/latex_tables](https://www.tablesgenerator.com/latex_tables)一个表格生成的网址

- 功能各异的表格宏包
  - 单元格处理：multirow、makecell
  - 长表格：longtable、xtab
  - 定宽表格：xtabular
  - 表线控制：booktabs、hhline、arydshln
  - 表列格式：array
  - 综合应用：tabu

- 插图：使用graphicx 宏包提供的\includegraphics 命令。

  ```latex
  \includegraphics[width=15cm]{foo.pdf}
  ```

  

- 浮动体：
  - figure 环境
  - table 环境
  - 其他环境可以使用float 宏包得到
  - 浮动体的标题用\caption 命令得到，自动编号。

- 自动化工具

  - 目录、交叉引用

  - hyperref：PDF 的链接与书签

    hyperref 产生链接和书签的原理与普通的交叉引用相同。hyperref会在PDF 中写入相应的“锚点”代码，在其他地方引用。交叉引用的代码并入.aux 文件，目录的代码并入.toc 文件，PDF 书签则产生单独的.out 文件。

  - 参考文献：略  biblatex





- 格式要与内容分离，这样才可以方便的迁移，而不用重新排版
- 作者编写文档只使用\title、\section、quote 这样的命令或环境，而不必考虑其具体实现。而有关格式的细节代码，则被封装在文档类、宏包中，或在导言区分离编写。
- 有很多事先设计好的模板可以使用，所以作者只用关心内容就好了
- 作者在填写内容时应该遵循分离原则。基本的方法就是只使用与内容相关的命令和环境。

- 使用宏包:
  - 宏包将可重用的代码提取出来，相当于其他程序语言中的“库”。使用宏包可以用简单的接口实现非常复杂的功能，有些对于个人来说是“不可能的任务”。
  - 第三方宏包可能破坏TEX 设计的“向前兼容性”；不同宏包之间如果出现兼容性问题更难解决
  - 应合理使用：
    - 尽可能多地用宏包实现功能
    - 尽可能排除不需要的宏包





- 如果自己必须要控制格式有以下几种：

  - 字体：

    ```latex
    \rmfamily, \textrm{...}
    \sffamily, \textsf{...}
    \ttfamily, \texttt{...}
    ```

  - 字号：

    ```latex
    \Huge, \LARGE, \Large, \large, \normalsize, \small,
    \footnotesize, \scriptsize, \tiny
    ```

  - 中文字号：

    ```latex
    \zihao{5}、\zihao{‐3}
    ```

  - 对齐：

    ```latex
    \centering、\raggedleft、\raggedright
    ```

  - 空白间距：

    ```latex
    \hspace{2cm}
    \vspace{3mm}
    ```

  - 版面布局：

    ```latex
    geometry 宏包
    fancyhdr 宏包等
    ```

  - 分页断行：

    ```latex
    \linebreak、\\
    \pagebreak、\newpage、\clearpage、\cleardoublepage
    ```

  - 盒子：

    ```latex
    \mbox{内容}
    \parbox{4em}{内容}、minipage
    ```









- 使用在导言区单独设置格式
  - 直接设置相关参数。如设置\parindent、\parskip、\linespread、\pagestyle。
  - 修改部分命令定义。如修改\thesection、\labelenumi、\descriptionlabel、\figurename。
  - 利用工具宏包完成设置。如使用ctex 宏包设置中文格式，使用tocloft 宏包设置目录格式。

- 利用自定义命令和环境：对于LATEX 没有直接提供的格式，可以使用自定义的命令和环境实现语义的接口。
- 各种直接修改输出格式的命令，如字体、字号、对齐、间距的命令，都应该放在文档格式设置或自定义的命令、环境中，而避免在正文中直接使用。

- 章节标题：ctex 宏包及文档类，用\ctexset 定制。西文用titlesec 等。
- 浮动标题：caption 宏包
- 列表环境：enumitem 宏包



















































