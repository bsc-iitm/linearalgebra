---
title: Exercise-12
pagetitle: 1C, Exercise-12
categories: LADR
order: 12
---

## Exercise [^1]

Prove that the union of two subspaces of $V$ is a subspace of $V$ if and only if one of the subspaces is contained in the other.

## Solution

Let $V_1$ and $V_2$ be two subspaces of $V$. We will prove the two implications in step-1 and step-2 respectively.

### Step-1

Assume that $V_1 \cup V_2$ is a subspace. 

#### Step-1.1

If $V_1 \subset V_2$ or $V_1 \supset V_2$ then we are done. If not, without loss of generality, let $x$ be an element of $V_1$ that is not present in $V_2$. Let $y \in V_2$.

#### Step-1.2

Since $x, y \in V_1 \cup V_2$ and $V_1 \cup V_2$ is a subspace, $x + y \in V_1 \cup V_2$. 

#### Step-1.3

Now, $x + y \in V_1$ or $x + y \in V_2$. 

#### Step-1.4

If $x + y \in V_2$, then $(x + y) - y = x \in V_2$, which is not possible by the assumption that we have started off with. 

#### Step-1.5

Therefore, $x + y \in V_1$. From this, it follows that $(x + y) - x = y \in V_1$. 

#### Step-1.6

We have shown that $y \in V_2 \implies y \in V_1$. Therefore, $V_2 \subset V_1$.

### Step-2

Now for the other direction. If $V_1 \subset V_2$, then $V_1 \cup V_2 = V_2$, which is a subspace. A similar reasoning holds if $V_2 \subset V_1$.






[^1]: Exercise-12, Exercises 1C, Page-25, Linear Algebra Done Right, Fourth Edition, Sheldon Axler

