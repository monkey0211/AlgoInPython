# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #先需要build parent: DFS. 然后bfs遍历每个node(while queue and distance<k), 进行level order. 
    # 把满足条件的node.left, node.right, node.parent都加入queue+visited
    # 最后queue里剩下的就是答案
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
       
        parents = {}
        self.buildparents(root, parents)
        visited = set()
        visited.add(target)
        distance = 0
        queue = collections.deque([target])
        
        while queue and distance < k: #不能等于 此时queue里还存在的node就是需要return的
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parents and parents[node] not in visited:
                    queue.append(parents[node])
                    visited.add(parents[node])
            distance += 1
                    
        return [item.val for item in queue]  
    
    def buildparents(self, root, parents):
        if not root:
            return None
        if root.left:
            parents[root.left] = root

        if root.right:
            parents[root.right] = root

            
        left = self.buildparents(root.left, parents)
        right = self.buildparents(root.right, parents)
        
        if left:
            parents[left] = root
   
        if right:
            parents[right] = root

            
            
            
            
        
        