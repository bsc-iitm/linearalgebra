---
title: Problem-8
pagetitle: Problem-8
categories: [row operations]
---

## Question

List the three elementary row operations that you can perform on a matrix. What are some properties that all three operations possess?

## Solution

- Interchange any two rows of a matrix.
- Add a multiple of a row to another row.
- Multiply a row by a non-zero constant.



### Property-1: Reversibility

All these operations are "reversible". This means that if we start with a matrix $A$ and perform a row operation to get the matrix $B$, we can get back $A$ by performing the opposite operation on $B$. For example, 

- If we swap the first and second rows of $A$ to get $B$, we can swap the first and second rows of $B$ to get $A$.
- If we add two times the first row to the second row of $A$ to get $B$, we can subtract two times the first row from the second row of $B$ to get $A$.
- If we multiply the third row of $A$ by three to get $B$, we can divide the third row of $B$ by three to get $A$.



### Property-2: Elementary matrices

Each elementary row operation is associated with a matrix. Let us consider the operation of interchanging two rows of the matrix $A$ to get $B$, where:
$$
A = \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}, B = \begin{bmatrix}
4 & 5 & 6\\
1 & 2 & 3\\
7 & 8 & 9
\end{bmatrix}
$$
The operation is:
$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix} \xrightarrow[]{R_1 \leftrightarrow R_2} \begin{bmatrix}
4 & 5 & 6\\
1 & 2 & 3\\
7 & 8 & 9
\end{bmatrix}
$$
This can be achieved by pre-multiplying $A$ with the matrix $E = \begin{bmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{bmatrix}$. Pre-multiply means to have $E$ before $A$. Recall that matrix multiplication is not commutative, that is, the order matters. You can verify that the following matrix multiplication comes through:
$$
EA = B
$$
$E$ is called an elementary matrix. Since the row operation is reversible, we can intuitively see that the matrix $E$ is reversible or invertible. Thus, we have:
$$
E^{-1} B = A
$$
Each row operation is associated with one such elementary matrix that is invertible. A sequence of row operations can therefore be seen as a string of matrix multiplications. If we perform three row operations on $A$ with the corresponding elementary matrices being $E_1, E_2, E_3$, then the resulting matrix is:
$$
E_3 E_2 E_1 A
$$
Note the apparent change in order: $3 \rightarrow 2 \rightarrow 1$. This is because, we first have $E_1A$, then we move to $E_2E_1A$ and finally move to $E_3 E_2 E_1 A$.