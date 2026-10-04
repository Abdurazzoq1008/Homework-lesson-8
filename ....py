a = int(input('1- sonni kiriting: '))
b = int(input('2- sonni kiriting: '))
c = int(input('3- sonni kiriting: '))
m = int(input('4- sonni kiriting: '))
eng_katta = a

if b > eng_katta:
    eng_katta = b
if c > eng_katta:
    eng_katta = c
if m > eng_katta:
    eng_katta = m

print('Eng katta son:', eng_katta)