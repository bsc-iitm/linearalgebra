---
title: Problem-13
pagetitle: Problem-13
sidebar: false
order: 13
categories: [vector spaces, triangular matrices]
---

## Question

Let $\mathbb{R}^{n \times n}$ be the vector space of $n \times n$ matrices with the usual matrix addition and scalar multiplication defined on matrices. Let $\mathcal{L}$ be the subspace of all $n \times n$ lower triangular matrices and $\mathcal{U}$ be the subspace of all $n \times n$ upper triangular matrices. Select all true statements.

(a) $\mathcal{L} \cap \mathcal{U}$ contains just the zero matrix.

(b) The dimension of $\mathcal{L}$ is $\cfrac{n(n + 1)}{2}$

(c) The dimension of $\mathcal{U}$ is $n^2$

(d) $\mathcal{L}$ and $\mathcal{U}$ are isomorhpic subspaces of $\mathbb{R}^{n \times n}$



## Solution


In a lower(upper) triangular matrix, $\cfrac{n(n + 1)}{2}$ elements can be non-zero and the rest have to be zero. The dimension of the space follows. Every upper triangular matrix in $\mathcal{U}$ can be mapped to its transpose in $\mathcal{L}$. This specifies an isomorphism between the two spaces. Every diagonal matrix is both upper triangular and lower triangular. Hence $\mathcal{L} \cap \mathcal{U}$ is actually more numerous than just the singleton set. In fact, the intersection of these two subspaces is the subspace made up of all $n \times n$ diagonal matrices.