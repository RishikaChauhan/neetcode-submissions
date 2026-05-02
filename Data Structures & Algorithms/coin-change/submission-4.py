class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        def dfs(amount):
            if amount in d:
                return d[amount]
            if amount==0:
                return 0
            res = float("inf")
            for coin in coins:
                if amount-coin>=0:
                    res = min(res, 1+dfs(amount-coin))
            d[amount]=res
            return res
        mn = dfs(amount)
        return -1 if mn ==float("inf") else mn
        
        
        
        
        
        
        
        
        coins.sort(reverse = True)
        ans = 0
        m = coins[-1]
        for i in coins:
            ans+=amount//i
            amount = amount%i
            if amount==0:
                break
            elif m>amount:
                return -1
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        coins.sort()
        coins = queue(coins)
        while q:
            a = coins.pop()
            if coins[0]>amount:
                return -1
            ans+=amount//a
            amount = amount%a        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        x = min(coins)
        coins.sort(reverse = True)
        l = 0
        r = len(coins)-1
        if coins[0]>amount:
            
            l = 0
            r = len(coins)-1
            while l<r:
                m = (l+r)//2
                if coins[m]<amount:
                    r = m-1
                elif coins[m]>amount:
                    l = m+1
            p = l
            print(p)
        ans = 0
        while amount>x:
            for i in coins[:l+1]:
                ans += amount//i
                amount = amount%i
        if amount==0:
            return ans
        else:
            return -1