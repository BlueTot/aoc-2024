package d1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashMap;

public class d1g {
    /**
     * Method used to get input data from given file
     * @param path Path to file
     * @return An array list of strings
     */
    private static ArrayList<String> getInput(String path) {
        ArrayList<String> output = new ArrayList<String>();
        try {
            File myObj = new File(path);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                output.add(myReader.nextLine());
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error occurred");
        }
        return output;
    }

    /**
     * Main method for AOC Day 1 Gold
     * @param args Arguments to method
     */
    public static void main (String[] args) {
        ArrayList<String> data = getInput("d1/data.txt");
        HashMap<Integer, Integer> counterY = new HashMap<Integer, Integer>();

        // populate counter
        for (String row : data) {
            String[] rowItems = row.split("   ");
            Integer key = Integer.parseInt(rowItems[1]);
            if (!counterY.containsKey(key)) {
                counterY.put(key, 1);
            } else {
                counterY.put(key, counterY.get(key) + 1);
            }  
        }
        
        int total = 0;
        for (String row : data) {
            String[] rowItems = row.split("   ");
            Integer key = Integer.parseInt(rowItems[0]);
            total += key * counterY.getOrDefault(key, 0);
        }
        System.out.println(total);
    }
}
