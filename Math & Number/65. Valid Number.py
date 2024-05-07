class Solution:
    # 对每种形式的字符进行判断, decimal, exponential, digit, sign作为flag判断之前是否见过
    # rules:
    # 2. decimal: only once, not after exponential
    # 3. "+-" sign: only first place, or after "Ee"(不需要考虑, in case of exponential, will consider this)
    # 4. "Ee" exponential: only once, only after digit
    # 5. anything else: return False
    # 6. return digit, 不是True. eg. "21e"

    def isNumber(self, s: str) -> bool:
        if not s: return False
        decimal, exponential, digit, sign = False, False, False, False

        for c in s:
            if c in "1234567890":
                digit = True
            elif c in "+-":
                if digit or decimal or sign: ## after "Ee"的情况在这里可以不考虑. after "Ee" those will flip and re-consider.
                    return False
                else:
                    sign = True
            elif c in "Ee":
                if exponential or digit==False:
                    return False
                else:
                    exponential = True
                    # 其他三种类型都重新activate, allowed. 
                    digit = False
                    sign = False
                    decimal = False
            elif c == ".":
                if decimal or exponential:
                    return False
                else:
                    decimal = True
            else:
                return False
        return digit

