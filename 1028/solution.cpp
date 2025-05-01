#include <iostream>
#include <stack>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* recoverFromPreorder(string traversal) {
        stack<TreeNode*> stack;
        string current_number_str = "";
        int current_depth = 0;
    
        traversal += '-';
            
        for (int i = 0; i < traversal.size(); i++) {
            if (traversal[i] == '-') {
                if (current_number_str != "") {
                    int current_number = stoi(current_number_str);
                    current_number_str = "";
                    TreeNode* new_node = new TreeNode(current_number);

                    while (stack.size() > current_depth) {
                        stack.pop();
                    }

                    if (!stack.empty()) {
                        if (stack.top()->left == nullptr) {
                            stack.top()->left = new_node;
                        } else {
                            stack.top()->right = new_node;
                        }
                    }

                    stack.push(new_node);
                    current_depth = 0;
                }
                current_depth += 1;
            } else {
                current_number_str += traversal[i];
            }
        }

        TreeNode* result = nullptr;
        while (!stack.empty()) {
            if (stack.size() == 1) {
                result = stack.top();
            }
            stack.pop();
        }

        return result;
    }
};

void printTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    cout << root->val << " ("; 
    printTree(root->left);
    cout << ", ";
    printTree(root->right);
    cout << ")";
}

int main() {
    printTree(Solution().recoverFromPreorder("1-2--3--4-5--6--7"));
    cout << endl;
    printTree(Solution().recoverFromPreorder("1-2--3---4-5--6---7"));
    cout << endl;
    printTree(Solution().recoverFromPreorder("1-401--349---90--88"));
    cout << endl;

    return 0;
}

