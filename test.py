import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    print(a[0],a[n-1])
    print(''.join(map(str, a)))


if __name__ == '__main__':
    main()