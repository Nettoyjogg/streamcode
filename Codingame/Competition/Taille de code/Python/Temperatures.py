print(0) if input()=='0' else print(sorted(sorted(list(map(int,input().split())))[::-1],key=abs)[0])
