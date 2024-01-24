---
title: Problem-21
pagetitle: Problem-21
sidebar: false
order: 21
categories: [rank, LU decomposition]
---

## Question

Consider the following matrix:
$$
\begin{equation*}
A = \begin{bmatrix}
1 & 2 & 0 & 1\\
2 & 4 & 1 & 4\\
3 & 6 & 3 & 9
\end{bmatrix}
\end{equation*}
$$

(a) Find the rank of $A$.

(b) Find a LU decomposition of $A$ if it exists.

## Solution

Let us compute the row-echelon form of $A$:



<u>Step-1</u>: $R_2 \rightarrow R_2 - 2R_1$


$$
\begin{bmatrix}
1 & 2 & 0 & 1\\
2 & 4 & 1 & 4\\
3 & 6 & 3 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
3 & 6 & 3 & 9
\end{bmatrix}
$$


<u>Step-2</u>: $R_3 \rightarrow R_3 - 3R_1$


$$
\begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
3 & 6 & 3 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
0 & 0 & 3 & 6
\end{bmatrix}
$$


<u>Step-3</u>: $R_3 \rightarrow R_3 - 3R_2$


$$
\begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
0 & 0 & 3 & 6
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
0 & 0 & 0 & 0
\end{bmatrix}
$$


Since there are two non-zero rows in the REF of $A$, the rank is $\boxed{2}$. Now for the LU decomposition. We already have $U$. It is the row echelon from of $A$. To get $L$, we start with the identity matrix, invert each of the three steps and perform them in reverse order:



<u>Step-1</u>: $R_2 \rightarrow R_2 + 3R_2$


$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 3 & 1
\end{bmatrix}
$$
<u>Step-2</u>: $R_3 \rightarrow R_3 + 3R_1$


$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 3 & 1
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
3 & 3 & 1
\end{bmatrix}
$$
<u>Step-3</u>: $R_2 \rightarrow R_2 + 2R_1$
$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
3 & 3 & 1
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 0 & 0\\
2 & 1 & 0\\
3 & 3 & 1
\end{bmatrix}
$$


We have $A = LU$:
$$
\boxed{\begin{bmatrix}
1 & 2 & 0 & 1\\
2 & 4 & 1 & 4\\
3 & 6 & 3 & 9
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0\\
2 & 1 & 0\\
3 & 3 & 1
\end{bmatrix} \begin{bmatrix}
1 & 2 & 0 & 1\\
0 & 0 & 1 & 2\\
0 & 0 & 0 & 0
\end{bmatrix}}
$$


Here $U$ is just a row-echelon form of $A$ and not an upper triangular matrix.



<hr>



Here is a loose argument as to why this algorithm works. Consider $E_1, \cdots, E_k$ as the sequence of elementary operations that convert $A$ to $U$. Then:


$$
\begin{aligned}
E_k \cdots E_1 A &= U\\
E_k \cdots E_1 A &= IU\\
A &= (E_1^{-1} \cdots E_k^{-1} I) U\\
A &= LU
\end{aligned}
$$


There are several points that have not been clarified. For one, is $E_{1}^{-1} \cdots E_{k}^{-1}$ a lower triangular matrix? Does every matrix have a LU decomposition? These issues will be taken up in a separate post.
