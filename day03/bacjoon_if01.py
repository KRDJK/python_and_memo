A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# ==를 맨 처음 if 문으로 시작하면 마지막을 else로 할 수 있음.\
# ==를 else 문에 사용하면 <=, >=, !=와 같은 경우가 나오기 때문에 안됨.
# 맞나??? 잘 모르겠음. 그냥 >, < 문구 이후 else 해도 나올거 같은뎅?
# 해보니 잘만 나옴