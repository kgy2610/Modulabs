def mysum(a, b):
    return a + b * 10


# 위치 인자 (Positioinal Argument)
print(mysum(1, 2))  # 21
print(mysum(2, 1))  # 12

# 키워드 인자 (Keyword Argument)
print(mysum(b=2, a=1))  # 21

# 위치 인자가 키워드 인자보다 먼저 지정되어야 합니다.