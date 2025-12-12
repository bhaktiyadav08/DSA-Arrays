def findFirst(nums, target):
    low, high = 0, len(nums) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid         # store possible answer
            high = mid - 1      # go left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first


def findLast(nums, target):
    low, high = 0, len(nums) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            last = mid          # store possible answer
            low = mid + 1       # go right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last


def searchRange(nums, target):
    return [findFirst(nums, target), findLast(nums, target)]


# Example
nums = [4,5,5,7,8,8]
target = 5
print(searchRange(nums, target))   # Output: [1, 2]
