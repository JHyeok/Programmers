package main.level2.탑;

public class OtherSolution {
    // 다른 사람의 풀이1
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length];

        for (int i = heights.length - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (heights[j] > heights[i]) {
                    answer[i] = j + 1;
                    break;
                }
            }
        }

        return answer;
    }

    // 다른 사람의 풀이2
    public int[] solutionTwo(int[] heights) {
        int[] answer = new int[heights.length];

        for (int i = 0; i < heights.length; i++) {
            for (int j = i + 1; j < heights.length; j++) {
                if (heights[i] > heights[j]) {
                    answer[j] = i + 1;
                }
            }
        }


        return answer;
    }
}
