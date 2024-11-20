#include <stdio.h>

#define SIZE 100

int main() {
    int arr[SIZE];
    int largest, smallest;

    // Input array elements
    printf("Enter 100 integers:\n");
    for (int i = 0; i < SIZE; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Initialize largest and smallest with the first element
    largest = arr[0];
    smallest = arr[0];

    // Traverse the array to find largest and smallest
    for (int i = 1; i < SIZE; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
    }

    // Display the results
    printf("The largest number in the array is: %d\n", largest);
    printf("The smallest number in the array is: %d\n", smallest);

    return 0;
}
