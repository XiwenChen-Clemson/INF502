# Assignment 1: Python Basics

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`
### source code
```python
import numpy as np

def pythagoreanTheorem(length_a, length_b):
    return np.sqrt(np.square(length_a) + np.square(length_b))
```

### results
```python
>>> pythagoreanTheorem(2, 2)
2.8284271247461903
>>> pythagoreanTheorem(3, 4)
5.0
>>> pythagoreanTheorem(5, 12)
13.0
```
**2. Write a function with the following signature:** `list_mangler(list_in)`.
### source code
```python
def list_mangler(list_in):
    list_out = list()
    
    for element in list_in:
        if element%2 ==0:
            list_out.append(element*2) 
        else:
            list_out.append(element*3)
        
    return list_out
    
```
### results

```python
>>> list_mangler([1,2,3,4])
[3, 4, 9, 8]
>>> list_mangler([19,29,73,47])
[57, 87, 219, 141]
>>> list_mangler([22,3,112,19])
[44, 9, 224, 57]
```




    




**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.
### description
To implement the function, we first sort (lowest to largest) the grades from the input list. Then pick the valid grades from the index 'to_drop' of the sorted list, which means the first 'to_drop' low score will be removed from the list. Finally, calculate the remained average grads and assign the corresponding letter score.
### source code
```python
import numpy as np

def grade_calc(grades_in, to_drop):
    grades_in.sort()
    grades_in = grades_in[to_drop:]
    final_grade = np.sum(grades_in)/len(grades_in)
    
    if   final_grade>=90:
            letter_grade = 'A'
    elif final_grade>=80:
            letter_grade = 'B' 
    elif final_grade>=70:
            letter_grade = 'C'
    elif final_grade>=60:
            letter_grade = 'D'
    else:
            letter_grade = 'F'
    
    return letter_grade
        
```

### results
```python
>>> grade_calc([100, 90, 80, 95], 2)
'A'
>>> grade_calc([60, 50, 77, 80,99], 3)
'B'
>>> grade_calc([18, 50, 30, 80,99], 1)
'D'
```




    


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.
### description
First, initialize the two sublists and output list by function 'list()'. Then deploy a loop to determine each element of the input list is odd or even, and apply 'list.append()' to assign the element to its corresponding sublists. Finally, apply 'list.append()' to cascade two sublists and output it.
### source code
```python
def odd_even_filter(numbers):
    even_numbers = list()
    odd_numbers  = list()
    output       = list()
    
    for element in numbers:
        if element%2==0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    
    output.append(even_numbers)
    output.append(odd_numbers)
    
    return output
    
```

### results
```python
>>> odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
>>> odd_even_filter([98, 82, 56, 7, 77, 6, 333])
[[98, 82, 56, 6], [7, 77, 333]]
>>> odd_even_filter([3, 9, 43, 7])
[[], [3, 9, 43, 7]]
```






    


