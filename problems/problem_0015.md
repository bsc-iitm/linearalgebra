---
title: Problem-15
pagetitle: Problem-15
sidebar: false
order: 15
categories: [fundamental matrix subspaces]
---

## Question

Does there exist a matrix whose row space contains $(1, 2, 1)$ and whose nullspace contains $(1, -2, 1)$?

## Solution

This is not possible as the row space is orthogonal to the nullspace. A proof this statement is given below. By convention all vectors are column vectors, hence row vectors are represented as $r_i^{T}$.



- Let $A=\begin{bmatrix}— & r_{1}^{T} & — \\ & \vdots  &  \\— & r_{n}^{T} & —\end{bmatrix}$.



- Let $x\in \mathcal{N}( A) \Longrightarrow Ax=0$





- Do this component wise. $r{_{i}}^{T} x=0$ for $1\leqslant i\leqslant n$ implying that $x$ is perpendicular to every row.





- Therefore $x$ is perpendicular to the row space of $A$. 





- It follows the row space is orthogonal to the nullspace of $A$.