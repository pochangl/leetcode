class Solution(object):
    def jump(self, nums):
        length = len(nums)
        last_index = length - 1
        if length < 2:
            return 0
        reaches = tuple([index + num for index, num in enumerate(nums)])

        step = 0
        start_index = 0
        search_index = 1

        while start_index <= last_index:
            max_value = 0
            max_index = start_index
            if reaches[start_index] >= last_index:
                step += 1
                return step
            for target_index in range(search_index, reaches[start_index] + 1):
                if max_value < reaches[target_index] and nums[target_index]:
                    max_index = target_index
                    max_value = reaches[target_index]
            step += 1
            search_index = reaches[start_index] + 1
            start_index = max_index
        return step



print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([1, 2, 3]))

print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))
print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))
