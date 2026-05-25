class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        stack = []
        pair = sorted(zip(position, speed))
        for i in range(len(pair)):
            res.append((target-pair[i][0])/pair[i][1])
        while res:
            cur = res.pop()
            if not stack or cur>stack[-1]:
                stack.append(cur)
            # if stack and stack[-1]<cur:
            #     count+=1
            #     stack[-1] = cur
            # stack.append(cur)
        return len(stack)
            