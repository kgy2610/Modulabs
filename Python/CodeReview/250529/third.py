# 심희현
'''
1. 학생 성적 관리 프로그램
- 딕셔너리 활용 : 학생 이름을 키(key), 점수를 값(value)으로 저장
- 리스트 컴프리헨션 대신 반복문 : 조건에 맞는 학생 필터링,
- sorted() 함수 : key=lambda x: x[1]로 점수 기준 정렬, reverse=True로 내림차순,
- enumerate() : 순위 매기기에 활용

주요 포인트:
sum(students.values())로 모든 점수의 합 계산
딕셔너리의 .items()로 (이름, 점수) 튜플 형태로 접근,
람다 함수 lambda x: x[1] 로 튜플의 두 번째 요소(점수) 기준 정렬
'''
def student_grade_manager():
    # 학생 데이터 초기화
    students = {}
    student_data = [("김철수",85),("이영희",92),("박민수",78),("최지영",88)]
    #1. 학생 추가
    for name, score in student_data:
        students[name] = score

    #2. 전체 학생의 평균 점수 계산
    total = sum(students.values())
    ave = total / len(students)
    print(f"전체 평균 점수 : {round(ave, 1)}점")

    #3. 80점 이상인 학생들만 출력
    print("\n[ 80점 이상 학생 ]")
    for name, score in students.items():
        if score >= 80:
            print(f"- {name}: {score}점")

    #점수 순으로 정렬(내림차순)
    print("\n[ 학생 순위(내림차순) ]")
    sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    for rank, (name, score) in enumerate(sorted_students, start=1):
        print(f"{rank}등: {name} ({score}점)")

#실행
student_grade_manager()


'''
2. 1의 갯수 반환

문제 설명
주어진 리스트의 값 중 1의 갯수를 반환하는 solution 함수를 완성해주세요.

제한 사항
- 0 ≤ 리스트의 길이 ≤ 10
- 1 ≤ 리스트 안의 수 ≤ 10000
- 들어온 리스트의 값은 정수로 되어 있습니다.
- 리스트의 길이가 0인경우 0을 반환해주세요.
'''
def solution(lst):
    if not lst:
        return 0
    
    count = 0
    for num in lst:
        count += str(num).count("1")
    return count

print(solution([11, 123, 41]))