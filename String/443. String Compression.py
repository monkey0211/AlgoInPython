# time O(n) space O(1)
def compress(self, chars: List[str]) -> int:
    if not chars:
        return 0
    res = []
    cnt = 1
    left = 0
    for right in range(1, len(chars)):

        if chars[right] == chars[left]:
            cnt += 1
        else:
            res.append(chars[left])
            res.append("%s" % cnt)

            left = right
            cnt = 1
         #最后剩一个right 要补上
        res.append(chars[left])
        res.append("%s" % cnt)
        return res if len(res) <= len(chars) else chars