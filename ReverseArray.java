
// INTITALIZE         


import java.util.*;
class ReverseArray {

    // public static List<String> reverseArray(List<String> arrayToReverse){
    //     List<String> reversedArray ;
    //     int lengthOfArray = arrayToReverse.size();
    //     int i = lengthOfArray - 1;

    //     while (i >= 0){
    //         //stream 
    //         //
    //         // reversedArray.add();
    //     }
    // }

    public static void main( String [] args){
        // ReverseArray.reversedArray();
        List<String> anArray = new ArrayList<String>();
        List<String> reversedArray = new ArrayList<String>();

        String[] arrayReversed = {"one", "two"};

        Integer[] arrayOfInt = {1,2,3};
        System.out.println("length of array of int " + arrayOfInt.length);


        System.out.println("lenght" + arrayReversed.length);
        anArray.add("one");
        anArray.add("two");
        System.out.println(anArray.size());
        // System.out.println(anArray.);
        // System.out.println(anArray.get(1));
        int i = (int) anArray.size() - 1;
        while (i >= 0){
            reversedArray.add(anArray.get(i));
            i--;
        }
        System.out.println("the output is " + reversedArray);

        String name = "test";
        System.out.println("lenght of name is " + name.length());
    }
}