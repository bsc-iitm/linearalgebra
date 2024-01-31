---
title: Problem-11
pagetitle: Problem-11
categories: [determinants]
order: 11
---

## Question

Compute $\displaystyle \begin{vmatrix}
a & b & c\\
b & c & a\\
c & a & b
\end{vmatrix}$.



## Hint

Row operations:

- $R_1 \rightarrow R_1 + R_2 + R_3$
- $C_1 \rightarrow  C_1 - C_2$
- $C_2 \rightarrow C_2 - C_3$



## Solution

$$
\begin{aligned}
\begin{vmatrix}
a & b & c\\
b & c & a\\
c & a & b
\end{vmatrix} & =\begin{vmatrix}
a+b+c & a+b+c & a+b+c\\
b & c & a\\
c & a & b
\end{vmatrix}\\\\
 & =( a+b+c) \cdot \begin{vmatrix}
1 & 1 & 1\\
b & c & a\\
c & a & b
\end{vmatrix}\\\\
 & =( a+b+c) \cdot \begin{vmatrix}
0 & 0 & 1\\
b-c & c-a & a\\
c-a & a-b & b
\end{vmatrix}\\\\
 & =( a+b+c)\left[( b-c)( a-b) -( c-a)^{2}\right]\\\\
 & =( a+b+c)\left[ ab-b^{2} -ac+bc-c^{2} -a^{2} +2ac\right]\\\\
 & =( a+b+c)\left[ ab+bc+ca-\left( a^{2} +b^{2} +c^{2}\right)\right]
\end{aligned}
$$

