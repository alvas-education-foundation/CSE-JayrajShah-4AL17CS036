package ques5;

import java.util.*;
public class BST {

	public class Node{
		
		int key;
		Node left, right;
		public Node(int item) {
			key=item;
			left=null;
			right=null;
		}
		
	}
	  
    Node root; 
  
    
    BST() {  
        root = null;  
    } 
    void insert(int key) { 
        root = insertNode(root, key); 
     } 
      
	Node insertNode(Node root,int key) {
		
		if(root==null) {
			root=new Node(key);
			return root;
		}
		else {
			
			if(key<root.key) {
				root.left=insertNode(root.left,key);
				return root;
			}
			else {
				root.right=insertNode(root.right,key);
				return root;
			}
		}
		
	}
	 void inorder()  { 
	       inorderTr(root); 
	    } 
	void inorderTr(Node root) {
	
		if(root!=null) {
			
	
			inorderTr(root.left);
			System.out.println(root.key);
			inorderTr(root.right);
		}
	}
	public static void main(String[] args) {
	
		
		Scanner sc =  new Scanner(System.in);
		System.out.println("Enter Number of Nodes ");
		int n=sc.nextInt();
		System.out.println("Enter Nodes : ");
		int[] a = new int[n];
		for (int i=0;i<n;i++) {
			a[i]=sc.nextInt();
			
		}
		BST b= new BST();
		for (int i=0;i<n;i++) {
			b.insert(a[i]);
		}
		
		System.out.println("----------Inorder Traversal----------");
		b.inorder();
		//System.out.println(b.root.key);
		
	}

}


