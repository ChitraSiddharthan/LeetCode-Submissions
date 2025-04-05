class Solution(object):
    def simplifyPath(self, path):
        stack = []
        
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        simplifiedPath = '/' + '/'.join(stack)
        
        return simplifiedPath
        