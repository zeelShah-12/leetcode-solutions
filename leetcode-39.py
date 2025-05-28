class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(index: int, current_sum: int, path: list[int]):
            
            if current_sum == 0:
                result.append(path[:])  
                return
            if current_sum < 0:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])  
                dfs(i, current_sum - candidates[i], path)  
                path.pop()  

        dfs(0, target, [])
        return result