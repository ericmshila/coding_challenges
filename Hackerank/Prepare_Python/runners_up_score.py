if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    others = [i for i in arr if i < max(arr)]
    list.sort(others)
    #print(others)
    runners_up = others[-1] 
    print(runners_up)
