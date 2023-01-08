This repository only contains few basics tasks related to Python using Numpy and Lambda.
I performed these tasks to get a strong grip on python as it was one  of my first development of programs using python.

Tasks are following:

TASK 1:
Create a list of areas that contains the areas of the bedroom, hallway, bathroom, kitchen, and living room of a house with the following values respectfuly.

112.0, 113.5, 189.5, 789.0 ,  230.2. 

Make a clone of the areas list and name it as float_area now remove all values except for float values in the float_area list. Do the same for string values as well and name it as str_area. Now you will have three lists.

Areas
Float_area
Str_area

a.	Print all elements of  lists using slicing 
b.	Print the area of bedroom along its name from Areas list using slicing 

TASK 2:
 Consider that you have won a lottery and you want to extend your house. Add 
another list of the pool_area with the area allotted as ‘112.7, 177.9’. Along with this add a list garage with an area of 112.0. The final list will look something like this
[‘bed’, 112.0 , ‘hall’, 113.5, ‘bath’, 189.5, ‘kit’,789.0, ‘liv’, 230.0 , [‘pool’,112.7,117.9],[‘grg’,112.0]].

Write a Python program to deep flattens the above list.Following is an example.

Original list elements:
[1, [2], [[3], [4], 5], 6]
Deep flatten the said list:
[1, 2, 3, 4, 5, 6]
Original list elements:
[[[1, 2, 3], [4, 5]], 6]
Deep flatten the said list:
[1, 2, 3, 4, 5, 6]



TASK 3:
Write a Python program to extract values from a given dictionaries and create a list of lists from those values.
Original Dictionary:

[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

Extract values from the said dictionarie and create a list of lists using those values:

[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
[[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
[['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]
And vice versa


TASK 4:
Let’s suppose that you have a list of lists. This basically is a list of people and their favorite food items. Write a python function that returns the indices of people whose list of favorite food items is not a subset of any other list of favorites food items.Keep in mind that ou have to return the indices in increasing order. Following is the given list of lists
Fav_food_items = [[‘pizza’,’burger’,’hotdogs’] ,

[‘pasta’,’hotdogs’],[‘pizza’],[‘burger’,’hotdogs’],[‘rice’ ,’pasta’] ,[‘pasta’]]

Output : [0,4]
TASK 5:
Builds a ten-element tuple of random numbers and then sort the tupple in increasing order without using built-in function. Rember the result should be a tupple.

Numpy 
TASK 1:
Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.


TASK 2:
Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

TASK 3:
Write a NumPy program to save a given array to a text file and load it.

TASK 4:
Write a NumPy program to create a three-dimension array with shape (3,5,4) and set to a variable, then swap rows and columns of a given array in reverse order. 

Lambda
TASK 5:
Write a Python program to square and cube every number in a given list of integers using Lambda.
