Year = int(input())
#n의 배수이려면 나머지는 0

if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):
    print('1')
else:
    print('0')