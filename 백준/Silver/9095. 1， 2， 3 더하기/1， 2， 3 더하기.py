TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    cnt = 0
    def dfs(level):
        global cnt
        if level > N:
            return

        if level == N:
            cnt += 1
            return

        for i in range(1,4):
            dfs(level+i)

    dfs(0)
    print(cnt)