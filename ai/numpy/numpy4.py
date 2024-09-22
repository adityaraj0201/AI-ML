import numpy as np
#sorting
matrix = np.array([[9, 4, 7], [3, 6, 2], [8, 1, 5]])
flattened = matrix.flatten()
sorted_array = np.sort(flattened)
print(sorted_array)
#Filtering 
data = np.array([1, 6, 2, 9, 5, 3, 8])
filtered_data = data[data > 5]  # Filter values greater than 5
print(filtered_data)

#Handling missing data
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
mean_value = np.nanmean(arr)  # Compute mean, ignoring NaN values
print(mean_value)