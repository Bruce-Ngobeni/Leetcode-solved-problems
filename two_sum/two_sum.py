def two_sum(nums,target):
    for index, i in enumerate(nums):
        for index_num, j in enumerate(nums):
            if i + j == target and index != index_num:
                return [index, index_num]


if __name__ == "__main__":
    print(two_sum([2,7,11,15],9))
    print(two_sum([3,2,4],6))
    print(two_sum([3,3],6))