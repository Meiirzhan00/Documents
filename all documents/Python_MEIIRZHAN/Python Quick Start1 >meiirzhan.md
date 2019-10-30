##                        Python Quick Start

Life is short, come and use Python ! Welcome to Python Quick Start!

Өмір қысқа,  келіңіз және Python-ды пайдаланыңыз !Питонды жылдам бастауға қош келдіңіз!

Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.

Python - бұл Гуидо Ван Россум құрған және 1991 жылы алғаш шығарылған, жалпы мақсатты бағдарламалауға арналған жоғары деңгейлі бағдарламалау тілі. 

## Питонды жылдам бастау

### 1. Preparing Python development environment

### 2. Python-ды дамыту ортасын дайындау

#### 2.1 Installing Python on Windows

#### 2.2 Windows-қа Python-ды орнату

#### 2.3 Installing Python on Mac OS

#### 2.4 Mac OS-қа Python-ды орнату

#### 2.5 Installing Python on Linux

#### 2.6 Linux-қа Python-ды орнату



#### 2.9 Verify Python installation 

#### 2.10 Python орнатылған ба тексеріңіз ?

#### 3 Python basic syntax

#### 4 Python негізгі синатксисі

##### 4.1 'Hello, World' in Python using command line

##### 4.1 ' Сәлем, Әлем ' Python команда жолы арқылы

Қазір шақыру бойынша келесі кодты жазыңыз:

print(Hello, World'')

##### 4.2 'Hello,World' Python file

Create a new file hello .py that contains the following line:

Келесі жолды қамтитын жаңа файл hello.py  құрыңыз:

#script: hello.py

In your terminal, navigate to the directory containing the file hello.py. Type python hello.py, then hit the Enter key.

Өзіңіздің терминалыңыздағы, hello.py деген файлдан тұратын каталогқа кіріңіз, python-ға hello.py деп енгізіңіз, содан соң Enter пернесін басыңыз.

you should see Hello, World printed to the console.

сен консольға шыққан Hello,World көру керексің.

​                  Hello, World

#### 4.3 Launch an interactive Python shell

#### 4.3 Python интерактивті қабығын іске қосу

By executing(running) the python command in your terminal, you are presented with an interactive Python shell. This is also known as the Python Interpreter.

Сіздің терминалыңызда python командасын орындау (іске қосу) кезінде сізге Python интерактивті қабығы беріледі. Бұл сондай-ақ Python интерпретаторы ретінде белгілі.

from your terminal, execute the command python.

өзіңіздің терминалыңызда python командасын орындаңыз.

​     python

Alternatively, start the interactive prompt and load file with python -i <file.py>

Сонымен қатар, интерактивті жолды іске қосыңыз және Python арқылы файлды жүктеп алыңыз .

In command line, run:

Командалық жолда, команданы орындаңыз:

python -i hello.py

Hello,World



There are multiple ways to close the Python shell:

Python қабығын жабудың бірнеше жолы:

​    exit()  or  quit()

Alternatively, CTRL + D will close the shell and put you back on your terminal's command line.

Сонымен қатар, CTRL + D қабықты жабу және сізді терминалдың командалық жолына қайтарады.

If you want to cancel a command you're in the middle of typing and get back to a clean command prompt, while staying inside the Interpreter shell, use CTRL + C .

Егер сіз теретін команданы алып тастағыңыз келсе, және интерпретатор қабықшасының ішінде қалып, таза командалық жолға қайта оралғыңыз келсе, Ctrl + C пайдаланыңыз.

#### 4.4 Run commands as a string

#### 4.4 Командаларды жол түрінде іске қосу

Python can be passed arbitrary code as a string in the shell:

Python еркін кодты қабықшада жол түрінде бере алады:

   python -c 'print ( " Hello, World ")'

This can be useful when concatenating the results of scripts together in the shell.

Бұл скрипттердің нәтижелерін қабықшамен біріктірген кезде пайдалы болуы мүмкін.

### 5 Variables

### 5 Айнымалы

To create a variable in Python, all you need to do is specify the variable name, and then assign a value to it.

Python-да айнымалы құру үшін, сізге барлық айнымалы атауын көрсету керек, содан соң оған мән беру керек.

​        <variable name> = < value >

Python uses=to assign values to variables. There's no need to declare a variable in advance ( or to assign a data type to it), assigning a value to a variable itself declares and initializes the variable with that value. There's no way to declare a variable without assigning it an initial value.

Python = мәндерді айнымалыға беру үшін пайдаланады. Айнымалыны алдын ала жариялау қажет емес (немесе оған деректер түрін тағайындау), айнымалының мәнін беру осы мәнмен айнымалыны өзі жариялайды және бастамалайды. Бастапқы мәнді тағайындамай, айнымалыны жариялау мүмкін емес.

```
# Integer
a = 2
print(a)
```

```
# Integer
b = 9876541325489
print(b)
```

```
# Floating point
pi = 3.14 
print(pi)
```

```
# String
c = 'A' 
print(c)
# Output: A
```

```
# String
name = 'John Doe' 
print(name)
```

```
# Boolean
q = True 
print(q)
# Output: True
```

```
# Empty value or null data type
x = None 
print(x)
# Output: None
```

 

Variable assignment works from left to right. So the following will give you an syntax error.

Айнымалыны беру солдан оңға қарай жұмыс істейді. Осылайша, сізге синтаксистік қате береді.

```
 0=x
```

You can not use python's keywords as a valid variable name. You can see the list of keyword by:

