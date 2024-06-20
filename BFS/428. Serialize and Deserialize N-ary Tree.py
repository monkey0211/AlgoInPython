"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node == None:
                result.append("null")
            else:
                queue.append(None)
                result.append(node.val)
                for child in node.children:
                    queue.append(child)

        while result and result[-1] == "null":
            result.pop()
            
        return ",".join(str(x) for x in result)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        parentNode = rootNode = None
        queue = deque()

        for item in data.split(","):
            if item == "null":
                parentNode = queue.popleft()
            elif item:
                childNode = Node(int(item), [])
                queue.append(childNode)
                if rootNode is None:
                    rootNode = childNode
                else:
                    parentNode.children.append(childNode)

        return rootNode
	
  
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))