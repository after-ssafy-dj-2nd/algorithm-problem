package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Solution60063 {	//2020 KAKAO BLIND RECRUITMENT > 블록 이동하기
	public static void main(String[] args) {
		int[][] board = {{0, 0, 0, 1, 1},{0, 0, 0, 1, 0},{0, 1, 0, 1, 1},{1, 1, 0, 0, 1},{0, 0, 0, 0, 0}};
        System.out.println(solution(board));
	}
    public static int solution(int[][] board) {
        int len = board.length;
        boolean[][][] visited = new boolean[len][len][2];
        Queue<Robot> queue = new LinkedList<>();
        queue.add(new Robot(0,0,0,0));
        visited[0][0][0] = true;
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        int[] r1 = {0,-1};
        int[] r2 = {1,0};
        while(!queue.isEmpty()) {
        	Robot r = queue.poll();
        	
        	if(r.x == len-1 && r.y == len-1) return r.time;
        	if(r.dir==0) {
        		if(r.x == len-1 && r.y+1 == len-1) return r.time;
        	}else {
        		if(r.x+1 == len-1 && r.y == len-1) return r.time;
        	}
        	
        	for (int d = 0; d < dx.length; d++) {
				int nx = r.x+dx[d];
				int ny = r.y+dy[d];
				if(nx>=0 && nx<len && ny>=0 && ny<len && !visited[nx][ny][r.dir] && board[nx][ny]==0) {
					if(r.dir==0) {
						if(ny+1>=len || board[nx][ny+1]==1) continue;
					}else {
						if(nx+1>=len || board[nx+1][ny]==1) continue;
					}
					queue.add(new Robot(nx,ny,r.time+1,r.dir));
					visited[nx][ny][r.dir] = true;
				}
			}
			if (r.dir == 0) {
				for (int d = 0; d < 2; d++) {
					int nx1 = r.x + r1[d];
					int nx2 = r.x + r2[d];
					if (nx1 >= 0 && nx1 < len && nx2 >= 0 && nx2 < len) {
						if((d==0 && board[nx2][r.y] == 0 && board[nx2][r.y + 1] == 0) || 
								(d==1 && board[nx1][r.y] == 0 && board[nx1][r.y + 1] == 0)) {
							if (!visited[nx1][r.y][1]) {
								queue.add(new Robot(nx1, r.y, r.time + 1, 1));
								visited[nx1][r.y][1] = true;
							}
							if (!visited[nx1][r.y + 1][1]) {
								queue.add(new Robot(nx1, r.y + 1, r.time + 1, 1));
								visited[nx1][r.y + 1][1] = true;
							}
						}
					}
				}
			} else {
				for (int d = 0; d < 2; d++) {
					int ny1 = r.y + r1[d];
					int ny2 = r.y + r2[d];
					if (ny1 >= 0 && ny1 < len && ny2 >= 0 && ny2 < len && board[r.x][ny2] == 0 && board[r.x + 1][ny2] == 0) {
						if((d==0 && board[r.x][ny2] == 0 && board[r.x+1][ny2] == 0) || 
								(d==1 && board[r.x][ny1] == 0 && board[r.x+1][ny1] == 0)) {
							if (!visited[r.x][ny1][0]) {
								queue.add(new Robot(r.x, ny1, r.time + 1, 0));
								visited[r.x][ny1][0] = true;
							}
							if (!visited[r.x + 1][ny1][0]) {
								queue.add(new Robot(r.x + 1, ny1, r.time + 1, 0));
								visited[r.x + 1][ny1][0] = true;
							}
						}
					}
				}
			}
        }
        return 0;
    }
    
    static class Robot {
    	int x, y, time, dir;

		public Robot(int x, int y, int time, int dir) {
			this.x = x;
			this.y = y;
			this.time = time;
			this.dir = dir;
		}
    }
}
