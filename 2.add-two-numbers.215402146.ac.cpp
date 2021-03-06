/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (30.71%)
 * Total Accepted:    791K
 * Total Submissions: 2.6M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum=NULL,*tail=NULL;
        int carry = 0;
        while(l1!=NULL || l2!=NULL){
            int val1 = (l1==NULL) ? 0 : l1->val;
            int val2 = (l2==NULL) ? 0 : l2->val;
            int add = val1 + val2 + carry;
            carry = add/10;
            add %= 10;
            if(sum==NULL){
                sum = tail = new ListNode(add);
            }else{
                tail->next = new ListNode(add);
                tail = tail->next;
            }
            l1 = (l1==NULL) ? l1 : l1->next;
            l2 = (l2==NULL) ? l2 : l2->next;
        }
        if(carry!=0)
            tail->next = new ListNode(carry);
        return sum;
    }
};
//solution record
