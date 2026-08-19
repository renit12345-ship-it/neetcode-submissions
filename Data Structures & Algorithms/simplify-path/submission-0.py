class Solution:
    def simplifyPath(self, path: str) -> str:
        stacks=[]
        path_split=path.split("/")
        for i in path_split:
            if i == "" or i == ".":
                continue 
            elif i == "..":
                if stacks :
                    stacks.pop()
            else : 
                stacks.append(i)
        return "/" + "/".join(stacks)