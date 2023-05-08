

def findLucky(arr):
    result = None
    lucky = {}
    for k in range(0, 10):
        lucky[k] = 0

    for num in arr:
        lucky[num] += 1

    result = max([num for num, value in lucky.items() if num == lucky[num]])

    return result if result != 0 else -1


if __name__ == '__main__':
    arr = input().strip().split()

    arr = [int(a) for a in arr]

    print(findLucky(arr))
