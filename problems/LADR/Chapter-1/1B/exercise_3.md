---
title: Exercise-3
pagetitle: 1B, Exercise-3
categories: LADR
order: 3
---

## Exercise [^1]

Suppose $v, w \in V$. Explain why there exists a unique $x \in V$ such that $v + 3x = w$.


## Solution

Since a vector space is closed under addition, we have $w - v \in V$.

$$
\begin{aligned}
w - v &= 1(w - v)\\
      &= \left(\cfrac{1}{3} \cdot 3 \right) (w - v)\\
      &= 3 \left(\cfrac{1}{3}(w - v)\right)\\
      &= 3 x
\end{aligned}
$$

where $x = \cfrac{1}{3}(w - v)$. We have shown the existence of an element $x \in V$ such that $w = v + 3x$. Now for the uniqueness. Let there exist a $y$ such that $w = v + 3y$, then we have:

$$
w - v = 3x = 3y \implies 3(x - y) = 0 \implies x = y
$$

This establishes uniqueness.

[^1]: Exercise-3, Exercises 1B, Page-16, Linear Algebra Done Right, Fourth Edition, Sheldon Axler