package d1;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class d1s {
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
     * Main method for AOC Day 1 Silver
     * @param args Arguments to method
     */
    public static void main (String[] args) {
        ArrayList<String> data = getInput("d1/data.txt");
        
        // parsing
        ArrayList<Integer> parsedDataX = new ArrayList<Integer>();
        ArrayList<Integer> parsedDataY = new ArrayList<Integer>();
        for (int i = 0; i < data.size(); i++) {
            String[] row = data.get(i).split("   ");
            parsedDataX.add(Integer.parseInt(row[0]));
            parsedDataY.add(Integer.parseInt(row[1]));
        }
        Collections.sort(parsedDataX);
        Collections.sort(parsedDataY);
        int total = 0;
        for (int i = 0; i < parsedDataX.size(); i++) {
            total += Math.abs(parsedDataX.get(i) - parsedDataY.get(i));
        }
        System.out.println(total);
    }
}