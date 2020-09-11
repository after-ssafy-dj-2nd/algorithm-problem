package programmers;

public class Solution60059 {	//2020 KAKAO BLIND RECRUITMENT > 자물쇠와 열쇠
	public static void main(String[] args) {
		int[][] key = {{0,0,0},{1,0,0},{0,1,1}};
		int[][] lock = {{1,1,1},{1,1,0},{1,0,1}};
        System.out.println(solution(key, lock));
	}
    public static boolean solution(int[][] key, int[][] lock) {
        int M = key.length;
        int xMax = -1;
        int xMin = lock.length;
        int yMax = -1;
        int yMin = lock.length;
        
        for (int i = 0; i < lock.length; i++) {
			for (int j = 0; j < lock.length; j++) {
				if(lock[i][j]==0) {
					xMax = Math.max(xMax, i);
					xMin = Math.min(xMin, i);
					yMax = Math.max(yMax, j);
					yMin = Math.min(yMin, j);
				}
			}
		}
        
        for (int i = xMax-M+1; i <= xMin; i++) {
			for (int j = yMax-M+1; j <= yMin; j++) {

				for (int r = 0; r < 4; r++) {
					boolean check = true;
					loop:
					for (int x = 0; x < M; x++) {
						for (int y = 0; y < M; y++) {
							if(i+x>=0 && i+x<lock.length && j+y>=0 && j+y<lock.length) {
								if(lock[i+x][j+y] == key[x][y]) {
									check = false;
									break loop;
								}
							}
						}
					}
					if(check) return true;
					
					key = rotate(key);
				}
				
			}
		}
        
        return false;
    }
    
    static public int[][] rotate(int[][] key) {
    	int len = key.length;
    	int[][] copy = new int[len][len];
    	
    	for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				copy[i][j] = key[len-j-1][i];
			}
		}
    	return copy;
    }
}
