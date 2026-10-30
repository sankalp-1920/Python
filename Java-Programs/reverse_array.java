import java.util.Scanner;

public class reverse_array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n , i,j;
        int temp;
        System.out.println("Enter the size of array:");
        n = sc.nextInt();
        int[] a = new int[n];
        System.out.println("Enter the array element:");
        {
            for(i=0;i<n;i++){
                a[i]=sc.nextInt();
            }
        }
        for(i=0;i<n;i++){
            for(j=i+1;j<n;j++)
            {
                temp = a[i];
                a[i]=a[j];
                a[j]=temp;
             }
           
        }
        System.out.println("Reverse Array:");  
        for(i= 0;i<n;i++)
        {
            System.out.println(a[i]);
         }

        
        
    }
    
}
