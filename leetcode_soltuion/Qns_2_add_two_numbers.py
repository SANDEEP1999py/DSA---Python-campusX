# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_num = str()
        l2_num = str()
        for i in range(len(l1)):
            l1_num = str(l1[i]) + l1_num
        for i in range(len(l2)):
            l2_num = str(l2[i]) + l2_num
        num = int(l1_num) + int(l2_num)
        num_arr = []
        i = 10
        while num != 0:
            reminder = num % i
            num_arr.append(int(reminder))
            num = int(num / i)
        return num_arr


if __name__ == "__main__":
    qns = Solution()
    reverse_l1 = qns.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])
    print(reverse_l1)