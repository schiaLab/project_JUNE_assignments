'''

이번 과제에선 슈퍼마켓 내부의 물건을 찾아주고, 그 정보를 알려주는 프로그램과 함께, 결제하는 프로그램 또한 만들어보려 합니다.
다른 과제들에서 사용한 다양한 코드들을 중복하여 사용하여도 됩니다. 재고는 앞서 우리가 다루었던 재고 목록 만들기에서 만드신 것을 들고오셔도 되고, 새로 만드셔도 됩니다. 단, 새로 만드실 때는
반드시 제품 이름, 제품 재고수, 그리고 가격을 포함하여야 합니다.
그리고, 정보를 알려줄 때는 해당 제품의 재고가 있는지 없는지, 있다면 가격이 얼마인지 등을 알려주어야 합니다.
결제를 할 때에는 고객에게 돈과 제품명, 제품 개수를 입력으로 받아 거스름돈을 출력으로 줘야 합니다.
재고 목록은 구매에 따라 그 재고가 업데이트되어야 합니다. 재고가 -1 이하가 되지 않도록 조심하세요.
만약 가능하다면 프로그램이 특정 값이 입력되기 전까지 계속 새로운 고객을 받도록 해보세요.

힌트를 조금 드리겠습니다.

딕셔너리 뒤에 .get(key, A)를 사용하면, 해당 key값이 있으면 그 key에 대한 value를, 없으면 A를 출력합니다.


'''

시리얼 = [2, 5000]
치약 = [4, 2000]
감자칩 = [0, 1500]
볼펜 =[10, 700]

stock = {"시리얼": 시리얼, "치약": 치약, "감자칩": 감자칩, "볼펜": 볼펜}

while True:

    command = input("슈퍼마켓에 온 걸 환영합니다. 무슨 작업이 필요하십니까? \n"
              "검색을 위해선 '검색'을, 결제를 위해선 '결제'를 입력해 주세요.")


    if command == "검색":


        #여기에 코드

        name = input("찾으시는 제품 이름이 무엇입니까?: ")

        result = stock.get(name, [])

        if not result:

            print("판매하지 않는 상품입니다.")

            continue

        else:

            print("현재 해당 제품은 %d개 남아있으며, 하나당 %d원입니다."%(result[0], result[1]))

            continue





    #추가 사실: Python은 독특하게 조건문 중 elif라는 것이 있습니다. 이것은 else + if로, 위의 if문 속 조건이 거짓일 때 실행되는 if문입니다. 이것도 일종의 if문
    #이기 때문에, else와 다르게 조건을 붙여줘야 합니다.

    elif command == "결제":

        product = input("구매하실 제품명을 입력해 주세요: ")
        num = int(input("구매 개수를 입력해 주세요: "))

        result = stock[product]

        if num > result[0]:

            print("재고가 부족합니다.")

            continue

        else:

            price = result[1] * num

            money = int(input("총 %d원입니다 돈을 입력해 주세요: "%price))


            leftover = money - price

            print(leftover)

            tenT = leftover // 10000
            leftover = leftover % 10000

            fiveT = leftover // 5000
            leftover = leftover % 5000

            thousand = leftover // 1000
            leftover = leftover % 1000

            fiveH = leftover // 500
            leftover = leftover % 500

            hundred = leftover // 100
            leftover = leftover % 100

            fifty = leftover // 50
            leftover = leftover % 50

            print("다음은 거스름돈입니다.")
            print("10000원 권:", tenT)
            print("5000원 권:", fiveT)
            print("1000원 권:", thousand)
            print("500원:", fiveH)
            print("100원:", hundred)
            print("50원:", fifty)
            print("10원:", leftover)

            continue





    elif command == "강제종료":

        break


    else:

        print("잘못 입력하셨습니다. 다시 입력해 주십시오.")

        continue

    #힌트: 사람은 실수하기 마련입니다. 특히 타이핑은요.