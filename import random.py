import random
num = input('user name ')
len_pas = int(input("Укажите длину пароля"))
pas = ''
for x in range(len_pas): 
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 

print('Hello, ', num, 'your password is: ', pas)
