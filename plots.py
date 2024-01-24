#| fig-align: center
#| echo: false
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['text.usetex'] = True
#######################################
plt.plot([0, 1], [0, 2], color = 'blue')
plt.text(0.5, 2, r'$\begin{bmatrix}1\\2\end{bmatrix}$')
plt.text(2.3, 1, r'$\begin{bmatrix}1\\2\end{bmatrix}$')
plt.plot([0, 2], [0, 1], color = 'blue')
plt.scatter([0, 1], [0, 2], color = 'red')
plt.scatter([0, 2], [0, 1], color = 'red')
plt.plot([1, 3], [2, 3], color = 'black', linestyle = '--')
plt.plot([2, 3], [1, 3], color = 'black', linestyle = '--')
########################################
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xticks([ ])
plt.yticks([ ])
plt.axhline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.axvline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.show()