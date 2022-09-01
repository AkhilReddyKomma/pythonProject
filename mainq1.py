#Question 1
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort() function to used to sort the list
# min() is used to find  thje minimum of a list
# and the max() is used to find the  maximum values of list.
ages.sort()
print("Final Sorted ages: ", ages)
print("Min value of ages: ", min(ages))
print("Max value of ages: ", max(ages))
# insert(position, value) - inserts the value in list at specified position
ages.insert(0,min(ages))
# append(value) - appends the value at the end of list
ages.append(max(ages))
print("List after update: ", ages)
#The biggest advantage of using median() function is that the data-list does not need to be sorted
#before being sent as parameter to the median() function using statistice module
print("Median of ages: ", statistics.median(ages))
print("Average of ages: ", statistics.mean(ages))
print("Range of ages: ", max(ages)-min(ages))

