import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Runtime to insert one file into binary tree is O(n).
# Runtime to search binary tree if file 2 matches file 1 is O(log n)
# Total runtime = O(nlog n) < O(n^2)

# add items from names_1 to BST
bst = BinarySearchTree(names_1[0])
names_i = 1
while names_i <= len(names_1[1:]):
    bst.insert(names_1[names_i])
    names_i += 1
# compare items from BST to names_2 and add to duplicates if ==
duplicates = [duplicate for duplicate in names_2 if bst.contains(duplicate)]


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
