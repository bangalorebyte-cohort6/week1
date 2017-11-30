## Homework Assignment 4

Submit the following by Monday, January 30th, 2017 at 6:10pm. 

In this homework you will write four basic matrix operations. Recall, that a matrix is a two dimensional list containing only integers, used in linear algebra to represent the coefficients of multivariable expressions. Submit the following in `matrix.py`. 

### Part 1

Write a function `matrix_transpose(matrix_A)` returns the transpose of matrix A as a two dimensional list. The definition of transpose can be found here: https://en.wikipedia.org/wiki/Transpose

### Part 2

Write a function `matrix_det(matrix_A)` that calculates the determinant (an integer) of matrix A if it is a 1x1 or 2x2 matrix. If the input matrix is not square, print this error message { \Cannot calculate determinant of a non-square matrix"; If the input matrix is square but has a higher dimension, print this error message { \Cannot calculate determinant of a n-by-n matrix", where you substitute n with the dimension of the input matrix. (from wikipedia https://en.wikipedia.org/wiki/Determinant)

### Part 3 

Recall matrix addition here https://en.wikipedia.org/wiki/Matrix_addition. Write a function `matrix_add(matrix_A, matrix_B)` that performs matrix addition if the dimensionality is valid. Note that the dimensionality is only valid if input matrix A and input matrix B are of the same dimension in both their row and column lengths. 

For example, you can add a 3x5 matrix with a 3x5 matrix, but you cannot add a 3x5 matrix with a 3x1 matrix. If the dimensionality is not valid, print this error message { \Cannot perform matrix addition between a-by-b matrix and c-by-d matrix", where you substitute a, b with the dimension of the input matrix A, and c,d with the dimension of the input matrix B.

### Part 4 

Recall matrix multiplication here https://en.wikipedia.org/wiki/Matrix_multiplication. Write a function `matrix_mult(matrix_A, matrix_B)` that performs matrix multiplication if the dimensionality is valid.

Note that the dimensionality is only valid if the number of columns of input matrix A is the same as the number of rows of input matrix B. Multiplying a 5x3 matrix with a 3x7 matrix is valid (resulting in a 5x7 matrix), while doing so with a 5x1 and a 7x1 matrix would not be. 

NOTE: order matters in matrix multiplication! Even though it is valid to multiply a 5x3 matrix with a 3x7 matrix in that order, it would not be valid to multiply a 3x7 matrix with a 5x3 matrix.

If the dimensionality is not valid, print this error message { \Cannot perform matrix multiplication between a-by-b matrix and c-by-d matrix", where you substitute a, b with the dimension of the input matrix A, and c,d with the dimension of the input matrix B.

### Part 5

Write a function `matrix_inverse(matrix_A)` that outputs the inverse matrix. 

### Part 6

Create a module called "matrix" and write a test script which will import the matrix module and perform matrix operations.

### Part 7

Write a "wordtools" python module which would support the following functionality

1. Remove white spaces in a string
2. Return a dictionary of characters against its count present in the string
3. Read the contents of the file, and returns the word count dictionary
4. Check whether a string is palindrom or not
5. Sort the word in an alphabetical order
6. Search and replace a string with new string
7. Convert all the characters in the string to lower case and return the lower case string
8. Convert all the characters in the string to upper case and return the upper case string



