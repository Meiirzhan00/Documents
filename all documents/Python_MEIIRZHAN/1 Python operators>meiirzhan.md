## 1 Python operators  1 Python операторлары

 #### 1.1  What is a operator?     1.1 Оператор деген не ?

Operators are the constructs which can manipulate the value of operands.

Операторлар-бұл операндтардың мәнін айла-шарғы ете алатын құрылымдар.

Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.

4 + 5 = 9 өрнегін қарастырайық. Мұнда 4 және 5 операнттар, ал + - оператор деп аталады.

### 1.2  Types of Operator    

![img](file:///home/meiirzhan/Desktop/python_hw/2-3%20Python%20operators%20and%20expressions/asset/types_of_operator.png)

 

### 1.3  Python Arithmetic Operators

 

#### 1.3.1  `+` Addition           1.3.1 толықтыру

Adds values on either side of the operator.

Оператордан екі жағынан да мәндерді қосады.

```
a=10
b=2 
a+b      
```

```
12 
```

```
c='Azat'
d='AI'
c+d      
```

```
'AzatAI'
```

#### 1.3.2  `-` Subtraction 

Subtracts right hand operand from left hand operand. 

Сол операндтан оң операндты шегереді.

```
a-b      
```

```
8
```

#### 1.3.3  `*`Multiplication 

multiplies values on either side of the operator

оператордан екі жағынан да мәндерді көбейтеді.

```
a*b      
```

```
20
```

#### 1.3.4  `/` Division

 Divides left hand operand by right hand operand

 Сол операндты оң операндқа бөледі.

```
a/b      
```

```
5.0
```

#### 1.3.5  `%` Modulus 

Divides left hand operand by right hand operand and returns remainder

Делит левый операнд на правый операнд и возвращает остаток.

```
a%b      
```

```
0
```

#### 1.3.6  `**` Exponent  1.3.6    Дәреже көрсеткіші 

```
f=2
b**2      0
```

```
4
```

#### 1.3.7 / / Қабаттарды Бөлу

Floor Division - The division of operands where the result is the  quotient in which the digits after the decimal point are removed. But if  one of the operands is negative, the result is floored, i.e., rounded  away from zero (towards negative infinity) −

 

```
a//b      
```

```
5
```

```
a//-2      
```

```
-5
```

### 1.4  Python comparison operations 

### 1.4 Python салыстыру операциялары

#### 1.4.1  `==` 

If the values of two operands are equal, then the condition becomes true.

Егер екі операндтың мәндері тең болса, онда шарт шынайы болады.

```
a==b      
```

```
False 
```

```
b==2      
```

```
True
```

#### 1.4.2  `!=` 

If values of two operands are not equal, then condition becomes true. 

Егер екі операндтың мәндері тең болмаса, онда шарт шынайы болады.

```
a!=2      
```

```
True 
```

```
b!=2      
```

```
False
```

#### 1.4.3  `>` 

If the value of left operand is greater than the value of right operand, then condition becomes true.

Егер сол операндтың мәні оң операндтың мәнінен артық болса, онда шарт шынайы болады. 

```
a>b      
```

```
True 
```

```
b>3      
```

```
False
```

#### 1.4.4  `<` 

If the value of left operand is less than the value of right operand, then condition becomes true.

Егер сол операндтың мәні оң операндтың мәнінен аз болса, онда шарт шынайы болады. 

#### 1.4.5  `>=`

```
If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. 
Егер сол операндтың мәні оң операндтың мәнінен артық немесе тең болса, онда шарт шынайы болады.
```

```
a>=b      
```

```
True
```

#### 1.4.6  `<=` 

If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

Егер сол операндтың мәні оң операндының мәнінен аз немесе тең болса, онда шарт шынайы болады.

### 1.5  Python Assignment operations

#### 1.5 Python тағайындау операциялары

#### 1.5.1  `=` 

Assigns values from right side operands to left side operand 

Оң операндтан сол операндқа мән береді.

```
a=10 
```

```
print(a)      
```

```
10
```

#### 1.5.2  `+=`  Add AND     добавлять и

Adds right operand to the left operand and assign the result to left operand

Оң операнданы сол операндқа қосады және сол операндқа нәтиже береді.

```
b=2 
```

```
a+=b    # a=a+b 
```

```
print(a)      
```

```
12
```

#### 1.5.3  `-=` Subtract AND    Вычесть и

It subtracts right operand from the left operand and assign the result to left operand.

Ол сол операндтан оң операндты шегеріп, сол операндқа нәтиже береді. 

```
a-=b # a= a-b
print(a)      
```

```
10
```

#### 1.5.4  `*=` Multiply AND      размножать и. 

It multiplies right operand with the left operand and assign the result to left operand

Ол оң операндты сол операндқа көбейтеді және сол операндқа нәтиже береді. 

```
a*=b # a=a*b
print(a)      
```

```
20
```

#### 1.5.5  `/=` Divide AND     разделить и. 

It divides right operand with the left operand and assign the result to left operand 

Ол оң операндты сол операндымен бөледі және сол операндқа нәтиже береді.

```
a/=b # a=a/b
print(a)      
```

```
5.0
```

#### 1.5.6  `%` Modulus AND      `%` модуль и.

It takes modulus using two operands and assign the result to left operand

Ол екі операндты пайдалана отырып, модульді қабылдайды және сол операндқа нәтиже береді. 

```
a%=b 
```

```
print(a)      
```

```
1.0
```

#### 1.5.7  `**=` Exponent AND           Экспонента И.

Performs exponential (power) calculation on operators and assign value to the left operand 

Операторлар бойынша экспоненциалды (дала) есептеуді орындайды және сол операндқа мән береді.

```
a*=b
print(a)      
```

```
2.0
```

#### 1.5.8  `//=` Floor Division     Қабаттарды Бөлу.

It performs floor division on operators and assign value to the left operand

Ол қабатты операторларға бөлуді орындайды және сол операндқа мән береді.

```
a//=b
print(a)      
```

```
1.0
```

### 1.6  Python Logical Operators 

### 1.6 Python Логикалық Операторлары 

#### 1.6.1  `and` Logical AND    и логичный и.

If both the operands are true then condition becomes true.

Егер екі операнда да шынайы болса, онда шарт шынайы болады.

```
a=True
b=False 
```

```
a and b      
```

```
False
```

#### 1.6.2  `or` Logical OR    или логическое или

If any the operands are true then condition becomes true. 

Егер қандай да бір операндалар шынайы болса, онда шарт шынайы болады.

```
a or b       
```

```
True
```

#### 1.6.3  `not` Logical NOT 

Used to reverse the logical state of its operand.

Операндтың логикалық күйін өзгерту үшін қолданылады.

```
not b      
```

```
True
```

### 1.7  Python Membership Operators 

### 1.7 Python Мүшелігінің Операторлары.

 #### 1.7.1  `in` 

Evaluates to true if it finds a variable in the specified sequence and false otherwise.

Көрсетілген тізбектегі айнымалыны тапса, true мәнін қабылдайды, және әйтпесе false.

```
some_list = [1,2,3,4,5]
a in some_list      
```

```
True 
```

```
90 in some_list      
```

```
False
```

#### 1.7.2  `not in` 

Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

Көрсетілген тізбектегі айнымалыны таппаса, true мәнін қабылдайды, және әйтпесе false. 

```
25 not in some_list      
```

```
True
```

### 1.8  Python Identity Operators 

### 1.8 Python Идентификация Операторлары 

#### 1.8.1  `is` 

```
Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. 
Егер оператор екі жағынан да айнымалы бір нысанды көрсетсе, true мәнін қабылдайды, және әйтпесе false.
```

```
a is b     
```

```
False 
```

```
type(a) is type(b)      
```

```
True
```

#### 1.8.2  `is not` 

```
Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. 
False мәнін қабылдайды, егер оператор екі жағынан да айнымалылар бір нысанды көрсетсе, және керісінше true.
```

```
a is not b      
```

```
True
```

## 2  Python Operators Precedence 

## 2 Python Операторларының Басымдылығы.

 

![img](file:///home/meiirzhan/Desktop/python_hw/2-3%20Python%20operators%20and%20expressions/asset/operator_precedence.png)

 

