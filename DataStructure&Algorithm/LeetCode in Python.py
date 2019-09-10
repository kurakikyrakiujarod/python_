#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 1.Two Sum
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in \
                    dict:
                dict[nums[i]] = i
            else:
                return dict[target - nums[i]], i

    # 7. Reverse Integer
    def reverse(self, x):
        a = abs(x)
        num = 0
        while a:
            temp = a % 10
            num = num * 10 + temp
            a = a // 10
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0

    # 9.  Palindrome Number
    def isPalindrome(self, x):
        a = abs(x)
        num = 0
        while a:
            temp = a % 10
            num = num * 10 + temp
            a //= 10
        if x >= 0 and x == num:
            return True
        else:
            return False

    # 13.  Roman To Integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                       "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                result += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                result += numeral_map[s[i]]
        return result

    # 14. Longest Common Prefix
    def longestCommonPrefix(self, strs):
        result = ''
        i = 0
        while True:
            try:
                temp = set([string[i] for string in strs])
                if len(temp) == 1:
                    result += temp.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result

    # def longestCommonPrefix(self, strs):
    #     if not strs:
    #         return ''
    #     for i in range(len(strs[0])):
    #         for string in strs[1:]:
    #             if i >= len(string) or strs[0][i] != string[i]:
    #                 return strs[0][:i]
    #     return strs[0]

    # 20. Valid Parentheses
    def isValid(self, s):
        stack = []
        lookup = {'(': ')', '[': ']', '{': '}'}
        for parentheses in s:
            if parentheses in lookup:
                stack.append(parentheses)
            elif len(stack) == 0 or lookup[stack.pop()] != parentheses:
                return False
        return len(stack) == 0

    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
                # print(nums)
        return count + 1

    # 27. Remove Element
    def removeElement(self, nums, val):
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[last], nums[i] = nums[i], nums[last]
                last -= 1
            else:
                i += 1
        return last + 1

    # 28. Implement strStr()
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    # 35. Search Insert Position
    def searchInsert(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

    # 38. Count and Say
    def countAndSay(self, n):
        seq = '1'
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ''
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq

    # 53. Maximum Subarray
    def maxSubArray(self, nums):
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
            # print(num,local_max,global_max)
        return global_max

    # 58. Length of Last Word
    def lengthOfLastWord(self, s):
        count = 0
        local_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count
        return count

    #  66. Plus One
    def plusOne(self, digits):
        num = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(num)]
        # for i in reversed(range(len(digits))):
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] += 1
        #         return digits
        # digits[0] = 1
        # digits.append(0)
        # return digits

    # 67. Add Binary
    def addBinary(self, a, b):
        # return str(bin(int(a, 2) + int(b, 2))).replace("0b", '')
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result += str(val)
        if carry:
            result += "1"
        return result[::-1]

    # 69. Sqrt(x)
    def mySqrt(self, x):
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1

        # for i in range(x + 1):
        #     if i ** 2 > x:
        #         return i - 1
        # return x

        # if x <= 1:
        #     return x
        # r = x
        # while r > x / r:
        #     r = (r + x / r) // 2
        # return int(r)

    # 70. Climbing Stairs
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # else:
        #     s1 = self.climbStairs(n - 1)
        #     s2 = self.climbStairs(n - 2)
        #     return s1 + s2

    # 83. Remove Duplicates from Sorted List
    def deleteDuplicates(self, head):
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head

    # 88. Merge Sorted Array
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m - 1 + n] = nums2[n - 1]
                n -= 1
            else:
                nums1[m - 1], nums1[m - 1 + n] = nums1[m - 1 + n], nums1[m - 1]
                m -= 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]

    # 100. Same Tree
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    # 101. Symmetric Tree
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)

    # 104. Maximum Depth of Binary Tree
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 107. Binary Tree Level Order Traversal II
    def levelOrderBottom(self, root):
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]

    # 108. Convert Sorted Array to Binary Search Tree
    def sortedArrayToBST(self, nums):
        def to_bst(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums, start, mid - 1)
            node.right = to_bst(nums, mid + 1, end)
            return node

        return to_bst(nums, 0, len(nums) - 1)

    # 110. Balanced Binary Tree
    def isBalanced(self, root):
        def get_height(root):
            if root is None:
                return 0
            left_tree, right_tree = get_height(root.left), get_height(root.right)
            if left_tree < 0 or right_tree < 0 or abs(left_tree - right_tree) > 1:
                return -1
            return max(left_tree, right_tree) + 1

        return get_height(root) >= 0

    # 111. Minimum Depth of Binary Tree
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # 112. Path Sum
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 118. Pascal's Triangle
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result

    # 119. Pascal's Triangle II
    def getRow(self, rowIndex):
        result = [1] + [0] * rowIndex
        # print(result)
        for i in range(rowIndex):
            for j in range(i + 1, 0, -1):
                result[j] = result[j] + result[j - 1]
                # print(result)
        return result

    # 121. Best Time to Buy and Sell Stock
    # def maxProfit(self, prices):
    #     max_profit, min_price = 0, float('inf')
    #     for price in prices:
    #         min_price = min(price, min_price)
    #         max_profit = max(max_profit, price - min_price)
    #     return max_profit

    # 122. Best Time to Buy and Sell Stock II
    def maxProfit(self, prices):
        # if len(prices) <= 1:
        #     return 0
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        return total

    # 125. Valid Palindrome
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    # 136. Single Number
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 5]
    target = 7
    # print(s.twoSum(nums, target))
    # print(s.reverse(112233))
    # print(s.isPalindrome(121))
    # print(s.romanToInt('IX'))
    # print(s.romanToInt('MCMXCIV'))
    # print(s.longestCommonPrefix(['flower', 'flower', 'flowerflower']))
    # print(s.isValid('([])'))
    # print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    # print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    # print(s.strStr('hello', 'll'))
    # print(s.searchInsert([1, 2, 3, 5], 9))
    # print(s.searchInsert([1, 2, 3, 5], 1))
    # print(s.countAndSay(6))
    # print(s.maxSubArray([-2, 1, -4, 4, -2, 2, 1, -5, 4]))
    # print(s.lengthOfLastWord('hello python'))
    # print(s.plusOne([9, 9, 9]))
    # print(s.addBinary('10', '100'))
    # print(s.mySqrt(101))
    # print(s.climbStairs(20))
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [1, 1, 6]
    # n = 3
    # print(s.merge(nums1=nums1, m=m, nums2=nums2, n=n))
    # print(nums1)
    # print(s.generate(5))
    print(s.getRow(3))
