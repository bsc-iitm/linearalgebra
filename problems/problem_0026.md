---
title: Problem-26
pagetitle: Problem-26
sidebar: false
order: 26
categories: [orthogonal matrices, geometry]
---

## Question

Let $v = (3, 1, 2)$ be a vector in $\mathbb{R}^{3}$. If $(a, b, c)$ is the vector obtained from $v$ after an anti-clockwise rotation of the $ZX$ plane with angle $45^{\circ}$ about the $Y$-axis, then find the value of $\sqrt{2}(a + b + c - 1)$.

## Solution

This rotation can be expressed as an orthogonal matrix. To get hold of this matrix, we can look at what happens when the standard basis elements undergo this transformation. Since the $ZX$ plane is rotated, both $e_x$ and $e_z$ will change while $e_y$ will remain fixed.
$$
Q = \begin{bmatrix}
\frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}}\ \\
0 & 1 & 0\\
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}\\
\end{bmatrix}
$$
To see what happens to $(3, 1, 2)$, we just have to apply the transformation on it. Recall that this is a simple matrix-vector product:
$$
Qv = \begin{bmatrix}
\frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}}\ \\
0 & 1 & 0\\
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}\\
\end{bmatrix} \begin{bmatrix}
3\\
1\\
2
\end{bmatrix} = \begin{bmatrix}
\frac{1}{\sqrt{2}}\ \\
1\\
\frac{5}{\sqrt{2}}
\end{bmatrix}
$$
The value $\sqrt{2}\left(\frac{1}{\sqrt{2}} + 1 + \frac{5}{\sqrt{2}} - 1 \right) = \boxed{6}$.
