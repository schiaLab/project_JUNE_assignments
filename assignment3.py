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


stock = ?


command = "슈퍼마켓에 온 걸 환영합니다. 무슨 작업이 필요하십니까? \n"
          "검색을 위해선 '검색'을, 결제를 위해선 '결제'를 입력해 주세요."


if command == ?:


    #여기에 코드


#추가 사실: Python은 독특하게 조건문 중 elif라는 것이 있습니다. 이것은 else + if로, 위의 if문 속 조건이 거짓일 때 실행되는 if문입니다. 이것도 일종의 if문
#이기 때문에, else와 다르게 조건을 붙여줘야 합니다.

elif command == ?:



else:

    print(??)

    #힌트: 사람은 실수하기 마련입니다. 특히 타이핑은요.