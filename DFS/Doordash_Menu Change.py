# https://leetcode.com/discuss/interview-question/1528907/doordash-phone-creen
# reference:
# https://vivo.pub/calculate-tree-node-changes/

from typing import List


class Node:
    def __init__(self, key:str=None, val:int=None, children:List['Node']=[]):
        self.key = key
        self.val = val
        self.children = children

class Solution:
    def compare_old_and_updated_menus(self, root_o: Node, root_u: Node) -> int:
        return self.dfs_compare(root_o, root_u)

    def count_nodes(self, root: Node) -> int:
        if not root:
            return 0
        num = 1
        for child in root.children:
            num += self.count_nodes(child)
        return num    

    def dfs_compare(self, root_o: Node, root_u: Node) -> int:
        if not root_o and not root_u:
            return 0
        if not root_o:
            return self.count_nodes(root_u)
        if not root_u:
            return self.count_nodes(root_o)
        if root_o.key != root_u.key:
            return self.count_nodes(root_u) + self.count_nodes(root_o)

        diff_cnt = 0
        if root_o.val != root_u.val:
            diff_cnt += 1
        
        origin_map = {}
        visited = set()
        for child in root_o.children:
            origin_map[child.key] = child

        for child in root_u.children:
            if child.key in origin_map:
                visited.add(child.key)
                diff_cnt += self.dfs_compare(origin_map[child.key], child)
            else:
                diff_cnt += self.count_nodes(child)
        
        for child in root_o.children:
            if child.key not in visited:
                diff_cnt += self.count_nodes(child)
        return diff_cnt


# case 1
# d_o, e_o, f_o = Node("d", 4), Node("e", 5), Node("f", 6)
# b_o, c_o = Node("b", 2, [d_o, e_o]), Node("c", 3, [f_o])
# a_o = Node("a", 1, [b_o, c_o])    # a_o is the root_o

# f_u = Node("f", 66)
# c_u = Node("c", 3, [f_u])
# a_u = Node("a", 1, [c_u])   # a_u is the root_u

# test = Solution()
# print(test.compare_old_and_updated_menus(a_o, a_u))

# Example usage
old_tree = Node("root", 1)
child1_old = Node("child1", 2)
child2_old = Node("child2", 3)
old_tree.children.append(child1_old)
old_tree.children.append(child2_old)

new_tree = Node("root", 1)
child1_new = Node("child1", 5)  # Value changed
child3_new = Node("child3", 4)  # New node
new_tree.children.append(child1_new)
new_tree.children.append(child3_new)

test = Solution()
print(test.compare_old_and_updated_menus(old_tree, new_tree))