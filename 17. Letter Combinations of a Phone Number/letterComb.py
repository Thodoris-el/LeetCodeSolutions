from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        let = {}
        let["2"] = ["a", "b", "c"]
        let["3"] = ["d", "e", "f"]
        let["4"] = ["g", "h", "i"]
        let["5"] = ["j", "k", "l"]
        let["6"] = ["m", "n", "o"]
        let["7"] = ["p", "q", "r", "s"]
        let["8"] = ["t", "u", "v"]
        let["9"] = ["w", "x", "y", "z"]

        res = []

        for i in digits:
            if len(res) == 0:
                res = let[i]
                continue
            l3 = []    
            for l1, l2 in product(res, let[i]):
                l3.append(l1+l2)
            res = l3
        return res