Python кілт сөздерін айнымалы деп пайдалануға болмайды. Сіз негізгі сөздер тізімін көре аласыз:

```
import keyword 
print(keyword.kwlist)
```

### 5.1 Rules for variable naming:

### 5.1 Айнымалыларды атау ережелері

1. Variables names must start with a latter or an underscore.
   1. Айнымалылардың аттары  соңынан басталуы немесе асты сызулы тиісті.

```
x = True # valid 
_y = True # valid
```

```
9x = False # starts with numeral 
```

```
$y = False # starts with symbol
```

1. The remainder of your variable name may consist of letters, numbers and underscores.

1. 

```
azat_0_ai_87 = 'Still Valid'
```

1.Names are case sensitive.

1. имена чувствительны к регистру.

```
x=9
X=10
```

```
x == X
```

 You can assign multiple values to multiple variables in one line.  Note that there must be the same number of arguments on the right and  left sides of the **=** operator:

Бір жолда бірнеше айнымалы мәндерді тағайындай аласыз. Оператор тораптарының оң және сол жақтағы аргументтер бір мәнді болу керек.

```
a, b, c = 1, 2, 3 
print(a, b, c)
# Output: 1 2 3
```

```
a, b, c = 1, 2
```

```
a, b = 1, 2, 3
```

You can also assign a single value to several variables simultaneously.

Сондай-ақ, бірнеше айнымалыға бір мәнді бере аласыз.

```
a=b=c=1 
print(a, b, c)
```

When using such cascading assignment, it is important to note that all 
three variables a, b and c refer to the same object in memory, an `int`
object with the value of 1. In other words, a, b and c are three 
different names given to the same int object. Assigning a different 
object to one of them afterwards doesn't change the others, just as 
expected:

При использовании такого каскадного назначения важно отметить, что все три переменные a,b и с относятся к одному и тому же обЪекту в памяти, int объект со значением. Другими словами, a,b и c  это три разных имена,присвоенные одному и тому же объекту int. Назначение другому объекту одного из них впоследствии не изменяет другие,как и ожидалось:

```
a = b = c = 1 # all three names a, b and c refer to same int object with value 1 
print(a, b, c)
# Output: 1 1 1
```

```
b = 2 # b now refers to another int object, one with a value of 2 
print(a, b, c)
# Output: 1 2 1  # so output is as expected.
```

The above is also true for mutable types (like list, dict, etc.) just as
it is true for immutable types (like int, string, tuple, etc.):

Жоғарыда айтылғандар сондай-ақ өзгертілетін түрлерге (мысалы, list, dict және т. б.)сондай-ақ, өзгермейтін түрлерге дұрыс болады (мысалы, int, string, tuple және т. б.).

```
x = y = [7, 8, 9] # x and y refer to the same list object just created, [7, 8, 9]
x = [13, 8, 9]  #x now refers to a different list object just created, [13, 8, 9]
print(y) # y still refers to the list it was first assigned
```

Nested lists are also valid in python. This means that a list can contain another list as an element.

Салынған тізімдер де python-да жарамды. Бұл тізім элемент ретінде басқа тізімді қамтуы мүмкін дегенді білдіреді.

```
x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print(x[2])
# Output: [3, 4, 5]
print(x[2][1])
# Output: 4
```

Lastly, variables in Python do not have to stay the same type as which they were first defined -- you can simply use = to assign a new value to a variable, even if that value is of a different type.

Наконец, переменные в Python не должны оставаться того же типа, как они были определены впервые-вы можете просто использовать = для присвоения нового значения переменной, даже если это значение другого типа.

```
a=2 
print(a)
# Output: 2
```

```
a = "New value" 
print(a)
# Output: New value
```

If this bothers you, think about the fact that what's on the left of = is just a name for an object. First you call the int object with value 2 a, then you change your mind and decide to give the name a to a string object, having value 'New value'. Simple, right?

Если это вас беспокоит, подумайте о том, что то, что находится слева от = - это просто имя для объекта. Сначала вы вызываете объект int со значением 2 a, затем передумываете и решаете дать имя a строковому объекту, имеющему значение 'New value'. Просто, правда?

#### 5.2 Built in data types

#### 5.2 Кірістірілген деректер түрлері

##### 5.2.1  Booleans

`bool`: A **boolean** value of either `True` or `False`. Logical operations like `and`, `or`, `not` can be performed on booleans.

bool: TRUE немесе False логикалық мәні. And, or, not сияқты логикалық операциялар буль мәндерімен орындалуы мүмкін.

```
x or y 
x and y # if x is False then x otherwise y 
not x # if x is True then False, otherwise True
```

If boolean values are used in arithmetic operations, their integer 
values (1 and 0 for True and False) will be used to return an integer 
result:

Егер арифметикалық операцияларда булевтар мәндер пайдаланылса, онда олардың бүтін мәндері (1 және 0 True және False үшін) бүтін нәтиже алу үшін пайдаланылады:

```
True * True == 1 # 1 * 1 == 1
True + False == 1 # 1 + 0 == 1
```

##### 5.2.2  Numbers

##### 5.2.2.1  int: Integer number

##### 5.2.2.1  int: Бүтін сандар

```
a=2
b = 100
c = 123456789
d = 38563846326424324
```

##### 5.2.2.2  float: Floating point number;

##### 5.2.2.2  float: Floating point number;

```
a = 2.0
b = 100.e0
c = 123456789.e1
```

##### 5.2.3  Strings

`str`: a **unicode** string. The type of 'hello'
`bytes`: a **byte** string. The type of b'hello'