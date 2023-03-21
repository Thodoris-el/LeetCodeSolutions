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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode res = new ListNode();
        ListNode ret = res;
        if(list1 == null && list2 == null){
                ret = null;
                return ret;

            }
        while(list1 !=null && list2 != null){
            res.val = Math.min(list1.val, list2.val);
            if (list1.val < list2.val){
                list1 = list1.next;
            }
            else{
                list2 = list2.next;
            }
            
            res.next = new ListNode();
            res = res.next;
        }
        
        while (list1 != null){
            res.val = list1.val;
            list1 = list1.next;
            if (list1 != null){
                res.next = new ListNode();
                res = res.next;
            }
            else{
                res.next = null;
            } 
        }

        while (list2 != null){
           res.val = list2.val;
            list2 = list2.next;
            if (list2 != null){
                res.next = new ListNode();
                res = res.next;
            }
            else{
                res.next = null;
            }
        }
        return ret;
    }
}
