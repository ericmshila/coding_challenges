if __name__ == '__main__':
    n = int(input())
    num_list = []
    for i in range(1, n+1):
        num_list.append(str(i))
    print(''.join(num_list))