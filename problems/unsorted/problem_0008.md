---
title: Problem-8
pagetitle: Problem-8
sidebar: false
order: 8
categories: [rank]
---

## Question

Let $A$ and $B$ be two matrices such that $AB$ is defined. Select the most appropriate statement.

(a) $\text{rank}(AB) = \text{rank}(A) + \text{rank}(B)$

(b) $\text{rank}(AB) = \text{rank}(A) \cdot \text{rank}(B)$

(c) $\text{rank}(AB) = \max(\text{rank}(A), \text{rank}(B))$

(d) $\text{rank}(AB) = \min(\text{rank}(A), \text{rank}(B))$

(e) $\text{rank}(AB) \leqslant \max(\text{rank}(A), \text{rank}(B))$

(f) $\text{rank}(AB) \leqslant \min(\text{rank}(A), \text{rank}(B))$

## Solution


Option (f) is correct. 





We can view matrix multiplication in the following way. If $B = \begin{bmatrix}b_1 & \cdots & b_n\end{bmatrix}$ has $n$ columns, then $AB$ can be written as:
$$
AB = \begin{bmatrix}
Ab_1 & \cdots & Ab_n
\end{bmatrix}
$$
We see that the $i^{th}$ column of $AB$ is a linear combination of the columns of $A$, with the multipliers coming from the $i^{th}$ column of $b$. Thus the column space of $AB$ is a subset of the column space of $A$. It follows that $\text{rank}(AB) \leqslant \text{rank}(A)$.

We could also view matrix multiplication in another way. If $A = \begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$ has $m$ rows, then $AB$ can be written as:
$$
AB = \begin{bmatrix}
r_1^TB\\
\vdots\\
r_m^TB
\end{bmatrix}
$$
We see that the $i^{th}$ row of $AB$ is a linear combination of the rows of $B$, with the multipliers coming form the $i^{th}$ row of $A$. Thus the row space of $AB$ is a subspace of the row space of $B$.  It follows that $\text{rank}(AB) \leqslant \text{rank}(B)$.

Combining the two inequalities, we have:
$$
\text{rank}(AB) \leqslant \min(\text{rank}(A), \text{rank}(B))
$$

