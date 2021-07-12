class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for x in paths:
            if x == "..":
                if stack:  # Root Directory condition
                    stack.pop()

            elif x == "." or not x:
                continue

            else:
                stack.append(x)

        return "/" + "/".join(stack)

"""BASE CASE TO RETURN ROOT DIRECTORY"""