x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0: #else를 써도 됐음.
    print('4')

# 이중 if문이란 것도 있다!!!!
#if x >= 0:
    #if y >= 0:
        #print('1')
    #else:
        #print('4')
#esle:
    #if y >= 0:
        #print('2')
    #else:
        #print('3')