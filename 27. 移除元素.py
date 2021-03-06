"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):
    """
    双指针
    当 nums[j] 与给定的值相等时，递增 j 以跳过该元素
    只要 nums[j] != val，我们就复制 nums[j] 到 nums[i] 并同时递增两个索引
    重复这一过程，直到 j 到达数组的末尾，该数组的新长度为 i
    """
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
