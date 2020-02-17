package com.algopro.IsValidBST;

class IsValidBST {

	private static class Node {
		public int val;
		public Node left;
		public Node right;

		public Node(int val_) {
			this.val = val_;
			this.left = null;
			this.right = null;
		}
	}

	/**
	 * <h1>ALGORITHM</h1>
	 * <ul>
	 * <li>Consider a node N, a pair of values representing the bounds that the
	 * subtree having N as root has.</li>
	 * 
	 * <li>If N is null, return true since absence of nodes is also valid tree
	 * structure.</li>
	 * 
	 * <li>If value at N is not within the bounds, return false.</li>
	 * 
	 * <li>Recursively call the function, pass right child of N, lower bound as the
	 * value at N, +infinity as upper bound
	 * <p>
	 * If the helper returns false, then the subtree is invalid, hence, return
	 * false.</li>
	 *
	 * <li>Basically the same as step 4, but pass the left child instead.</li>
	 * 
	 * <li>At the exit point, return true because all failure tests are passed.</li>
	 * </ul>
	 * 
	 * @param node  the current node in question, the root of the subtree in
	 *              question
	 * @param lower the lower bound the current subtree's nodes' values should be
	 *              greater than
	 * @param upper the upper bound the current subtree's nodes' values ought to be
	 *              less than
	 * @return true if the current subtree is valid BST, false otherwise.
	 */
	public static boolean Helper(Node node, int lower, int upper) {
		if (node == null)
			return true;
		if (node.val <= lower || node.val >= upper)
			return false;
		if (!Helper(node.right, node.val, upper))
			return false;
		if (!Helper(node.left, lower, node.val))
			return false;
		return true;
	}

	public static boolean Solution(Node root) {
		return Helper(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
	}

	public static void main(String[] args) {
		Node root = new Node(5);
		root.left = new Node(1);
		root.right = new Node(7);
		Node r = root.right;
		r.left = new Node(6);
		r.right = new Node(8);
		System.out.println(Solution(root));
	}
}
