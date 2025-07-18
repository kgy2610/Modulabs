## 파이썬 부트캠프 실습 문제 50제

"""
문제 1: 인사하기
사용자의 이름을 입력받아 "안녕하세요, [이름]님!" 형태로 출력하는 프로그램을 작성하세요.
"""
# name = str(input("이름을 입력하세요 : "))
# print(f"안녕하세요, {name}님!")

## ---------------------------------------------------------------------------

"""
문제 2: 에코 프로그램
사용자가 입력한 문자열을 그대로 세 번 반복하여 출력하는 프로그램을 작성하세요.
"""
# name = str(input("이름을 입력하세요 : "))
# print(f"{name} {name} {name}")

## ---------------------------------------------------------------------------

"""
문제 3: 나이 계산기
사용자의 출생연도를 입력받아 현재 나이를 계산하여 출력하는 프로그램을 작성하세요.
(현재 연도는 2025년으로 가정합니다)
"""
# year = int(input("출생연도를 입력하세요 : "))
# age = 2025 - year
# print(f"당신의 나이는 {age}세 입니다.")

## ---------------------------------------------------------------------------

"""
문제 4: 원 넓이 계산
반지름을 입력받아 원의 넓이(π×r²)를 계산하여 출력하는 프로그램을 작성하세요.
(π 값은 3.14로 가정합니다)
"""
# r = float(input("반지름을 입력하세요 : "))
# extent = 3.14 * r**2
# print(f"반지름이 {r}인 원의 넓이 : {extent}")

## ---------------------------------------------------------------------------

"""
문제 5: 여행 거리 계산
시속(km/h)과 시간(h)을 입력받아 총 이동 거리를 계산하는 프로그램을 작성하세요.
"""
# kmh, h = map(int, input("시속과 시간을 입력해주세요 : ").split())
# move = kmh * h
# print(f"총 이동거리 : {move}km")

## ---------------------------------------------------------------------------

"""
문제 6: 문장 합치기
첫번째 문장과 두번째 문장을 입력받아 하나로 합쳐서 출력하는 프로그램을 작성하세요.
"""
# a = input("첫 번째 문장을 입력해주세요 : ")
# b = input("두 번째 문장을 입력해주세요 : ")
# print(a + " " + b)

## ---------------------------------------------------------------------------

"""
문제 7: 인치-센티미터 변환
인치 값을 입력받아 센티미터로 변환하는 프로그램을 작성하세요. (1인치 = 2.54cm)
"""
# inch = float(input("인치 값을 입력해주세요 : "))
# cm = inch * 25.4
# if cm.is_integer() :
#     print(f"{inch:.0f}인치는 {int(cm)}센티미터입니다.")
# else :
#     print(f"{inch:.0f}인치는 {cm:.1f}센티미터입니다.")

## ---------------------------------------------------------------------------

"""
문제 8: 팁 계산기
식사 금액과 팁 비율(%)을 입력받아 팁 금액과 총 지불 금액을 계산하는 프로그램을 작성하세요.
"""
# cost, tip = map(int, input("식사금액과 팁 비율(%)을 입력하세요 : ").split())
# tAmount = cost * (tip / 100)
# total = cost + tAmount
# print(f"팁 금액 : {int(tAmount)}원 \n총 지불 금액 : {int(total)}원")

## ---------------------------------------------------------------------------

"""
문제 9: BMI 계산기
키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하는 프로그램을 작성하세요.
(BMI = 몸무게(kg) / (키(m)²))
"""
# cm, kg = map(int, input("키와 몸무게를 입력해주세요 : ").split())
# m = cm / 100
# bmi = kg / (m ** 2)
# print(f"BMI : {bmi:.2f}")

## ---------------------------------------------------------------------------

"""
문제 10: 다중 입력
여러 숫자를 공백으로 구분하여 입력받고, 첫 번째와 마지막 숫자를 출력하는 프로그램을 작성하세요.
"""
# num = list(map(int, input("숫자 다섯개를 입력해주세요 : ").split()))
# print(f"첫 번째 숫자 : {num[0]} \n마지막 숫자 : {num[-1]}")

## ---------------------------------------------------------------------------

