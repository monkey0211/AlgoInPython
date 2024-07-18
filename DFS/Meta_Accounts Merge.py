import collections
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