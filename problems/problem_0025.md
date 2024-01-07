Choose the correct options.

(a) The set $\{(1, 2, 3), (4, 5, 6), (7, 8, 9)\}$ is linearly dependent.

(b) The set $\{(1, 2, 3), (4, 5, 6), (5, 7, 9)\}$ is linearly independent.

(c) The set $\{(1, 2, 3), (0, 5, 6), (0, 0, 9)\}$ is linearly independent.

(d) The set $\{(1, 2, 3), (0, 0, 6), (0, 0, 9)\}$ is linearly independent.

<hr>



Options (a) and (c) are correct. Here is an algorithm that will work for any set of vectors:

- Add the vectors as the rows of a matrix. 
- If the rank of the resulting matrix is equal to the number of rows, then the vectors are linearly independent.
- If the rank of the matrix is less than the number of rows, then the vectors are linearly dependent.



<u>Option-(a)</u>
$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & -3 & -6\\
7 & 8 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & -3 & -6\\
0 & -6 & -12
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & 1 & 2\\
0 & 1 & 2
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & 1 & 2\\
0 & 0 & 0
\end{bmatrix}
$$
The vectors are linearly dependent.

<u>Option-(b)</u>
$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
5 & 7 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & -3 & -6\\
5 & 7 & 9
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & -3 & -6\\
0 & -3 & -6
\end{bmatrix} \rightarrow \begin{bmatrix}
1 & 2 & 3\\
0 & 1 & 2\\
0 & 0 & 0
\end{bmatrix}
$$
The vectors are linearly dependent.

<u>Option-(c)</u>
$$
\begin{bmatrix}
1 & 2 & 3\\
0 & 5 & 6\\
0 & 0 & 9
\end{bmatrix}
$$
This is clearly linearly independent.

<u>Option-(d)</u>

$\{(1, 2, 3), (0, 0, 6), (0, 0, 9)\}$ is dependent. We can see that the third and second vectors are just multiples of each other.