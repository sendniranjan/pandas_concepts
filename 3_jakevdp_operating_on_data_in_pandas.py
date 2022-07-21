"""
LEARNING NOTES
--------------------------
ufunc
=========================
Pandas includes a couple useful twists, however: for unary operations like negation and trigonometric 
functions, these ufuncs will preserve index and column labels in the output, and for binary operations 
such as addition and multiplication, Pandas will automatically align indices when passing the objects to 
the ufunc.

## Ufuncs: Index Preservation
================================



"""

import pandas as pd
import numpy as np

rng = np.random.RandomState(42)


def pandas_data_operations():
	A = pd.Series([2, 4, 6], index=[0, 1, 2])
	B = pd.Series([1, 3, 5], index=[1, 2, 3])
	print("------------A------------")
	print(A)

	print("\n------------B------------\n")
	print(B)

	print("\n------------A + B------------\n")
	print(A + B)

	print("\n------------A.add(B,fill_value=0)------------\n")
	print(A.add(B,fill_value=0))

	## Index alignment in DataFrame

	A=pd.DataFrame(rng.randint(0,100,(2,2)))
	B = pd.DataFrame(rng.randint(0,100,(3,2)))

	print("------------A------------")
	print(A)

	print("\n------------B------------\n")
	print(B)

	print("\n------------A + B------------\n")
	print(A + B)

	print("\n------------A.add(B, fille_value=A.stack().mean())------------\n")
	print(A.add(B, fill_value=A.stack().mean()))

	A= rng.randint(10, size=(3,4))

	df = pd.DataFrame(A, columns=list('PQRS'))

	print("------------df------------")
	print(df)

	print("------------df.subtract(df['R'], axis=0)------------")
	print(df.subtract(df['R'], axis=0))

	print("------------df.mul(df['R'], axis=0)------------")
	print(df.mul(df['R'], axis=0))

	print("------------df.mul(df, axis=0)------------")
	print(df.mul(df, axis=0))


print(__doc__)
pandas_data_operations()


