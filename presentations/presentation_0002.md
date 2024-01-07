---
title: "Linear Transformations"
pagetitle: "Linear Transformations"
subtitle: "Maths-2 | Week-5"
author: "Karthik Thiagarajan"
institute: "IIT Madras"
toc: true
toc-title: "Plan"
format: revealjs
history: false
slide-number: true
show-slide-number: all
chalkboard: true
incremental: true
fontsize: 35px
margin: 0.1
width: 1600
height: 800
revealjs-plugins:
  - pointer
---

## Linear Transformation

::: {.fragment .absolute left=0 top=100}
$$
T: V \rightarrow W
$$

- $T(u + v) = T(u) + T(v)$
- $T(cv) = cT(v)$

:::



::: {.fragment .absolute left=600 top=50}

Examples

- $T: \mathbb{R} \rightarrow \mathbb{R}$, $T(x) = 3x$
  - $T(u + v) = 3(u + v) = 3u + 3v = T(u) + T(v)$
  - $T(cv) = 3(cv) = c(3v) = cT(v)$

|
|

- $T: \mathbb{R}^{2} \rightarrow \mathbb{R}^2, T(x, y) = (-x, y - x)$
  - $T((x_1, y_1) + (x_2, y_2))$
    - $= T(x_1 + x_2, y_1 + y_2)$
    - $=(-x_1 -x_2, y_1 + y_2 - x_1 - x_2)$
    - $=(-x_1, y_1 - x_1) + (-x_2, y_2 - x_2)$
    - $=T(x_1, y_1) + T(x_2, y_2)$
  - $T(c(x, y)) = (-cx, cy - cx) = c(-x, y - x) = cT(x, y)$

:::



## Transformations, Basis, Matrix

$$
T: \mathbb{R}^2 \rightarrow \mathbb{R}^2
$$

::: {.fragment .absolute left=0 top=220}

- $(x, y)$
  - $(x, y) = x(1, 0) + y(0, 1)$
- $T(x, y)$
  - $= T(x(1, 0) + y(0, 1))$
  - $=xT(1, 0) + yT(0, 1)$

:::



::: {.fragment .absolute left=600 top=220}

- $T(1, 0) = (a, c)$
- $T(0, 1) = (b, d)$
- $T(x, y)$
  - $= x(a, c) + y(b, d)$
  - $=(ax + by, cx + dy)$

:::



::: {.fragment .absolute left=1100 top=300}

$T(x, y) = \begin{bmatrix}a & b\\c & d\end{bmatrix} \begin{bmatrix}x\\y\end{bmatrix}$

:::



## Inective, Surjective and Bijective

$$
T: V \rightarrow W
$$

::: {.fragment .absolute left=0 top=200}

<u>Inective (one-one)</u>
$$
T(u) = T(v) \implies u = v
$$
:::

::: {.fragment .absolute left=0 top=400}

<u>Surjective (onto)</u>
$$
\forall v \in W, \exists u \in V, \text{ such that } T(u) = v
$$
:::

::: {.fragment .absolute left=0 top=600}

<u>Bijective (one-one and onto) </u>

- $T$ is bijective if it is both injective and surjective
- A bijective linear transformation is called an isomorphism.

:::

::: {.fragment .absolute left=800 top=200}

<u>Examples</u>

- $T: \mathbb{R}^{2} \rightarrow \mathbb{R}^2, T(x, y) = (2x, 3y)$
- $T: \mathbb{R}^3 \rightarrow \mathbb{R}^{3}, T(x, y, z) = (z, y, x)$

:::

::: {.fragment .absolute left=800 top=400}

<u>Non-examples</u>

- $T: \mathbb{R}^{2} \rightarrow \mathbb{R}, T(x, y) = x$
- $T: \mathbb{R}^3 \rightarrow \mathbb{R}^{4}, T(x, y, z) = (z, y, x, 0)$

:::
