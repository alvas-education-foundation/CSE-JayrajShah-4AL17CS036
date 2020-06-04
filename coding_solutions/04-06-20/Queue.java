package ques7;
import java.util.*;

public class Queue {
	
	int capacity;
	int[] a;
	int rear,front,size;
	public Queue(int capacity) {
		this.capacity=capacity;
		this.front=this.size=this.rear=0;
		this.a=new int[this.capacity];
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue queue = new Queue(1000);
		queue.menu();
	}
	
	public void add(int element) {
	
		if(isFull()) {
			System.out.println("Queue is Full");
			return;
		}

		else {
			a[this.rear++]=element;
			this.size++;
		}
		
	}
	
	public void delete() {
		if(isEmpty()) {
			System.out.println("Queue is Empty");
			return;
		}
		else {
			System.out.println("Deleted "+this.a[this.front]+" at "+ (this.front+1));
			this.front++;
			this.size--;
			
		}
	}
	public void display() {
		if(isEmpty()) {
			System.out.println("Queue is Empty");
			return;
		}
		else {
			for(int i = this.rear-1 ; i >= this.front;i--) {
				System.out.print(this.a[i]+" ");
			}
			System.out.println();
		}
	}
	public boolean isFull() {
		if(this.size==this.capacity) {return true;}
		else return false;
	}
	public boolean isEmpty() {
		if(this.size==0 && this.capacity>0) {return true;}
		else return false;
	}
	public void menu() {
		int ch;
		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter your choice");
		System.out.println("1. Add");
		System.out.println("2. Delete");
		System.out.println("3. Display");
		System.out.println("4. Exit");
		System.out.println("-----Enter Your Choice-----");
		ch = sc.nextInt();
		switch(ch) {
		
		case 1 :
			System.out.println("Enter a element");
			int ele=sc.nextInt();
			add(ele);
			menu();
			break;
		case 2 :
			delete();
			menu();
			break;
		case 3 :
			display();
			menu();
			break;
		case 4 :
			return;
		default:
			System.out.println("Invalid Input");
			menu();
			
		}
	}
}




















