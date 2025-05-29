# 최은빈
'''
1. 짝수의 합
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
(두 가지 방법을 사용해서 풀어보세요.)

1) 반복문 사용
2) sum()과 range() 사용 

Q. 어떤 방법이 메모리를 더 아낄 수 있을까?
'''
# 방법1
# def solution(n):
#     total = 0
#     for i in range(n + 1):
#         if i % 2 == 0:
#             total += i
#     return total


# 방법2
def solution(n):
    return sum(range(0, n + 1, 2))

# 출력
print(solution(10))

# 어떤 방법이 메모리를 더 아낄 수 있을까?
# 답)
# 둘 다 비슷한 메모리 사용량.
# 굳이 따지자면 for문의 메모리 사용량이 더 적음


'''
중복된 숫자 개수,
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
(두 가지 방법을 사용해서 풀어보세요.)

1) count 사용 
2) Counter사용 

Q. count와 Counter는 모두 데이터 안에 있는 값의 개수를 셀 수 있어
그렇다면 각각 어떤 상황에서 써야 메모리를 더 아낄 수 있을까?
'''
# 방법1
# def solution(array, n):
#     return array.count(n)

# array = [1, 2, 3]
# n = 2
# print(solution(array, n))

# 방법2
from collections import Counter

array = [1, 2, 2, 3, 3, 3]
n = 3
def solution(array, n):
    counter = Counter(array)
    return counter[n]
print(solution(array, n))


# count와 Counter는 모두 데이터 안에 있는 값의 개수를 셀 수 있어
# 그렇다면 각각 어떤 상황에서 써야 메모리를 더 아낄 수 있을까?

# 답)
# count -> 딱 하나의 값만 셀 때
# counter -> 여러 값의 개수를 한 번에 많이 셀 때