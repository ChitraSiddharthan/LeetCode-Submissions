class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return 
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                current.append(candidates[j])
                dfs(j, current, total + candidates[j])
                current.pop()
        
        dfs(0, [], 0)
        return result