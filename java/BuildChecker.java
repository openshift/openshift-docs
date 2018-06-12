import java.io.File;
import java.io.IOException;
import java.nio.file.Files;


public class BuildChecker {

  public static void main(String args[]) throws IOException {
    
    String dirName = "../";

    Files.list(new File(dirName).toPath())
            .forEach(path -> {
                System.out.println(path);
            });    
    
  }
}
