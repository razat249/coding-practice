# final = []
# def palindrome_paritioning(str):
# 	global final
# 	if len(str) == 1:
# 		final.append(str)
# 		return
# 	if str == str[::-1]:
# 		print "Pupu"
# 		final.append(str)
# 	x = int(len(str)/2)
# 	palindrome_paritioning(str[:x])
# 	palindrome_paritioning(str[x:])

# palindrome_paritioning("abb")

# print final

class Solution:
	def partition(self, s):
	    res = []
	    self.dfs(s, [], res)
	    return res

	def dfs(self, s, path, res):
	    if not s:
	        res.append(path)
	        return
	    for i in range(1, len(s)+1):
	        if self.isPal(s[:i]):
	            self.dfs(s[i:], path+[s[:i]], res)
	    
	def isPal(self, s):
	    return s == s[::-1]


s = Solution()
print s.partition("aab")