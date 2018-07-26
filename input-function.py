# name=input('what is your name?')
# print('\n '+ name)

# num1=input('first number ?')
# num2=input('second number ?')
# print(int(num1) + int(num2))
# print(int(num1) - int(num2))
# print(int(num1) * int(num2))
# print(int(num1) / int(num2))
# print(int(num1) % int(num2))

# fruits=['apple', 'banana', 'kiwi','watermalon']
# for fruit in fruits:
    # print(fruit + '가 있습니다.')

# index=0
# while index < 4:
#     print(fruits[index] + "를 꺼냈습니다.")
#     index = index +1

# # message=""
# while message != 'quit':
#     message=input('typing you message:')
#     print('>' + message)

# number=0
# while number < 10:
#     number = number+1
#     if (number%2==0):
#         continue
#     print(number)

grade = [1,2,3]
no=[1,2,3,4,5]
for g in grade:
    for n in no:
        print(str(g) + '-' + str(n))
