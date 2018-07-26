import random

# 로또번호는  1~46, 총 6개 당첨번호

today=[]

for i in range(0,6):
    today=random.sample(range(1,47),6)
    # today.append(random.randrange(1,47,1))
    # for j in range(0,i):
    #     if today[j]== today[i]:
    #         today[i]=random.randrange(1,47,1)

print('오늘의 추천 번호는 ')
print(today)
# print(str(today[0]) + str(today[1]) + str(today[2]) + 
# str(today[3]) + str(today[4]) + str(today[5]) + "입니다")