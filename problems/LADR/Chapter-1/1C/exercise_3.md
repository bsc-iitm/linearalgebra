---
title: Exercise-3
pagetitle: 1C, Exercise-3
categories: LADR
order: 3
---

## Exercise [^1]

Show that the set of differentiable real-valued functions $f$ on the interval $(-4, 4)$ such that $f^{\prime}(-1) = 3f(2)$ is a subspace of $\mathbb{R}^{(-4, 4)}$.

## Solution

Let us call this set $S$.

### Step-1

$0 \in S$ as it satisfies the condition trivially.

### Step-2

Let $f, g \in S$. Then $f^{\prime}(-1) = 3f(2)$ and $g^{\prime}(-1) = 3g(2)$. Now:
$$
\begin{aligned}
(f + g)^{\prime}(-1) &= f^{\prime}(-1) + g^{\prime}(-1)\\
&= 3f(2) + 3g(2)\\
&= 3(f(2) + g(2))\\
&= 3(f + g)(2)
\end{aligned}
$$
$f + g \in S$. Therefore $S$ is closed under addition.

### Step-3

If $f \in S$, then $\lambda f \in S$. The argument is similar to step-2.




[^1]: Exercise-3, Exercises 1C, Page-24, Linear Algebra Done Right, Fourth Edition, Sheldon Axler

