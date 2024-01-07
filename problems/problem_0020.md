Let $T: \mathbb{R}^{3} \rightarrow \mathbb{R}$ be a function. Select all linear transformations.

(a)  $T(v) = v/||v||$

(b) $T(v) = v_1 + v_2 + v_3$, where $v = (v_1, v_2, v_3)$

(c) $T(v) = \text{smallest component of } v$

(d) $T(v) = 0$



<hr>



Options (b) and (d) are correct.



- Option (a) is clearly wrong as $T(0)$ is not defined. That is, the domain doesn't even contain $0$. On the other hand, a linear transformation should take the $0$ vector to $0$.





- Option-(b) is correct. It can be verified that:
  - $T((x_1, x_2, x_3) + (y_1, y_2, y_3)) = T(x_1, x_2, x_3) + T(y_1, y_2, y_3)$
  - $T(c(x, y, z)) = cT(x, y, z)$





- Option (c) is wrong. Here is one example where the linearity is broken:
  - $T((-1, 0, 0) + (1, 0, -1)) = T(0, 0, -1) = -1$. But $T(-1, 0, 0) + T(1, 0, -1) = -2$.





- Option-(d) is correct. It is the zero-transformation.