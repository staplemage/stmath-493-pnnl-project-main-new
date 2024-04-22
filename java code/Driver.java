import java.io.*;
import java.util.ArrayList;

public class Driver {
    // Constant defining the size of chunks to read from each DNA file. 
    // It's set to 1 to compare the DNA sequences one character at a time.
    private static final int CHUNK_SIZE = 1;

    public static void main(String[] args) {
        // Initial message for indicating the start of the program
        System.out.println("Testing");

        // An ArrayList to store the similarity score for each chunk compared.
        ArrayList<Float> similarityScores = new ArrayList<>();

        // Using try-with-resources for automatic resource management
        try (BufferedReader reader1 = new BufferedReader(new FileReader("dna1.txt"));
             BufferedReader reader2 = new BufferedReader(new FileReader("dna2.txt"))) {

            // Buffers to store the chunks of DNA sequences being compared.
            char[] buffer1 = new char[CHUNK_SIZE];
            char[] buffer2 = new char[CHUNK_SIZE];

            // Variables to keep track of the number of characters read from each file
            int readChars1, readChars2;

            // Counter for extra nucleotides and a flag to identify which DNA is longer
            int extraNucleotides = 0;
            boolean isDNA1Longer = false;

            // Looping indefinitely to read and compare the DNA sequences
            while (true) {
                // Reading chunks from both DNA files
                readChars1 = reader1.read(buffer1, 0, CHUNK_SIZE);
                readChars2 = reader2.read(buffer2, 0, CHUNK_SIZE);

                // Checking if the end of either file is reached
                if (readChars1 == -1 || readChars2 == -1) {
                    // If DNA1 ends before DNA2
                    if (readChars1 == -1) {
                        // Counting the remaining characters in DNA2
                        extraNucleotides += readChars2;
                        while ((readChars2 = reader2.read(buffer2, 0, CHUNK_SIZE)) != -1) {
                            extraNucleotides++;
                        }
                    }
                    // If DNA2 ends before DNA1
                    else if (readChars2 == -1) {
                        isDNA1Longer = true; // Setting flag as DNA1 is longer
                        // Counting the remaining characters in DNA1
                        extraNucleotides += readChars1;
                        while ((readChars1 = reader1.read(buffer1, 0, CHUNK_SIZE)) != -1) {
                            extraNucleotides++;
                        }
                    }
                    break; // Exiting the loop when either file ends
                }

                // Calculating the similarity for the current chunk and adding to the list
                float similarity = calculateSimilarity(buffer1, buffer2, Math.min(readChars1, readChars2));
                similarityScores.add(similarity);

                // Output for each chunk comparison
                System.out.println("Comparing: " + new String(buffer1, 0, readChars1) + " with " + new String(buffer2, 0, readChars2) + " - Similarity: " + similarity);
            }

            // Calculating the average similarity across all chunks
            float averageSimilarity = calculateAverageSimilarity(similarityScores);
            System.out.println("Average Similarity: " + averageSimilarity);

            // Reporting extra nucleotides if present in either DNA
            if (extraNucleotides > 0) {
                String dnaSequenceWithExtra = isDNA1Longer ? "DNA 1" : "DNA 2";
                System.out.println(dnaSequenceWithExtra + " has " + extraNucleotides + " extra nucleotides.");
            }
        } catch (IOException e) {
            // Handling file reading errors
            System.err.println("Error reading files: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            // Handling other potential errors
            System.err.println("Error: " + e.getMessage());
        }
    }

    /**
     * Calculates the similarity between two char arrays.
     * @param array1 The first character array.
     * @param array2 The second character array.
     * @param length The length up to which to compare the arrays.
     * @return The percentage of similarity as a float.
     */
    private static float calculateSimilarity(char[] array1, char[] array2, int length) {
        int matches = 0;
        // Counting matching characters
        for (int i = 0; i < length; i++) {
            if (array1[i] == array2[i]) {
                matches++;
            }
        }
        // Returning the percentage of similarity
        return (float) matches / length * 100;
    }

    /**
     * Calculates the average of all similarity scores in the list.
     * @param similarityScores The list of similarity scores.
     * @return The average similarity percentage.
     */
    private static float calculateAverageSimilarity(ArrayList<Float> similarityScores) {
        if (similarityScores == null || similarityScores.isEmpty()) {
            return 0.0f;
        }

        int totalComparisons = similarityScores.size();
        int totalMatches = 0;
        // Counting scores that are 100% matches
        for (float score : similarityScores) {
            if (score == 100.0f) {
                totalMatches++;
            }
        }

        // Returning the average similarity percentage
        return (float) totalMatches / totalComparisons * 100;
    }
}
// Hi!

