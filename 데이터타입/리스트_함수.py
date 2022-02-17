"""
리스트 값 삽입, 삭제, 수정 (append, insert, extend, remove, map 등)
"""

a = ['a', 'b']
b = [1, 2, 3]

# 맨 뒤에 추가
a.append('c')
print(a) # ['a', 'b', 'c']

# 더하기 연산으로 맨 뒤에 추가 (리스트 형태, 값 형태 모두 가능하며, 반대로 -연산은 불가)
a += ['d']
a += 'e'
print(a) # ['a', 'b', 'c', 'd', 'e']

# 원하는 인덱스에 값 추가
a.insert(0, 'zero')
print(a) # ['zero', 'a', 'b', 'c', 'd', 'e']

# 맨 뒤에 리스트 더하기
a.extend([1, 2])
print(a) # ['zero', 'a', 'b', 'c', 'd', 'e', 1, 2]

# 원하는 요소 지우기
a.remove('zero')
print(a) # ['a', 'b', 'c', 'd', 'e', 1, 2]

# 맨 뒤 요소 삭제
a.pop()
print(a) # ['a', 'b', 'c', 'd', 'e', 1]

# map 함수, lambda 식을 활용한 형변환, 값 수정
print(list(map(lambda x: str(x), b))) # ['1', '2', '3']
print(list(map(str, b))) # ['1', '2', '3']
print(list(map(lambda x: str(x) if x < 2 else x, b))) # ['1', 2, 3]
print(list(map(lambda x: x+1, b))) # [2, 3, 4]
print(list(map(lambda x: list(range(0, x)), b))) # [[0], [0, 1], [0, 1, 2]]


"""
리스트 정렬 (sort, sorted, reverse, reversed, slicing)
"""

# sorted는 정렬된 값을 반환하지만, 리스트 자체를 정렬하지는 않음
# sort는 정렬된 값을 반환하지 않지만, 리스트 자체를 정렬해줌

b = [2, 3, 1]

print(sorted(b)) # [1, 2, 3]
print(sorted(b, reverse = True)) # [3, 2, 1]
print(b) # [2, 3, 1]

print(b.sort()) # None
print(b) # [1, 2, 3]
b.sort(reverse = True)
print(b) # [3, 2, 1]

# reverse는 sort와 같이 뒤집은 값을 반환하지는 않고, 대신 리스트 자체를 뒤집어줌
# reversed는 reverse와는 달리 list에서 제공하지 않는 내장함수임
#   => 따라서 list(reversed(c))와 같은 형태로 사용해주어야 함 (sorted와 마찬가지로, 반환만 할 뿐 리스트 자체를 수정하지는 않음)

c = [1, 2, 2, 3]

print(reversed(c)) # <list_reverseiterator object at 0x10b4c6880>
print(list(reversed(c))) # [3, 2, 2, 1]
print(c.reverse()) # None
print(c) # [3, 2, 2, 1]

# 슬라이싱을 활용하면 list(reversed(c))와 같은 효과를 낼 수 있음
print(c[::-1]) # [1, 2, 2, 3]

# key 키워드
# sort, sorted 함수 모두 reverse 뿐만 아니라 key 매개변수를 가진다.
# key는 정렬을 목적으로 하는 함수를 값으로 넣는데, lambda를 이용할 수 있다.
# key값을 기준으로 정렬되고, 기본값은 오름차순이다.

d = ['apple', 'hi', 'hello', 'e']
e = [(2, 'a'), (3, 'b'), (1, 'd'), (1, 'c')]

d.sort(key = lambda x: len(x)) # 각 요소의 길이를 기준으로 정렬
e.sort(key = lambda x: (x[0], x[1])) # 튜플의 앞 요소 기준으로 정렬, 같을 경우 뒷 요소 기준 정렬
print(d) # ['e', 'hi', 'apple', 'hello']
print(e) # [(1, 'c'), (1, 'd'), (2, 'a'), (3, 'b')]


"""
리스트 검색, 연산 (slicing, all, any, max, min, enumerate, filter, sum, reduce, zip, len 등)
"""

list_a = [1, 2, 3]
list_b = [1, 0, 0]
list_c = ['a', 'b', 'c']

# 파이썬에서는 인덱스로 -1을 입력하면 가장 마지막 요소를 가리킴
print(list_a[-1]) # 3

# 슬라이싱을 활용하면 리스트 자체는 그대로 두고, 원하는 범위의 값들을 반환해줌
print(list_a[0:2]) # [1, 2]
print(list_a[:2]) # [1, 2]
print(list_a[2:]) # [3]

# all은 하나라도 0(False)가 있으면 False를 반환해줌 (전부 다 True여야 True로 인정)
# any는 하나라도 1(True)가 있으면 True를 반환해줌 (몇 개만 True여도 True로 인정)
print(all(list_a)) # True
print(all(list_b)) # False
print(any(list_a)) # True
print(any(list_b)) # True

# 최대, 최소
print(max(list_a)) # 3
print(min(list_a)) # 1

# 열거하는 함수로, 순서가 있는 자료형을 입력으로 받아서 인덱스 값을 포함하는 enumerate 객체를 반환 (보통 for 문으로 많이 사용)
for i, name in enumerate(list_c):
    print(i, name)
# 0 a
# 1 b
# 2 c

# filter 함수, lambda 식을 활용한 값 검색
print(list(filter(lambda x: x == 0, list_b))) # [0, 0]

# 모든 요소의 합
print(sum(list_a)) # 6

# 누적 연산 (파이썬3에서는 reduce 사용하려면 아래와같은 선언 필요)
from functools import reduce
print(reduce(lambda x, y: x + y, list_a)) # 6

# 묶어주기 (같은 인덱스 요소끼리 묶어줌)
print(list(zip(list_a, list_b))) # [(1, 1), (2, 0), (3, 0)]
print(list(zip(list_a, list_b, list_c))) # [(1, 1, 'a'), (2, 0, 'b'), (3, 0, 'c')]

# 길이
print(len(list_a)) # 3
