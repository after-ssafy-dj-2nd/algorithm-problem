package programmers;

import java.util.*;

public class Solution42889 {	//2019 KAKAO BLIND RECRUITMENT > 실패율
	public static void main(String[] args) {
		int N = 5;
		int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
		int[] answer = solution(N,stages);
		for (int i = 0; i < answer.length; i++) {
			System.out.print(answer[i]+" ");
		}
	}
	public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        User[] stage = new User[N];
        
        for (int i = 0; i < N; i++) {
        	stage[i] = new User();
		}
        
        for (int i = 0; i < stages.length; i++) {
        	for (int j = 1; j <= stages[i]; j++) {
        		if(j>N) break;
        		//스테이지 도달한 플레이어 수
        		stage[j-1].challenge++;
        	}
        	if(stages[i]<=N) {
        		//아직 클리어하지 못한 플레이어 수
        		stage[stages[i]-1].fail++;        		
        	}
		}
        
        for (int i = 0; i < N; i++) {
        	stage[i].stage = i+1;
        	if(stage[i].challenge==0 || stage[i].fail==0)	//스테이지에 도달한 유저가 없는 경우
        		stage[i].fail = 0.0;
        	else
        		stage[i].fail = (double) stage[i].fail / stage[i].challenge;
		}
        
        //실패율 내림차순, 스테이지 오름차순
        Arrays.sort(stage);
        
        for (int i = 0; i < N; i++) {
			answer[i] = stage[i].stage;
		}        
        
        return answer;
    }
	static class User implements Comparable<User>{
		int stage, challenge;
		double fail;
		@Override
		public int compareTo(User o) {
			if(o.fail == this.fail)
				return this.stage - o.stage;
			else if(o.fail - this.fail > 0)
				return 1;
			else
				return -1;
		}	
	}
}
