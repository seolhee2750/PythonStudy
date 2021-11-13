"""
input 함수는 입력되는 모든 것을 문자열로 취급
"""

a = input()
print(a) # in: 1 -> out: 1

b = int(input())
print(b) # in: 1 -> out: 1

c, d = map(int, input().split())
print(c, d) # in: 1 2 -> out: 1 2

c, d = map(str, input().split())
print(c, d) # in: 1 2 -> out: 1 2

input_list1 = input().split()
print(input_list1) # in: 1 2 -> ['1', '2']

input_list2 = list(map(lambda x: int(x), input().split()))
print(input_list2) # in: 1 2 -> out: [1, 2]