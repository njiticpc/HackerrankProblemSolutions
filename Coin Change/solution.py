# Problem: https://www.hackerrank.com/challenges/coin-change/problem
# Video Explanation: https://youtu.be/N1CtYbpBJH0

def coinChange(target, coins):
    dp = [1]+[0]*target # creates [1,0,0,0,0...] up to length of target

    for coin in coins:
        for targetSum in range(coin, target+1):
            dp[targetSum] += dp[targetSum-coin]

    return dp[target]
