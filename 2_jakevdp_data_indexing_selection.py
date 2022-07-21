"""
LEARNING NOTES
--------------------------
Data Selection in Series
=========================

### Series as dictionary ###
- Seies is mix of the dictionary and numpy array.
- It supports operations like accessing by key, data addition like dictionary and keys(), list(items())

### Series as one-dimensional array ###
- Slices, masking, and fancy indexing
- Notice that when slicing with an explicit index (i.e., data['a':'c']), the final index is included 
  in the slice, while when slicing with an implicit index (i.e., data[0:2]), the final index is excluded
  from the slice.

### Indexers: loc, iloc, and ix ###
- These slicing and indexing conventions can be a source of confusion.
  For example, if your Series has an explicit integer index, an indexing operation such as data[1] 
  will use the explicit indices, while a slicing operation like data[1:3] will use the 
  implicit Python-style index.

- Because of this potential confusion in the case of integer indexes, Pandas provides some special 
  indexer attributes that explicitly expose certain indexing schemes

## loc [explicit - direct]
- First, the loc attribute allows indexing and slicing that always references the explicit index

DIFFERENCE
--------------
Example
-------
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
1    a
3    b
5    c

data[1] -> 'a'                   data.loc[1] -> 'a'
data[1:3] -> 3 b                 data.loc[1:3] -> 1 a      same for data.loc[1:4]
             5 c                                  3 b


## iloc [implicit - indirect]
- The iloc attribute allows indexing and slicing that always references the implicit Python-style index.


data.iloc[1] -> 'b'
data.iloc[1:3] -> 3 b    
                  5 c

Pandas DataFrame
================

-  the column names conflict with methods of the DataFrame, this attribute-style access is not possible
- Like data.area is data['area'] -> True
	   data.pop is data['pop']   -> False

iloc
------
- Numeric values, [::val, ::val] (for rows and columns), [::val] (for rows) 


unstack
--------
- Multiindex

>> data

              area       pop
California  423967  38332521
Texas       695662  26448193
New York    141297  19651127
Florida     170312  19552860
Illinois    149995  12882135

>>> data.unstack()
area  California      423967
      Texas           695662
      New York        141297
      Florida         170312
      Illinois        149995
pop   California    38332521
      Texas         26448193
      New York      19651127
      Florida       19552860
      Illinois      12882135

- Access it

>>> data.unstack()['area','Texas']
695662
>>> data.unstack()['area']['Texas']
695662
>>> data.unstack().values
array([  423967,   695662,   141297,   170312,   149995, 38332521,
       26448193, 19651127, 19552860, 12882135], dtype=int64)
>>> data.unstack().index
MultiIndex([('area', 'California'),
            ('area',      'Texas'),
            ('area',   'New York'),
            ('area',    'Florida'),
            ('area',   'Illinois'),
            ( 'pop', 'California'),
            ( 'pop',      'Texas'),
            ( 'pop',   'New York'),
            ( 'pop',    'Florida'),
            ( 'pop',   'Illinois')],
           )
>>>


update
--------

- df1.update(df2) # df1 is updated with matching column,index values of df2


truncate
-----------

- df.truncate(before=start_index, after=end_index, axis="\n")


"""

import pandas as pd
import numpy as np


def data_selection_series():
	# Series as dictionary


	data = pd.Series([0, 0.2, 0.4, 0.6, 0.8,1], index = ['a1', 'a2','a3','a4','a5','a6'])
	print("\ndata\n")
	print(data)

	if 'a3' in data:
		print(data['a3'])

	print("\ndata.keys()\n")
	print(data.keys())

	print("\nlist(data.items())\n")
	print(list(data.items()))

	data['a7'] = 2
	print("\ndata\n")
	print(data)

	### Series as one-dimensional array ###

	# slicing by implicit integer index
	print("\nslicing by implicit integer index\n")
	print(data[0:2])

	# slicing by explicit index
	print("\nslicing by explicit index\n")
	print("\ndata['a1':'a4']\n")
	print(data['a1':'a4'])

	print("\ndata[(data > 0.2) & (data < 0.9)]\n")
	print(data[(data > 0.2) & (data < 0.9)])
	
	print("\ndata[['a1','a3','a7']]\n")
	print(data[['a1','a3','a7']])

	### Indexers: loc, iloc, and ix ###
	print("\nIndexers: loc, iloc, and ix\n")

	data1 = pd.Series(['a','b','c'], index=[1,3,5])

	# loc - explicit or direct
	print("\nloc - explicit or direct\n")
	print("\ndata1.loc[1]\n")     ## 'a'
	print(data1.loc[1])     ## 'a'

	print("\ndata1.loc[1:3]\n")   ## 1 'a', 3 'b'
	print(data1.loc[1:3])   ## 1 'a', 3 'b'

	#iloc - implicit or indirect
	print("\ndata1.loc[1:3]\n")   ## 1 'a', 3 'b'
	print(data1.loc[1:3])   ## 1 'a', 3 'b'

	print("\ndata1.iloc[1:3]\n")  ## 3 'b', 5 'c'
	print(data1.iloc[1:3])  ## 3 'b', 5 'c'





def data_selection_df():
	area = pd.Series({'California': 423967, 'Texas': 695662,
	                  'New York': 141297, 'Florida': 170312,
	                  'Illinois': 149995})
	pop = pd.Series({'California': 38332521, 'Texas': 26448193,
	                 'New York': 19651127, 'Florida': 19552860,
	                 'Illinois': 12882135})
	data = pd.DataFrame({'area':area, 'pop':pop})

	
	print("\ndata.area is data['area']\n")
	print(data.area is data['area'])

	print("\ndata.pop is data['pop']\n") # failed in case of the existing default functions
	print(data.pop is data['pop']) # failed in case of the existing default functions

	print("\ndata.values\n") # all the data in the df
	print(data.values) # all the data in the df

	print("\ndata.values[0:3]\n")  # first 2 rows
	print(data.values[0:3])  # first 2 rows

	#iloc
	print("\n\niloc\n\n")
	print(data.iloc[0:3,0:2])  # Row - 0,1,2, Columns - 0, 1
	print(data.iloc[0:1,0:1])  # Row - 0, Columns - 0 		[California  423967]
	print(data.iloc[::-1, ::]) # reverse the rows (Last becomes first)
	print(data.iloc[::-1])      # reverse the rows (Last becomes first)
	print(data.iloc[:, ::-1])  # reverse the columns (Last becomes first)

	#unstack
	print("\n\nunstack\n\n")
	print(data.iloc[0:3,0:2].unstack()['area','Texas'])

	#loc and other
	print(data['Florida':'Illinois'])   # same as data[1:3] 
	print(data[data.area > 400000])     # Filtering


	




print(__doc__)
# print(pandas_df.__doc__)

print("\n Function data_selection_series \n")
data_selection_series()	
print("\n Function data_selection_df \n")
data_selection_df()	