"""
문제 11: 변수 교환
두 변수 a와 b의 값을 다중 할당을 사용하여 교환하는 프로그램을 작성하세요.
"""
# a, b = map(int, input("숫자 두 개를 입력하세요 : ").split())
# print(f"교환 전 : a = {a}, b = {b}")
# a, b = b, a
# print(f"교환 후 : a = {a}, b = {b}")

## ---------------------------------------------------------------------------

"""
문제 12: 문자열 정보 출력
문자열을 입력받아 길이와 첫 글자, 마지막 글자를 출력하는 프로그램을 작성하세요.
"""
# text = list(input("문장을 입력하세요 : "))
# print(f"문자열 길이 : {len(text)} \n첫 글자 : {text[0]} \n마지막 글자 : {text[-1]}")

## ---------------------------------------------------------------------------

"""
문제 13: 이니셜 만들기
이름의 성과 이름을 공백으로 구분하여 입력받아 이니셜을 출력하세요.
(예: "홍 길동" -> "H.G.")
"""
# eng_dict = {
#     "홍" : "H",
#     "길" : "G",
#     "동" : "D",
#     "김" : "K",
#     "가" : "G",
#     "영" : "Y"
# }
# fName, lName = map(str, input("성과 이름을 공백으로 구분하여 입력해주세요 : ").split())

# fEng = eng_dict.get(fName[0], "?")
# lEng = eng_dict.get(lName[0], "?")

# ini = f"{fEng.upper()}.{lEng.upper()}."
# print(f"이니셜 : {ini}")

## ---------------------------------------------------------------------------

"""
문제 14: 소수점 자릿수
실수를 입력받아 소수점 2자리까지 표시하는 프로그램을 작성하세요.
"""
# num = float(input("실수를 입력하세요 : "))
# print(f"{num:.2f}")

## ---------------------------------------------------------------------------

"""
문제 15: 나이 구간 판별
나이를 입력받아 "미성년자"(19세 미만), "청년"(19-34세), "중장년"(35-64세),
"노년"(65세 이상) 중 하나로 출력하는 프로그램을 작성하세요.
"""
# age = int(input("나이를 입력하세요 : "))
# if age < 19 :
#     print("미성년자")
# elif age <= 34 :
#     print("청년")
# elif age <= 64 :
#     print("중장년")
# else : 
#     print("노년")

## ---------------------------------------------------------------------------

"""
문제 16: 문자열 분석
문자열을 입력받아 공백 수, 숫자 수, 문자 수를 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을 입력하세요 : ")

# space_count = 0
# num_count = 0
# char_count = 0

# for ch in text :
#     if ch.isspace() :
#         space_count += 1
#     elif ch.isdigit() :
#         num_count += 1
#     else :
#         char_count += 1

# print(f"공백 수 : {space_count} \n숫자 수 : {num_count} \n문자 수 : {char_count}")

## ---------------------------------------------------------------------------

"""
문제 17: 참/거짓 변환
문제 설명
다양한 값을 불리언으로 변환한 결과를 출력하는 프로그램을 작성하세요.
"""
# val = [0, 1, "\"\"", "\"hello\"", "\"0\"", "\"False\""]

# for v in val :
#     print(f"{v} -> {bool(val)}")

## ---------------------------------------------------------------------------

"""
문제 18: 홀짝 판별
숫자를 입력받아 홀수인지 짝수인지 판별하는 프로그램을 작성하세요.
"""
# num = int(input("숫자를 입력하세요 : "))
# if num % 2 == 0 :
#     print(f"{num}은(는) 짝수입니다.")
# else :
#     print(f"{num}은(는) 홀수입니다.")

## ---------------------------------------------------------------------------

"""
문제 19: 문자열 분할
문장을 입력받아 쉼표(,)로 구분된 단어들로 분할하여 출력하는 프로그램을 작성하세요.
"""
# word = input("단어들을 공백으로 구분하여 입력하세요 : ").split()
# print(", ".join(word))

## ---------------------------------------------------------------------------

"""
문제 20: 온도 단위 변환기
온도와 단위(C/F)를 입력받아 다른 단위로 변환하는 프로그램을 작성하세요.
C는 섭씨, F는 화씨를 의미합니다. (화씨 = 섭씨 * 9/5 + 32, 섭씨 = (화씨 - 32) * 5/9)
"""
# tem, unit = input("온도와 단위(C/F)를 입력해주세요 : ").split()
# tem = float(tem)

# if unit.upper() == 'C' :
#     C = (float(tem) - 32) * (5/9)
#     print(f"{tem:.2f}°C는 {C:.2f}°F입니다.")
# elif unit.upper() == 'F' : 
#     F = (float(tem) * (9/5) + 32)
#     print(f"{tem:.2f}°F는 {F:.2f}°C입니다.")
# else :
#     print("잘못된 입력입니다.")

## ---------------------------------------------------------------------------

"""
문제 21: 대소문자 변환
문자열을 입력받아 대문자, 소문자, 첫 글자만 대문자로 변환하여 출력하는 프로그램을 작성하세요.
"""
# text = input("영어로 된 문장을 입력해주세요 : ")
# print(f"대문자 : {text.upper()} \n소문자 : {text.lower()} \n첫 글자만 대문자 : {text.title()}")

## ---------------------------------------------------------------------------

"""
문제 22: 문자열 슬라이싱
문자열을 입력받아 앞에서 3글자, 뒤에서 3글자, 그리고 거꾸로 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을 입력해주세요 : ")
# print(f"앞 3글자 : {text[0:3]} \n뒤 3글자 : {text[-3:]} \n거꾸로 : {text[::-1]}")

