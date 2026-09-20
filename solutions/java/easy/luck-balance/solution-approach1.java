// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true
// Problem     Luck Balance
// Difficulty  Easy
// Subdomain   Greedy
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-09-20, 08:45 p.m.
// ──────────────────────────────────────────────────

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'luckBalance' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER k
     *  2. 2D_INTEGER_ARRAY contests
     */

    public static int luckBalance(int k, List<List<Integer>> contests) {
        int luck = 0;
        List<Integer> important = new ArrayList<>();

        for (List<Integer> contest : contests) {
            int l = contest.get(0);
            int t = contest.get(1);

            if (t == 0) {
                luck += l;
            } else {
                important.add(l);
            }
        }

        Collections.sort(important, Collections.reverseOrder());

        for (int i = 0; i < important.size(); i++) {
            if (i < k) {
                luck += important.get(i);
            } else {
                luck -= important.get(i);
            }
        }

        return luck;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);
        int k = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> contests = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] contestsRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> contestsRowItems = new ArrayList<>();

            for (int j = 0; j < 2; j++) {
                int contestsItem = Integer.parseInt(contestsRowTempItems[j]);
                contestsRowItems.add(contestsItem);
            }

            contests.add(contestsRowItems);
        }

        int result = Result.luckBalance(k, contests);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
