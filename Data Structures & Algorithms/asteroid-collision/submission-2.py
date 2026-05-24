class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            flag = False
            while res and (res[-1] > 0 and i < 0):
                p = res[-1]
                if abs(p) < abs(i):
                    res.pop()
                    continue
                elif abs(p) == abs(i):
                    res.pop()
                flag = True
                break
            if not flag:
                res.append(i)
        return res