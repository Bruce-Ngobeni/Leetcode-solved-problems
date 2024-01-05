def two_sum(nums, target):
    """
    Given a list 'nums' of integers and a target sum, this function finds /and returns
    the indices of two numbers in the list whose sum equals the target.

    The function uses a dictionary to store the indices of numbers as it iterates through
    the list. It calculates the complement for each number and checks if the complement is
    present in the dictionary. If found, it returns the indices of the two numbers.

    Parameters:
    - nums (List[int]): A list of integers.
    - target (int): The target sum to be achieved.

    Returns:
    - List[int] or None: A list containing the indices of two numbers whose sum equals the target.
    If no such pair is found, returns None.
    """

    indinces = {}

    for index, num in enumerate(nums):

        compliment = target - num

        if compliment in indinces:
            return [indinces[compliment],index]

        indinces[num] = index
    
    return None


if __name__ == "__main__":
    pass