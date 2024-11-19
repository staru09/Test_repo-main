#include <stdio.h>

int main() {
    int number;

    // Input
    printf("Enter a number: ");
    scanf("%d", &number);

    // Condition check
    if (number % 2 == 0) {
        printf("The number %d is even.\n", number);
    } else {
        printf("The number %d is odd.\n", number);
    }

    // Loop
    printf("Counting from 1 to %d:\n", number);
    for (int i = 1; i <= number; i++) {
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
