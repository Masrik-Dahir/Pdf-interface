package Main;// Merging multiple pdf documents here

import org.apache.pdfbox.multipdf.PDFMergerUtility;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Restart implements Comparable  {

    ArrayList<String> arr = null;
    public Restart(){
        arr = new ArrayList<>();
    }

    public String merge(String path) throws IOException {
        // Instantiating PDFMergerUtility class
        this.walk(path);
        PDFMergerUtility obj = new PDFMergerUtility();
        Restart restart = new Restart();
        String root = restart.parent(arr.get(0));

        obj.setDestinationFileName(root + "result.pdf");

        ArrayList<Sort> before_sort = new ArrayList<>();
        for (String i: arr){
            before_sort.add(new Sort(i));
        }
        Collections.sort(before_sort);

        ArrayList<String> after_sort = new ArrayList<>();
        for (Sort i: before_sort){
            after_sort.add(i.getName());
        }

        for(String i: after_sort){
            obj.addSource(new File(i));
        }

        obj.mergeDocuments(null);

        return "result.pdf";
    }

    public ArrayList<String> walk( String path) {

        File root = new File( path );
        File[] list = root.listFiles();

        if (list == null)
            return arr;

        for ( File f : list ) {
            if ( f.isDirectory() ) {
                walk( f.getAbsolutePath() );
//                System.out.println( "Dir:" + f.getAbsoluteFile() );
            }
            else {
//                System.out.println( "File:" + f.getAbsoluteFile() );
                arr.add(f.getAbsoluteFile().toString());
            }
        }

        return arr;
    }

    public String parent(String dir){
        String dirs[] = dir.split("\\\\");
        StringBuilder br = new StringBuilder();
        for (int i = 0; i <= dirs.length - 2; i++){
            br.append(dirs[i]).append("\\\\");
        }
        return br.toString();
    }

    public int toInt(String str){
        return Integer.parseInt(str.split("\\.")[0]);

    }


    @Override
    public int compareTo(Object o) {
        return 0;
    }
}
