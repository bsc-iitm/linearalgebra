---
title: Problem-1
pagetitle: Problem-1
categories: [system of equations]
order: 1
---

## Question

$$
\begin{equation*}
\begin{aligned}
x_{1} +2x_{2} -x_{3} & =0\\
x_{2} -x_{3} & =2\\
x_{2} +x_{3} & =4
\end{aligned}
\end{equation*}
$$

This system is represented as $Ax=b$. Find $A$, $x$ and $b$. Solve for $x$. How many solutions does this system have?

## Hint



Use equations $(2)$ and $(3)$ to eliminate $x_2$ or $x_3$.



## Solution

$$
\begin{equation*}
A=\begin{bmatrix}
1 & 2 & -1\\
0 & 1 & -1\\
0 & 1 & 1
\end{bmatrix} ,\ x=\begin{bmatrix}
x_{1}\\
x_{2}\\
x_{3}
\end{bmatrix} ,\ \ b=\begin{bmatrix}
0\\
2\\
4
\end{bmatrix}
\end{equation*}
$$





Adding equations $(2)$ and $(3)$ and solving for $x_2$, we get $x_2 = 3$. Substituting this back in equation $(3)$ gives $x_3 = 1$. Finally, plugging $x_2 = 3, x_3 = 1$ into equation $(1)$ gives $x_1 = -5$. $\begin{bmatrix}
-5\\
3\\
1
\end{bmatrix}$ is the only solution to this system.