## ---------------------------------------------------------------------------

"""
문제 23: 단어 위치 찾기
문장과 찾을 단어를 입력받아 해당 단어의 위치(인덱스)를 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을을 입력해주세요 : ")
# word = input("찾을 단어를 입력해주세요 : ")

# index = text.find(word)

# if index != -1 : # 문장에 찾고자하는 단어가 있을 때
#     print(f"단어 '{word}'의 위치 : {index}")
# else :
#     print(f"단어 '{word}'을(를) 찾을 수 없습니다.")

## ---------------------------------------------------------------------------

"""
문제 24: 문자 교체
문장과 교체할 문자, 새 문자를 입력받아 모든 교체할 문자를 새 문자로 바꾸는 프로그램을 작성하세요.
"""
# text = input("문장을 입력해주세요 : ")
# chWord = input("교체할 문자를 입력해주세요 : ")
# newWord = input("새 문자를 입력해주세요 : ")

# newText = text.replace(chWord, newWord)

# print(newText)

## ---------------------------------------------------------------------------

"""
문제 25: 문자 출현 횟수
문장과 찾을 문자를 입력받아 해당 문자가 몇 번 등장하는지 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을 입력해주세요 : ")
# word = input("찾을 단어를 입력해주세요 : ")

# count = text.count(word)

# print(f"문자 '{word}'은(는) 총 {count}번 등장합니다.")

## ---------------------------------------------------------------------------

"""
문제 26: 이메일 유효성 검사
간단한 이메일 주소 유효성 검사(@ 포함 여부)를 하는 프로그램을 작성하세요.
"""
# mail = input("이메일을 입력하세요 : ")

# if "@" in mail :
#     print("유효한 이메일 주소입니다.")
# else :
#     print("유효하지 않은 이메일 주소입니다.")

## ---------------------------------------------------------------------------

"""
문제 27: 문자열 패딩
문자열과 원하는 길이를 입력받아, 원하는 길이가 될 때까지 '*'로 오른쪽을 채우는 프로그램을 작성하세요.
"""
# text = input("문자열을 입력하세요 : ")
# le = int(input("길이를 입력하세요 : "))
# pd_text = text.ljust(le, '*')

# print(pd_text)

## ---------------------------------------------------------------------------

"""
문제 28: 문자열 중앙 문자
문자열을 입력받아 중앙에 위치한 문자(들)를 출력하는 프로그램을 작성하세요.
(홀수 길이면 가운데 1글자, 짝수 길이면 가운데 2글자)
"""
# text = input("문자열을 입력해주세요 : ")
# le = len(text)
# mid = le // 2

# if le % 2 == 0 :
#     result = text[mid - 1 : mid + 1]
# else :
#     result = text[mid]

