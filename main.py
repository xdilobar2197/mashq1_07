mashq1_07
# 1 - misol
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

son = int(input('Son kiriting: '))
print('Faktorial: ', factorial(son))


#2 - misol
def palindrome(s):
    return s == s[::-1]

soz = input('Soz kiriting: ')
if palindrome(soz):
    print('Bu soz palindrom: ')
else:
    print('Bu soz palindrom emas.')

#3 - misol
def katta_kichik(lst):
    return max(lst), min(lst)

sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
katta, kichik = katta_kichik(sonlar)
print('Eng katta: ', katta, 'Eng kichik:', kichik)


##4 - misol
def unli_xarif(s):
    unlilar = 'aeiouA'
    sanash = sum(1 for harf in s if harf in unlilar)
    return  sanash
matn = input('Matn kiriting: ')
print('unli hariflar soni: ', unli_xarif(matn))
