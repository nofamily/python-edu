person = {'name':'no', 'address':'cheonan', 'email':"no@naver.com"}
print(person)
print(person['name'])
print(person['email'])
print(person.items())
for key, value in person.items():
    print("\nkey  \\ " + key)
    print("value  \\ " + value)
person['name']='nonono'
print(person['name'])