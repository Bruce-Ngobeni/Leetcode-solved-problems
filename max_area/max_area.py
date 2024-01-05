def maxArea(height):
    """
    Given a list 'height' representing the heights of vertical lines on a plane,
    this function calculates the maximum area formed between two lines by selecting two indices.

    The function uses a two-pointer approach starting from the outermost lines and moving
    towards the center. It keeps track of the maximum area encountered.

    Parameters:
    - height (List[int]): A list of non-negative integers representing the heights of vertical lines.

    Returns:
    - int: The maximum area formed by selecting two lines from the 'height' list.
    """
        
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        x = right - left
        y = min(height[left], height[right])

        area = x * y
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


if __name__ == "__main__":
    pass