#1 Sort List by Key in Python
#When we sort a list it’s sorted by values. If we have a list of tuples, it’s sorted by the first element by default.
#print('Sorted list:', my_list)
my_list = [(5, 7), (4, 3), (8, 6), (3, 5)]
my_list.sort()
print('Sorted list:', my_list)



#2 Let’s that we want to use a key to sort a list by the second element.
# takes second element for sort
def secondElement(elem):
    return elem[1] 
my_list = [(5, 7), (4, 3), (8, 6), (3, 5)] 
# sorts with a key
my_list.sort(key=secondElement)

print('Sorted list:', my_list)


#3 takes second element for sort
def thirdElement(elem):
    return elem[2]
my_list = [(5, 7, 4), (4, 3, 8), (8, 6, 2), (3, 5, 1)]
# sorts with a key
my_list.sort(key=thirdElement)
print('Sorted list:', my_list)


















