#include <iostream>
using namespace std;

int main() {
    int number;
    
    // Input
    cout << "Enter a number: ";
    cin >> number;

    // Condition check
    if (number % 2 == 0) {
        cout << "The number " << number << " is even." << endl;
    } else {
        cout << "The number " << number << " is odd." << endl;
    }

    // Loop
    cout << "Counting from 1 to " << number << ":" << endl;
    for (int i = 1; i <= number; i++) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
