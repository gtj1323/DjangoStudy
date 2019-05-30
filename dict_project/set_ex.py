# 1. 셋 만들기
"""
셋은 중복이 없고, 인덱스로 찾을 수 없음.
"""
# 1-1.
s1 = set([1,2,3])
print(s1)
# 1-2.
s2=set('hello')
print(s2)
# 1-3-1.
s3=set()
print(type(s3))
# 1-3-2. 주의 셋만들기 아님.
s4={}
print(type(s4))

# 2. set다루기
set1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])
# 2-1. 교집합
print(set1 & set2)
print(set1.intersection(set2))
# 2-2. 합집합
print(set1 | set2)
print(set1.union(set2))
# 2-3. 차집합
print(set1 - set2)
print(set1.difference(set2))
print(set2.difference(set1))