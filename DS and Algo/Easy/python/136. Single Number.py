#https://leetcode.com/problems/single-number/
#complexity to remove elements from list
#complexity for count
#XOR LOGIC
#a ⊕ 0 = a
#a ⊕ a = 0
#a ⊕ b ⊕ a = ( a ⊕ a ) ⊕ b = 0 ⊕ b = b

# complexity is O(N)
class Solution:
    def singleNumberXor(self, nums: list) -> int:
        a = 0
        for i in nums:
            a ^= i
            print(a)
        return a

# complexity is O(N * N)
    def singleNumberBrute(self, nums: list) -> int:

        for i in nums:
            if (nums.count(i) == 1):
                return i

    def singleNumberHashmapdefaultdict(self, nums: list) -> int:
        from collections import defaultdict
        hashtable = defaultdict(int)
        print(hashtable)
        for i in nums:
            hashtable[i] += 1

        for i in hashtable:
            if hashtable[i] == 1:
                return i

    def singleNumberHashmap(self, nums: list) -> int:
        hashtable = {}
        for i in nums:
            if i in hashtable:
                hashtable[i] +=  1
            else:
                hashtable[i] = 1
        for i in hashtable:
            if (hashtable[i] == 1):
                return i
        print(hashtable)


sol = Solution()

print(sol.singleNumberXor([5,3]))
#print(sol.singleNumberHashmap([2,1,2]))

# 12 ^ 0 = 12
#12 ^ 11 = 7
#7 ^ 11 =  11
