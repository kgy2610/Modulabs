import os
import json

class TransferManager:
    def __init__(self):
        # 테스트 코드 
        from TransactionManager import TransactionManager

        self.transfers_file = "data/transfers.json"
        self.otp_file = "data/otp.json"

        # 테스트 코드 
        self.transaction = TransactionManager()

    # 테스트 코드 
    def withdraw(self, acc, amt):
        return self.transaction.withdraw(acc, amt)

    # 테스트 코드 
    def deposit(self, acc, amt):
        return self.transaction.deposit(acc, amt)

    def verify_recipient(self, account_no):
        return account_no in self.transaction.balances
    
    # 계좌 이체 함수
    def transfer(self, from_acc, to_acc, amount):
        # 송금 계좌 존재 확인 
        if not self.verify_recipient(to_acc):
            print("존재하지 않는 계좌입니다.")
            return

        # 잔액 확인 및 출금
        if not self.withdraw(from_acc, amount):
            print("잔액이 부족합니다.(출금 실패)")
            return
        
        # 입금
        self.deposit(to_acc, amount)

        # 내역 저장
        self.record_transfer_history(from_acc, to_acc, amount)
        print("이체 완료")

    # OTP 생성 함수
    def generate_otp(self):
        import random, json
        otp = str(random.randint(100000, 999999))
        with open(self.otp_file, "w") as f:
            json.dump({"otp":otp}, f)
        print(f"OTP 발송됨: {otp}")
    
    def verify_otp(self, user_input):
        import json
        with open(self.otp_file, "r") as f:
            saved = json.load(f)
        return user_input == saved.get("otp")

    # 이체 기록 저장 함수
    def record_transfer_history(self, from_acc, to_acc, amount):
        import json, datetime, os
        record = {
            "from": from_acc,
            "to": to_acc,
            "amount": amount,
            "datetime": datetime.datetime.now().isoformat()
        }

        if os.path.exists(self.transfers_file):
            with open(self.transfers_file, "r") as f:
                history = json.load(f)
        else:
            history = []

        history.append(record)
        with open(self.transfers_file, "w") as f:
            json.dump(history, f, indent = 2)

# 테스트 코드
if __name__ == "__main__":
    tm = TransferManager()

    # 테스트용 계좌: 1001 → 1002로 3000원 이체
    tm.transfer("1001", "1002", 3000)