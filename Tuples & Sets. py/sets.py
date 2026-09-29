# A set is a collection of unordered and unindexed.No duplicate members.

fruits_set = {"apple", "banana", "orange"}

# checking if in set
print("orange" in fruits_set)

# adding in set
fruits_set.add("mango")
# print(fruits_set)

# adding duplicate
fruits_set.add("apple")

# removing from set
fruits_set.remove("banana")
print(fruits_set)

# clear set
fruits_set.clear()

# delete set
del fruits_set

print(fruits_set)