Consider the following system of linear equations:

$$
\begin{aligned}
x_1 - 3x_2 &= 4\\
3x_1 + kx_2 &= -12
\end{aligned}
$$

where $k \in \mathbb{R}$. If the given system has a unique solution, comment on the value that $k$ cannot assume.

<hr>



If $A$ is a square matrix, then the system $Ax = b$ has a unique solution when $A$ is invertible. This happens when $\text{det}(A) \neq 0$. Since we are asked to comment on the values that $k$ cannot assume, we can set the determinant equal to zero:
$$
\begin{vmatrix}
1 & -3\\
3 & k
\end{vmatrix} = 0 \implies k + 9 = 0 \implies k = -9
$$
The system will have a unique solution as long as $\boxed{k \neq -9}$.