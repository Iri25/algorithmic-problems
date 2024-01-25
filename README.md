# algorithmic-problems

Python project that contains the efficient solution of some algorithmic problems in terms of complexity (temporal and spatial).

The list of problems is:
1. Determine the last (alphabetical) word that can appear in a text containing multiple words separated by " " (space).

`For example. the last (alphabetical) word in "Ana has red and yellow apples" is the word "si".`

2. Determine the Euclidean distance between two locations identified by pairs of numbers.
3. 
`For example, the distance between (1,5) and (4,1) is 5.0.`

4. Determine the dot product of two sparse vectors containing real numbers. A vector is sparse when it contains many null elements. Vectors can have any size. `For example, dot product of 2 one-dimensional vectors [1,0,2,0,3] and [1,2,0,3,1] is 4.`
5. Determine the words of a text that appear exactly once in that text. `For example, the words that appear only once in "ana has ana has apples tomatoes ana" are: 'apples' and 'tomatoes'.`
6. For an n-element string containing values from the set {1, 2, ..., n - 1} such that a single value is repeated twice, identify that repeated value. `For example, in the string [1,2,3,4,2] the value 2 appears twice.`
7. For a string of n integers that also contains duplicates, determine the majority element (which appears more than n / 2 times). `For example, 2 is the majority element in the string [2,8,7,2,2,5,2,3,1,2,2].`
8. Determine the kth largest element of a string of numbers with n elements (k < n). `For example, the 2nd largest element in the string [7,4,6,3,9,1] is 7.`
9. Generate all the numbers (in binary representation) between 1 and n. `For example, if n = 4, the numbers are: 1, 10, 11, 100.`
10. Considering a matrix with n x m integer elements and a list of pairs consisting of the coordinates of 2 cells in the matrix ((p,q) and (r,s)), to calculate the sum of the elements in the sub-matrices identified by each pair.
`For example, for the matrix
[[0, 2, 5, 4, 1],
[4, 8, 2, 3, 7],
[6, 3, 4, 6, 2],
[7, 3, 1, 8, 3],
[1, 5, 7, 9, 4]]
and the list of pairs ((1, 1) and (3, 3)), ((2, 2) and (4, 4)), the sum of the elements in the first sub-matrix is 38, and the sum of the elements in the 2nd sub-matrix is 44.`
11. Considering a matrix with n x m binary elements (0 or 1) sorted ascending on the lines, identify the index of the line containing the most elements of 1.
`For example. in the matrix
[[0,0,0,1,1],
   [0,1,1,1,1],
   [0,0,1,1,1]]
the second line contains the most elements 1.`
12. Considering a matrix with n x m binary elements (0 or 1), replace with 1 all occurrences of elements equal to 0 that are completely surrounded by 1.
`For example. matrix
[[1,1,1,1,0,0,1,1,0,1],
  [1,0,0,1,1,0,1,1,1,1],
  [1,0,0,1,1,1,1,1,1,1],
  [1,1,1,1,0,0,1,1,0,1],
  [1,0,0,1,1,0,1,1,0,0],
  [1,1,0,1,1,0,0,1,0,1],
  [1,1,1,0,1,0,1,0,0,1],
  [1,1,1,0,1,1,1,1,1,1]]
becomes
[[1,1,1,1,0,0,1,1,0,1],
  [1,1,1,1,1,0,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,1],
  [1,1,1,1,1,1,1,1,0,0],
  [1,1,1,1,1,1,1,1,0,1],
  [1,1,1,0,1,1,1,0,0,1],
  [1,1,1,0,1,1,1,1,1,1]]`
