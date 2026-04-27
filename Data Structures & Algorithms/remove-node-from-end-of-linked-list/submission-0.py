# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Bước 1: Reverse lần 1 (Đảo ngược danh sách)
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Sau bước này, 'prev' là đầu của danh sách đã đảo ngược
        new_head = prev
        
        # Bước 2: Xóa node thứ n (bây giờ là từ đầu tính lại)
        # Trường hợp đặc biệt: Xóa ngay cái đầu tiên (n = 1)
        if n == 1:
            new_head = new_head.next
        else:
            # Tìm node đứng TRƯỚC node cần xóa (vị trí n-1)
            cur = new_head
            for _ in range(n - 2): # Đi n-2 bước để đến node thứ n-1
                if cur:
                    cur = cur.next
            
            # Thực hiện xóa bằng cách nhảy cóc
            if cur and cur.next:
                cur.next = cur.next.next
        
        # Bước 3: Reverse lần 2 (Đưa danh sách về hướng ban đầu)
        prev_back = None
        curr_back = new_head
        while curr_back:
            tmp_back = curr_back.next
            curr_back.next = prev_back
            prev_back = curr_back
            curr_back = tmp_back
            
        # Trả về 'prev_back' là head cuối cùng sau khi đã sửa đổi
        return prev_back
        




        


        