# with open('mypage') as file
# 한글은 에러가 나므로 아래 방식으로 오픈해야함

with open('mypage', 'rt',encoding='UTF8') as file:
    content1 = file.read()

with open('mypage', 'rt',encoding='UTF8') as file:
    content2 = file.readlines()

print(content1)    
print(content2)

num=1
for line in content2:
    print(str(num) + " : " + line)
    num +=1