# 배주완
"""
[문제1]음식 주문 시스템 만들기,
🍔 문제 설명,
MenuItem 클래스와 Order 클래스를 만들어
간단한 음식 주문 시스템을 구현해보세요.

📌 조건
🔸 클래스: MenuItem
속성: 이름(name), 가격(price)
__str__() 사용 시 "김치찌개 - 7000원"처럼 출력

🔸 클래스: Order,
속성: 음식 목록 (리스트로 관리),
메서드:
add_item(item) - 메뉴를 주문 목록에 추가
total_price() - 전체 가격 계산
print_order() - 주문한 항목과 총합 출력

---

🎯 예시 실행
python
복사편집
item1 = MenuItem("김치찌개", 7000)
item2 = MenuItem("불고기", 9000)

order = Order()
order.add_item(item1)
order.add_item(item2)
order.print_order()

출력:
yaml
복사편집
김치찌개 - 7000원
불고기 - 9000원
총합: 16000원
"""
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def __str__(self):
#         return f"{self.name} - {self.price}원"

# class Order:
#     def __init__(self):
#         # 음식 목록을 저장할 리스트
#         self.items = []
    
#     def add_item(self, item):
#         # 음식 추가
#         self.items.append(item)

#     def total_price(self):
#         # 음식 가격 합계 계산
#         return sum(item.price for item in self.items)

#     def print_order(self):
#         # MenuItem 클래스의 str 함수 호출
#         for item in self.items:
#             print(item)
#         print(f"총합 : {self.total_price()}원")

# item1 = MenuItem("김치찌개", 7000)
# item2 = MenuItem("불고기", 9000)

# order = Order()
# order.add_item(item1)
# order.add_item(item2)
# order.print_order()


"""
[문제2]온라인 강의 플랫폼 시스템
📌 요구사항:
Course, Student, Platform 클래스를 만들어 다음과 같은 기능을 구현하세요.

👨‍🏫 클래스: Course
속성: 강의 제목, 강사 이름, 수강생 명단
메서드:
add_student(student) → 수강생 추가
remove_student(student) → 수강생 제거
list_students() → 수강생 목록 출력

---

👤 클래스: Student
속성: 이름, 이메일
__str__()로 "이름 (이메일)" 출력

---

💻 클래스: Platform
강의들을 담는 리스트 self.courses
메서드:
add_course(course) → 강의 추가
list_courses() → 강의 제목 리스트 출력

---

🎯 예시 사용:
python
복사편집
s1 = Student("김철수", "kim@naver.com")
s2 = Student("이영희", "lee@gmail.com")

c1 = Course("파이썬 입문", "홍강사")
c1.add_student(s1)
c1.add_student(s2)

p = Platform()
p.add_course(c1)
p.list_courses()   # ['파이썬 입문']

c1.list_students()
# 출력:
# 김철수 (kim@naver.com)
# 이영희 (lee@gmail.com)
"""
# class Student:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
    
#     def __str__(self):
#         # 출력 예시 : 김철수 (kim@naver.com)
#         return f"{self.name} ({self.email})"

# class Course:
#     def __init__(self, title, instructor):
#         self.title = title
#         self. instructor = instructor
#         # 수강생 명단
#         self.students = []
    
#     def add_student(self, student):
#         self.students.append(student)
    
#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
    
#     def list_students(self):
#         # Student 클래스의 __str__ 호출
#         for student in self.students:
#             print(student)

# class Platform:
#     def __init__(self):
#         # 강의 저장 
#         self.courses = []
    
#     def add_course(self, course):
#         self.courses.append(course)

#     def list_courses(self):
#         titles = [course.title for course in self.courses]
#         print(titles)

# s1 = Student("김철수", "kim@naver.com")
# s2 = Student("이영희", "lee@gmail.com")

# c1 = Course("파이썬 입문", "홍강사")
# c1.add_student(s1)
# c1.add_student(s2)

# p = Platform()
# p.add_course(c1)
# p.list_courses()  # ['파이썬 입문']
# c1.list_students()

"""
위니브 회의 시간표 정렬
[ 문제 설명 ]
- 위니브 A 회의실에는 회의 시간 목록이 AM/PM 형식으로 표현되어 있습니다.
- 이 시간들을 24시간제로 변환한 뒤, 오름차순으로 정렬하는 코드를 작성해주세요.
- 시간은 'HH:MM AM' 또는 'HH:MM PM' 형식으로 주어지며,
12시간제를 24시간제로 변환할 때 '12:00 AM'은 '00:00', '12:00 PM'은 '12:00'으로 변환합니다.

[ 제한 사항 ]
- 시간은 'HH:MM AM' 또는 'HH:MM PM' 형식으로 주어집니다.
- 'HH'는 01에서 12 사이, 'MM'은 00에서 59 사이입니다.
- 시간 목록에는 최소 1개에서 최대 100개의 시간이 주어집니다.

[ 입출력 예 ]
# 입력
['01:00 PM', '11:30 AM', '12:45 PM', '09:00 AM', '12:00 AM']
# 출력
['12:00 AM', '09:00 AM', '11:30 AM', '12:45 PM', '01:00 PM']

# 입출력 설명
주어진 시간을 24시간제로 변환하고 오름차순으로 정렬합니다.
예를 들어, '01:00 PM'은 24시간제로 '13:00'이 되고, '12:00 AM'은 '00:00'이 됩니다.
이러한 변환을 거쳐 정렬된 결과는 ['12:00 AM', '09:00 AM', '11:30 AM', '12:45 PM', '01:00 PM']가 됩니다.
"""
from datetime import datetime

def sort_meeting_times(times):
    # 1. AM/PM -> 24시간 형식으로 바꾸고, 튜플로 저장(24시간값, 기존값)
    converted = []
    for time in times:
        # 12시간제 -> datetime 객체
        # 1:00 PM -> datetime 객체로 변환 
        dt = datetime.strptime(time, "%I:%M %p")
        # 24시간값 문자열, 기존값 문자열
        # datetime 객체 -> '13:00' 같은 24시간 문자열 
        converted.append((dt.strftime("%H:%M"), time))
    
    # 2. 24시간 기준으로 정렬
    # 00:00, 09:00, 11:30, 12:45, 13:00 순서로 정렬
    # 현재 datetime 객체에는 24시간 문자열로 변환한 값이 있음 
    converted.sort(key=lambda x: x[0])

    # 3. AM/PM 형식 추출 후 결과 반환
    # 00:00 -> 12:00 AM 등으로 다시 변환환
    return [t[1] for t in converted]

times = ['01:00 PM', '11:30 AM', '12:45 PM', '09:00 AM', '12:00 AM']
result = sort_meeting_times(times)
print(result)