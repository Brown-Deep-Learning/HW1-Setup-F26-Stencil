import tensorflow as tf

"""_______________________________________ Basic Tensor Creation _______________________________________"""
#1. Make a tf Tensor of zeros with shape (5,10). 
zeros = ...
assert(zeros.shape == (5,10))
assert(tf.reduce_max(zeros) == tf.reduce_min(zeros) == 0)

# 2. Slice the array to get the first *column* of ones! 
# (Hint: Try passing in `:` as one of the slice indices!) 
first_col = ...
assert(first_col.shape == (5,))

# 3. Create a new dimension on the zeros array. 
# You should end up with shape $(5,10,1)$. (Check out `tf.expand_dims`)
expanded = ...
assert(expanded.shape == (5,10,1))

# 3. Cast a list `[1,2,3]` into a tensor. (Check out tf.convert_to_tensor)
arr = ...
...
assert(tf.reduce_all(arr == [1,2,3]))


# 4. Make a tensor of integers $0$ to $9$, 
# inclusive, in shape $(2,5)$ using `tf.range` and `tf.reshape`. 
incr = ...
...
assert(incr.shape == (2,5))
assert(tf.reduce_all(incr == [[0,1,2,3,4],[5,6,7,8,9]]))

"""_______________________________________ Basic Operations _______________________________________"""
# 1. Add two tensors of ones with shape $(5,10)$. 
ones_1 = ...
ones_2 = ...
sum_ones = ...

assert(sum_ones.shape == (5,10))
assert(tf.reduce_max(sum_ones) == tf.reduce_min(sum_ones) == 2)


# 2. Multiply a tensor of ones with shape $(5,10)$ by the scalar two. 
scaled = ...

assert(scaled.shape == (5,10))
assert(tf.reduce_max(sum_ones) == tf.reduce_min(scaled) == 2)

"""_______________________________________ Matrix Operations _______________________________________"""
# 1. Use Tensorflow matrix multiplication (`tf.matmul` or using the `@` symbol) 
# to calculate the matrix product of matrices m1 and m2. 
m1 = tf.convert_to_tensor([[1, 2, 3],\
                            [0, 1, 0]])
m2 = tf.convert_to_tensor([[4,  6],\
                            [2, 1],\
                            [0, 5]])
mat_prod = ...

m_target = tf.convert_to_tensor([[8, 23],\
                                [2, 1]])
tf.debugging.assert_equal(mat_prod, m_target)


# 3. Use NumPy element-wise matrix multiplication (using the `*` symbol) 
# to calculate the element-wise product of matrices m1 (above) and m3).
m3 = tf.convert_to_tensor([[4, 6, 2],\
                [1, 0, 5]])
elem_prod = ...

e_target = tf.convert_to_tensor([[4, 12, 6],\
                                [0, 0, 0]])
tf.debugging.assert_equal(elem_prod, e_target)

# 5. Use Tensorflow functions to find the average of the entries in matrix m5. 
# Do it again, but get the average per row
# Then, do it per column
m5 = tf.convert_to_tensor([[1,2],\
                        [0,1]], dtype=tf.float32)
avg = ...
row_avg = ...
col_avg = ...

assert(avg == 1)
assert(tf.reduce_all(row_avg == [1.5, 0.5]))
assert(tf.reduce_all(col_avg == [0.5, 1.5]))

""" _______________________________________ Logical Operations _______________________________________"""
# 1. Use a masking operation on matrix m1. 
# We want masked to be a matrix whose entries are `False` where 
# m1's entries are less than $6$, and `True` otherwise. 
m1 = tf.convert_to_tensor([[1, 9, 5],\
                [8, 0, 2]])
masked = ...

masked_target = tf.convert_to_tensor([[False, True, False],\
                        [True, False, False]])
tf.debugging.assert_equal(masked, masked_target)

# 2. Use `tf.argmax` on matrix m1 to find, per row, 
# the index of the greatest element. 
max_inds = ...

target_inds = [1,0]
assert(tf.reduce_all(max_inds == target_inds))

"""_______________________________________ Broadcasting _______________________________________"""

A = tf.convert_to_tensor([[0,1,2],[3,4,5]]) # shape (2,3)
B = tf.convert_to_tensor([[1,1,1]]) # shape (1,3)
C = tf.convert_to_tensor([[-1,-1,-1],[1,1,1]]) # shape (2,3)

# 1. Create matrix D as A - B using broadcasting.
# 2. Create matrix E with shape (3,2) by reshaping C
# 3. Create matrix F with shape (2,2) by matrix multiplying D and E
D = ...
E = ...
F = ...