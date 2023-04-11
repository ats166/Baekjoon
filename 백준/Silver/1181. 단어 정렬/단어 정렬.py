N = int(input())
data_list = []

for i in range(N):
    data = input()
    data_list.append(data);

data_list = list(set(data_list))

data_list.sort()
data_list.sort(key=lambda x : len(x))

for i in range(len(data_list)):
    print(data_list[i])