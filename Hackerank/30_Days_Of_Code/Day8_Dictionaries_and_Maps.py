# https://www.hackerrank.com/challenges/30-dictionaries-and-maps


n = int(input()) # number of entries


phone_dict = {}
for _ in range(n):
    names = input().split()
    phone_dict[names[0]] = names[1]

while True:
    try:
        queries = input().split()
    except EOFError:
        break
    for query in queries:
        if query in phone_dict:
            print(f"{query}={phone_dict[query]}")
        else:
            print("Not found")  

