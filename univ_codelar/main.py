# n = int(input('n sonini kiriting n='))
#
# a,b,c = 0,0,0
#
# i,s = 0,0
#
# while i<n:
#     a,b,c = b,c,int(input('sonni kiriting'))
#     if i>1:
#         if b>a and b>c:
#             s=s+1
#
#     i+=1
#
#
# print(s)
# n = int(input('nechta son kiritmoqchisiz: '))
# i = 1
# s = 0
#
# while i < n + 1:
#     a = int(input('son='))
#     if i % 2 == 0:
#         s = s + a
#     i = i + 1
#
# print(s)
# from math import sqrt
#
# print("Nexia", "Tico", 'Damas' " ko'rganlar qilar havas")
# print(5 ** 4)
# print(22 % 4)
# print(125 ** 2, 125 * 4)
# print((12 / 2) ** 2 * 3.14)
# print(sqrt(6 ** 2 + 7 ** 2))
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius ** 2
# print("Radiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)
#
# kocha = input('kocha: ')
# mahalla = input('kocha: ')
# tuman = input('kocha: ')
# viloyat = input('kocha: ')
# print(kocha.title(), mahalla.upper(), tuman.lower(), viloyat.capitalize())
# print(kocha,'tumano', mahalla,'tumano', tuman,'tumano', viloyat,'tumani')
#
#
# names = ['dilshod','qahramon','sunnat tojiyev','bobur']
# print(type(names))
# print(type(names[2]))
# print(names[2].title())
# print(f'Mening do\'stim {names[0].title()}')
# print(f'Mening do\'stim {names[1].title()}')
# print(f'Mening do\'stim {names[2].title()}')
# print(f'Mening do\'stim {names[3].title()}')
# print(len(names))
#
#
#
#
# print(names)
#
#
#
#

# guests = ['Qahramon', 'Sunnat','Bobur']
# print(f'Assalomu alaykum Hurmatli {guests[0].capitalize()} sizni soat 12:00 da oshga taklif qilamiz')
# print(f'Assalomu alaykum Hurmatli {guests[1].capitalize()} sizni soat 12:00 da oshga taklif qilamiz')
# print(f'Assalomu alaykum Hurmatli {guests[2].capitalize()} sizni soat 12:00 da oshga taklif qilamiz')
#
# a = guests[0]
# b = guests[1]
# guests[0] = 'Nodir'
# guests[1] = 'Sobit'
# print(f'Assalomu alaykum Hurmatli {guests[0].capitalize()} sizni soat 12:00 da oshga taklif qilamiz')
# print(f'Assalomu alaykum Hurmatli {guests[1].capitalize()} sizni soat 12:00 da oshga taklif qilamiz')
# print('kelmaganlar',a,b)

#
#
# son = int(input('sonni kiriting: '))
# a = son % 10
# b = (son // 10) % 10
# c = (son // 100) % 10
#
#
# if a == 1:
#     a = 'bir'
# elif a==2:
#     a = 'ikki'
#
# elif a == 3:
#     a = 'uch'
# elif a==4:
#     a = 'tort'
# elif a==5:
#      a = 'besh'
#
#
# elif a == 6:
#     a = 'olti'
# elif a==7:
#     a = 'yetti'
# elif a==8:
#     a = 'sakkiz'
#
#
# elif a==9:
#     a = 'toqqiz'
# elif a==0:
#     a=''
#
#
# if b == 1:
#     b = "o'n"
# elif b == 2:
#     b = 'yigirma'
#
# elif b == 3:
#     b = "o'ttiz"
# elif b == 4:
#     b = 'qirq'
# elif b == 5:
#     b = 'ellik'
#
#
# elif b == 6:
#     b = 'oltmish'
# elif b == 7:
#     b = 'yetmish'
# elif b == 8:
#     b = 'sakson'
#
#
# elif b == 9:
#     b = 'toqson'
# elif b == 0:
#     b = ''
#
#
# if c == 1:
#     c = "bir yuz"
# elif c == 2:
#     c = 'ikki yuz'
#
# elif c == 3:
#     c = "uch yuz"
# elif c == 4:
#     c = "to'rt yuz"
# elif c == 5:
#     c = 'besh yuz'
#
#
# elif c == 6:
#     c = 'olti yuz'
# elif c == 7:
#     c = 'yetti yuz'
# elif c == 8:
#     c= 'sakkiz yuz'
#
#
# elif c == 9:
#     c = "to'qqiz yuz"
# elif c == 0:
#     c = ""
#
#
#
# print(c,b,a)


# message = input('Tell me something,and I will repeat it back to you: ')
# print(message)