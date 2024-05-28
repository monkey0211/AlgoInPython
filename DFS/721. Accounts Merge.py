class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        visited = set()
        res = []
        
        # Building adjacency list:
        # for every email, add edge between first email to all other emails in the account
        for account in accounts:
            firstemail = account[1]

            for i in range(2, len(account)):
                graph[firstemail].add(account[i])
                graph[account[i]].add(firstemail)
                
        

        for account in accounts:
            node = account[1]
            
            if node not in visited:
                visited.add(node)
                emaillist = []
                emaillist.append(account[0])
                emaillist.append(node)

                self.dfs(node, emaillist, graph, visited)

                emaillist[1:] = sorted(emaillist[1:])
                res.append(emaillist)

        return res

    def dfs(self, node, emaillist, graph, visited):
        if node not in graph:
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                emaillist.append(neighbor)
                self.dfs(neighbor, emaillist, graph, visited)
                
    