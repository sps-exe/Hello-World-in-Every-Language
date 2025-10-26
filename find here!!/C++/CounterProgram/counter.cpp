#include <iostream>
using namespace std;

int main() {
    int count;
    
    cout << "Enter the number to count up to: ";
    cin >> count;
    
    cout << "\nCounting from 1 to " << count << ":\n";
    
    for(int i = 1; i <= count; i++) {
        cout << i << " ";
    }
    
    cout << "\n\nCountdown from " << count << " to 1:\n";
    
    for(int i = count; i >= 1; i--) {
        cout << i << " ";
    }
    
    cout << "\n\nCounter program completed!\n";
    
    return 0;
}
