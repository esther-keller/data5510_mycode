'''----Instructions----
2. Given an array of integers, write a function that 
finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, 
and include it in the comments of your program.'''

# find the second largest number in the array
nums = [11, 45, 0, 5, 3, 8, 2, 7, 4]
largest = nums[0] #keep track of largest to compare to second largest
second_largest = nums[0]

for num in nums: #O(n) -> runs n times
    if num > largest: #O(1) comparison
        second_largest = largest #if num is bigger than largest, then we need to move largest down to second largest
        largest = num #replace if it's bigger
    elif num > second_largest and num < largest:
        second_largest = num #replace if it's bigger
print("Second Largest: ", second_largest)

'''----Comments----
Time Complexity: O(n)

The loop visits each element in the array 1 time
It runs through each element 1 time (n # of times)
The comparison loop only takes constant time (O(1))
'''