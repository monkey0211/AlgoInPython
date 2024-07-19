class Solution:
    #先split成list. 用stack
    # 如果遇到“..”: 
    #      如果有stack就pop. 如果“.” or "", continue. else stack.append
    def simplifyPath(self, path: str) -> str:
        # Meta variation with cwd&cd: path = cwd + "/" + cd
        stack = []
        pathList = path.split("/")
        
        for string in pathList:
            if string == "." or string == "":
                continue
            elif string == "..":
                if stack:
                    stack.pop()
            # Meta variation
            # elif string == "":
            #     stack.clear()
            else:
                stack.append(string)
                
        return "/" + "/".join(stack)