---
title: python知识点
date: 2020-12-15
tags:
mathjax: true
---



注释前言

math包用法

···

<!-- more -->



# math

[中文文档](https://docs.python.org/zh-cn/3/library/math.html)

[英文文档](https://docs.python.org/2/library/math.html)

- Python math 模块提供了许多对浮点数的数学运算函数。
- Python cmath 模块包含了一些用于复数运算的函数。
- cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
- 要使用 math 或 cmath 函数必须先导入
- 该模块提供了以下函数。除非另有明确说明，否则所有返回值均为浮点数。

- math 模块是标准库中的

## 数论与表示函数

- `math.ceil`(*x*)

  返回 *x* 的上限，即大于或者等于 *x* 的最小整数。如果 *x* 不是一个浮点数，则委托 `x.__ceil__()`, 返回一个 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) 类的值

- `math.comb`(*n*, *k*)  *3.8 新版功能.*

  返回不重复且无顺序地从 *n* 项中选择 *k* 项的方式总数。

  当 `k <= n` 时取值为 `n! / (k! * (n - k)!)`；当 `k > n` 时取值为零。

  如果任一参数不为整数则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。 如果任一参数为负数则会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。

- `math.copysign`(*x*, *y*)

  返回一个基于 *x* 的绝对值和 *y* 的符号的浮点数。在支持带符号零的平台上，`copysign(1.0, -0.0)` 返回 *-1.0*.

- `math.fabs`(*x*)

  返回 *x* 的绝对值。

- `math.factorial`(*x*)

  以一个整数返回 *x* 的阶乘。 如果 *x* 不是整数或为负数时则将引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。

- `math.floor`(*x*)

  返回 *x* 的向下取整，小于或等于 *x* 的最大整数。如果 *x* 不是浮点数，则委托 `x.__floor__()` ，它应返回 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) 值。

