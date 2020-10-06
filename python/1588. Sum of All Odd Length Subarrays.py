class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        for i in range(0, len(arr), 2):
            for j in range(len(arr) - i):
                total += sum(arr[j: j+i+1])
        return total


# a better solution : Complexity Time O(N), Space O(1)
# Example of array [1,2,3,4,5]
# 1 2 3 4 5 subarray length 1
# 1 2 X X X subarray length 2
# X 2 3 X X subarray length 2
# X X 3 4 X subarray length 2
# X X X 4 5 subarray length 2
# 1 2 3 X X subarray length 3
# X 2 3 4 X subarray length 3
# X X 3 4 5 subarray length 3
# 1 2 3 4 X subarray length 4
# X 2 3 4 5 subarray length 4
# 1 2 3 4 5 subarray length 5

# 5 8 9 8 5 total times each index was added.
# 3 4 5 4 3 total times in odd length array with (x + 1) / 2
# 2 4 4 4 2 total times in even length array with x / 2

# class Solution(object):
#     def sumOddLengthSubarrays(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
    # def sumOddLengthSubarrays(self, A):
    #     res, n = 0, len(A)
    #     for i, a in enumerate(A):
    #         res += ((i + 1) * (n - i) + 1) / 2 * a
    #     return res