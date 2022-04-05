#상품의 이름         !!#ctrl+스페이스바 활용
product_name = input('상품명을 입력하세요: ')
#상품의 가격
price = int(input('원가를 입력하세요: ')) #int로 형변환을 한거였음(day02기준)

#할인가격
discount = price - price * 0.1

#메세지 출력
print(f'{product_name}의 할인가격은 {discount}원입니다.')
#{}는 변동되는 데이터가 들어갈 때 사용. ' 앞에 f 넣기
print(f'{product_name}의 원가는 {price}원이며, 할인가격은 {discount}원입니다.')
