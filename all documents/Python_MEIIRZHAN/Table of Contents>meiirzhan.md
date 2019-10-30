# Table of Contents



- [1  `if` statement](file:///home/meiirzhan/Desktop/python_hw/2-4. Python control flow statements/4. Python control flow statements.html#if-statement)

- [2  `while` statement](file:///home/meiirzhan/Desktop/python_hw/2-4. Python control flow statements/4. Python control flow statements.html#while-statement)

- [3  `for` statement](file:///home/meiirzhan/Desktop/python_hw/2-4. Python control flow statements/4. Python control flow statements.html#for-statement)

- [4  `break` statement](file:///home/meiirzhan/Desktop/python_hw/2-4. Python control flow statements/4. Python control flow statements.html#break-statement)

- 5  `continue` statement

  

  ## 1  `if` statement         if операторы

`if` statement structure:      if операторының құрылымы:

```
1. 
if(expression):
    statement

2. 
if(expression):
    statement
else:
    statement

3. 
if(expression):
    statement
elif:
    statement
else:
    statement
```

```
a=7
if a==7:
    print(a)      
```

```
7 
```

```
if a!=7:
    print(o) 
```

```
if a<5:
    print('less than 5')
else:
    print('greater than 5')      
```

```
greater than 5 
```

```
a=3
if 3<=a<4:
    print('Normal')
elif 4<=a<4.5:
    print('Good')
elif 4.5<=a<5:
    print('Excellent')
else:
    print('😭')      
```

```
Normal
```

## 2  `while` statement     while операторы

`while` statement structure:            while операторының құрылымы:

```
1.
while (expression):
    statement
    ..
2. 
while (expression):
    statement
else:
    statement
```

```
a=5
while a>0:
    print(a)
    a-=1      
```

```
5
4
3
2
1 
```

```
a=5
while a>0:
    print(a)
    a-=1
else:
    print('ok')      
```

```
5
4
3
2
1
ok 
```

```
a=1
while a<10:
    if a<=5:
        print(a)
    else:
        print('Hello')
    a+=1
else:
    print('Done!')      
```

```
1
2
3
4
5
Hello
Hello
Hello
Hello
Done!
```

## 3  `for` statement 

`for` statement structure:

```
1.  
for i in <sequence>:
    statement
2. 
for i in range(<range>):
    statement
3.
for i in <some sequence or range>:
    statement
else:
    statement 
```

```
import math
for i in [1,2,4,8,16]:
    print(math.sqrt(i))      
```

```
1.0
1.4142135623730951
2.0
2.8284271247461903
4.0 
```

```
for i in range(3):
    print(i)      
```

```
0
1
2 
```

```
for i in range(4,9): #including 4 not including 9
    print(i)      
```

```
4
5
6
7
8 
```

```
for i in range(1,10):
    print(i)
else:
    print('Done')     
```

```
1
2
3
4
5
6
7
8
9
Done 
```

```
for i in range(10):
    if i%2==0:
        print(i)
        print('i is an even nummber')
    else:
        print(i)
        print('i is an odd number')      
```

```
0
i is an even nummber
1
i is an odd number
2
i is an even nummber
3
i is an odd number
4
i is an even nummber
5
i is an odd number
6
i is an even nummber
7
i is an odd number
8
i is an even nummber
9
i is an odd number 
```

```
for i in range(5):
    print('Now printing the {}th number!'.format(i))      
```

```
Now printing the 0th number!
Now printing the 1th number!
Now printing the 2th number!
Now printing the 3th number!
Now printing the 4th number!
```

## 4  `break` statement 

The break statement terminates the loop containing it.

Оператор break завершает цикл, содержащий его.

 

![img](file:///home/meiirzhan/Desktop/python_hw/2-4.%20Python%20control%20flow%20statements/asset/flowchart-break-statement.jpg)

 

```
a = 1
while True:
    print(a)
    a+=1
    if a==10:
        break      
```

```
1
2
3
4
5
6
7
8
9 
```

```
for i in range(5,9):
    print(i)
    if i>7:
        break      
```

```
5
6
7
8 
```

```
a=10
while a<=12:
    a+=1
    for i in range(1,7):
        print(i) 
        if i==5:
            break      
```

```
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
```



####  5  `continue` statement 

The continue statement is used to skip the rest of **the code inside a loop for the current iteration only**. Loop does not terminate but continues on with the next iteration.

Continue операторы тек ағымдағы Итерация үшін цикл ішінде кодтың қалған бөлігін өткізу үшін пайдаланылады. Цикл аяқталмайды, келесі итерацияда жалғасады. 

![img](file:///home/meiirzhan/Desktop/python_hw/2-4.%20Python%20control%20flow%20statements/asset/continue-statement-flowchart.jpg)

 

```
a=1
while a<7:
    a+=1
    print(a)      
```

```
2
3
4
5
6
7 
```

```
a=1
while a<7:
    a+=1
    if a==3:
        continue
    print(a)      
```

```
2
4
5
6
7 
```

```
for i in range(1,7):
    if i==3:
        continue
    print(i)      
```

```
1
2
4
5
6 
```

```
for i in range(1,7):
    print(i)
    if i==3:
        continue      
```

```
1
2
3
4
5
6 
```

```
a=1
while a<7:
    a+=1
    if a==4:
        continue
    for i in range(7,10):
        if i=='9':
            continue
        print(i)      
```

```
7
8
9
7
8
9
7
8
9
7
8
9
7
8
9
```

```
for i in range(10,19):
    if i==15:
        continue
    print(i)      
```

```
10
11
12
13
14
16
17
18 
```

```
for i in range(10,19):
    if i==15:
        break
    print(i)      
```

```
10
11
12
13
14
```

## 