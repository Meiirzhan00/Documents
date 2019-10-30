# Table of Contents



- [1  Function in Python](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Function-in-Python)
  - [1.1  `len()`](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#len())
  - [1.2  `split()`](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#split())
  - [1.3  Define a function in Python](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Define-a-function-in-Python)
- [2  Parameters](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Parameters)
- [3  Global Variable and Local Variable](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Global-Variable-and-Local-Variable)
- [4  Function application and function return](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Function-application-and-function-return)
- [5  Python Docstrings](file:///home/meiirzhan/Desktop/python_hw/2-5.Python function/2-5.Python Function.html#Python-Docstrings)

## 1  Function in Python  1 Python  функциясы 

 Functions are an essential part of the Python programming language:  you might have already encountered and used some of the many fantastic  functions that are built-in in the Python language

  Функциялар Python бағдарламалау тілінің ажырамас бөлігі болып табылады: мүмкін, сіз Python тіліне енгізілген көптеген фантастикалық функцияларды тап және пайдаландыңыз.

### 1.1  `len()` 

```
name = 'AzatAI'
len(name)      
```

```
6
```

### 1.2  `split()` 

```
text = 'student'
textB=text.split('u')
print(text)
print(textB)      
```

```
student
['st', 'dent'] 
```

```
textC='student'
textD=textC.split('.')
print(textD)      
```

```
['student'] 
```

```
sentence = 'I am a student, I live in Almaty. This is my Unversity-KazNU!'
sentenceB = sentence.split('.')
print(sentenceB)      
```

```
['I am a student, I live in Almaty', ' This is my Unversity-KazNU!'] 
```

```
for item in sentenceB:
    print(item)      
```

```
I am a student, I live in Almaty
 This is my Unversity-KazNU!
```

 

```
std_sentence = []
for item in sentenceB:
    std_item = item.split(',')
    std_sentence.append(std_item) 
```

```
print(std_sentence)      
```

```
[['I am a student', ' I live in Almaty'], [' This is my Unversity-KazNU!']] 
```

```
std_sentence = []
for item in sentenceB:
    if ',' not in item:
        std_sentence.append(item)
    else:
        std_item_list = item.split(',')
        for std_item in std_item_list:
            std_sentence.append(std_item) 
```

```
print(std_sentence)      
```

```
['I am a student', ' I live in Almaty', ' This is my Unversity-KazNU!'] 
```

```
std_check_sentence  = []
for item in std_sentence:
    item_word_list = item.split(' ')
    if len(item_word_list)>=13:
        std_check_sentence.append(item) 
```

```
print(std_check_sentence)      
```

```
[]
```

 #### 1.3  Define a function in Python

#### 1.3  Python функциясын анықтау 

Here blow, we will write a function to split the long text or  sentence to short sentences, while split, those sentence that has no  more than 13 words will be removed.

Міне соққы, біз ұзын мәтінді немесе сөйлемді қысқа сөйлемдерге бөлу функциясын жазамыз, ал 13 сөзден аспайтын сөйлемдер алынып тасталады.

### 