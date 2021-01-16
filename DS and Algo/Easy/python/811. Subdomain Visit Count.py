class Solution:
    def subdomainVisits2(self, cpdomains: list) -> list:

        checkMap = {}

        for i in cpdomains:
            num = int(i.split(" ")[0])
            value = '.' + i.split(" ")[1]

            for i in reversed(range(len(value))):
                if (value[i] == "."):
                    val = value[i+1:]
                    if ( val in checkMap):
                        checkMap[val] = checkMap[val] + num
                    else:
                        checkMap[val] = num

        final = []

        print(checkMap)

        for key in checkMap:
            output = str(checkMap[key]) + " " + key
            final.append(output)
        return final

    def subdomainVisits(self, cpdomains: list) -> list:

        checkMap = {}

        for i in cpdomains:

            num = int(i.split(" ")[0])
            value = i.split(" ")[1].split(".")

            if (len(value) == 3):

                val1 = value[0] + "." + value[1] + "." + value[2]

                if (val1 in checkMap):

                    checkMap[val1] = checkMap[val1] + num
                else:
                    checkMap[val1] = num

            val2 = value[len(value) - 2] + "." + value[len(value) - 1]

            if (val2 in checkMap):

                checkMap[val2] = checkMap[val2] + num
            else:
                checkMap[val2] = num

            val3 = value[len(value) - 1]

            if (val3 in checkMap):

                checkMap[val3] = checkMap[val3] + num
            else:
                checkMap[val3] = num

        final = []

        print(checkMap)

        for key in checkMap:
            output = str(checkMap[key]) + " " + key
            final.append(output)
        return final


sol = Solution()
prices =["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(sol.subdomainVisits2(prices))