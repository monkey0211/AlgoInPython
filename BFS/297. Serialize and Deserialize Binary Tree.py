# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root: return ""
        queue = collections.deque([root])
        while queue:
            root = queue.popleft()
            if not root: 
                res.append("#")
            else:
                res.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
        while res and res[-1] == "#":
            res.pop()
        return "{" + ",".join(map(str, res))+"}"


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "[]":
            return 
 
        nodes = []
        data = data[1:-1].split(",")
        print("data", data)
        root = TreeNode(data[0])
        queue = collections.deque([root])
        for d in data:
            nodes.append(TreeNode(d)) # 把所有string都变为Tree Node
        i = 1 #root已经拿出 从1开始
        while queue:
            node = queue.popleft()
            if i < len(nodes):         
                if nodes[i].val == "#":
                    node.left = None
                else:
                    node.left = nodes[i]
                    queue.append(nodes[i])
                i += 1
            if i < len(nodes):         
                if nodes[i].val == "#":
                    node.right = None
                else:
                    node.right = nodes[i]
                    queue.append(nodes[i])
                i += 1
        return root