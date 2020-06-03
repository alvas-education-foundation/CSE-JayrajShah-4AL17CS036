import java.util.Stack;
public class BracketBalance {

	public static boolean brackets(String in) {
		// Use a stack
		Stack<Character> s = new Stack();
		for (char c : in.toCharArray()) {
			if (s.empty()) {
				s.push(c);
				continue;
			}
			char last = s.peek();
			
			switch (c) {
			case ')':
				if (last != '(') {
					return false;
				}
				s.pop();
				break;
			case '}':
				if (last != '{') {
					return false;
				}
				s.pop();
				break;
			case ']':
				if (last != '[') {
					return false;
				}
				s.pop();
				break;
			default:
				if (c=='(' || c=='[' || c=='{') {
					s.push(c);
				}
				if (c==')' || c==']' || c=='}') {
					return false;
				}
				break;
			}
		}
		return true;
	}
	public static void main(String[] args) {
		System.out.println(brackets("()[]{}(([])){[()][]}")); // true
		System.out.println(brackets("())[]{]{}")); // false
	}
}