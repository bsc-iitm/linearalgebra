---
title: "Rank, Nullspace, Nullity, Rank-Nullity Theorem"
pagetitle: "Rank, Nullspace, Nullity, Rank-Nullity Theorem"
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

## Subspaces | Matrix

::: {.fragment .absolute left="0" top="200" .fade-in-then-out}
$$
A = \begin{bmatrix}
\Large- & r_1 & \Large-\\
 & \vdots &\\
 \Large- & r_m & \Large-
\end{bmatrix}
$$
:::

::: {.fragment .absolute left="0" top="200"}
$$
A = \begin{bmatrix}
\Large- & r_1 & \Large-\\
 & \vdots &\\
 \Large- & r_m & \Large-
\end{bmatrix} = \begin{bmatrix}
| & & |\\
v_1 & \cdots & v_n\\
| & & |
\end{bmatrix}
$$
:::

::: {.fragment .absolute left="0" top="500"}
$$
\begin{aligned}
\text{Row space} &= \text{span}\{r_1, \cdots, r_m\} \subset \mathbb{R}^n\\
\text{Column space} &= \text{span}\{c_1, \cdots, c_n\} \subset \mathbb{R}^m
\end{aligned}
$$
:::

::: {.fragment .absolute left="900" top="100" .fade-in-then-out}

For any $m \times n$ matrix $A$:

|
|

| Subspace     | Parent           | Dimension (term)   |
| ------------ | ---------------- | ------------------ |
| Row space    | $\mathbb{R}^{n}$ | rank (row rank)    |
| Column space | $\mathbb{R}^{m}$ | rank (column rank) |
|              |                  |                    |

:::

::: {.fragment .absolute left="900" top="100"}

For any $m \times n$ matrix $A$:

|
|

| Subspace     | Parent           | Dimension (term)   |
| ------------ | ---------------- | ------------------ |
| Row space    | $\mathbb{R}^{n}$ | rank (row rank)    |
| Column space | $\mathbb{R}^{m}$ | rank (column rank) |
| Null space   | $\mathbb{R}^{n}$ | nullity            |

:::



## Null space

::: {.fragment .absolute left=100 top=100}
$$
\text{null space}(A) = \{x\ |\ Ax = 0 \text{ and } x \in \mathbb{R}^n\}
$$
:::



::: {.fragment .absolute left=100 top=400}
$$
\text{null space}(A) = \text{set of solutions to the homogenous equation } Ax = 0
$$
:::



## Null space is a subspace

::: {.fragment .absolute left="0" top="100"}

$\text{null space}(A) = \{x\ |\ Ax = 0 \text{ and } x \in \mathbb{R}^n\}$ is a subspace of $\mathbb{R}^{n}$

:::



::: {.fragment .absolute left=0 top=200}

- $0 \in \text{null space}(A)$
- $x, y \in \text{null space}(A)$
  - $Ax = Ay = 0$
  - $A(x + y) = 0 \implies (x + y) \in \text{null space}(A)$
  - $A(cx) = c(Ax) = 0 \implies cx \in \text{null space}(A)$

:::



## Null space of $A$ and $\text{RREF}(A)$

::: {.fragment .absolute left="0" top="300"}

$A$ and $\text{RREF}(A)$ have the same null space

- $R = \text{RREF}(A)$

- There exists some invertible matrix $E$ such that
- $R = EA$

:::



::: {.fragment .absolute left="900" top="0"}

- $x \in \text{null space}(A)$
  - $Ax = 0$
  - $EAx = 0$
  - $Rx = 0$
  - $x \in \text{null space}(R)$

:::



::: {.fragment .absolute left="900" top="400"}

- $x \in \text{null space}(R)$
- $Rx = 0$
- $EAx = 0$
- $Ax = 0$
- $x \in \text{null space}(A)$

:::



## Solving $Rx = 0$

$$
\begin{bmatrix}
\boxed{1} & 1 & 0 & -1 & 0\\
0 & 0 & \boxed{1} & 0 & 2\\
0 & 0 & 0 & 0 & 0\\
\end{bmatrix} \begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4\\
x_5
\end{bmatrix} = \begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
$$

::: {.fragment .absolute left=0 top=450}

- Dependent variables
  - $x_1, x_3$
- Independent variables
  - $x_2, x_4, x_5$

:::



::: {.fragment .absolute left=600 top=450}

- $x_2 = 1, x_4 = 0, x_5 = 0$
  - $x_1 = -1, x_3 = 0$
- $x_2 = 0, x_4 = 1, x_5 = 0$
  - $x_1 = 1, x_3 = 0$
- $x_2 = 0, x_4 = 0, x_5 = 1$
  - $x_1 = 0, x_3 = -2$

:::



::: {.fragment .absolute left=1200 top=450}
$$
B = \begin{aligned}
\{
&(-1, 1, 0, 0, 0)\\
&(1, 0, 0, 1, 0)\\
&(0, 0, -2, 0, 1)\}\\
\end{aligned}
$$

$$
\text{null space}(R) = \text{span}(B)
$$

:::



## Rank Nullity Theorem

For any $m \times n$ matrix $A$, we have:

::: {.fragment .absolute left=500 top=300}
$$
\Large \boxed{\text{rank}(A) + \text{nullity}(A) = n}
$$
:::



::: {.fragment .absolute left=0 top=500}

- Rank
  - Number of non-zero rows in $Rx = 0$
  - Number of dependent variables in $Rx = 0$
- Nullity
  - Number of independent variables in $Rx = 0$

:::

