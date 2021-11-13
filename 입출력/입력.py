"""
input 함수는 입력되는 모든 것을 문자열로 취급!
"""

a = input()
print(a) # in: 1 -> out: 1

b = int(input())
print(b) # in: 1 -> out: 1

c = input("입력: ") # 프롬프트 띄워서 입력 받는 것도 가능


"""
split 함수 : 공백 등 어떤 입력을 기준으로 나눠서 입력받을 수 있으며, 리스트 형태로 반환
=> 문자열.split([[sep=]'구분자'], [[maxsplit=]분할 횟수]) 형태로 사용!
    
    (1) 구분자 생략 시 공백을 기준으로 나누어줌 
        (구분자 생략 시, maxsplit 키워드는 생략 불가! -> 문자열.split(maxsplit=1) 이렇게 사용해줘야 함
        문자열.split(1) 이런 식으로 사용하게 되면, 1을 구분자로 인식하게 되기 때문에 오류가 발생할 수 있음)
    (2) 분할 횟수 생략 시 나눌 수 있는 모든 분할을 시행함
    (3) 문자열에만 사용이 가능하고, input 함수 또한 문자열 형태로 반환하기 때문에 input().split() 이런 식으로 사용 가능!
"""

d, e = map(int, input().split())
print(d, e) # in: 1 2 -> out: 1 2

f, g = map(str, input().split())
print(f, g) # in: 1 2 -> out: 1 2

input_list1 = input().split()
print(input_list1) # in: 1 2 -> ['1', '2']

input_list2 = list(map(lambda x: int(x), input().split()))
print(input_list2) # in: 1 2 -> out: [1, 2]