# print("중앙 문자 : ", result)

## ---------------------------------------------------------------------------

"""
문제 29: 특수문자 제거
문자열에서 특수문자(., !, ? 등)를 제거하는 프로그램을 작성하세요.
"""
# text = input("문자열을 입력하세요 : ")
# remove = ['.', ',', '!', '?']

# for re in remove :
#     text = text.replace(re,'')

# print(text)

## ---------------------------------------------------------------------------

"""
문제 30: 이스케이프 시퀀스 연습
이스케이프 시퀀스를 사용하여 따옴표, 탭, 줄바꿈이 포함된 문자열을 출력하는 프로그램을작성하세요.
"""
# print("그녀가 말했다: \"안녕하세요!\" \n이름 나이 직업 \n홍길동 \t30 \t개발자 \n안녕! \n반가워요!")

## ---------------------------------------------------------------------------

"""
문제 31: 사칙연산 계산기
두 수와 연산자(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.
"""
# a = int(input("첫 번째 숫자를 입력하세요 : "))
# b = int(input("두 번째 숫자를 입력하세요 : "))
# op = input("연산자(+, -, *, /)를 입력해주세요 : ")

# if op == '+' :
#     print(f"{a} + {b} = {a + b}")
# elif op == '-' :
#     print(f"{a} - {b} = {a - b}")
# elif op == '*' :
#     print(f"{a} * {b} = {a * b}")
# elif op == '/' :
#     print(f"{a} / {b} = {a / b}")
# else :
#     print("잘못된 입력입니다.")

## ---------------------------------------------------------------------------

"""
문제 32: 세금 계산기
금액과 세율(%)을 입력받아 세금과 세후 금액을 계산하는 프로그램을 작성하세요.
"""
# amount = int(input("금액을 입력하세요 : "))
# rate = int(input("세율(%)를 입력하세요 : "))

# tax = amount * (rate / 100)
# afterAmount = amount - tax

# print(f"세금 : {tax:.1f} \n세후 금액 : {afterAmount:.1f}")

## ---------------------------------------------------------------------------

"""
문제 33: 논리 연산 테이블
두 불리언 값(True 또는 False)을 입력받아 AND, OR, NOT 연산 결과를 출력하는 프로그램을 작성하세요.
"""
# a = input("불리언 값을 입력하세요 (True 또는 False) : ") == "True"
# b = input("불리언 값을 입력하세요 (True 또는 False) : ") == "True"

# print(f"{a} AND {b} = {a and b} \n{a} OR {b} = {a or b} \nNOT {a} = {not a} \nNOT {b} = {not b}")

## ---------------------------------------------------------------------------

"""
문제 34: 할인 계산기
원래 가격과 할인율(%)을 입력받아 할인 금액과 최종 가격을 계산하는 프로그램을 작성하세요.
"""
# amount = int(input("원가를 입력해주세요 : "))
# sale = int(input("할인율(%)을 입력해주세요 : "))

# saleAmount = amount * (sale / 100)
# totalAmount = amount - saleAmount

# print(f"할인 금액 : {saleAmount:.1f} \n최종 가격 : {totalAmount:.1f}")

## ---------------------------------------------------------------------------

"""
문제 35: 큰 수 판별
세 개의 숫자를 입력받아 가장 큰 수를 출력하는 프로그램을 작성하세요.
"""
# a, b, c = map(int, input("세 개의 숫자를 입력해주세요 : ").split())

# biggest = max(a, b, c)
# print(f"가장 큰 수 : {biggest}")

## ---------------------------------------------------------------------------

"""
문제 36: 윤년 판별
연도를 입력받아 윤년인지 아닌지 판별하는 프로그램을 작성하세요.
(윤년: 4로 나누어 떨어지고 100으로 나누어 떨어지지 않거나, 400으로 나누어 떨어지는해)
"""
# year = int(input("연도를 입력하세요 : "))

# if (year % 4 == 0 and year % 100 != 0) or year % 2 == 0 :
#     print(f"{year}년은 윤년입니다.")
# else :
#     print(f"{year}년은 윤년이 아닙니다.")

