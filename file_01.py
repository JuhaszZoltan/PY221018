# 4 típus, amit használni fogunk:
# - karakteres (string) -> 'karakterlánc
a:str = 'cica'
b:str = "kutya"
print("Don't give up!")
print('Pisti azt mondta: "Nem érdekel!"')

# "konkatenáció" -> "összefűzés"
print('kutya' + 'ház')  # -> 'kutyaház'
print('Pisti azt mondja: "Don' + "'t" + ' give up!"')
amit_mond = "Don't give up!"
print(f'Pisti azt mondja: "{amit_mond}"')
print(3 * 'cica ')  # -> 'cica cica cica '

# - numerikus
#    - egész (integer) -> decimális egész szám
c:int = 1992
#    - lebegőpontos (floating point number) -> "racionális" szám
d:float = 3.14
# int és float típuskompatibilis egymással:
print(10 + 3) # -> 13
print(10 - 3) # ->  7
print(10 * 3) # -> 30

print(10 / 3)   # -> 3.33333...
print(10 // 3)  # -> 3           [DIV]
print(10 % 3)   # -> 1           [MOD]

print(2 ** 10)  # -> 1024        [POW]   hatványozás
print(16 ** .5) # -> 4           [SQRT]  "gyökvonás"

# - logikai (Boolean) igaz/hamis
e:bool = True
f:bool = False

print(True and False)  # -> F
print(True or False)   # -> T
print(not True)        # -> F

# compare 'összehasonlító' operátorok:
# numerikus alkalmazás:
print(10 < 3)          # -> F
print(10 <= 3)         # -> F
print(10 > 3)          # -> T
print(10 >= 3)         # -> T

# általános alkalmazás:
print(10 == 3)           # -> F
print('cica' == "cica")  # -> T
print(True == False)     # -> F

print(10 != 3)           # -> T
print('cica' != "cica")  # -> F
print(True != False)     # -> T

print(10 < 3 or 'kutya' != "macska")  # -> T

# 'tartalmazza-e?'  <érték> in <kollekció> -> :logikai
print(3 in [10, 3, 5, 5, 11, 42, 3, 44, 1]) # -> T
print('A' not in {'A', 'a', 'B', 'c', 'W'}) # -> F