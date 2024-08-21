import collections
from typing import List
# LC721的变形:https://leetcode.com/problems/accounts-merge/submissions/1244670006/.
# 每个账号对应多个邮箱, 邮箱有重合就表示账号相同, 把相同的账号group起来并返回
# // === Input ===
# // A1: alice@yahoo.com, alice_1@gmail.com
# // A2: bob@facebook.com
# // A3: alice_1@gmail.com, alice_2@hotmail.com
# // A4: alice_2@hotmail.com
# // A5: bob@facebook.com
# // A6: carol@gmail.com

# // === Output ===
# // ((A1,A3,A4), (A2,A5), (A6))

class Solution: 
    def accountMerge(self, accounts):
        graph = collections.defaultdict(set)
        accountToName = {} # email->key
        for key, emails in accounts.items():
            for i in range(len(emails)):
                
                if i >= 1:
                    graph[emails[0]].add(emails[i])
                    graph[emails[i]].add(emails[0])
                else:
                    graph[emails[0]] = set()
                    
                accountToName[emails[i]] = key
        
        print("graph", graph)
        res = []
        keySet = set()
        visited = set()
        for email1 in graph:
            if not graph[email1]: #没有其他email, 只有一个key
                res.append({accountToName[email1]})
                continue
            restEmails = graph[email1]
      
            for email in restEmails:
                if email not in visited:
                    visited.add(email)
                    tmp = []
                    tmp.append(email1)
                    self.dfs(email, graph, visited, tmp)
                    
                    for i in range(len(tmp)):
                        keySet.add(accountToName[tmp[i]])   
                    res.append(keySet)
        return res
        
    def dfs(self, node, graph, visited, tmp):
        if node not in graph:
            return
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                tmp.append(nei)
                self.dfs(nei, graph, visited, tmp)

test = Solution()
accounts = {"A1": ["alice@yahoo.com", "alice_1@gmail.com"],
"A2": ["bob@facebook.com"],
"A3": ["alice_1@gmail.com", "alice_2@hotmail.com"]}     
print(test.accountMerge(accounts))

# Aaron version: Union-Find
# 1. 记录每个邮箱在哪些name下出现过 构建{email:[names]}索引
# 2. 将共享邮箱的人 用并查集合并
# time O(n) (find操作的时间复杂度近似常数)  space: O(n)
def accounts_merge(accounts: dict[str, List[str]]) -> List[List[str]]:
    if not accounts:
        return [[]]
    # 记录每个邮箱在哪些name下出现过 构建{email:[names]}索引
    email_to_names = collections.defaultdict(list)
    parent = {}
    for name, email_list in accounts.items():
        parent[name] = name # 初始化parent字典 每个人都以自己为根
        for email in email_list:
            email_to_names[email].append(name)
    # 将共享邮箱的人 用并查集合并
    # 同一个name_list里的所有人 统一放在name_list[0]的名字下面
    for name_list in email_to_names.values():
        root = name_list[0]
        for k in range(1, len(name_list)):
            parent[find(parent, name_list[k])] = find(parent, root)
    print("parent", parent)
    
    # 按相同的parent 把user group在一起
    # user{parent: list: {userA, userB, userC...}} list里面等于查重后 指向一个user
    user_group = collections.defaultdict(list)
    for user, parent in parent.items():
        user_group[parent].append(user)
    # 最后把相同的user集合取出来
    ret = []
    for user_list in user_group.values():
        ret.append(user_list)
    return ret 

def find(parent:dict[str, str], name:str) -> str:
     # parent不是自己: 递归寻找parent 并把自己挂在first level parent上
     # 路径压缩
    if parent[name] != name:
        parent[name] = find(parent, parent[name])
    return parent[name]


# unit test
accounts = {"A1": ['alice@yahoo.com', 'alice_1@gmail.com'],
"A2": ["bob@facebook.com"],
"A3": ["alice_1@gmail.com", "alice_2@hotmail.com"],
"A4": ['alice_2@hotmail.com'],
"A5": ['bob@facebook.com'],
"A6": ['carol@gmail.com']}     
print(accounts_merge(accounts))