class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []  
        for val in path:
            if val == "" or val == ".":
                continue
            elif val == "..":
                stack.pop()
            else:
                stack.append(val)
        return "/" + ("/".join(stack))