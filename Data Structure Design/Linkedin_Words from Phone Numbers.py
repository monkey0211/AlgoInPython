import collections
# output all words that can be formed from any n-ditis phone number from the list of given KNOW_WORDS considering the mapping mentioned from phone number
# time o (MN) M is length of wordList, N is length of maxWord. 
class Solution:
    def __init__(self, KNOWN_WORDS, KEYBOARD):
        self.KNOWN_WORDS = KNOWN_WORDS
        self.KEYBOARD = KEYBOARD
        
        #以下是part2优化部分: pre-processing
        # 创建一个新的dict, 存letterToDict, 再创建一个defaultdict, 存word->number
        self.letterToDigit = {}
        for digit, letters in KEYBOARD.items():
            for letter in letters:
                self.letterToDigit[letter] = digit
        
        self.wordDigits = collections.defaultdict(list)
        for word in KNOWN_WORDS:
            tmp = ""
            for i in range(len(word)):
                tmp += self.letterToDigit[word[i]] 
            self.wordDigits[tmp].append(word)
        
    def wordsFromPhoneNumber1(self, phoneNumber):
        phoneNumber = str(phoneNumber)
        res = []
        for word in KNOWN_WORDS:
            flag = False
            for i in range(len(word)):
                if len(phoneNumber) != len(word):
                    break
                if word[i] not in KEYBOARD[phoneNumber[i]]:
                    break
                if i == len(word) - 1:
                    flag = True
            if flag == True:
                res.append(word)
        return res
                
#part2: adjust implementation for use case when new words can be added and existing words can be removed from the dictionary at runtime. 
#需要pre-processing, create letterToDigit dict. 
# 优点: 节省function的处理时间 把处理都放在pre-processing阶段
# 缺点: 1) if words are frequent changing, read queries很少进行的时候. 2) words数量少(体现不出优势)
        
    def wordsFromPhoneNumber2(self, phoneNumber):
        phoneNumber = str(phoneNumber)
        
            
        if phoneNumber in self.wordDigits:
            return self.wordDigits[phoneNumber]
        else:
            return ""
                  

KEYBOARD = {"1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
KNOWN_WORDS = ["careers", "linkedin", "hiring", "interview", "linkedgo"]
phoneNumber1 = 54653346
phoneNumber2 = 2273377
test = Solution(KNOWN_WORDS, KEYBOARD)
print(test.wordsFromPhoneNumber2(phoneNumber1))
print(test.wordsFromPhoneNumber2(phoneNumber2))
