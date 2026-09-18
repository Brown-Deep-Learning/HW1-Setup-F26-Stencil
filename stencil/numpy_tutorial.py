import numpy as np

########################################################################################
########################### Making Numpy arrays (also shapes)###########################
########################################################################################
#1. Make a NumPy array of zeros with shape (5,10). 
zeros = ...
assert(zeros.shape == (5,10))
assert(np.max(zeros) == np.min(zeros) == 0)

# 2. Do it again, but make it full of ones!
ones = ...
assert(ones.shape == (5,10))
assert(np.max(ones) == np.min(ones) == 1)

# 3. Slice the array to get the first row of ones!
first_row = ...
assert(first_row.shape == (10,))

# 4. Slice the array to get the first column of ones! 
# (Hint: Try passing in `:` as one of the slice indices!) 
first_col = ...
assert(first_col.shape == (5,))

# 5. Create a new dimension on the ones array. 
# You should end up with shape (5,10,1). (Check out `np.expand_dims`)
expanded = ...
assert(expanded.shape == (5,10,1))

# 6. Cast a list `[1,2,3]` into a NumPy array. 
# Then, change the first element to `4`.
arr = ...
...
np.testing.assert_array_equal(arr, np.array([4,2,3]))

# 7. Make a NumPy array of integers 0 to 9, 
# inclusive, in shape (2,5$ using `np.arange` and `np.reshape`. 
incr = ...
assert(incr.shape == (2,5))
np.testing.assert_array_equal(incr, np.array([[0,1,2,3,4],[5,6,7,8,9]]))

# 8. With incr from 7., use `np.vstack` to add 
# a new row `[10, 11, 12, 13, 14]`.
vstacked = ...
v_target = [[0,  1,  2,  3,  4], [5,  6,  7,  8,  9], [10, 11, 12, 13, 14]]
np.testing.assert_array_equal(vstacked, np.array(v_target))

# 9. With incr from 7., use `np.hstack` to add a new column of 0's. 
# Hint: think about the dimensionality of the original matrix. 
# What dimensions do you need to represent a new column?
hstacked = ...
h_target = [[0,  1,  2,  3,  4, 0], [5,  6,  7,  8,  9, 0]]
np.testing.assert_array_equal(hstacked, np.array(h_target))

########################################################################################
################## Basic Operations (addition, subtraction, scalars)####################
########################################################################################
# 1. Add two NumPy arrays of ones with shape $(5,10)$. 
ones_1 = ...
ones_2 = ...
sum_ones = ...
assert(sum_ones.shape == (5,10))
assert(np.max(sum_ones) == np.min(sum_ones) == 2)

# 2. Subtract a NumPy arrays of ones with shape $(5,10)$ from another one. 
# Reuse ones_1 and ones_2
diff_ones = ...
assert(diff_ones.shape == (5,10))
assert(np.max(diff_ones) == np.min(diff_ones) == 0)

# 3. Multiply a NumPy array of ones with shape $(5,10)$ by the scalar two. 
scaled = ...
assert(scaled.shape == (5,10))
assert(np.max(scaled) == np.min(scaled) == 2)

########################################################################################
#### Matrix Operations (matrix product, element-wise product/division, mean, axes)######
########################################################################################
#1. Use NumPy matrix multiplication (`np.matmul` or using the `@` symbol)
# to calculate the inner product of vectors v1, v2
v1 = np.array([1,2,3])
v2 = np.array([3,2,1])
inner_prod = ...
assert(inner_prod == 10)

# 2. Use NumPy matrix multiplication (`np.matmul` or using the `@` symbol) 
# to calculate the matrix product of matrices m1 and m2. 
m1 = np.array([[1, 2, 3],\
                [0, 1, 0]])
m2 = np.array([[4,  6],\
                [2, 1],\
                [0, 5]])
mat_prod = ...

m_target = np.array([[8, 23],\
                    [2, 1]])
np.testing.assert_array_equal(mat_prod, m_target)

# 3. Use NumPy element-wise matrix multiplication (using the `*` symbol) 
# to calculate the element-wise product of matrices m1 (above) and m3).
m3 = np.array([[4, 6, 2],\
                [1, 0, 5]])
elem_prod = ...
e_target = np.array([[4, 12, 6],\
                    [0, 0, 0]])
np.testing.assert_array_equal(elem_prod, e_target)

# 4. Use NumPy element-wise matrix division (using the `/` symbol)
# to calculate the element-wise quotient of matrices m1 and m4. 
m4 = np.array([[4, 6, 2],\
                [1, 1, 5]])
quot = ...
q_target = np.array([[0.25, 0.33333333, 1.5],\
                    [0., 1., 0.]])
np.testing.assert_allclose(quot, q_target)

# 5. Use NumPy functions to find the average of the entries in matrix m5. 
# Do it again, but get the average per row
# Then, do it per column
m5 = np.array([[1,2],\
                [0,1]])
avg = ...
row_avg = ...
col_avg = ...
assert(avg == 1)
np.testing.assert_allclose(row_avg, [1.5, 0.5])
np.testing.assert_allclose(col_avg, [0.5, 1.5])

########################################################################################
################## Logical Operations (masking, np.where, argmax)#######################
########################################################################################
# 1. Use a masking operation on matrix m1. 
# We want masked to be a matrix whose entries are `False` where 
# m1's entries are less than $6$, and `True` otherwise. 
m1 = np.array([[1, 9, 5],\
                [8, 0, 2]])
masked = ...
masked_target = np.array([[False, True, False],\
                        [True, False, False]])
np.testing.assert_array_equal(masked, masked_target)

# 2. Use `np.where` on matrix m1 to 
# keep entries greater than or equal to 6 
# and replace any entries less than 6 with 0. 
replaced = ...
replaced_target = np.array([[0, 9, 0],\
                            [8, 0, 0]])
np.testing.assert_array_equal(replaced, replaced_target)

# 3. Use `np.argmax` on matrix m1 to find, per row, 
# the index of the greatest element. 
max_inds = ...
target_inds = [1,0]
np.testing.assert_array_equal(max_inds, target_inds)

########################################################################################
################################## Questions:###########################################
########################################################################################
# Given the following matrices A, B, and C:
A = np.array([[0,1,2],[3,4,5]]) # shape (2,3)
B = np.array([[1,1,1]]) # shape (1,3)
C = np.array([[-1,-1,-1],[1,1,1]]) # shape (2,3)

# 1. Create matrix D as A - B using broadcasting
D = ...

# 2. Create matrix E with shape (3,2) by reshaping C
E = ...

# Create matrix F with shape (2,2) by matrix multiplying D by E
F = ...

assert(np.all(D == [[-1,0,1],[2,3,4]]))
assert(np.all(E == [[-1,-1],[-1,1],[1,1]]))
assert(np.all(F == [[2,2],[-1,5]]))