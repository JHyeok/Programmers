package main.level1.평균구하기;

import java.util.Arrays;

public class OtherSolution {
    public double solution(int[] arr) {
        return (int) Arrays.stream(arr).average().orElse(0);
    }
}
