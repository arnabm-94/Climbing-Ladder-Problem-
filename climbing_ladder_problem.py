'''
Write a python function for this climbing ladder problem.

Given a ladder containing N steps, you can take a jump of 
1, 2 or 3 at each step. Find the number of ways to climb the ladder. 

'''
'''
#Solution Statement :

To solve the climbing ladder problem where we can take 
a jump of 1, 2, or 3 steps at a time, you can use dynamic programming. 
The idea is to use a bottom-up approach where you build the solution for all steps from 0 up to N.

'''

def count_ways_to_climb_ladder(N):
    # Base cases
    if N == 0:
        return 1  # One way to stay at the ground (do nothing)
    elif N == 1:
        return 1  # One way to reach the first step (one 1-step jump)
    elif N == 2:
        return 2  # Two ways: (1+1) or (2)
    
    # Initialize dp array where dp[i] means the number of ways to reach the i-th step
    dp = [0] * (N + 1)
    dp[0] = 1  # One way to stay at the ground
    dp[1] = 1  # One way to reach the first step
    dp[2] = 2  # Two ways to reach the second step

    # Fill dp array using the bottom-up approach
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[N]

# Example usage:
N = 5
print(f"Number of ways to climb a ladder with {N} steps: {count_ways_to_climb_ladder(N)}")

'''
#Explanation

Base Cases:

dp[0] = 1: There's only one way to stay at the ground (do nothing).
dp[1] = 1: There's only one way to reach the first step (a single 1-step jump).
dp[2] = 2: There are two ways to reach the second step: (1+1) or (2).

Dynamic Programming Array:

dp[i] represents the number of ways to reach the i-th step.
For each step i from 3 to N, the number of ways to reach step i can be calculated as the sum of the number of ways to reach the previous three steps: dp[i-1], dp[i-2], and dp[i-3].
Iterative Calculation:

Using a loop from 3 to N, fill the dp array using the relation dp[i] = dp[i-1] + dp[i-2] + dp[i-3].
This approach ensures that you efficiently compute the number of ways to climb the ladder with a time complexity of O(N) and a space complexity of O(N).
'''
