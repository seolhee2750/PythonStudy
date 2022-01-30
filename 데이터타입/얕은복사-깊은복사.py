"""
객체는 mutable, immutable로 나눌 수 있는데,
list, set, dict 등은 mutable 객체, bool, int, str 등은 immutable 객체이다.
"""

"""
mutable 객체와 immutable 객체 비교 (list vs str)
"""
a = [1, 2, 3]
print(id(a)) # output : 4507373056
a[0] = 0
print(id(a)) # output : 4507373056

b = "abc"
print(id(b)) # output : 4507295344
# b[0] = "d" 하나의 글자 변경 불가
b = "def"
print(id(b)) # output : 4507969456

"""
mutable 객체와 immutable 객체의 변수 대입 비교 (list vs str) - 얕은 복사
"""
x1 = [1, 2, 3]
x2 = x1
x2[0] = 0
print(x1, x2) # output : [0, 2, 3] [0, 2, 3]
print(id(x1), id(x2)) # output : 4481772864 4481772864

y1 = "abc"
y2 = y1
y2 = "def"
print(y1, y2) # output : abc def
print(id(y1), id(y2)) # output : 4516896368 4517570352

"""
mutable 객체의 깊은 복사 - copy 모듈이용 (deepcopy 메소드)
"""
import copy
deep_a = [1, 2, 3]
deep_b = copy.deepcopy(deep_a)
print(id(deep_a), id(deep_b)) # output : 4520427392 4520425664
deep_b[0] = 0
print(deep_a, deep_b) # output : [1, 2, 3] [0, 2, 3]
