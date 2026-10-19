'''----Instructions----
3. Write a function that takes an array of integers as 
input and returns the maximum difference between any two numbers 
in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, 
and include it in the comments of your program.'''



nums = [3567, 6654, 345, 345, 34, 9, 8, 59, 0, 90]
lgst = nums[0]
smlst = nums[0]

for num in nums: #loop through array 1 time
    if num > lgst: #O(1)
        lgst = num

    if num < smlst:
        smlst = num
max_diff = lgst - smlst
print('Maximum Difference: ', max_diff)

'''----Comments----
Time Complexity: O(n)



'''