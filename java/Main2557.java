import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main2557 {
    
    public static void main(String[] args) throws IOException {
        // System.out.println("Hello World!");

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("Hello World!");
        bw.flush();
		bw.close();
    }
}