- `math.fmod`(*x*, *y*)

  返回 `fmod(x, y)` ，由平台C库定义。请注意，Python表达式 `x % y` 可能不会返回相同的结果。C标准的目的是 `fmod(x, y)` 完全（数学上到无限精度）等于 `x - n*y` 对于某个整数 *n* ，使得结果具有 与 *x* 相同的符号和小于 `abs(y)` 的幅度。Python的 `x % y` 返回带有 *y* 符号的结果，并且可能不能完全计算浮点参数。 例如， `fmod(-1e-100, 1e100)` 是 `-1e-100` ，但Python的 `-1e-100 % 1e100` 的结果是 `1e100-1e-100` ，它不能完全表示为浮点数，并且取整为令人惊讶的 `1e100` 。 **出于这个原因，函数 [`fmod()`](https://docs.python.org/zh-cn/3/library/math.html#math.fmod) 在使用浮点数时通常是首选，而Python的 `x % y` 在使用整数时是首选。**

- `math.frexp`(*x*)

  返回 *x* 的尾数和指数作为对``(m, e)``。 *m* 是一个浮点数， *e* 是一个整数，正好是 `x == m * 2**e` 。 如果 *x* 为零，则返回 `(0.0, 0)` ，否则返回 `0.5 <= abs(m) < 1` 。这用于以可移植方式“分离”浮点数的内部表示。

- `math.fsum`(*iterable*)

  返回迭代中的精确浮点值。通过跟踪多个中间部分和来避免精度损失

- `math.gcd`(**integers*)  *3.5 新版功能.*

  返回给定的整数参数的最大公约数。 如果有一个参数非零，则返回值将是能同时整除所有参数的最大正整数。 如果所有参数为零，则返回值为 `0`。 不带参数的 `gcd()` 返回 `0`。

- `math.isclose`(*a*, *b*, *, *rel_tol=1e-09*, *abs_tol=0.0*)  *3.5 新版功能.*

  若 *a* 和 *b* 的值比较接近则返回 `True`，否则返回 `False`。

  根据给定的绝对和相对容差确定两个值是否被认为是接近的。

  *rel_tol* 是相对容差 —— 它是 *a* 和 *b* 之间允许的最大差值，相对于 *a* 或 *b* 的较大绝对值。例如，要设置5％的容差，请传递 `rel_tol=0.05` 。默认容差为 `1e-09`，确保两个值在大约9位十进制数字内相同。 *rel_tol* 必须大于零。

  *abs_tol* 是最小绝对容差 —— 对于接近零的比较很有用。 *abs_tol* 必须至少为零。

  如果没有错误发生，结果将是： `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)` 。

  `NaN` 不被认为接近任何其他值，包括 `NaN` 。 `inf` 和 `-inf` 只被认为接近自己。

- `math.isfinite`(*x*)  *3.2 新版功能.*

  如果 *x* 既不是无穷大也不是NaN，则返回 `True` ，否则返回 `False` 。 （注意 `0.0` 被认为 *是* 有限的。）

- `math.isinf`(*x*)

  如果 *x* 是正或负无穷大，则返回 `True` ，否则返回 `False` 。

- `math.isnan`(*x*)

  如果 *x* 是 NaN（不是数字），则返回 `True` ，否则返回 `False` 

- `math.isqrt`(*n*)  *3.8 新版功能.*

  返回非负整数 *n* 的整数平方根。 这就是对 *n* 的实际平方根向下取整，或者相当于使得 *a*² ≤ *n* 的最大整数 *a*。

  对于某些应用来说，可以更适合取值为使得 *n* ≤ *a*² 的最小整数 *a* ，或者换句话说就是 *n* 的实际平方根向上取整。 对于正数 *n*，这可以使用 `a = 1 + isqrt(n - 1)` 来计算。

- `math.lcm`(**integers*)  *3.9 新版功能.*

  返回给定的整数参数的最小公倍数。 如果所有参数均非零，则返回值将是为所有参数的整数倍的最小正整数。 如果参数之一为零，则返回值为 `0`。 不带参数的 `lcm()` 返回 `1`。

- `math.ldexp`(*x*, *i*)

  返回 `x * (2**i)` 。 这基本上是函数 [`frexp()`](https://docs.python.org/zh-cn/3/library/math.html#math.frexp) 的反函数。

- `math.modf`(*x*)

  返回 *x* 的小数和整数部分。两个结果都带有 *x* 的符号并且是浮点数。

- `math.nextafter`(*x*, *y*)  *3.9 新版功能.*

  返回 *x* 趋向于 *y* 的最接近的浮点数值。

  如果 *x* 等于 *y* 则返回 *y*。

- `math.perm`(*n*, *k=None*)  *3.8 新版功能.*

  返回不重复且有顺序地从 *n* 项中选择 *k* 项的方式总数。

  当 `k <= n` 时取值为 `n! / (n - k)!`；当 `k > n` 时取值为零。

  如果 *k* 未指定或为 None，则 *k* 默认值为 *n* 并且函数将返回 `n!`。

  如果任一参数不为整数则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。 如果任一参数为负数则会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。

- `math.prod`(*iterable*, ***, *start=1*)  *3.8 新版功能.*

  计算输入的 *iterable* 中所有元素的积。 积的默认 *start* 值为 `1`。

  当可迭代对象为空时，返回起始值。 此函数特别针对数字值使用，并会拒绝非数字类型。

- `math.remainder`(*x*, *y*)  *3.7 新版功能.*

  返回 IEEE 754 风格的 *x* 相对于 *y* 的余数。对于有限 *x* 和有限非零 *y* ，这是差异 `x - n*y` ，其中 `n` 是与商 `x / y` 的精确值最接近的整数。如果 `x / y` 恰好位于两个连续整数之间，则最近的 * even* 整数用于 `n` 。 余数 `r = remainder(x, y)` 因此总是满足 `abs(r) <= 0.5 * abs(y)` 。

  特殊情况遵循IEEE 754：特别是 `remainder(x, math.inf)` 对于任何有限 *x* 都是 *x* ，而 `remainder(x, 0)` 和 `remainder(math.inf, x)` 引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 适用于任何非NaN的 *x* 。如果余数运算的结果为零，则该零将具有与 *x* 相同的符号。

  在使用IEEE 754二进制浮点的平台上，此操作的结果始终可以完全表示：不会引入舍入错误。

- `math.trunc`(*x*)

  返回 [`Real`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Real) 值 *x* 截断为 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) （通常是整数）。 委托给 [`x.__trunc__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__trunc__)。

- `math.ulp`(*x*)  *3.9 新版功能.*

  返回浮点数 *x* 的最小有效比特位的值:

  - 如果 *x* 是 NaN (非数字)，则返回 *x*。
  - 如果 *x* 为负数，则返回 `ulp(-x)`。
  - 如果 *x* 为正数，则返回 *x*。
  - 如果 *x* 等于，则返回 *去正规化的* 可表示最小正浮点数 (小于 *正规化的* 最小正浮点数 [`sys.float_info.min`](https://docs.python.org/zh-cn/3/library/sys.html#sys.float_info))。
  - 如果 *x* 等于可表示最大正浮点数，则返回 *x* 的最低有效比特位的值，使得小于 *x* 的第一个浮点数为 `x - ulp(x)`。
  - 在其他情况下 (*x* 是一个有限的正数)，则返回 *x* 的最低有效比特位的值，使得大于 *x* 的第一个浮点数为 `x + ulp(x)`。

  ULP 即 "Unit in the Last Place" 的缩写。

## 幂函数与对数函数

- `math.exp`(*x*)

  返回 *e* 次 *x* 幂，其中 *e* = 2.718281... 是自然对数的基数。这通常比 `math.e ** x` 或 `pow(math.e, x)` 更精确。

- `math.expm1`(*x*)  *3.2 新版功能.*

  返回 *e* 的 *x* 次幂，减1。这里 *e* 是自然对数的基数。对于小浮点数 *x* ， `exp(x) - 1` 中的减法可能导致 [significant loss of precision](https://en.wikipedia.org/wiki/Loss_of_significance)； [`expm1()`](https://docs.python.org/zh-cn/3/library/math.html#math.expm1) 函数提供了一种将此数量计算为全精度的方法

- `math.log`(*x*[, *base*])

  使用一个参数，返回 *x* 的自然对数（底为 *e* ）。

  使用两个参数，返回给定的 *base* 的对数 *x* ，计算为 `log(x)/log(base)` 。

- `math.log1p`(*x*)[¶](https://docs.python.org/zh-cn/3/library/math.html#math.log1p)

  返回 *1+x* (base *e*) 的自然对数。以对于接近零的 *x* 精确的方式计算结果。

- `math.log2`(*x*)  *3.3 新版功能.*

  返回 *x* 以2为底的对数。这通常比 `log(x, 2)` 更准确。

- `math.log10`(*x*)

  返回 *x* 底为10的对数。这通常比 `log(x, 10)` 更准确。

- `math.pow`(*x*, *y*)

  将返回 `x` 的 `y` 次幂。特殊情况尽可能遵循C99标准的附录'F'。特别是， `pow(1.0, x)` 和 `pow(x, 0.0)` 总是返回 `1.0` ，即使 `x` 是零或NaN。 如果 `x` 和 `y` 都是有限的， `x` 是负数， `y` 不是整数那么 `pow(x, y)` 是未定义的，并且引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 。

  与内置的 `**` 运算符不同， [`math.pow()`](https://docs.python.org/zh-cn/3/library/math.html#math.pow) 将其参数转换为 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 类型。使用 `**` 或内置的 [`pow()`](https://docs.python.org/zh-cn/3/library/functions.html#pow) 函数来计算精确的整数幂。

- `math.sqrt`(*x*)[¶](https://docs.python.org/zh-cn/3/library/math.html#math.sqrt)

  返回 *x* 的平方根



## 三角函数

- `math.acos`(*x*)

  返回以弧度为单位的 *x* 的反余弦值。 结果范围在 `0` 到 `pi` 之间。

- `math.asin`(*x*)

  返回以弧度为单位的 *x* 的反正弦值。 结果范围在 `-pi/2` 到 `pi/2` 之间。

- `math.atan`(*x*)

  返回以弧度为单位的 *x* 的反正切值。 结果范围在 `-pi/2` 到 `pi/2` 之间。.

- `math.atan2`(*y*, *x*)

  以弧度为单位返回 `atan(y / x)` 。结果是在 `-pi` 和 `pi` 之间。从原点到点 `(x, y)` 的平面矢量使该角度与正X轴成正比。 [`atan2()`](https://docs.python.org/zh-cn/3/library/math.html#math.atan2) 的点的两个输入的符号都是已知的，因此它可以计算角度的正确象限。 例如， `atan(1)` 和 `atan2(1, 1)` 都是 `pi/4` ，但 `atan2(-1, -1)` 是 `-3*pi/4` 。

- `math.cos`(*x*)

  返回 *x* 弧度的余弦值。

- `math.dist`(*p*, *q*)  *3.8 新版功能.*

  返回 *p* 与 *q* 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。

- `math.hypot`(**coordinates*)  *在 3.8 版更改:* 添加了对 n 维点的支持。 之前的版本只支持二维点。

  返回欧几里得范数，`sqrt(sum(x**2 for x in coordinates))`。 这是从原点到坐标给定点的向量长度。对于一个二维点 `(x, y)`，这等价于使用毕达哥拉斯定义 `sqrt(x*x + y*y)` 计算一个直角三角形的斜边。

- `math.sin`(*x*)

  返回 *x* 弧度的正弦值。

- `math.tan`(*x*)

  返回 *x* 弧度的正切值。



## 角度转换

- `math.degrees`(*x*)

  将角度 *x* 从弧度转换为度数。

- `math.radians`(*x*)

  将角度 *x* 从度数转换为弧度。

## 双曲函数

- `math.acosh`(*x*)

  返回 *x* 的反双曲余弦值。

- `math.asinh`(*x*)

  返回 *x* 的反双曲正弦值。

- `math.atanh`(*x*)

  返回 *x* 的反双曲正切值。

- `math.cosh`(*x*)

  返回 *x* 的双曲余弦值。

- `math.sinh`(*x*)

  返回 *x* 的双曲正弦值。

- `math.tanh`(*x*)

  返回 *x* 的双曲正切值。

## 特殊函数

- `math.erf`(*x*)  *3.2 新版功能.*

  返回 *x* 处的 [error function](https://en.wikipedia.org/wiki/Error_function) 。

  [`erf()`](https://docs.python.org/zh-cn/3/library/math.html#math.erf) 函数可用于计算传统的统计函数

- `math.erfc`(*x*)  *3.2 新版功能.*

  返回 *x* 处的互补误差函数。 [互补错误函数](https://en.wikipedia.org/wiki/Error_function) 定义为 `1.0 - erf(x)`。 它用于 *x* 的大值，从其中减去一个会导致 [有效位数损失](https://en.wikipedia.org/wiki/Loss_of_significance)。

- `math.gamma`(*x*)  *3.2 新版功能.*

  返回 *x* 处的 [伽马函数](https://en.wikipedia.org/wiki/Gamma_function) 值。

- `math.lgamma`(*x*)  *3.2 新版功能.*

  返回Gamma函数在 *x* 绝对值的自然对数。



## 常数

- `math.pi`

  数学常数 *π* = 3.141592...，精确到可用精度。

- `math.e`

  数学常数 *e* = 2.718281...，精确到可用精度。

- `math.tau`  *3.6 新版功能.*

  数学常数 *τ* = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2*π*，圆的周长与半径之比。

- `math.inf  *3.5 新版功能.*

  浮点正无穷大。 （对于负无穷大，使用 `-math.inf` 。）相当于 `float('inf')` 的输出。

- `math.nan  *3.5 新版功能.*

  浮点“非数字”（NaN）值。 相当于 `float('nan')` 的输出。


















