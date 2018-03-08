import numpy as np

import pprint

# Transpose - https://www.khanacademy.org/math/linear-algebra/matrix-transformations/matrix-transpose/v/linear-algebra-transpose-of-a-matrix

mat = np.arange(9).reshape(3, 3)

pprint.pprint(mat)

mat_transpose = np.transpose(mat)

pprint.pprint(mat_transpose)


