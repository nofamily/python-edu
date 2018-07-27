with open('mypage', 'r', encoding='UTF8') as file:
    print(file.read())

with open('mypage', 'a', encoding='UTF8') as file:
    file.write('\n 한글로 입력 new line write')

with open('mypage', 'r', encoding='UTF8') as file:    
    print(file.read())