/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int rem = 0;
        ListNode res = new ListNode((l1.val + l2.val)% 10);
        rem = (l1.val + l2.val) / 10;
        ListNode res1 = res;
        while (l1.next != null && l2.next != null){
            l1 = l1.next;
            l2 = l2.next;
            ListNode tmp = new ListNode((l1.val + l2.val + rem) % 10);
            rem = (l1.val + l2.val + rem) / 10;
            res.next = tmp;
            res = res.next;
        }
        while (l1.next != null){
            l1 = l1.next;
            ListNode tmp = new ListNode((l1.val + rem) % 10);
            rem = (l1.val + rem) / 10;
            res.next = tmp;
            res = res.next;
        }
        while (l2.next != null){
            l2 = l2.next;
            ListNode tmp = new ListNode((l2.val + rem) % 10);
            rem = (l2.val + rem) / 10;
            res.next = tmp;
            res = res.next;
        }
        if (rem != 0){
            ListNode tmp = new ListNode(rem);
            rem = 0;
            res.next = tmp;
            res = res.next;
        }
        return res1;
    }
}
