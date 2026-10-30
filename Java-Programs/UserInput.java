
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your First Name : ");
        String name = sc.next();

        System.out.println("Enter your Middle Name : ");
        String middleName = sc.next();

        System.out.println("Enter your Last Name : ");
        String lastName = sc.next();

        System.out.println("Enter your Roll No. : ");
        int rollNo = sc.nextInt();

        System.out.println();
        System.out.println(name + " " + middleName + " " + lastName );
        System.out.println("Roll No. " + rollNo);


        // System.out.println("Enter First Number : ");
        // int num1 = sc.nextInt();
        // System.out.println("Enter Second Number : ");
        // int num2 = sc.nextInt();

        // int res = num1 + num2;
        // System.out.println("Sum of First & Second : " + res);
    }
}
