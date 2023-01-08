#Programming By Abdul Samie Ishfaq

#Task 1
#Area of room
Area = ["bedroom",112.0,"hallway", 113.5,"bathroom",189.5,"kitchen", 789.0,"living room", 230.2]

str_Area = Area.copy()
for i in str_Area:
  if type(i) == float:
    str_Area.remove(i)

#printing area after deleting float values
print(str_Area)

float_Area = Area.copy()
for i in float_Area:
  if type(i) == str:
    float_Area.remove(i)

#printing area after deleting string values
str_Area

#Task 2
Area = ["bed",112.0,"hall", 113.5,"bath",189.5,"kit", 230.0]
#Entering given list
List = [1, [2], [[3], [4], 5], 6]

listflattenArr = []
for i in List:
    if isinstance(i, list):
        List.extend(i)
    else:
        listflattenArr.append(i)

print(listflattenArr)

pool=['pool',112.7,117.9]
garage=['grg',112.0]
Area.append(pool)
Area.append(garage)

area_list= []
print(Area)

flattenArr  = []
for i in Area:
    if isinstance(i, list):
        Area.extend(i)
    else:
        flattenArr.append(i)

print(flattenArr)

#Task 3
List_Dictionary = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'LulaPowell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
{'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name':'Zachary Simon', 'class': 'VII'}]

my_List = []

for i in List_Dictionary:
    my_List.append(list(i.values()))

print(my_List)

#Task 4

Fav_food_items = [['pizza', 'burger', 'hotdogs'], ['pasta', 'hotdogs'], ['pizza'], ['burger', 'hotdogs'], ['price', 'pasta'], ['pasta']]
def Fav_food_indices(Fav_food_items):
    fav = [ ]
    for i in range(6):
        present = True
        for j in range(6):
            a = Fav_food_items[i]
            b = Fav_food_items[j]
            if a != b:
                if all(item in a for item in b):
                    present = False
            if present != True:
                fav.append(i)
        print(fav)

Fav_food_indices(Fav_food_items)

#Task 5
import random

def indexing(n):
    return n[-1]  
 
def sorting(tuples):
    return sorted(tuples, key = indexing)

tupleList = [(random.randrange(0, 100), random.randrange(0, 10)) for i in range(10)]
print(sorting(tupleList))

#Task 6
import numpy as np
num=np.zeros(10)
print("Array with ten zero : ")
print(num)
num=np.ones(10)
print("Array with ten one : ")
print(num)
num=np.ones(10)*5
print("Array with ten five : ")
print(num)

#Task 7
import numpy as np
nums = np.arange(10,22).reshape((3, 4))
print(nums)

#Task 8
import numpy as np
import os
arr = [1,2,3,4,5]
print("Saving array:")
print(arr)
header = 'This file is going to save now...'
np.savetxt('lab01.txt', arr, fmt="%d", header = header) 
print("Reading text file:")
readLine = np.loadtxt('lab01.txt')
print(readLine)

#Task 9
import numpy as np

nums = np.array([[[2,17,8], [51, 7,6]], [[81, 91,90], [58, 62, 70]],[[76, 36, 44],[20, 19, 17]]])
print("Create 3-d array:",nums)
print("Original array:")
print(nums)
print("Swapping rows and columes and priniting in reverse order:")
new_nums = print(nums[::-1, ::-1])
print(new_nums)

