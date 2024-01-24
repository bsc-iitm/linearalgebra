---
title: Problem-5
pagetitle: Problem-5
categories: [system of equations]
---

## Question

$x_{1}$ and $x_{2}$ are two distinct solutions of $Ax=b$. Find at least one solution for each of the following systems:

- $Ax=0$ 
- $Ax=2b$.



## Hint

Add and subtract the two systems.



## Solution

Adding the two systems:
$$
\begin{equation*}
\begin{aligned}
Ax_{1} & =b\\
Ax_{2} & =b
\end{aligned} \Longrightarrow \begin{aligned}
Ax_{1} +Ax_{2} & =2b\Longrightarrow A( x_{1} +x_{2}) =2b
\end{aligned}
\end{equation*}
$$

$x_1 + x_2$ is a solution of the system $Ax = 2b$.

Subtracting the two systems:
$$
\begin{equation*}
\begin{aligned}
Ax_{1} & =b\\
Ax_{2} & =b
\end{aligned} \Longrightarrow A( x_{1} -x_{2}) =0
\end{equation*}
$$

$x_1 - x_2$ is a non-trivial solution of the system $Ax = 0$. It should be clear that $0$ is a trivial solution to $Ax = 0$.

Note that we have abused the notations a bit here. $x_{1}$ and $x_{2}$ are vectors and not components of the vector $x$.