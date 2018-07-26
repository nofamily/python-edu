def hello(name='nick', age='10'):
    # name=input('what is your name?')
    print('hello '+ name)
    print(age + ' years old')

name=input('what is your name?')
age=input('how old are you')

hello(name, age)
hello(name)
hello()
hello(age='5', name='test')