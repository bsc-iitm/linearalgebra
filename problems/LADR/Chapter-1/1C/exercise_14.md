---
title: Exercise-14
pagetitle: 1C, Exercise-
categories: LADR
order: 14
---

## Exercise [^1]

Suppose

$U = \{(x, -x, 2x) \in \mathbb{F}^{3}\ :\ x \in \mathbb{F}\}$ and $W = \{(x, x, 2x) \in \mathbb{F}^{3}\ :\ x \in \mathbb{F}\}$

Describe $U + W$ using symbols, and also give a description of $U + W$ that uses no symbols.

## Solution

### Step-1

We have:
$$
U + W = \{u + w\ |\ u \in U, w \in W\}
$$

### Step-2

Let $u = (x, -x, 2x)$ and $v = (y, y, 2y)$. Then:
$$
U + W = \{(x + y, y - x, 2(x + y)) \in \mathbb{F}^{3}\ |\ x, y \in \mathbb{F}\}
$$

### Step-3

$U + W$ is a subspace each of whose elements can be written as the sum of two vectors, one of which is in $U$ and the other in $W$. It is the smallest subspace that contains both $U$ and $W$.

::: {.callout-note}

If $\mathbb{F} = \mathbb{R}$, then we can give a geometric description of $U$, $W$ and $U + W$.

- $U$ is the line passing through the origin and the point $(1, -1, 2)$. 
- $W$ is the line passing through the origin and the point $(1, 1, 2)$.
- $U + W$ is the plane passing through the origin that contains the vectors $(1, -1, 2)$ and $(1, 1, 2)$.

:::


[^1]: Exercise-14, Exercises 1C, Page-25, Linear Algebra Done Right, Fourth Edition, Sheldon Axler

