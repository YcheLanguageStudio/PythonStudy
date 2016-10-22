package Prime;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/**
 * Created by cheyulin on 10/22/16.
 */
public class AllPrimes {

    public static int calculateNumber(int Nmax) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("../primes.txt"));
        boolean[] isPrime = new boolean[Nmax + 1];
        for (int i = 3; i <= Nmax; i += 2)
            isPrime[i] = true;
        isPrime[2] = true;
        for (int i = 3; i <= Math.sqrt(Nmax); i += 2) {
            if (isPrime[i]) {
                int j = i * i;
                int n = i;
                while (j <= Nmax) {
                    isPrime[j] = false;
                    while (Nmax / j >= i) {
                        isPrime[j *= i] = false;
                    }
                    n += 2;
                    while (!isPrime[n])
                        n += 2;
                    j = i * n;
                }
            }
        }
        int primeNum = 0;
        for (int i = 1; i <= Nmax; i++) {
            if (isPrime[i] == true) {
                bufferedWriter.write(Integer.toString(i));
                bufferedWriter.newLine();
                primeNum++;
            }
        }
        bufferedWriter.close();
        return primeNum;
    }

    public static void main(String[] args) throws IOException {
        final int Nmax = 10000000;
        double startTime = System.currentTimeMillis();
        int primeNum = AllPrimes.calculateNumber(Nmax);
        double timeSpent = (System.currentTimeMillis() - startTime) / 1000;
        System.out.println("The prime numbers from 1 to " + Nmax + " is " + primeNum);
        System.out.println("Time spent : " + timeSpent + " s");
    }
}
