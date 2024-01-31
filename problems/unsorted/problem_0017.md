---
title: Problem-17
pagetitle: Problem-17
sidebar: false
order: 17
categories: [projections]
---

## Question

Let $P$ be the projection matrix that projects vectors in $\mathbb{R}^{4}$ onto the line $(1, 2, -1, 1)$. Compute the trace of $P$.

## Solution

$P$ is a projection transformation for $\mathbb{R}^{n}$ onto the vector $v=( v_{1} ,\cdots ,v_{n})$. Then for any $x\in \mathbb{R}^{n}$:



$$
\begin{equation*}
\begin{aligned}
P( x) & =\frac{x^{T} v}{v^{T} v} v
\end{aligned}
\end{equation*}
$$



The matrix corresponding to this transformation is given by:


$$
\begin{equation*}
P=\begin{bmatrix}
| &  & |\\
P( e_{1}) & \cdots  & P( e_{n})\\
| &  & |
\end{bmatrix} =\frac{1}{v^{T} v}\begin{bmatrix}
| &  & |\\
v_{1} v & \cdots  & v_{n} v\\
| &  & |
\end{bmatrix} =\frac{1}{v^{T} v} vv^{T}
\end{equation*}
$$



We have $P_{ii} =\frac{v_{i}^{2}}{v^{T} v}$. Summing this from $i=1$ to $i=n$, we get the trace as $1$.