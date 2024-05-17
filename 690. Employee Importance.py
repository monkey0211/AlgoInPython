"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        total = 0
        dict= {}
        # need to build a dict : id-> Employee object
        queue = collections.deque()
        for e in employees:
            if e.id == id:
                queue.append(e)
            dict[e.id] = e

        while queue:
            employee = queue.popleft()
            total += employee.importance 
            if employee.subordinates:
                for sub in employee.subordinates:
                    queue.append(dict[sub]) #给出的是id 需要放入Employee才可以 所以需要建立dict
        return total


        