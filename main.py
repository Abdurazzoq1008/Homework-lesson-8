a = int(input('1- sonni kiriting: '))
b = int(input('2- sonni kiriting: '))
c = int(input('3- sonni kiriting: '))
m = int(input('4- sonni kiriting: '))


if a > b :
    if c > m :
        if   a > c :
            eng_katta = a
        else:
            eng_katta = c
    else:
        if a > m :
            eng_katta = a
        else:
             eng_katta = m
else:
    if c > m :
        if b > c :
            eng_katta = b
        else:
            eng_katta = c
    else:
        if b > m :
            eng_katta = b
        else:
            eng_katta = m

print('Eng katta son: ', eng_katta)