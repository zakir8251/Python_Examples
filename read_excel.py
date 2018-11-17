import sys
import pandas as pd

print('Python version: ' + sys.version)
print('Pandas version: ' + pd.__version__)


df = pd.read_excel('//path/to/file.xlsx', sheet_name=5, usecols=1, header=2, nrows=5) 
# Load 6th sheet, up to 2nd col and 5 rows, header is row 3; 
df = pd.read_excel('//path/to/file.xlsx', sheet_name=5, usecols=[8,9], header=2, nrows=5).sort_values('COL_NAME', ascending=False) 
# Load 6th sheet, Col#8 and 9 and 5 rows, header is row 3 and sort by COL_NAME in descending order; 
print(df)

# Classic python loop uisng enumerate - Slowest
for i, row in enumerate(df.values):
	item = df.index[i]
	x, y = row
	print(f"{x} : {y}") 
print("\n")

# Most used and faster but still slow
for index, row in df.iterrows():
	print(f"{(row['Col 1'])}: {(row['Col 2'])}")

print("\n")
# Fastest
df.columns = df.columns.str.replace(r'\s+', '_') #This replaces ' ' with '_' in col names
for row in df.itertuples():
	print(f"{row.Col_1} : {row.Col_2}")
