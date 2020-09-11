package programmers;

import java.util.Arrays;

public class Solution60060 {	//2020 KAKAO BLIND RECRUITMENT > 가사 검색
	public static void main(String[] args) {
		String[] words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
		String[] queries = {"fro??", "????o", "fr???", "fro???", "pro?"};
        System.out.println(Arrays.toString(solution(words, queries)));
	}
    public static int[] solution(String[] words, String[] queries) {
    	//유효성 X
    	int[] answer = new int[queries.length];
    	
    	for (int i = 0; i < queries.length; i++) {
			int start = -1;
			int end = -1;
			
			//문자 시작,끝 지점 확인
			for (int j = 0; j < queries[i].length(); j++) {
				if(queries[i].charAt(j)!='?') {
					if(start==-1) {
						start = j;
						end = j+1;
						continue;
					}else {
						end = j+1;
					}
				}
			}
			
			if(start==end) {	//모두 ? 경우
				for (int j = 0; j < words.length; j++) {
					if(words[j].length() == queries[i].length()) 
						answer[i]++;
				}
			}else {
				for (int j = 0; j < words.length; j++) {
					if(words[j].length() == queries[i].length() && words[j].substring(start, end).equals(queries[i].substring(start, end))) 
						answer[i]++;
				}
			}			
		}
        return answer;
    }
}
