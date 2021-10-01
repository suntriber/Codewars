package _5kyu;

import java.util.ArrayList;

/***********************************************************************************************************************
 * Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation
 * marks untouched.
 *
 * Examples
 * pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
 * pigIt('Hello world !');     // elloHay orldway !
 *
 **********************************************************************************************************************/
public class Simple_Pig_Latin {

    public static void main(String[] args) {


        System.out.println("igPay atinlay siay oolcay" + ", " + pigIt("Pig latin is cool"));
        System.out.println("hisTay siay ymay tringsay" + ", " + pigIt("This is my string"));
        System.out.println("elloHay orldway !" + ", " + pigIt("Hello world !"));
    }


    public static String pigIt(String str) {
        String sp[] = str.split(" ");
        ArrayList<String> arrL = new ArrayList<>();
        for (String s : sp) {
            if (s.contains(".")) {
                s.replace(".", "");
                arrL.add(s.substring(1) + s.charAt(0) + 'a' + 'y');
            } else if (s.chars().allMatch(Character::isLetter)) {
                arrL.add(s.substring(1) + s.charAt(0) + 'a' + 'y');
            }else{arrL.add(s);}
        }

        StringBuilder s = new StringBuilder();
        for (int i = 0; i < arrL.size(); i++) {
            if (i != 0) s.append(" ");
            s.append(arrL.get(i));
        }
        return s.toString();
    }
}


/*
    public static String pigIt(String str) {
        return str.replaceAll("(\\w)(\\w*)", "$2$1ay");
    }

    public static String pigIt(String str) {
        return Arrays.stream(str.trim().split(" "))
                .map(v -> v.matches("[a-zA-Z]+") ? v.substring(1).concat(v.substring(0, 1)).concat("ay") : v)
                .collect(Collectors.joining(" "));
    }

    public class PigLatin {
    public static String pigIt(String str) {
        return Stream.of(str.split(" "))
                .map(word -> word.matches("^[a-zA-Z]+$")
                        ? (new StringBuilder(word)).append(word.charAt(0)).deleteCharAt(0).append("ay").toString()
                        : word)
                .collect(Collectors.joining(" "));
    }

 */