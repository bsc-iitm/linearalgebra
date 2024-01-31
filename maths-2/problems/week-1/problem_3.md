---
title: Problem-3
pagetitle: Problem-3
categories: [system of equations, matrices]
order: 3
---

## Question

Is the following statement true or false: If the system $Ax=b$ has a solution, say $x^{*}$, then we can express it as $x^{*} =A^{-1} b$.

## Hint

Think about what happens when there are $2$ equations and $3$ unknowns.



## Solution

This statement is false. Generating a counter example. Let $x^{*}$ be a solution to a system $Ax = b$ as given below:

$$
\begin{equation*}
x^{*} =\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}
\end{equation*}
$$

$$
\begin{equation*}
\begin{aligned}
2x_{1} +x_{2} -x_{3} & =1\\
x_{1} -x_{3} & =0
\end{aligned}
\end{equation*}
$$

$$
\begin{equation*}
A=\begin{bmatrix}
2 & 1 & -1\\
1 & 0 & -1
\end{bmatrix} ,\ \ x=\begin{bmatrix}
x_{1}\\
x_{2}\\
x_{3}
\end{bmatrix} ,\ \ b=\begin{bmatrix}
1\\
0
\end{bmatrix}
\end{equation*}
$$

$A$ is not a square matrix. Inverse exists only for square matrices. Even if $A$ is a square matrix, it need not be invertible. For example, consider the following example:

$$
\begin{equation*}
A=\begin{bmatrix}
1 & -1\\
-2 & 2
\end{bmatrix} ,\ b=\begin{bmatrix}
0\\
0
\end{bmatrix} \ \rightarrow \ x^{*} =\begin{bmatrix}
1\\
1
\end{bmatrix}
\end{equation*}
$$

Here the system $Ax=b$ has a solution $x^{*}$, but it cannot be written as $A^{-1} b$ as $A$ is not invertible. Note that the above system has infinitely many solutions and only one of them was listed.
