'''
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

 

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
'''


class Solution(object):
    def balancedStringSplit(self, s):
        result, countL, countR = 0, 0, 0
        for i in s:
            if i == 'L':
                countL += 1
            else:
                countR += 1

            if countL == countR:
                countR, countL = 0, 0
                result += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.balancedStringSplit('LLLLRRRR'))
