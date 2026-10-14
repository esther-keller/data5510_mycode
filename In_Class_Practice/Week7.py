#big o notation: a mathmatical notation that calculaes the worst case scenario to run
#n = the input size of the algorithm
#compute or number of operatiosn performed by the cpu is big o notation * n


'''O(1) constatnt: check whether a queue is empty
O(log n) logarithmic: look up a word in a dictioanry by repeatedly opening to middle section (binary)
O(n) linear: look up a word in a dictionary by reading each word one by one
O(n log n) linearithmic: sorting a list of words in a dictionary
O(n^2) quadratic: bubble sort, selection sort, insertion sort
O(n^3) cubic: check every possible combintation of 3 students in a class
ploynomial: O(n^k) Matrix algorithms or netstied-loop operations with a fixed number of loops
exponential: O(2^n) generate every possible password combination or every subset of a set

when you have your variable in the base, that's ploymonial growth, when it's in the exponent, that's exponential growth
'''

'''in order to speed up an algorith, then look at your algorithm and figure out how to decrease an n (divide and concor your data, paralize your data)'''



lst = [3,1,4,1,5,9,2,6]

#swapping numbers in python:
#lst[0], lst[1] = lst[1], lst[0]

#sort and put in order
for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)
    
    
  