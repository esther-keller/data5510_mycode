'''----Instructions----
1. Given an array of integers, write a function to calculate the 
sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote,
and include it in the comments of your program.'''

# test code w/o big o to learn how it works
nums = [4,7,2,9]
total = 0

for num in nums: #O(n) -> runs n times
    total += num #O(1) -> runs each number 1 time
print('Total: ',total)

'''----Comments----

Time Complexity: O(n)
the loop visits each element in the list exactly 1 time
the loop runs through the list containing 'n' number of elements 'n' number of times

The run time grows linearly with the size of the input (n) which is exactly what makes it time complexity O(n)
'''