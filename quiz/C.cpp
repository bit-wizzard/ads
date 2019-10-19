#include <iostream>
#include <map>
#include <cstring>

using namespace std;
const int N = 1e6 + 15;
struct TreeNode{
  int val;
  TreeNode * left;
  TreeNode * right;
  TreeNode(int x) {
    val = x;
    left = right = NULL;
  }
};

void insert(int x, TreeNode* &root) {
  TreeNode * cur = new TreeNode(x);
  if (root == NULL) {
    root = cur;
    return;
  }
  else if (x < root -> val) {
    insert(x, root -> left);
  }
  else insert(x, root -> right);
}
int cnt=0;
void leafs(TreeNode * root) {
  if (root == NULL) {
    return;
  }
  if (root -> left == NULL && root -> right == NULL) {
        cnt++;
    //cout << root -> val << '\n';
  }
  leafs(root -> left);
  leafs(root -> right);
}

int main() {
  TreeNode* root = NULL;
  map<int, int> m;
  int x,n;
  cin>>n;
  for(int i=0;i<n;i++) {
        cin>>x;
    if (!x) break;
    if (!m[x]) insert(x, root);
    m[x]++;
  }
  leafs(root);
    cout<<cnt;
}
// с
// const int N = 1e6 + 15;
