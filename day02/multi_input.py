#A = int(input())
#B = int(input())
#예제입력에서 세로로 나와있으면 이렇게 하는게 맞으나 가로로 1 2라고 되어있는 경우

#가로로 띄어쓰기 구분해서 한 줄에 입력받기

#A, B = map(int, input().split())
#print(A * B)
#C, D = map(int, input().split())
#print(C * D)

#A, B = map(int, input().split())
#print(A + B)

#A, B, C = map(int, input().split().split())
#print((A + B) % C)
#print((A % C) + (B % C) % C)
#print(A×B)%C
#print((A%C) × (B%C))%C


#ID = input()
#print(ID + '??!')

#이건 왜 틀렸다고 하는건지...
#A B, C = map(int, input(,).split())
#print((A + B) % C)
#print((A % C) + (B % C) % C)
#print((A*B)%C)
#print(((A%C) * (B%C))%C)


#10진수라서
#푸는 것도 중요하지만, 규칙을 만드려고 항상 시도해보기!
A = int(input())
B = int(input())
#C=A*(B // 1 % 10) = 10**0 % 10
#D = A*(B // 10 % 10) = 10**1 % 10
#E = A*(B // 100 % 10) = 10**2 % 10
#F = (C*10**0) + (D*10) + (E*100)
print(A*(B%10))
print(A*((B%100)//10))
print(A*(B//100))
print(A*B)
#연습문제
n1, n2 = map(int, input().split())
m1, m2 = map(int, input().split())
k1, k2 = map(int, input().split())

print(f'case #1: {n1 + n2}')
print(f'case #2: {m1 + m2}')
print(f'case #3: {k1 + k2}')

#연습문제2 안되는거 같은데..?
n1, n2 = map(int, input().split())
m1, m2 = map(int, input().split())
k1, k2 = map(int, input().split())
print(f'case #1: \'{n1} + {n2} = {n1+n2}')
print(f'case #2: \'{m1} + {m2} = {m1+m2}')
print(f'case #3: \'{k1} + {k2} = {k1+k2}')