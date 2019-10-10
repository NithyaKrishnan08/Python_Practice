# To find superfactorial of a number

def fact(n):
    if n < 0:
        print('Invalid input for factorial')
    elif n == 0:
        return 1
    else:
        ans = 1
        for i in range(1, n + 1):
            ans = ans * i
        return ans

def superfactorial(m):
    if m < 0:
        print('Invalid input for factorial')
    elif m == 0:
        return 1
    else:
        superAns = 1
        for i in range(1, m + 1):
            superAns = superAns * fact(i)
        return superAns

print(superfactorial(4))