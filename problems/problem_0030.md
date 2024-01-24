---
title: Problem-30
pagetitle: Problem-30
sidebar: false
order: 30
categories: [matrices]
---

## Question

Does the following equation have a solution for $A\in \mathbb{R}^{2\times 2}$:

$$
\begin{equation*}
A^{2} +A+I=0
\end{equation*}
$$

##  Solution

Let $A=\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}$, then we have:


$$
\begin{equation*}
\begin{aligned}
A^{2} +A+I & =\begin{bmatrix}
a^{2} +bc+a+1 & ab+bd+b\\
ac+cd+c & bc+d^{2} +d+1
\end{bmatrix}\\
 & \\
 & =\begin{bmatrix}
0 & 0\\
0 & 0
\end{bmatrix}
\end{aligned}
\end{equation*}
$$

From this, we get:

$$
\begin{equation*}
\begin{aligned}
\left( a^{2} +a+1\right) +bc & =0\\
\left( d^{2} +d+1\right) +bc & =0\\
b( a+d+1) & =0\\
c( a+d+1) & =0
\end{aligned}
\end{equation*}
$$

We know that $a^{2} +a+1 >0$ for all $a\in \mathbb{R}$. This shows that $bc< 0$. This means that one of $b$ or $c$ is less than zero. Without loss of generality, let $b >0$ and $c< 0$. This means that $a+d+1=0$. Let $a=0,d=-1,b=1,c=-1$. Plugging this into $A$:

$$
\begin{equation*}
A=\begin{bmatrix}
0 & 1\\
-1 & -1
\end{bmatrix}
\end{equation*}
$$

Verify:

$$
\begin{equation*}
\begin{aligned}
 \begin{array}{l}
A^{2} +A+I\\
\end{array} & =\begin{bmatrix}
0 & 1\\
-1 & -1
\end{bmatrix}\begin{bmatrix}
0 & 1\\
-1 & -1
\end{bmatrix} +\begin{bmatrix}
0 & 1\\
-1 & -1
\end{bmatrix} +\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}\\
 & \\
 & =\begin{bmatrix}
-1 & -1\\
1 & 0
\end{bmatrix} +\begin{bmatrix}
0 & 1\\
-1 & -1
\end{bmatrix} +\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}\\
 & \\
 & =\begin{bmatrix}
0 & 0\\
0 & 0
\end{bmatrix}
\end{aligned}
\end{equation*}
$$

Thus the matrix equation $A^{2} +A+I=0$ has at least one solution. This is similar to this [problem](/problems/problem_0029.md){target=_blank}. Though the scalar version — $a^2 + a + 1 = 0$ — has no real solutions, the matrix version — $A^2 + A + I = 0$ — has at least one solution in $\mathbb{R}^{2 \times 2}$.
