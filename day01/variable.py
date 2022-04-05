'''

'''
#variable = 변수
#데이터를 저장하는 공간
#개발자가 이름을 붙여서 사용
print(157+985)
lucky_number = 157+985 #<-- 이런게 변수 //이름은 내 맘대로 짓기
print(lucky_number*3)
print(lucky_number)
lucky_number = lucky_number*3 #컴퓨터에서 '='은 같다가 아니라 대입. 같으려면(equal) '==' !!! =의 좌항에는 문자만!!! 
print(lucky_number*2)
login_user_name = '홍길동' #변수의 이름은 간결하고, 명확하게 지을 것!! <- 띄어쓰기 x 일할 때 편하려면 더더욱!
login_user_name = '김철수' #이러면 위의 홍길동은 지워짐.
login_user_name2 = '김민수' #터미널엔 뜨지 않음. but, 나중에 출력하라고 시키면 보여줌.
print(login_user_name + ' 안녕?') #나중에 일괄변경이 가능!!
print('당신은 ' + login_user_name + '!')
print('내친구 '+ login_user_name +'~~')

print('Let\'s go') # '를 문자에 입력하고 싶으면 \\ 역 슬래시 활용
print('\\') # \를 하나 출력하고 싶으면 \\ 두 번!!

#our_living_planet = 'Earth' -> snake case >> PYTHON
#ourLivingPlanet = '지구' = camel case >>JAVA
#예약어는 안되지만(print, if 등등) 앞을 대문자로 바꿔서 쓰면 괜찮 ex) If = ~~~