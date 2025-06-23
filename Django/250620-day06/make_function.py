# 일급 함수를 지원하는 언어 : 파이썬, 자바스크립트 등
def make_function():
    # 지역변수(local variable)
    base = 10 # 매 make_function 호출 시마다 생성
    
    # 함수를 동적으로 생성.
    # func = lambda number: number + base

    def func(number):
        return number + base
    
    return func

ret1 = make_function()
print(ret1(1))

ret2 = make_function()
ret3 = make_function()