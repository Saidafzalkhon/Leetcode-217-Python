if __name__ == "__main__":
    nums = list(map(int,input().split()))
    s = set(nums)
    if len(s)<len(nums):
        print(True)
    else: print(False)