#| fig-align: center
#| echo: false
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.dpi'] = 100
#######################################
fig, ax = plt.subplots()
X = np.array([[1, 3],
              [3, 1]])
ax.scatter(X[:, 0], X[:, 1])
ax.text(0.3, 3.2, r'$(b, d)$')
ax.text(3.3, 0.7, r'$(a, c)$')
ax.text(2, 2, r'$\Delta$')
pgram = patches.Polygon([(0, 0), (1, 3), (4, 4), (3, 1)], linestyle = '--', linewidth = 1, fill = False)
ax.add_patch(pgram)
########################################
#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.xticks([ ])
plt.yticks([ ])
plt.axhline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.axvline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.gca().set_aspect('equal')
plt.show()


#### DUMP ####

#| fig-align: center
#| echo: false
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.dpi'] = 75
#######################################
fig, ax = plt.subplots()
X = np.array([[1, 0],
              [2, 0],
              [0, 1],
              [0, 3]])
ax.scatter(X[:, 0], X[:, 1])
ax.text(0.7, -0.5, r'$(1, 0)$')
ax.text(1.7, -0.5, r'$(2, 0)$')
ax.text(-0.7, 1, r'$(0, 1)$')
ax.text(-0.7, 3, r'$(0, 3)$')
rect_1 = patches.Rectangle((0, 0), 1, 1, linestyle = '--', linewidth = 1, fill = False)
rect_2 = patches.Rectangle((0, 0), 2, 3, linestyle = '--', linewidth = 1, fill = False)
ax.add_patch(rect_1)
ax.add_patch(rect_2)
########################################
#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.xticks([ ])
plt.yticks([ ])
plt.axhline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.axvline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.gca().set_aspect('equal')
plt.show()

################

#| fig-align: center
#| echo: false
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 15
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.dpi'] = 75
#######################################
fig, ax = plt.subplots()
X = np.array([[1, 3],
              [3, 1]])
ax.scatter(X[:, 0], X[:, 1])
ax.text(0.3, 3.2, r'$(b, d)$')
ax.text(3.3, 0.7, r'$(a, c)$')
ax.text(2, 2, r'$\Delta$')
pgram = patches.Polygon([(0, 0), (1, 3), (4, 4), (3, 1)], linestyle = '--', linewidth = 1, fill = False)
ax.add_patch(pgram)
########################################
#plt.xlabel(r'$x$')
#plt.ylabel(r'$y$')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.xticks([ ])
plt.yticks([ ])
plt.axhline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.axvline(color = 'black', linewidth = 0.5, linestyle = '--')
plt.gca().set_aspect('equal')
plt.show()