package programmers;

import java.util.Stack;

public class Solution60058 {	//2020 KAKAO BLIND RECRUITMENT > °ýÈ£ º¯È¯
	public static void main(String[] args) {
        System.out.println(solution("(()())()"));
	}
    public static String solution(String p) {
    	if(isCorrect(p)) return p;
    	
    	int o = 0;
    	int c = 0;
    	String u = "";
    	String v = "";
    	for (int i = 0; i < p.length(); i++) {
			if(p.charAt(i)=='(') {
				o++;
			}else {
				c++;
			}
			
			if(o==c) {
				u = p.substring(0, i+1);
				if(i+1<p.length()) {
					v = p.substring(i+1);
				}
				break;
			}
		}
    	
    	if(isCorrect(u)) {
    		return u+solution(v);
    	}else {
    		return "("+solution(v)+")"+change(u);
    	}   	
    }
    
    static String change(String str) {
    	StringBuilder sb = new StringBuilder(str.substring(1, str.length()-1));
    	for (int i = 0; i < sb.length(); i++) {
			if(sb.charAt(i)=='(') {
				sb.setCharAt(i, ')');
			}else {
				sb.setCharAt(i, '(');
			}
		}
    	return sb.toString();
    }
    
    static boolean isCorrect(String str) {
    	Stack<Character> stack = new Stack<>();
    	for (int i = 0; i < str.length(); i++) {
			if(str.charAt(i)=='(') {
				stack.add(str.charAt(i));
			}else {
				if(stack.isEmpty())
					return false;
				stack.pop();
			}
		}
    	
    	return stack.isEmpty() ? true : false;
    }
}
