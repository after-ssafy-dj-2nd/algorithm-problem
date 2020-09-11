package programmers;

public class Solution60057 {	//2020 KAKAO BLIND RECRUITMENT > 문자열 압축
	public static void main(String[] args) {
        System.out.println(solution("aabbaccc"));
	}
    public static int solution(String s) {
        int answer = s.length();
        
        for (int i = 1; i <= s.length()/2; i++) {
			StringBuilder sb = new StringBuilder();
			
			String str = s.substring(0,i);
			int cnt = 1;
			for (int j = i; j < s.length(); j += i) {
				String word = "";
				
				if(j+i > s.length()) {
					word = s.substring(j,s.length());
				}else {
					word = s.substring(j, j+i);
				}
				
				if(word.equals(str)) {
					cnt++;
				}else {
					if(cnt>1) {
						sb.append(cnt+str);
						cnt = 1;
					}else {
						sb.append(str);						
					}
					
					str = word;
				}
			}
			
			if(cnt>1) {
				sb.append(cnt+str);
			}else {
				sb.append(str);
			}
			
			answer = Math.min(answer, sb.length());
		}
        return answer;
    }
}
