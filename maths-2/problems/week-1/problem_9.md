---
title: Problem-9
pagetitle: Problem-9
categories: [determinants]
order: 9
---

## Question

Is $\text{det}(A + B) = \text{det}(A) + \text{det}(B)$? If it is true, prove it. If not, give a counter example.



## Hint

Think about $I$ and $-I$.



## Solution

We have:
$$
A = \begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}, \quad B = \begin{bmatrix}
-1 & 0\\
0 & -1
\end{bmatrix}
$$
The determinant of both matrices is $1$. So $\text{det}(A) + \text{det}(B) = 2$. However, $A + B$ is the zero matrix, whose determinant is zero. It follows that $\text{det}(A + B)$ need not necessarily be equal to $\text{det}(A) + \text{det}(B)$. An even simpler example:
$$
\text{det}(I + I) = \text{det}(2I) = 4
$$
But $2 \cdot \text{det}(I) = 2$.