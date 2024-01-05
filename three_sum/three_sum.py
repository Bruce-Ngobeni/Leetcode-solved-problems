def three_sum(nums):
    """
    The function uses a combination of sorting and a two-pointer approach. It iterates through
    the sorted list, selecting the first element of the triplet. It then uses two pointers to
    find the remaining two elements such that their sum equals zero. Duplicates are skipped
    to ensure unique triplets.

    Parameters:
    - nums (List[int]): A list of integers.

    Returns:
    - List[List[int]]: A list containing lists representing unique triplets that sum to zero.
    """
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

if __name__ == "__main__":
    pass