---
title: Problem-29
pagetitle: Problem-29
sidebar: false
order: 29
categories: [matrices]
---


::: {.hidden}
$$
\newcommand{\notimplies}{\;\not\!\!\!\implies}
$$
:::


## Question

<u>Statement-1</u>: If $A$ is a $2\times 2$ matrix such that $A^{2} =I$, then $A=I$ or $A=-I$. 

<u>Statement-2</u>: If $A$ is a $2\times 2$ matrix such that $A^{2} =0$, then $A=0$. 

For each statement, give a proof if the statement is true and a counterexample otherwise.

## Solution

Let the matrix be $A=\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}$. Then:

$$
\begin{equation*}
\begin{aligned}
A^{2} & =\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}\\
 & =\begin{bmatrix}
a^{2} +bc & ab+bd\\
ac+cd & bc+d^{2}
\end{bmatrix}
\end{aligned}
\end{equation*}
$$

<u>Statement-1</u>

We have:

$$
\begin{gather*}
b( a+d) =c( a+d) =0\\
a^{2} +bc=bc+d^{2} =1
\end{gather*}
$$

If $a=0$, then $d=0$. This would make $bc=1$. One counterexample is then:

$$
\begin{equation*}
A=\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}
\end{equation*}
$$

Verify:

$$
\begin{equation*}
A^{2} =\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix} =\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix} =I
\end{equation*}
$$

<u>Statement-2</u>

Now for the second statement where $A^{2} =0$. Here, setting $a=b=d=0$ and $c=1$ gives us the following counterexample:

$$
\begin{equation*}
A=\begin{bmatrix}
0 & 0\\
1 & 0
\end{bmatrix}
\end{equation*}
$$

Verify:

$$
\begin{equation*}
A^{2} =\begin{bmatrix}
0 & 0\\
1 & 0
\end{bmatrix}\begin{bmatrix}
0 & 0\\
1 & 0
\end{bmatrix} =\begin{bmatrix}
0 & 0\\
0 & 0
\end{bmatrix} =0
\end{equation*}
$$

Both statements are false. The key idea behind this problem is to note the fact that when simple algebraic equations involving scalars are generalized to their matrix equivalents, their solutions do not get generalized. That is:

| Scalar                   | Matrix                  |
| ------------------------ | ----------------------- |
| $a^2 = 0 \implies a = 0$ | $A^2 = 0 \notimplies A = 0$ |
| $a^2 = 1 \implies a = \pm 1$ | $A^2 = I \notimplies A = \pm I$ |

