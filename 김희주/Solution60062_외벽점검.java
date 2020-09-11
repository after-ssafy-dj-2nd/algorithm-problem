package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution60062 {	//2020 KAKAO BLIND RECRUITMENT > 외벽 점검
	public static void main(String[] args) {
		int[] weak = {1, 3, 4, 9, 10};
		int[] dist = {3, 5, 7};
		System.out.println(solution(12, weak, dist));
	}
	
	static boolean check;
	static int[] w,d;
    public static int solution(int n, int[] weak, int[] dist) {
        int answer = 0;
        d = dist;
        w = weak;
        
        //인원수 늘려가면서
        for (int i = 1; i <= dist.length; i++) {
        	boolean[] wall = new boolean[n];
        	for (int j = 0; j < weak.length; j++) {
        		wall[weak[j]] = true;
        	}
        	
			dfs(i,0, wall);
			
			if(check) {
				answer = i;
				break;
			}
		}
        
        return check ? answer : -1;
    }
    static public void dfs(int num, int n, boolean[] wall) {
    	if(num==n) {
    		for (int i = 0; i < wall.length; i++) {
				if(wall[i]) 
					return;
			}
    		check = true;
    		return;
    	}
    	
    	for (int i = 0; i < w.length; i++) {
			if(wall[w[i]]) { //아직 고치지 않은 벽 찾아서
				List<Integer> list = new ArrayList<>();
				
				//이동할 수 있는 만큼 고치기
				int idx = w[i];
				for (int j = 0; j <= d[d.length-n-1]; j++) {
					if(wall[idx]) {
						list.add(idx);
						wall[idx] = false;
					}
					if(++idx>=wall.length)
						idx=0;
				}
				
				dfs(num,n+1,wall);
				
				//원상복구
				for (int j = 0; j < list.size(); j++) {
					wall[list.get(j)] = true;
				}
				
				if(check) return;
			}
		}
    }
}
