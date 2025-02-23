class Solution {
    int pre_idx=0;
    int post_idx=0;
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        TreeNode* curr = new TreeNode(preorder[pre_idx]);
        pre_idx++;

        if(curr->val != postorder[post_idx])
            curr->left = constructFromPrePost(preorder,postorder);
        if(curr->val != postorder[post_idx])
            curr->right = constructFromPrePost(preorder,postorder);
        
        post_idx++;
        return curr;
    }
};