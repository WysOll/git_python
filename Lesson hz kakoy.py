a=int(input('Vvedite vklad'))
p=int(input('Cherez skolo days you snimite money?:'))
m=int(input('Vvedite mesyac'))
if m>12:
    s=a+a*(p/100)
    print(s)
else:
    print(a)
