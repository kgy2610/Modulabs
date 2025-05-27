# 테스트 TransactionManager 클래스
class TransactionManager:
    def __init__(self):
        # 계좌번호별 잔액을 가상의 딕셔너리로 저장
        self.balances = {
            "1001": 10000,
            "1002": 5000,
        }

    def withdraw(self, account_no, amount):
        if account_no not in self.balances:
            print("계좌 없음")
            return False
        if self.balances[account_no] < amount:
            print("잔액 부족")
            return False
        self.balances[account_no] -= amount
        print(f"{account_no} 출금: {amount}원 (잔액: {self.balances[account_no]}원)")
        return True

    def deposit(self, account_no, amount):
        if account_no not in self.balances:
            self.balances[account_no] = 0
        self.balances[account_no] += amount
        print(f"{account_no} 입금: {amount}원 (잔액: {self.balances[account_no]}원)")