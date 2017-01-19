# def cartesion(b, a):
# 	if len(a) == 0:
# 		return list(b)
# 	result = []
# 	for i in a:
# 		for j in b:
# 			result.append(i + j)
# 	return result

# # print cartesion(["a", "b"], ["c"])

# final = []
# def letterPhone(str):
# 	map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
# 	global final
# 	if len(str) == 0:
# 		return final
# 	final = cartesion(map[int(str[0])], final)	
# 	letterPhone(str[1:])
# 	return final

# print letterPhone("4")

# # print final

class Solution:
    # @param A : string
    # @return a list of strings
    final = []
    def cartesion(self, b, a):
    	if len(a) == 0:
    		return list(b)
    	result = []
    	for i in a:
    		for j in b:
    			result.append(i + j)
    	return result
    
    def letterCombinations(self, str):
        map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    	if len(str) == 0:
    		return Solution.final
    	Solution.final = self.cartesion(map[int(str[0])], Solution.final)	
    	self.letterCombinations(str[1:])
    	return Solution.final

s = Solution()
print s.letterCombinations("17")