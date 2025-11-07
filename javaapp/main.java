import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeExample {
    public static void main(String[] args) {
        LocalDateTime now = LocalDateTime.now();  // current date & time

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        String formattedDateTime = now.format(formatter);

        System.out.println("Current Date & Time: " + formattedDateTime);
    }
}
