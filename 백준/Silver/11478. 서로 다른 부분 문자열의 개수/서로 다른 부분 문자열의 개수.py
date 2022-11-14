S = input()
s_arr = []

for i in range(len(S)):
    text = ''
    for j in range(i,len(S)):
        text += S[j]
        s_arr.append(text)
set_arr = set(s_arr)
print(len(set_arr))