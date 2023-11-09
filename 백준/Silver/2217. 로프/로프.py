n = int(input()) # 로프의 수
data = [] # 각 로프들에 대한 정보
result = []

for i in range(n):
    x = int(input())
    data.append(x)

data.sort(reverse=True)

for i in range(n):
    result.append((i+1)*data[i])

print(max(result))