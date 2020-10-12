'''

이 과제에서는 슈퍼마켓에서 주로 사용되는 기능들을 간단히 구현해 보겠습니다.
1. 슈퍼마켓 잔돈 계산하기: 상품 가격과 받은 금액을 이용해 잔돈을 출력하십시오.
2. 슈퍼마켓 브랜드 검색기: 아래의 라면 이름에서 회 명을 분리하시오.

'''


#1 잔돈 계산하기: 물건 가격이 담긴 price 변수와 받은 금액 수인 money를 이용해 돌려줘야 하는 1000원, 500원, 100원, 50원, 10원 수를 순서대로 출력하시오.

price = 13960
money = 15000

leftover = money - price

print(leftover)

thousand = leftover // 1000
leftover = leftover % 1000

fiveH = leftover // 500
leftover = leftover % 500

hundred = leftover // 100
leftover = leftover % 100

fifty = leftover // 50
leftover = leftover % 50

#여기에 코드

print("1000원 권:", thousand)
print("500원:", fiveH)
print("100원:", hundred)
print("50원:", fifty)
print("10원:",leftover)


#2. 회사 이름 출력하기: 다음은 다양한 라면 이름이 있습니다. 각 라면의 회사명을 출력하시오.

ramen1 = "농삼 나팔라면"
ramen2 = "오뚝이 삼평라면"

#여기에 코드

print("나팔라면 제조회사:", ramen1[:-5])
print("삼평라면 제조회사:", ramen2[:-5])