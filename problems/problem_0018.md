Select all true statements.

(a) $A^TA$ is positive semi-definite.

(b) $A^TA$ and $AA^T$ have the same eigenvectors.

(c) $A^TA$ is symmetric if and only if $A$ is symmetric.

(d) $A^TA$ and $AA^T$ have the same non-zero eigenvalues.

<hr>


Options (a) and (d) are correct.



Let $(\lambda ,v)$ be an eigenpair of of $A^{T} A$ with $\lambda \neq 0$:


$$
\begin{equation*}
\begin{aligned}
\left( A^{T} A\right) v & =\lambda v\\
\left( AA^{T}\right) Av & =\lambda ( Av)\\
\left( AA^{T}\right)( Av) & =\lambda ( Av)
\end{aligned}
\end{equation*}
$$



This is of the form $\left( AA^{T}\right) u=\lambda u$. For $( \lambda ,u)$ to be an eigenpair of $AA^{T}$, $u=Av$ has to be non-zero. To show this, do the following. If $u=Av=0$, then $A^{T} Av=0\Longrightarrow \lambda v=0$. Since $\lambda \neq 0$, $v=0$ which contradicts the fact that $( \lambda ,v)$ is an eigenpair of $A^{T} A$.



<hr>


Let $( \lambda ,v)$ be an eigenpair of $A^{T} A$. Then:


$$
\begin{equation*}
\begin{aligned}
A^{T} Av & =\lambda v\\
v^{T} A^{T} Av & =\lambda \left( v^{T} v\right)\\
( Av)^{T}( Av) & =\lambda \left( v^{T} v\right)\\
\Longrightarrow \lambda  & =\frac{||Av||^{2}}{||v||^{2}} \geqslant 0
\end{aligned}
\end{equation*}
$$



We can divide by $||v||^{2}$ as $v\neq 0$ for it is an eigenvector. Since all the eigenvalues of $A^{T} A$ are non-negative, $A^{T} A$ is positive semi definite.