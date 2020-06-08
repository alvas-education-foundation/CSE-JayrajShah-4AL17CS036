package ques8;

// CODE BY JAYRAJ
public class SLL {
	
	Node head=null;
	static class Node{
		int value;
		Node next;
		
		Node(int value){
			this.value=value;
			this.next=null;
		}
		
	}
	
	public static void main(String args[]) {
		
		SLL s = new SLL();
		s.insert(1);
		s.insert(2);
		s.insert(3);
		s.insert(4);
		s.insert(5);
	
		s.display();
		s.deleteMiddle();
		s.display();
		
	}
	// CODE BY JAYRAJ
	void insert(int value) {
		if(head==null) {
			head=new Node(value);
		}
		else {
			Node temp=head;
			while(temp.next!=null) {
				temp=temp.next;
			}
			temp.next=new Node(value);
		}
	}
	void deleteMiddle() {
		if(head==null) {
			System.out.println("List is empty");
		}
		// CODE BY JAYRAJ
		else {
			Node temp =head;
			int len=0;
			while(temp!=null) {
				len++;
				temp=temp.next;
			}
			Node del=head;
			int cc=0;
		
			while(cc!=len/2-1) {
				cc++;
				del=del.next;
			
			}
			if(len%2!=0) {
				del=del.next;
			}
			Node prev=head;
			while(prev.next!=del)
				prev=prev.next;
			temp=del.next;
			
			System.out.println("DELETED : "+del.value);
			del.next=null;
			prev.next=temp;
			
			
			
		}
	}
	// CODE BY JAYRAJ
	void display() {
		if(head==null) {
			System.out.println("List is empty");
		}
		else {
			Node temp=head;
			while(temp!=null) {
				System.out.println(temp.value);
				temp=temp.next;
			}
		}
	}

}
//CODE BY JAYRAJ
