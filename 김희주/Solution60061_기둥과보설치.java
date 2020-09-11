package programmers;

import java.util.Arrays;

public class Solution60061 {	//2020 KAKAO BLIND RECRUITMENT > 기둥과 보 설치
	public static void main(String[] args) {
//		int[][] build_frame = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
		int[][] build_frame = {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0}, {2,2,0,1}};
		int[][] result = solution(5, build_frame);
		for (int i = 0; i < result.length; i++) {
			System.out.println(Arrays.toString(result[i]));
		}
	}
	
	static boolean[][][] map;
    public static int[][] solution(int n, int[][] build_frame) {
        map = new boolean[n+3][n+3][2];
        int cnt = 0;
        
        for (int i = 0; i < build_frame.length; i++) {
			int y = build_frame[i][0]+1;
			int x = build_frame[i][1]+1;
			int a = build_frame[i][2];
			int b = build_frame[i][3];
			
			if(b==1) {	//��ġ
				if(a==0) {
					if(canPillar(x,y)) {
						map[x][y][0] = true;
						cnt++;
					}
				}else {
					if(canBeam(x,y)) {
						map[x][y][1] = true;
						cnt++;
					}
				}
			}else {	//����
				if(a==0)
					map[x][y][0] = false;
				else
					map[x][y][1] = false;
				
				if(delete(x,y,a,n)) {
					cnt--;
					continue;
				}
				
				if(a==0)
					map[x][y][0] = true;
				else
					map[x][y][1] = true;
				
			}
		}
        
        int idx = 0;
        int[][] answer = new int[cnt][3];
        for (int j = 1; j <= n+1; j++) {
			for (int i = 1; i <= n+1; i++) {
				for (int k = 0; k < 2; k++) {
					if(map[i][j][k]) {
						answer[idx][0] = j-1;
						answer[idx][1] = i-1;
						answer[idx][2] = k;
						idx++;
					}
				}
			}
		}
        
        return answer;
    }
    static public boolean canPillar(int x,int y) {
    	if(x==1 || map[x-1][y][0] || map[x][y-1][1] || map[x][y][1]) {
    		return true;
    	}
    	return false;
    }
    static public boolean canBeam(int x,int y) {
    	if(map[x-1][y][0] || map[x-1][y+1][0] || (map[x][y-1][1] && map[x][y+1][1])) {
    		return true;
    	}
    	return false;
    }
    static public boolean delete(int x, int y, int a, int n) {
//    	for (int i = 1; i <= n+1; i++) {
//			for (int j = 1; j <= n+1; j++) {
//				if(map[i][j][0]) {
//					if(!canPillar(i, j)) {
//						return false;
//					}
//				}
//				if(map[i][j][1]) {
//					if(!canBeam(i, j)) {
//						return false;
//					}
//				}
//			}
//		}
    	
    	if(a==0) {
    		if(map[x+1][y][0]) {
    			if(!(map[x+1][y][1] || map[x+1][y-1][1]))
    				return false;
    		}
    		if(map[x+1][y-1][1]) {
    			if(!(map[x][y-1][0] || (map[x+1][y-2][1] && map[x+1][y][1])))
    				return false;
    		}
    		if(map[x+1][y][1]) {
    			if(!(map[x][y+1][0] || (map[x+1][y-1][1] && map[x+1][y+1][1])))
    				return false;
    		}
    	}else {
    		if(map[x][y][0]) {
    			if(!(map[x-1][y][0] || map[x][y-1][1]))
    				return false;
    		}
    		if(map[x][y+1][0]) {
    			if(!(map[x-1][y+1][0] || map[x][y+1][1]))
    				return false;
    		}
    		if(map[x][y-1][1]) {
    			if(!(map[x-1][y-1][0] || map[x-1][y][0]))
    				return false;
    		}
    		if(map[x][y+1][1]) {
    			if(!(map[x-1][y+1][0] || map[x-1][y+2][0]))
    				return false;
    		}
    	}
    	return true;
    }
}
