Consider the matrix $A = \begin{bmatrix}1 & 0\\C & 1\end{bmatrix}$, where $C$ is some real number.



(a) What are the eigenvalues of $A$?

(b) Suppose $\sigma_1$ and $\sigma_2$ are the two singular values of $A$, what is $\sigma_1^2 + \sigma_2^2$?

<hr>



Since $A$ is a triangular matrix, the eigenvalues are the elements on the diagonal. $1$ is the only eigenvalue here, but repeated twice. The singular values of $A$ are the square roots of the eigenvalues of $A^TA$. 
$$
A^TA = \begin{bmatrix}
1 & C\\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0\\
C & 1
\end{bmatrix} = \begin{bmatrix}
1 + C^2 & C\\
C & 1
\end{bmatrix}
$$
We are asked to find $\sigma_1^2 + \sigma_2^2$. This is the sum of the roots of the following characteristic polynomial:


$$
\begin{aligned}
\left[(1 + C^2) - \lambda\right](1 - \lambda) - C^2 &= 0\\
\implies \lambda^2 - (2 + C^2) \lambda + (1 - C^2) &= 0
\end{aligned}
$$
The required sum is therefore $\boxed{2 + C^2}$.