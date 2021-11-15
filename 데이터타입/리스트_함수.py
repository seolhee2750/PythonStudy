"""
리스트 값 삽입, 삭제 (append, insert, remove 등)
"""

a = ['a', 'b']

a.append('c')
print(a) # ['a', 'b', 'c']

a += ['d']
a += 'e'
print(a) # ['a', 'b', 'c', 'd', 'e']

a.insert(0, 'zero')
print(a) # ['zero', 'a', 'b', 'c', 'd', 'e']

a.remove('zero')
print(a) # ['a', 'b', 'c', 'd', 'e']


"""
리스트 정렬 (sort, sorted, reverse, reversed)
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


"""
리스트 검색 (slicing, all, any, max, min, enumerate, filter, map, sum, zip)
"""


