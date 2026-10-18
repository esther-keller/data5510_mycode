''' ------Lists vs Arrays------ 
list: 
memory is not memory adjacent -- data will be in different spots in memory
mutible data types -- can have strings, ints, floats, etc. in the same list (can be changed)
list = [3,1,4,1,5,9,2,6]
can mix types (heterogeneous data)

numpy array:
looks like python lists, but it's c arrays
memory adjacent -- all data will be in the same spot 
list = numpy.array([3,1,4,1,5,9,2,6])
cannot mix types (homogeneous data)
THIS IS FASTER OVERALL THAN LISTS

pandas: python analytical data and statistics
looks like python data but it's actually c data types


list comprehension: 
lst = []
for i in range(200):
    lst.append(random.randint(1,100))

list2 = [random.randint(1,100) for x in range(200)]  # this is a list comprehension, it does the same thing as the for loop above]
could use x in the front of the for loop 


queues- most are ordered by time, 
FIFO --> 2951413 -->
priority queue you can add a 2nd parameter to the queue to determine the priority of the item in the queue

stacks- 
LIFO --> 5     -->
            1
            4
            2
            3
'''