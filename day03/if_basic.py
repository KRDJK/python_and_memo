
age = int(input('몇 살이세요?? '))

# 비교 연산자 : 2개의 값을 비교해서 참, 거짓을 표현.
# ( <, <=, >, >=, ==, != ) '='은 항상 다른 기호 오른쪽에 쓰기. 같냐고 물어볼거면 '=='
# !=는 다르다. 평소 수학에서 =에 / 하던거 ㅇㅇ

#if문에서 참, 거짓이 나오는 식을 만들어 준 후, :을 써준다. 이후에는 들여쓰기(스페이스바 4번) 해야함.
if age > 19:
    print('당신은 성인입니다.') #참일 경우, 실행되나, 거짓일 경우에는 실행되지 않음.
    print('주류를 구매할 수 있습니다!')

#print를 이 중간 if문 사이에 쓰면 안됨. 중간에 끊어 먹는 행위 (아래에 else가 없다면 상관없음.)

else: #종속코드는 들여쓰기가 되어있는 코드의 수로 확인 가능. if와 else의 종속코드가 같을 필요는 없음.
    print('당신은 미성년자입니다.')
    print('주류 구매가 불가능합니다!')

print('안녕히 가세요!')

# else: <-- o,x 경우처럼 겹쳐서 true가 있는 경우가 아니면, else를 사용할 수 있음.
# if 뒤에는 식을 써주어야 하나, else는 식을 쓰는 것이 아님.
# 앞의 if에 대한 o,x 퀴즈 경우의 무조건 반대의 결과가 나올 경우, else로 쓰고 식 쓰지 않음.
# 100번째 로그인한 경우, 스타벅스를 주고 그 이전엔 아무것도 안주면 else는 아예 쓸 필요도 없음.
# else는 필수가 아님. 그러나 룰렛 형식이라 당첨, 비당첨이 있어서 비당첨을 알려줘야 한다면 else를 사용.
# 종속코드를 만들 때 들여쓴 만큼, 그 하위 종속코드에서도 똑같이 들여써야함.


# 총점 계산
# a = a1 + a2 + a3

# 평균 계산(2자리까지 반올림)
# avg = round(a / 3 , 2)