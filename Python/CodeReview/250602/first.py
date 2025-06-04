# 김가영
"""
짝수 제곱 리스트 구하기
정수 n이 주어질 때, 1부터 n까지의 수 중에서 짝수만 골라 제곱한 값들을
리스트로 만들어 return 하도록 solution 함수를 완성하세요.

[ 조건 ]
n은 1 이상 자연수,
리스트 컴프리헨션을 이용하여 작성,
return 형식: 짝수들의 제곱 리스트,
# 예시 입력
n = 10
# 예시 출력
[4, 16, 36, 64, 100]
"""
def solution(n):
    """
    1부터 n까지의 정수 중 짝수만 골라 제곱한 값을 리스트로 반환
    
    매개변수 : n (int): 1 이상의 자연수

    반환값: List[int]: 짝수들의 제곱으로 구성된 리스트
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            square = i ** 2
            result.append(square)

    return result
    # return [i**2 for i in range(1, n+1) if i % 2 == 0]
print(solution(10))