# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, s):
        check = {"(al)":"al", "()":"o","G":"G"}
        t,ans ="",""
        for i in range(len(s)):
            t+=s[i]
            if t in check:
                ans+=check[t]
                t=""
        return ans