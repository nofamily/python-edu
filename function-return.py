# def sum(num1, num2):
#     return num1+num2
# num1=10
# num2=20
# print(sum(num1, num2))

def cart(fruits):
    print('장바구니 안에는 다음과 같은 과일이 있어요.')
    for fruit in fruits:
        print(fruit)

fruits=['apple', 'banana', 'orange']
cart(fruits)
