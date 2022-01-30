"""
input보다 sys.stdin.readline()을 사용했을 때 시간과 메모리를 아낄 수 있다.

- input은 입력으로부터 한 줄을 읽고, 발생한 개행문자(\n)을 없애여 문자열로 변환한 뒤 return한다.
- sys.stdin.readline()의 경우 input과 마찬가지로 문자열을 return하지만, 개행문자를 함께 반환한다.
    (개행문자는 int로 형변환 시 자동으로 사라지고 정수 형태만 남는다.)
"""

import sys

a = sys.stdin.readline()
print(a) # input: 1 / output: "1\n"

b = sys.stdin.readline().strip()
print(b) # input: 1 / output: "1"

c = int(sys.stdin.readline())
print(c) # input: 1 / output: 1

d, e = map(int, sys.stdin.readline().split())
print(d, e) # input: 1 2 / output: 1 2

f = [sys.stdin.readline().strip().split() for _ in range(2)]
print(f) # input: 1 2\n2 3 / output: [['1', '2'], ['2', '3']]

# (아래와 같은 표현) g = [list(map(lambda x: int(x), sys.stdin.readline().strip.split())) for _ in range(2)]
g = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
print(g) # input: 1 2\n2 3 / output: [[1, 2], [2, 3]]