print(5+5)
print('안녕하세요')
print(54/84*100)

A, B, C = map(int, input().split())
print((A + B) % C)
print((A % C) + (B % C) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

#위에는 틀린, 아래는 맞음 괄호의 갯수가 다름.

A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)