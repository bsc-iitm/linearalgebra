---
title: Problem-10
pagetitle: Problem-10
categories: [determinants]
order: 10
---

## Question

Compute $\begin{vmatrix}
1 & a & bc\\
1 & b & ca\\
1 & c & ab
\end{vmatrix}$.



## Hint

Row operations:

- $R_2 \rightarrow R_2 - R_1$
- $R_3 \rightarrow R_3 - R_1$



## Solution

There are four steps here, each one corresponding to one row operation. The sequence of steps is as follows:

1. $R_2 \rightarrow R_2 - R_1$
2. $R_3 \rightarrow R_3 - R_1$
3. Take $(b - a)$ and $(c - a)$ out of row-2 and row-3 respectively. This is the scaling operation, but performed slightly differently.
4. Expand the determinant along the first column.

This is how it works out:

$$
\begin{equation*}
\begin{aligned}
\begin{vmatrix}
1 & a & bc\\
1 & b & ca\\
1 & c & ab
\end{vmatrix} & =\begin{vmatrix}
1 & a & bc\\
0 & b-a & c( a-b)\\
0 & c-a & b( a-c)
\end{vmatrix}\\
 & \\
 & =( b-a)( c-a)\begin{vmatrix}
1 & a & bc\\
0 & 1 & -c\\
0 & 1 & -b
\end{vmatrix}\\
 & \\
 & =( b-a)( c-a)( c-b)\\
 & \\
 & =( a-b)( b-c)( c-a)
\end{aligned}
\end{equation*}
$$