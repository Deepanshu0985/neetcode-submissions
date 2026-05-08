/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root==null){
            return "";
        }
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> q = new LinkedList<>();
        
        q.offer(root);

        while(!q.isEmpty()){
            TreeNode node = q.poll();
        
            if (node==null){
                sb.append("#,");
                continue;
            }
            sb.append(node.val).append(",");
            q.offer(node.left);
            q.offer(node.right);

        }
        System.out.print(sb);
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty()){
            return null;
        }
        String arr[] = data.split(",");
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
        q.offer(root);
        int i = 1;

        while (i<arr.length && !q.isEmpty()){
            TreeNode node = q.poll();

            if (!arr[i].equals("#")){
                node.left =  new TreeNode(Integer.parseInt(arr[i]));
                q.offer(node.left);
            }
            i++;
            if (!arr[i].equals("#")){
                node.right =  new TreeNode(Integer.parseInt(arr[i]));
                q.offer(node.right);
            } 
            i++;
        }
        
        return root;
    }
}
