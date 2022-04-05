A = int(input('국어 : '))
B = int(input('영어 : '))
C = int(input('수학 : '))
V = (A+B+C)/3

print(f'당신의 평균점수 : {round(V, 2)}점')

if V >= 60:
    print('이번 시험에 통과하셨습니다.')
    
if V < 60: #else: 이것도 사용 가능.
    print('재수강 대상자입니다.')

print('열공하세요!')