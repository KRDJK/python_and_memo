user_name = input('이름: ')
user_age = int(input('나이: '))
user_born_year = 2022 - user_age + 1 #식 정리 하지 않는게 중요! 코드에선 의도파악이 중요. 2022가 올해인것과 추가로 +1이 한국 나이를 반영한 것을 쉽게 파악 가능.
print(f'{user_name}님은 {user_born_year}년생이시군요!')
