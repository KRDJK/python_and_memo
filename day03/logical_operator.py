#논리연산이란, true와 true를 연산하거나, true, false 간, false와 false간 연산을 위해 사용.

# 놀이기구 키 140cm 이상, 나이 8세 이상이어야 함.
# TT, TF, FT, FF의 4가지 논리연산이 존재.
# and 연산(T and T 등)과 or 연산(T or T 등)이 있음.

# T and T = T ex) 로그인시 아이디, 비번 입력
# T and F = F
# F and T = F
# F and F = F

# T or T = T 둘 중에 하나만 맞아도 될 때  사용.
# T or F = T
# F or T = T
# F pr F = F 미성년자가 심야에 pc방 방문시, 신분증 검사 성인 인증 or 보호자 동반 경우 등.

T = True
F = False

print(T and T)  #깨알 복붙 팁!! Alt + shift + 방향키 아래키
print(T and F)
print(F and T)
print(F and F)

print('=============================')

print(T or T)
print(T or F)
print(F or T)
print(F or F)

print('=============================')

a = 5 # -5라고 하면 else값이 도출됨. and 기준 좌항은 불충분조건, 우항은 충분조건 and 연산이라 둘 다 충족해야하기 때문.

if (a > 1) and (a < 10): #두 조건을 다 만족해야 True 값이 나옴. why? and 연산이기 때문.
    print('a는 1과 10 사이의 정수입니다!')
else:
    print('a는 범위 안의 정수가 아닙니다.')

print('=============================')

b = 3
if (b == 2) or (b == 4):
    print('b는 2 또는 4입니다.')
else:
    print('b는 2 또는 4가 아닙니다.')