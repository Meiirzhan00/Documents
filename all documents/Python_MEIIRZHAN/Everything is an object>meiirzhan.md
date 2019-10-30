###                         Everything is an object

```
def ask(name='AzatAI'):
    print(name)
    
my_func = ask() # what this doing is initializing the function, that means the function will run when we initialize it.  
Бұл функцияны іске қосады, бұл функция біз оны іске асырғанда жұмыс істейді дегенді білдіреді.
```

```
AzatAI
```

```
my_func2 = ask # assign the function to a variable. Айнымалы функцияны белгілеңіз.
my_func2('Hello')
```

```
Hello
```

```
class Person:
    def __init__(self):
        print('Hello')
        
my_class = Perso
```

```
my_class
```

```
__main__.Person 
```

```
my_class()      
```

```
Hello      
```

```
<__main__.Person at 0x7ffb50489350> 
```

```
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())      
```

```
AzatAI
None
Hello
<__main__.Person object at 0x7ffb806f2350>
```

item is asking for the function return value, however if we do not return anything in a function, the function will return `None`

Элемент функцияның қайтарылатын мәнін сұрайды, бірақ функцияға ештеңе қайтармаса, функция ештеңе қайтармайды. 

```
def decorator_func():
    print('dec start')
    return ask 
```

```
my_ask = decorator_func()
my_ask('Tom')      
```

```
dec start
Tom
```

## 2  type, object and class 

### 2.1  type 

```
a=1
```

```
b='abc' 
```

```
type(1)      
```

```
int 
```

```
type(int)      
```

```
type 
```

```
type(a)      
```

```
int 
```

type->int->1 

```
type(b)
```

```
str 
```

```
type('abc')      
```

```
str 
```

```
type(str)      
```

```
type 
```

type -> str - > 'abc 

```
class Student():
    pass

class MyStudent():
    pass

stu = Student() 
```

```
type(stu)      
```

```
__main__.Student 
```

```
type(Student)      
```

```
type 
```

type -> class - > obj 

From above it's not hard to find that:

Жоғарыдан табу қиын емес:

```
class` is generated from `type` and `obj` is generated from `class
```

type - > class -> obj 

```
type(int)      
```

```
type 
```

```
type(1)      
```

```
int 
```

```
type(type)      
```

```
type 
```

```
a=1 
```

```
type(a)      
```

```
int 
```

```
print(type(a))      
```

```
<class 'int'> 
```

```
print(type(int))      
```

```
<class 'type'> 
```

```
Student.__base__      
```

```
object 
```

```
class MyStudent(Student):
    pass 
```

```
MyStudent.__base__      
```

```
__main__.Student 
```

Then we can find that all class is inherited from `obj` 

Тогда мы можем обнаружить, что весь класс наследуется от `obj` .

```
type.__base__      
```

```
object 
```

This means type is an object, and `type` inherited from `object` 

Это означает, что тип является объектом, а " тип "наследуется от "объекта".

```
type(object)      
```

```
type 
```

```
object.__base__ 
```

```
print(object.__base__)      
```

```
None 
```

That means object is the top level class and didn't inherited from anything.

Это означает, что объект является классом верхнего уровня и не наследуется ни от чего.

## 3  Built in types of Python 

### 3.1  Three characteristics of the object 

#### 3.1.1  object identity 

object identity is the object's stored address of object in memory. we can get a object's identity by `id` method. 

Нысанның идентификаторы-жадта сақталған объектінің мекен-жайы. біз "id"әдісімен объектінің идентификаторын ала аламыз.

```
a=5
id(a)     
```

```
4515498928 
```

```
b=[]
id(b)      
```

```
140718168212576 
```

```
a=6 
```

```
id(a)      
```

```
4515498960 
```

```
id(5)      
```

```
4515498928 
```

```
id(6)      
```

```
4515498960
```

 

![img](file:///home/meiirzhan/Documents/python_hw/3-2.%20Everything%20is%20an%20object%20in%20Python/asset/variable)

 

![img](file:///home/meiirzhan/Documents/python_hw/3-2.%20Everything%20is%20an%20object%20in%20Python/asset/variable.png)

 

![img](file:///home/meiirzhan/Documents/python_hw/3-2.%20Everything%20is%20an%20object%20in%20Python/asset/variable_changed.png)

 

#### 3.1.2  object type 

```
type(1)      
```

```
int 
```

```
type(a)      
```

```
int 
```

```
type(b)      
```

```
list 
```

#### 3.1.3  object value 

```
a      
```

```
6 
```

```
b      
```

```
[] 
```

```
print(a)      
```

```
6 
```

```
print(b)      
```

```
[]
```

```
### Python object types 
```

#### 3.1.4  None 

`None` object type can be one and only one in the global environment. 

"None" нысанының түрі жаһандық ортада бір ғана болуы мүмкін.

```
a=None 
```

```
b=None 
```

```
a==b      
```

```
True 
```

```
id(a)      
```

```
4515197016 
```

```
id(b)      
```

```
4515197016 
```

As we can see, both a and b stored in the same place in the memory. 

Как мы видим, и a, и b хранятся в одном и том же месте в памяти.

#### 3.1.5  numbers 

##### 3.1.5.1  `int` 

```
type(100)      
```

```
int 
```

```
type(1)      
```

```
int 
```

```
type(-32)      
```

```
int 
```

##### 3.1.5.2  `float` 

```
type(3.14159)      
```

```
float 
```

```
type(3.21)      
```

```
float 
```

##### 3.1.5.3  `complex` 

```
type(3+2j)      
```

```
complex 
```

##### 3.1.5.4  `bool` 

```
type(True)      
```

```
bool 
```

```
type(False)      
```

```
bool
```

### 3.2  Sequence type 

#### 3.2.1  `list` 

```
type([])      
```

```
list 
```

#### 3.2.2  bytes,byte array,memory view 

```
type(b'\\213')      
```

```
bytes 
```

#### 3.2.3  range 

#### 3.2.4  `tuple` 

```
type((2,3))      
```

```
tuple 
```

#### 3.2.5  `str` 

```
type('AzatAI')     
```

```
str 
```

#### 3.2.6  `array` 

### 3.3  `dict` 

### 3.4  `set` 

#### 3.4.1  `set` 

#### 3.4.2  `frozenset` 

### 3.5  `with`  

### 3.6  Others 

#### 3.6.1  Module 

#### 3.6.2  class 

#### 3.6.3  function 

#### 3.6.4  method 

#### 3.6.5  code 

#### 3.6.6  object

 3.6.7  type 

#### 3.6.8  elipsis

#### 3.6.9  notimplemented