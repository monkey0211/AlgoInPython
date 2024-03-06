class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split("/")
        stack = []
        for s in pathlist:
            if s == "." or s == "":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)