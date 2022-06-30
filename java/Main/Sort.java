package Main;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Sort implements Comparable<Sort>{
    String name;
    int number;

    public Sort(String name){
        this.name = name;
        String names[] = name.split("\\\\");
        this.number = Integer.parseInt(onlyDigits(names[names.length - 1].split("\\.")[0]));
    }

    public String getName(){
        return this.name;
    }

    public int getNumber(){
        return this.number;
    }

    @Override
    public int compareTo(Sort o) {
        return Integer.compare(this.number, o.number);
    }

    public static String onlyDigits(String str) {
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(str);
        StringBuilder res = new StringBuilder("0");
        while(m.find()) {
            res.append(m.group());
        }
        return res.toString();
    }



}
