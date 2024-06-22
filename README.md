# Climbing-Ladder-Problem-
Given a ladder containing N steps, you can take a jump of 
1, 2 or 3 at each step. Find the number of ways to climb the ladder. 
=========================================================================================================================================================================================


Use dynamic programming to solve the problem of climbing a ladder with N steps where you can take jumps of 1, 2, or 3 steps. Build the solution from the bottom up, starting at step 0 and working up to step N. This approach efficiently calculates the number of ways to reach the top by considering all possible jumps at each step.
------------------------------------------------------------


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
