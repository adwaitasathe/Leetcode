class Solution:
    def isAlienSorted(self, words: list, order: str) -> bool:

        checkMap = {}
        a = 0

        for i in order:
            checkMap[i] = a
            a = a + 1

        for i in range(len(words) - 1):

            minlength = min(len(words[i]), len(words[i + 1]))

            for j in range(minlength):
                if (checkMap[words[i][j]] == checkMap[words[i + 1][j]]):
                    continue
                elif (checkMap[words[i][j]] > checkMap[words[i + 1][j]]):
                    return False
                else:
                    break

            if (words[i][0:minlength] == words[i + 1][0:minlength] and len(words[i]) > len(words[i + 1])):
                return False
        return True

sol = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(sol.isAlienSorted(words,order))