## ---------------------------------------------------------------------------

"""
문제 37: 문자열 포함 여부
두 문자열을 입력받아 첫 번째 문자열에 두 번째 문자열이 포함되어 있는지 확인하는 프로그램을 작성하세요.
"""
# a = input("문자열을 입력해주세요 : ")
# b = input("찾을 문자열을 입력해주세요 : ")

# if b in a :
#     print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있습니다.")
# else :
#     print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있지 않습니다.")

## ---------------------------------------------------------------------------

"""
문제 38: 조건부 출력
점수를 입력받아 90점 이상이면 "A", 80점 이상이면 "B",
70점 이상이면 "C", 60점 이상이면 "D",
그 미만이면 "F" 등급을 출력하는 프로그램을 작성하세요.
"""
# score = int(input("점수를 입력하세요 : "))

# if score >= 90 :
#     print("학점 : A")
# elif score >= 80 :
#     print("학점 : B")
# elif score >= 70 :
#     print("학점 : C")
# elif score >= 60 :
#     print("학점 : D")
# else :
#     print("학점 : F")

## ---------------------------------------------------------------------------

"""
문제 39: 자릿수 합계
양의 정수를 입력받아 각 자릿수의 합을 계산하는 프로그램을 작성하세요.
"""
# num = input("정수를 입력하세요 : ")
# sum = sum(int(n) for n in num)
# print(f"자릿수 합계 : {sum}")

## ---------------------------------------------------------------------------

"""
문제 40: 복합 조건
나이와 회원 여부(Y/N)를 입력받아 입장료를 출력하는 프로그램을 작성하세요.
- 성인(19세 이상) & 비회원: 10000원
- 성인(19세 이상) & 회원: 8000원
- 청소년(19세 미만): 5000원
"""
# age = int(input("나이를 입력하세요 : "))
# member = input("회원여부를 입력하세요(Y/N) : ")

# if age > 19 and member == 'N' or member == 'n' :
#     print("입장료 : 10,000원")
# elif age > 19 and member == 'Y' or member == 'y' :
#     print("입장료 : 8,000원")
# elif age < 19 :
#     print("입장료 : 5,000원")

## ---------------------------------------------------------------------------

"""
문제 41: 비밀번호 강도 검사
비밀번호를 입력받아 길이가 8자 이상이고 문자와 숫자가 모두 포함되어 있는지 확인하는 프로그램을 작성하세요.
"""
# pwd = input("비밀번호를 입력하세요 : ")
# alCheck = any(char.isalnum() for char in pwd)
# numCheck = any(char.isdigit() for char in pwd)

# if alCheck and numCheck:
#     print("안전한 비밀번호입니다.")
# else :
#     print("문자 또는 숫자가 부족합니다.")

# any() : 조건을 만족하는 항목이 하나라도 있으면 True
# isdigit() : 숫자인지 확인
# isalpha() : 알파벳인지 확인
# isalnum() : 알파벳 또는 숫자인지 확인 // 알파벳과 숫자 중 하나만 있어도 True
# isspae() : 공백 문자인지 확인

## ---------------------------------------------------------------------------

