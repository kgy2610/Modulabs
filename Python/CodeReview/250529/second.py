# 배주완
'''
1. 간단한 은행 계좌 클래스
BankAccount 클래스를 만들어서 다음 기능을 구현하세요.

📌 조건:,
생성 시 이름과 초기 잔액을 입력받음
deposit(amount) 메서드: 잔액에 돈을 입금
withdraw(amount) 메서드: 잔액에서 돈을 출금
출금하려는 금액이 잔액보다 많으면 "잔액 부족" 출력
check_balance() 메서드: 현재 잔액 출력

====================================================
예시출력
acc = BankAccount("주완", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()   # 출력: 현재 잔액은 1200원입니다.
acc.withdraw(2000)    # 출력: 잔액 부족
====================================================
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name # 계좌 주인 이름
        self.balance = balance # 초기 잔액
    
    def deposit(self, amount):
        self.balance += amount  # 잔액 + 입금액
    
    def withdraw(self, amount):
        if amount > self.balance: # 출금액 > 잔액 
            print("잔액 부족")
        else: # 출금액 < 잔액
            self.balance -= amount # 잔액에서 출금
    
    def check_balance(self):
        print(f"현재 잔액은 {self.balance}원입니다.")

acc = BankAccount("주완", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()   # 출력: 현재 잔액은 1200원입니다.
acc.withdraw(2000)    # 출력: 잔액 부족


'''
2. 온라인 쇼핑 장바구니 클래스,
ShoppingCart 클래스를 만들어 다음 기능을 구현하세요.

📌 조건:,
생성 시 빈 장바구니를 리스트로 준비,
add_item(item_name, price) 메서드: 장바구니에 항목 추가,
total_price() 메서드: 장바구니 안 항목들의 총 가격 출력,
show_items() 메서드: 장바구니에 들어간 물건 이름과 가격 출력
'''
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name, price):
        self.items.append({
            "name": item_name,
            "price" : price
            })
    
    def total_price(self):
        total = sum(item["price"] for item in self.items)
        print(f"총 가격은 {total}원입니다.")
    
    def show_items(self):
        if not self.items:
            print("장바구니가 비었습니다.")
        else:
            print("[ 장바구니 ]")
            for item in self.items:
                print(f"- {item['name']} : {item['price']}원")

cart = ShoppingCart()

cart.add_item("사과", 1000)
cart.add_item("바나나", 1500)
cart.add_item("딸기", 3000)

cart.show_items()
cart.total_price()