class RandomizedSet:
# 用hashmap + array(list):  dict[val] = index of array, array[index] = val
# insert:  直接append
# delete: 每次先把list尾巴元素和原来元素交换 然后删除最后一个(list.pop)
# getRandom: 随机数random.randomint(0, len-1)

    def __init__(self):
        self.list = []
        self.dict = {}      

    def insert(self, val: int) -> bool:
        #list: append. dict: add val->index in array
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            index = len(self.list)-1
            self.dict[val] = index
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]       
            lastValue = self.list[-1]

            #list里面的需要remove的元素和tail交换(只需要记住交换之后当前位置元素即可), 然后pop tail
            self.dict[lastValue] = index
            self.list[index] = lastValue 

            del self.dict[val]
            self.list.pop()
            return True
        return False     

    def getRandom(self) -> int
        prob = random.randint(0, len(self.list)-1)
        return self.list[prob]
        