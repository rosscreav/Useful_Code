import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class Data_in_out {

	   public static void Save( Object object,String directory) {
		   try {
		         FileOutputStream fileOut =new FileOutputStream(directory);
		         ObjectOutputStream out = new ObjectOutputStream(fileOut);
		         out.writeObject(object);
		         out.close();
		         fileOut.close();
		         System.out.printf("Save succesful \n");
		      } catch (IOException i) {
		         i.printStackTrace();
		      }
	   }
	   
	   public static Object Load(String directory) {
		   try {
		         FileInputStream fileIn = new FileInputStream(directory);
		         ObjectInputStream in = new ObjectInputStream(fileIn);
		         Object loaded_data = (Object) in.readObject();
		         in.close();
		         fileIn.close();
		         System.out.printf("Load succesful\n");
		         return loaded_data;
		      } catch (IOException i) {
		         i.printStackTrace();
		         return null;
		      } catch (ClassNotFoundException c) {
		         System.out.println("File not found");
		         c.printStackTrace();
		         return null;
		      }
		
	   }
	   
	   public static String Readfile(String directory_string) {
		   Path directory = Paths.get(directory_string);
		   try {
			   byte[] encoded = Files.readAllBytes(directory);
			   return new String(encoded,Charset.defaultCharset());
		   }
		   catch(Exception e) {
			   System.out.println("Read Failed");
			   e.printStackTrace();
		   }
		   return null;
	}
}