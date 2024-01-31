---
title: Problem-9
pagetitle: Problem-9
sidebar: false
order: 9
categories: [similarity]
---

## Question

$A$ and $B$ are two square matrices. Select all correct options.

(a) If $A$ and $B$ are similar then they have the same rank.

(b) If $A$ and $B$ have the same rank then they are similar.

(c) If $A$ and $B$ have the same trace, then $A$ and $B$ are similar.

(d) Any two diagonal matrices are similar.

## Solution


Option-(a) is the only correct answer.



- If $A$ and $B$ are similar, there is an invertible matrix $P$ such that $A = P^{-1} B P$. Multiplying a matrix by an invertible matrix doesn't change the rank of the resulting product. Hence the rank of $A$ is equal to rank of $B$.



- If $A$ and $B$ have the same rank, then they need not be similar. As a counter example, consider the matrices $\alpha I$ and $\beta I$, where $I$ is the identity matrix and $\alpha \neq \beta$. As long as $\alpha \beta \neq 0$, both matrices have the same rank (full rank). But they are not similar. This is because the only matrix similar to a scalar matrix is the matrix itself, which follows from this observation: $P^{-1}(\alpha I)P = \alpha I$.



- If $A$ and $B$ have the same trace, then they need not be similar. As a counter example, consider $\alpha I$ and a matrix $A$ which has $n \alpha$ as one of its diagonal entries and zero in all other places. Here $n$ is the order of the matrix. These two matrices have the same trace but are not similar and the argument is the same as the one presented in the previous bullet point.



- Any two diagonal matrices need not be similar. Refer to option-(b) for a counter example.