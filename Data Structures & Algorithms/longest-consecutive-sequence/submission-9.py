class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        mcount = 0
        for i in num_set:      
            if (i-1) not in num_set:
                curr_num = i
                count = 1
                while (curr_num +1) in num_set:
                    curr_num+=1
                    count+=1
                mcount = max(mcount, count)
        return mcount       
        # if not nums: return 0
        
        # num_set = set(nums)
        # mcount = 0

        # for i in num_set:
        #     if (i - 1) not in num_set:
        #         curr_num = i
        #         count = 1

        #         while (curr_num + 1) in num_set:
        #             curr_num += 1
        #             count += 1
                
        #         mcount = max(mcount, count)
        # return mcount