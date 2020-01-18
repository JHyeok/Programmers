package main.level1.체육복;

import java.util.HashSet;

class OtherSolution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        answer = n;

        for (int i = 0; i < lost.length; i++) {
            boolean rent = false;
            int j = 0;
            while (!rent) {
                if (j == reserve.length) break;
                if (lost[i] == reserve[j]) {
                    reserve[j] = -1;
                    rent = true;
                } else if (lost[i] - reserve[j] == 1) {
                    reserve[j] = -1;
                    rent = true;
                } else if (lost[i] - reserve[j] == -1) {
                    reserve[j] = -1;
                    rent = true;
                } else {
                    j++;
                }
            }
            if (!rent) answer--;
        }
        return answer;
    }
}

class OtherSolutionTwo {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        HashSet<Integer> ko = new HashSet<Integer>();
        for (int k : reserve) {
            ko.add(k);
        }
        for (int i = 0; i < lost.length; i++) {
            if (ko.contains(lost[i])) {
                //System.out.println("내껀내가입지");
                answer++;
                ko.remove(lost[i]);
                lost[i] = -1;
            }
        }


        for (int i = 0; i < lost.length; i++) {
            //System.out.println(i);

            if (ko.contains(lost[i] - 1)) {
                //System.out.println("있다");
                answer++;
                ko.remove(lost[i] - 1);
            } else if (ko.contains(lost[i] + 1)) {
                //System.out.println("있다");
                answer++;
                ko.remove(lost[i] + 1);
            }
            //System.out.println("없다");
        }


        return answer;
    }
}