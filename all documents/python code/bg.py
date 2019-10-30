students = ['Michael','Bob','Tracy','Thomas','Einstain','Elun','Abay','Al-Faraby','Shekspir','Sam']
##for i in students:
##    print(i)

for each in students:
    if len(each)>=5:
        students.remove(each)
        if len(students)<=4:
            break
print(students)

# def a():
#     i=1
#     return i
# a()

# def multiply(i,j):
#     k=i*j
#     return k
# multiply(4,8)

#students = ['Michael','Bob','Tracy','Thomas','Einstain','Elun','Abay','Al-Faraby','Shekspir','Sam']
# for i in range(10):
#    name = input('What is your name? :')
#    students.append(name)
# print(students)
#
# sn =[]
# for each in students:
#     if len(each) <=5:
#         sn.append(each)
#         if len(sn)>4:
#             break
# print(sn)

# def sort_students(x=11):
#     x=[]
#     students1=[]
#     for each in x:
#          if len(each) <=5:
#             students1.append(each)
#             if len(students1)>4:
#                  break
#     return students1
# x = ['Michael','Bob','Tracy','Thomas','Einstain','Elun','Abay','Al-Faraby','Shekspir','Sam']
# print(sort_students(x))
#
def hello():
    name = input("plz input your name:\n")
    print('Hello{}'.format(name))
    return name

# Note :
# This python modules, asks user to input their name
# and greets them

# from a2 import hello
# from Python2.py import rec_area
# width = input(" Hey now much is the width of ur  rec:\n")
# height = input(" Hey now much is the height of ur  rec:\n")
#
# result = rec_area(float(width),float(height))
# hello()
# print(" Hey ur rec ares ".format(result))

# from Python2.py import r_area
# r=input()
# res = r_area(float(r))
# print(res)

#
# def students_list():
#     stu_list=[]
#     while True:
#         student_name = input(" plz input stu name chjdscbhi  ok: ")
#         if student_name=='ok':
#             break
#         else:
#             stu_list.append(student_name )
#     return  stu_list
#
# # students=students_list()
# def students_stores(stus):
#     stu_stores =[]
#     for each in stus:
#         store = input(" cdsjcs dschj cdshj  : {}'s Store \n")
#         stu_stores.append(int(store))
#         print(stu_stores)
#     return students_stores()
#
# def tapsir():
#     retake=[]
#     all_students = students_list()
#     stores = students_stores(all_students)
#     avarage_scores = sum(stores) / len(stores)
#     print(avarage_scores)
#     for i in range(len(all_students)):
#         if stores[i]<avarage_scores:
#             retake.append(all_students[i])
#     return retake