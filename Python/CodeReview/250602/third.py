# 최은빈 
"""
#1번 각도기
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각, 180도는 평각으로 분류합니다.
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를
return하도록 solution 함수를 완성해주세요.

예각 : 0 < angle < 90
직각 : angle = 90
둔각 : 90 < angle < 180
평각 : angle = 180 
"""
def solution(angle):
    if 0 < angle < 90:
        # 예각
        return 1
    elif angle == 90:
        # 직각 
        return 2
    elif 90 < angle < 180:
        # 둔각
        return 3
    elif angle == 180:
        # 평각
        return 4

print(solution(30)) # 예각
print(solution(90)) # 직각
print(solution(150)) # 둔각
print(solution(180)) # 평각

"""
#2번 배열 원소의 길이 
문자열 배열 strlist가 매개변수로 주어집니다.
strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ strlist 원소의 길이 ≤ 100
strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.

<입출력 예>
["We", "are", "the", "world!"] ->[2, 3, 3, 6]
["I", "Love", "Programmers."] -> [1, 4, 12]
"""
def solution(strlist):
    """
    for문으로 리스트에서 문자열을 하나씩 꺼냄,
    문자열 길이 계산 후
    리스트에 하나씩 추가
    """
    result = []
    for s in strlist:
        result.append(len(s))
    return result

# 리스트 컴프리헨션
def solution(strlist):
    return [len(s) for s in strlist]

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))

"""
#3번 
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

<제한사항>
sides의 원소는 자연수입니다.
sides의 길이는 3입니다.
1 ≤ sides의 원소 ≤ 1,000

<입출력 예>
[1,2,3] -> 2 
[3,6,2] -> 2
"""
def solution(sides):
    """
    오름차순 정렬, 가장 큰 정수가 맨 뒤 
    """
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([3, 4, 5]))
