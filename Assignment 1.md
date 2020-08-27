```python
import numpy as np

def pythagoreanTheorem(length_a, length_b):
    return np.sqrt(np.square(length_a) + np.square(length_b))
```


```python
pythagoreanTheorem(2, 2)
```




    2.8284271247461903




```python
pythagoreanTheorem(3, 4)
```




    5.0




```python
pythagoreanTheorem(5, 12)
```




    13.0




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


```python
list_mangler([1,2,3,4])
```




    [3, 4, 9, 8]




```python
list_mangler([19,29,73,47])
```




    [57, 87, 219, 141]




```python
list_mangler([22,3,112,19])
```




    [44, 9, 224, 57]




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


```python
grade_calc([100, 90, 80, 95], 2)
```




    'A'




```python
grade_calc([60, 50, 77, 80,99], 3)
```




    'B'




```python
grade_calc([18, 50, 30, 80,99], 1)
```




    'D'




```python
def odd_even_filter(numbers):
    even_numbers = list()
    odd_numbers = list()
    
    
    for element in numbers:
        if element%2==0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    
    numbers.clear()
    numbers.append(even_numbers)
    numbers.append(odd_numbers)
    
    return numbers
    
```


```python
odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
```




    [[2, 4, 6, 8], [1, 3, 5, 7, 9]]




```python
odd_even_filter([98, 82, 56, 7, 77, 6, 333])
```




    [[98, 82, 56, 6], [7, 77, 333]]




```python
odd_even_filter([1222,4454,646,1993,99,87,68,24])
```




    [[1222, 4454, 646, 68, 24], [1993, 99, 87]]


