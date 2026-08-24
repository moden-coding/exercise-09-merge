#!/usr/bin/env python3

def merge(L1, L2):
    pass

def main():
    l1 = [1, 5, 2, 5, 6,1 ,2, 7, 0]
    l1.sort()
    print(l1)

    l2 = [9, 1, 2, 6, 1, 9,6, 52]
    l2.sort()
    print(l2)

    print(merge(l1, l2))

if __name__ == "__main__":
    main()
