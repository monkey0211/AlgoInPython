import collections


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
            if not graph[email1]: 
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