package programmers;

import java.util.*;

public class Solution42890 {	//2019 KAKAO BLIND RECRUITMENT > 후보키
	public static void main(String[] args) {
		String[][] relation = {{"100","ryan","music","2"}, {"200","apeach","math","2"}, {"300","tube","computer","3"}, 
				{"400","con","computer","4"}, {"500","muzi","music","3"}, {"600","apeach","music","2"}};
		System.out.println(solution(relation));
	}
	
	static ArrayList<HashSet<Integer>> key;
	static int csize;
	static String[][] table;
	public static int solution(String[][] relation){
		key = new ArrayList<>();
		csize = relation[0].length;
		table = relation;
		
		//부분집합 만들기
		for(int i = 1 ; i <= csize ; ++i) {
			dfs(0, 0, i, new HashSet<>());
		}
		
		return key.size();
	}

	static public void dfs(int idx, int n, int size, HashSet<Integer> hs) {
		if(n == size) {		
			for (int i = 0; i < key.size(); i++) {
				//최소성 체크(이미 만들어진 후보키가 포함되어있는지)
				if(hs.containsAll(key.get(i)))
					return;
			}
			
			//유일성 체크
			HashSet<String> unique = new HashSet<>();
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < table.length; i++) {
				for(int j: hs) {
					sb.append(table[i][j]+"/");
				}
				unique.add(sb.toString());
				sb.delete(0, sb.length());
			}
			
			if(unique.size()==table.length) {
				key.add(hs);
			} 
			return;
		}
		
		for(int i = idx; i < csize ; ++i) {
			HashSet<Integer> nhs = new HashSet<>(hs);
			nhs.add(i);
			dfs(i+1, n + 1, size, nhs);
		}
	}
}
