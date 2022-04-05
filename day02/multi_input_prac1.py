print('2개의 정숫값을 입력하세요.')
o1 = int(input('정수 1 : '))
o2 = int(input('정수 2 : '))
A = o1 * o2
print(f'두 값의 곱은 {A}입니다')


print('3개의 정숫값을 입력하세요.')
a1 = int(input('정수 1 : '))
a2 = int(input('정수 2 : '))
a3 = int(input('정수 3 : '))
a4 = a1 + a2 + a3
print(f'세 값의 합은 {a4}입니다.')


B = int(input('정수를 입력하세요 : '))
print(f'10을 더하면 {B+10}입니다.')
print(f'10을 빼면 {B-10}입니다.')
print(f'10을 곱하면 {B*10}입니다.')
print(f'10으로 나눈 몫은 {B//10}입니다.')
print(f'10으로 나눈 나머지는 {B%10}입니다.')


print('2개의 정숫값을 입력하세요.')
x1 = int(input('정수 x : ')) # = 우항에 입력을 받은 후, 좌항에 저장하겠다.
x2 = int(input('정수 y : '))
#백분율 계산
# x / y * 100
# ratio(백분율) = x/y*100
# 반올림(round) or 쳐내기(int)
print(f'x값은 y값의 {round(x1/x2*100)}%입니다.')


print('2개의 정숫값을 입력하세요.')
z1 = int(input('정수 x : '))
z2 = int(input('정수 y : '))
#평균의 반전값
#reverse = int(-((x+y)/2))
print(f'평균값의 부호를 반전한 값은 {int(-((z1+z2)/2))}입니다.')

#게시물 377개
# 1페이지당 게시물 10개
# 총 페이지 38페이지 <- 반올림이 아닌 그냥 올림 371개여도 38페이지