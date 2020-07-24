
'''
解题思路：

寻找数组中的重复数字，直接想到的方法是遍历数组，并使用 HashMap 统计每个数字的数量，遇到数量大于 11 的数字则返回。此方法时间复杂度和空间复杂度均为 O(N)O(N) 。
题目指出 在一个长度为 n 的数组 nums 里的所有数字都在 0 ~ n-1 的范围内 。 因此，可遍历数组并通过交换操作使元素的 索引 与 值 一一对应（即 nums[i] = i ）。因而，就能通过索引找到对应的值。

遍历中，当第二次遇到数字 x 时，一定有 nums[x] = x （因为第一次遇到 x 时已经将其交换至 nums[x] 处了）。利用以上方法，即可得到一组重复数字。

算法流程:

遍历数组 nums ，设索引初始值为 i = 0:
若 nums[i] == i ： 说明此数字已在对应索引位置，无需交换，因此执行 i += 1 与 continue ；
若 nums[nums[i]] == nums[i] ： 说明索引 nums[i] 处的元素值也为 nums[i]，即找到一组相同值，返回此值 nums[i]；
否则： 当前数字是第一次遇到，因此交换索引为 i 和 nums[i] 的元素值，将此数字交换至对应索引位置。
若遍历完毕尚未返回，则返回 -1−1 ，代表数组中无相同值。
复杂度分析：
时间复杂度 O(N)O(N) ： 遍历数组使用 O(N)O(N) ，每轮遍历的判断和交换操作使用 O(1)O(1) 。
空间复杂度 O(1)O(1) ： 使用常数复杂度的额外空间。
'''

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


nums = [2, 1, 3, 2, 4]
r = Solution().findRepeatNumber(nums)
print(r)