"""
문제 42: 단어 뒤집기
문제 설명
여러 단어로 이루어진 문장을 입력받아 각 단어를 뒤집어서 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을 입력하세요 : ").split()
# reverse = [word[::-1] for word in text]
# result = ' '.join(reverse)

# print(result)

## ---------------------------------------------------------------------------

"""
문제 43: 문자 카운터
문장을 입력받아 모음(a, e, i, o, u)과 자음의 개수를 출력하는 프로그램을 작성하세요.
"""
# text = input("문장을 입력하세요 : ")
# text = text.lower()

# vowel = 'aeiou'

# vCount = 0
# cCount = 0

# for ch in text :
#     if ch.isalpha() :
#         if  ch in vowel:
#             vCount += 1
#         else :
#             cCount += 1

# print(f"자음 개수 : {vCount} \n모음 개수 : {cCount}")

## ---------------------------------------------------------------------------

"""
문제 44: 근삿값 계산
실수를 입력받아 가장 가까운 정수를 계산하는 프로그램을 작성하세요.
"""
# num = float(input("실수를 입력하세요 : "))
# print(round(num))

## ---------------------------------------------------------------------------

"""
문제 45: 날짜 유효성 검사
연월일(YYYY-MM-DD 형식)을 입력받아 유효한 날짜인지 검사하는 프로그램을 작성하세요.
"""
# year, month, day = map(int, input("날짜를 입력하세요(YYYY-MM-DD) : ").split('-'))
# leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# if month == 2 :
#     maxDay = 29 if leap else 28
# elif month in [4, 6, 9, 11] :
#     maxDay = 30
# elif month in [1, 3, 5, 7, 8, 10, 12] :
#     maxDay = 31
# else : 
#     print("유효하지 않는 날짜입니다.")

# if 1 <= day <= maxDay :
#     print("유효한 날짜입니다.")
# else :
#     print("유효하지 않는 날짜입니다.")

## ---------------------------------------------------------------------------

"""
문제 46: 파일 확장자 추출
파일명을 입력받아 확장자를 추출하는 프로그램을 작성하세요. (예: "document.txt" -> "txt")
"""
# file = input("파일명과 확장자를 입력하세요 : ").split('.')
# extn = [word[::1] for word in file]
# print(f"확장자 : {extn[-1]}")

## ---------------------------------------------------------------------------

"""
문제 47: 문자열 압축
연속된 문자를 문자와 개수로 압축하는 프로그램을 작성하세요. (예: "aabbbcccc" -> "a2b3c4")
"""
# text = input("문자열을 입력하세요 : ")

# result = '' # 최종 결과
# pre = ''    # 이전 문자
# count = 0

# for ch in text :    # 문자열 반복문
#     if ch == pre :  # 반복 중, 이전 문자와 같으면
#         count += 1  # 갯수 증가
#     else :
#         if pre != '' :  # 이전 문자가 존재한다면
#             result += pre + str(count)  # 이전 문자와 갯수를 결과에 저장
#         pre = ch    # 이전 문자를 현재 문자로 바꾸고
#         count = 1   # 갯수는 다시 1부터 시작

# result += pre + str(count)  # 마지막 문자
# ## -> 마지막 문자는 for문에서 처리되지 않기 때문에 별도 처리

# print(result)

## ---------------------------------------------------------------------------

"""
문제 48: 팰린드롬 검사
입력된 문자열이 앞뒤로 읽어도 같은 팰린드롬인지 검사하는 프로그램을 작성하세요.
"""
# text = input("문자열을 입력하세요 : ").split()
# reText = [word[::-1] for word in text]

# if text == reText :
#     print(f"{text}은(는) 팰린드롬입니다.")
# else :
#     print(f"{text}은(는) 팰린드롬이 아닙니다.")

## ---------------------------------------------------------------------------

"""
문제 49: 간단한 암호화
문자열을 입력받아 각 문자를 3글자씩 뒤로 미루는 시저 암호로 암호화하는 프로그램을 작성하세요.
(예: 'A' -> 'D', 'Z' -> 'C')
"""
# text = input("문자열을 입력하세요 : ")
# result = ''

# for ch in text :    # 입력 문자열 반복문
#     if 'a' <= ch <= 'z' : # 만약 소문자라면
#         result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
#     elif 'A' <= ch <= 'Z' : #만약 대문자라면
#         result += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
#     else :              # 알파벳이 아니면
#         result += ch    # 그대로 추가

# print(f"암호화 : {result}")

## ---------------------------------------------------------------------------

"""
문제 50: IP 주소 검증
IP 주소를 입력받아 각 부분이 0-255 사이의 숫자인지 검증하는 프로그램을 작성하세요.
"""
ip = input("IP주소를 입력하세요 : ").split('.')

if len(ip) != 4 :
    print("유효하지 않은 IP 주소입니다.")
else :
    valid = True

    for part in ip :
        if not part.isdigit() : # 숫자가 아닐 때
            valid = False
            break
        num = int(part)
        if num < 0 or num > 255 : # 0~255 범위를 벗어날 때
            valid = False
            break
    
    if valid :
        print("유효한 IP 주소입니다.")
    else : 
        print("유효하지 않은 IP 주소입니다.")