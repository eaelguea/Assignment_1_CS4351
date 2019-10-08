/**
 * @author ericelguea
 * @version 1.0
 * OnlineFind performs an online attack to a victim website providing username
 * and trying passwords by brute force
 * 
 * Output from terminal:
   UTEP-160504:src ericelguea$ time ./onlineShell.sh
   johnathan17_-d7A - tx
   real	13m37.274s
   user	0m24.947s
   sys	0m12.560s
 */

import java.util.Random;

public class OnlineFind{
    public static void main(String[] args) throws Exception{
        int length = 2;
        char[] password = generatePasswords(length);
        System.out.println(new String(password));
    }

    /**
     * 
     * @param length
     * @return generates new password
     */
    public static char[] generatePasswords(int length){
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        Random random = new Random();
        char[] password = new char[length];
        int index = 0;

        for(int i=0; i<length; i++){
            index = i(random, length, password);
            password[index] = alphabet.charAt(random.nextInt(alphabet.length()));
        }
        return password;
    }

    /**
     * 
     * @param Random r
     * @param int l
     * @param char[] ch
     * @return position in password string
     */
    public static int i(Random r, int l, char[] ch){
        int index = r.nextInt(l);
        while(ch[index = r.nextInt(l)] !=0);
        return index;
    }
}