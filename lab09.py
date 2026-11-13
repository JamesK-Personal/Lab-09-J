# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   use two for loops that will go through every number and check it against every other number until the sum is equal to the target
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    length = len(nums)
    for x in range (length):
        for y in range (length):
            #print(f"{nums[x]}+{nums[y]} = {nums[x]+nums[y]}")
            if x != y:
                if  nums[x]+nums[y] == target:
                        return [x, y]
    pass


def max_profit(prices):
    # Outline:
    #   use a for loops to find the lowest price, then find the max prophet after that day
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    maxP = 0
    if len(prices) == 0:
        return 0
    LowP = prices[0]
    length = len(prices)
    for x in range(length):
        if prices[x] < LowP:
            LowP = prices[x]
        elif prices[x] - LowP > maxP:
            maxP = prices[x]-LowP
    return maxP


def max_subarray(nums):
    # Outline:
    # iderate through the nums array adding them together in the sum interger
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    MaxSum = nums[0]
    CurrentSum = nums[0]
    for num in nums[1:]:
        CurrentSum = max(num,CurrentSum+  num)
        MaxSum = max(MaxSum, CurrentSum)
    return MaxSum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    #print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))   # [0, 1]
    print(two_sum([3, 3], 6))
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    pass


if __name__ == "__main__":
    main()
