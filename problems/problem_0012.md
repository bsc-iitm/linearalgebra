Find the number of true statements. Your answer should be between $0$ and $4$:

- The product of two upper triangular matrices is upper triangular.
- The product of two lower triangular matrices is lower triangular.
- If $L$ is a lower triangular matrix then $L^T$ is lower triangular.
- If $U$ is an upper triangular matrix then $U^T$ is lower triangular.



<hr>



Three of these statements are correct. 



- The product of any two upper (lower) triangular matrices is upper (lower) triangular. Another way of stating this is that the set of upper (lower) triangular matrices is closed under the operation of matrix multiplication. 

  

  - If this is not immediately apparent, consider two upper triangular matrices $A$ and $B$. We can express $AB$ as $\begin{bmatrix}Ab_1 & \cdots & Ab_n\end{bmatrix}$, where $b_i$ is the $i^{th}$ column of $B$. The $i^{th}$ column of $AB$ is a linear combination of the columns of $A$ with multipliers coming from $b_i$. Since $B$ is upper triangular, all entries below the $i^{th}$ coefficient in $b_i$ are zero. This means that $Ab_i$ will just be a linear combination of the first $i$ columns of $A$. Since $A$ is also upper triangular, all the elements below the $i^{th}$ row are zero for the first $i$ columns implying that $Ab_i$ will also retain this property. As $i$ was chosen arbitrarily, this property holds good for $AB$ as a whole. $AB$ is therefore upper triangular.



- An upper triangular matrix is the transpose of a lower triangular matrix and vice versa.