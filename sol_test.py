from max_diff import Solution
def test_minMaxDifference():
    sol = Solution()

    # Test case 1
    num = 11891
    print(f"Input: {num}, Output: {sol.minMaxDifference(num)}")  # Expected: 99009 - 11000 = 88009

    # Test case 2
    num = 999
    print(f"Input: {num}, Output: {sol.minMaxDifference(num)}")  # Expected: 999 - 0 = 999

    # Test case 3
    num = 100
    print(f"Input: {num}, Output: {sol.minMaxDifference(num)}")  # Expected: 999 - 0 = 999

    # Test case 4
    num = 909
    print(f"Input: {num}, Output: {sol.minMaxDifference(num)}")  # Expected: 999 - 0 = 999

test_minMaxDifference()
