import pandas as pd
import numpy as np

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


"""
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

dict_series()
