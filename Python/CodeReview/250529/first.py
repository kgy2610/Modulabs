# 김가영
'''
1. 홀수의 평균 구하기
정수 n 이 주어질 때, n 이하의 홀수들의 평균을 구해서 return 하도록 solution 함수를 완성하세요.

[ 조건 ]
- n은 1 이상의 자연수,
- 평균은 소수점 이하 첫째 자리까지 출력(소수점 자리 반올림),

[ 풀이 방식 ]
리스트 컴프리헨션과 sum()/ len()을 이용하여 구하기
===========================
# 예시 입력
n = 10

# 예시 출력
5.0  # 1, 3, 5, 7, 9의 평균
===========================
'''
# 방법 1
def solution(n):
    odd_num = [i for i in range(1, n+1) if i % 2 == 1]
    ave = sum(odd_num) / len(odd_num)
    return round(ave, 1) # round() : 반올림

print(solution(10))

# 방법 2
def solution(n):
    total = 0
    count = 0

    for i in range(1, n+1):
        if i % 2 == 1:
            total += i
            count += 1
    ave = total / count
    return round(ave, 1)

print(solution(10))


'''
2. 최고 점수 학생 찾기
학생 이름과 점수가 담긴 딕셔너리 scores가 주어질 때, 가장 점수가 높은 학생의 이름을 return 하도록 solution 함수를 완성하세요.

[ 조건 ]
딕셔너리의 key는 문자열(이름), value는 정수(점수),
최고 점수를 받은 학생이 여럿일 경우 아무나 리턴,

[ 풀이 방식 ]
max() 함수와 lambda를 사용하여 구하기
======================================================
# 예시 입력
scores = {"철수": 85, "영희": 92, "민수": 78, "영지": 88}

# 예시 출력
"영희"
======================================================
'''
# 방법 1
def solution(scores):
    best = max(scores.items(), key=lambda x: x[1])
    return best[0]  # 이름만 반환

# 방법 2
def solution(scores):
    maxSc = -1 # 비교값
    maxName = ""
    
    for name, score in scores.items():
        if score > maxSc:
            maxSc = score
            maxName = name
    return maxName

scores = {"철수": 85, "민수": 92, "영희": 92, "영지": 88}
print(solution(scores))