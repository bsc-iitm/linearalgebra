---
title: Exercise-8
pagetitle: 1B, Exercise-8
categories: LADR
order: 8
---

## Exercise [^1]

Give an example of a nonempty subset $\mathcal{U}$ of $\mathbb{R}^{2}$ such that $\mathcal{U}$ is closed under scalar multiplication, but $\mathcal{U}$ is not a subspace of $\mathbb{R}^{2}$.

## Solution

### Step-1

Consider the subset $\mathcal{U} = \{(x,y)\ |\ xy = 0, x,y \in \mathbb{R}\}$. This is the collection of all vectors that either lie on the x-axis or the y-axis. 

### Step-2

Any vector in this set is either of the form $(a, 0)$ or $(0, b)$. We see that $(ka, 0)$ and $(0, kb)$ are in $\mathcal{U}$, hence $\mathcal{U}$ is closed under scalar multiplication.

### Step-3

But it is not closed under scalar addition as: $(a, 0) + (0, b) = (a, b) \notin \mathcal{U}$ as long as at $(a, b) \neq (0, 0)$.


[^1]: Exercise-8, Exercises 1C, Page-24, Linear Algebra Done Right, Fourth Edition, Sheldon Axler

