
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class java_client {
   public static void main(String[] args) throws Exception {
      String url = "http://localhost:5000/convert";

      // JSON payload
      System.out.print("Enter the amount you want to convert: ");
      Scanner scanner = new Scanner(System.in);
      
      double amountInRs = scanner.nextDouble();
      String jsonInputString = "{\"amount_in_rs\": "+amountInRs+"}";
      scanner.close();

      URL obj = new URL(url);
      HttpURLConnection con = (HttpURLConnection) obj.openConnection();
      con.setRequestMethod("POST");
      con.setRequestProperty("Content-Type", "application/json");

      // Send POST request
      con.setDoOutput(true);
      OutputStream os = con.getOutputStream();
      os.write(jsonInputString.getBytes());
      os.flush();
      os.close();

      // Get response
      int responseCode = con.getResponseCode();
      BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
      String inputLine;
      StringBuffer response = new StringBuffer();
      while ((inputLine = in.readLine()) != null) {
         response.append(inputLine);
      }
      in.close();

      // Print result
      System.out.println("Response Code: " + responseCode);
      System.out.println("Response: " + response.toString());
   }
} 
