package main.level1.체육복;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        answer = n - lost.length;

        // 체육복을 빌려주면 -1 을 넣는다.
        // 여벌 체육복 가져온 아이가 체육복을 도난당했을 수 있다.
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (lost[i] == reserve[j]) {
                    answer++;
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }
            }
        }

        // 체육복을 빌려준다.
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                int result = reserve[j] - lost[i];
                if (Math.abs(result) == 1) {
                    answer++;
                    reserve[j] = -1;
                    break;
                }
            }
        }

        return answer;
    }
}