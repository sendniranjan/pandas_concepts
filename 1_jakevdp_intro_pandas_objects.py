"""
LEARNING NOTES
--------------------------
Pandas Series
==============
1. If dictionary is given as input then
	If dictionary Keys are in sorted order -> Output Series would be in sorted order
	If dictionay keys are not sorted -> Output series would be in any order

	If Index is given in Series method
		Output would be printed like given in Index
		If index length is More than values, unassigned index would be NAN (Not error)
		If index length is less than values, only those index values would be printed (Not error)

Pandas DataFrame
=================

DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column 
names.

Index length
	- Should match the data length if data has len(data) > 1 [like in list]
	- If data is single dictionary then index length can be >=1 [It would repeat data for all indexes]

Index is immutable
	- This immutability makes it safer to share indices between multiple DataFrames and arrays, 
	  without the potential for side effects from inadvertent index modification.

Index as ordered set
	- Pandas objects are designed to facilitate operations such as joins across datasets, 
	  which depend on many aspects of set arithmetic. The Index object follows many of the 
	  conventions used by Python's built-in set data structure, so that unions, intersections,
	  differences, and other combinations can be computed in a familiar way:

"""

import pandas as pd
import numpy as np


def normal_series():
	S1 = pd.Series([0.2, 0.4, 0.6, 0.8 , 1])
	print(S1)
	print(S1.index)
	print(S1.values)

	print(S1[0:3].values)


def dict_series():

	# Unsorted Order
	d={'California': 38332521,'Texas': 26448193,'New York': 19651127,'Florida': 19552860,'Illinois': 12882135}
	S2= pd.Series(d)
	# print(S2) # Unsorted series will be printed, use pd.Series(d).sort_index() to sort it

	# Sorted Order
	d={'California': 38332521,
	'Florida': 19552860,
	'Illinois': 12882135,
	'New York': 19651127,
	'Texas': 26448193}

	populaion= pd.Series(d)
	print(populaion)
	# print(populaion.index)

	# Index
	S2 = pd.Series(d, index=['Texas', 'Illinois','Florida','California',  'New York'])
	# print(S2) # will be printed exactly like given in index

	S2 = pd.Series(d, index=['Texas', 'Illinois','Florida','California',  'New York', 'Delhi', 'Mumbai'])
	# print(S2) # will be printed NAN for Delhi, Mumbai

	S2 = pd.Series(d, index=['Texas', 'New York','Florida'])
	print(S2) # will be printed for given index only

	# population slicing
	print(populaion['California':'Illinois'])

def pandas_df():
	"""
	The Pandas DataFrame Object

	DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column 
	names.

	Index length
		- Should match the data length if data has len(data) > 1 [like in list]
		- If data is single dictionary then index length can be >=1 [It would repeat data for all indexes]

	Index is immutable
		- This immutability makes it safer to share indices between multiple DataFrames and arrays, 
		  without the potential for side effects from inadvertent index modification.

	Index as ordered set
		- Pandas objects are designed to facilitate operations such as joins across datasets, 
		  which depend on many aspects of set arithmetic. The Index object follows many of the 
		  conventions used by Python's built-in set data structure, so that unions, intersections,
		  differences, and other combinations can be computed in a familiar way:




	"""

	####################### Index Length ########################
	try:
		df=pd.DataFrame([{'a':1,'b':2,'c':3},{'a':4,'b':7,'c':9}],index=[100])
		# error above as index is missing
	except Exception as e:
		pass

	df=pd.DataFrame([{'a':1,'b':2,'c':3},{'a':4,'b':7,'c':9}],index=[100, 101])
	# df=
	# 	     a  b  c
	# 	100  1  2  3
	# 	101  4  7  9
	df=pd.DataFrame({'a':1,'b':2,'c':3},index=[9])
	# df=
	# 	   a  b  c
	# 	9  1  2  3
	df=pd.DataFrame({'a':1,'b':2,'c':3},index=[9,10,11])
	# df=
	# 	    a  b  c
	# 	9   1  2  3
	# 	10  1  2  3
	# 	11  1  2  3

	####################### Index Length End ########################

	####################### Index as ordered set ####################

	indA = pd.Index([1,3,5,7,9])
	indB = pd.Index([2,4,6,8,10])

	# print(indA, indB)
	# print(indA & indB)
	# print(indA | indB)

	####################### Index as ordered set End ####################
	


print(__doc__)
# print(pandas_df.__doc__)

pandas_df()	
