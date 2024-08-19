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

'''
Meta version
Given current directory and change directory path, return final path.

For Example:
Curent                 Change            Output

/                    /facebook           /facebook
/facebook/anin       ../abc/def          /facebook/abc/def
/facebook/instagram   ../../../../.      /
'''

def change_path(cwd, cd) -> str:
    path = cwd + "/" + cd
    stack = []
    for dir in path.split("/"):
        if dir == ".":
            continue
        elif dir == "..":
            if stack: 
                stack.pop()
        elif not dir:
            stack.clear()
        else:
            stack.append(dir)

    return "/" + "/".join(stack)

# unit test
cwd1 = '/facebook/anin'
cd1 = '../abc/def'
print(change_path(cwd1, cd1))
cwd2 = '/'
cd2 = '/facebook'
print(change_path(cwd2, cd2))