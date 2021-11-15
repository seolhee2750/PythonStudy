"""
1차원 리스트 생성
"""

# 비어있는 리스트 생성
a = []
b = list()
print(a, b) # [] []

# 반복된 값 저장하여 생성
c = [0] * 10
print(c) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 다양한 타입을 한 리스트에 저장하는 것도 가능
d = ['a', 0, True]

# 범위 지정해서 생성
e = list(range(5))
f = list(range(1, 5))
g = list(range(1, 5, 2))
print(e, f, g) # [0, 1, 2, 3, 4] [1, 2, 3, 4] [1, 3]

"""
다차원 리스트 생성
"""

# 2차원 리스트 생성
a_2 = [[0 for j in range(2)] for i in range(3)]
b_2 = [[0] * 2 for i in range(3)]
print(a_2) # [[0, 0], [0, 0], [0, 0]]
print(b_2) # [[0, 0], [0, 0], [0, 0]]

# 3차원 리스트 생성
a_3 = [[[0 for k in range(2)] for j in range(3)] for i in range(2)]
b_3 = [[[0] * 2 for i in range(3)] for i in range(2)]
print(a_3) # [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]
print(b_3) # [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]


"""
톱니형 리스트 생성
"""

jagged = [[0] * i for i in [1, 3, 2, 5]]
print(jagged) # [[0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]
