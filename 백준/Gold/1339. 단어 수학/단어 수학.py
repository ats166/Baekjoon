import sys

n = int(sys.stdin.readline())

alphabet_dict = {}
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)

for alphabet in pocket:
    for i, char in enumerate(alphabet):
        num = 10 ** (len(alphabet) - i - 1)
        if char not in alphabet_dict:
            alphabet_dict[char] = 0
        alphabet_dict[char] += num

alphabet_list = [value for value in alphabet_dict.values() if value > 0]
sorted_list = sorted(alphabet_list, reverse=True)

for i, value in enumerate(sorted_list):
    answer += value * (9 - i)

print(answer)