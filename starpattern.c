#include <stdio.h>

int main() {
    int rows, i, j;

    // Define the number of rows for the triangle
    printf("Enter the number of rows for the right-angled triangle: ");
    scanf("%d", &rows);

    // Loop through each row
    for(i = 1; i <= rows; i++) {
        // Loop for printing stars
        for(j = 1; j <= i; j++) {
            printf(arr[j]);
        }
        // Move to the next line after each row
        printf("\n");
    }

    return 0;
}
