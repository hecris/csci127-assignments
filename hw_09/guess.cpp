#include <iostream>
#include <string>

using namespace std;

int prompt(string message){
    cout << message << "\n";
    int input;
    cin >> input;
    return input;
}

int main(){
    int i = prompt("Enter a number (0-99)");
    if (!(0 <= i && i <= 99)){
        cout << "Not a valid number\n";
        return -1;
    }
    int lower = 0;
    int upper = 99;
    int guess;
    while (true){
        guess = (lower + upper) / 2;
        cout << guess << "\n";
        int input = prompt("Correct?");
        if (input == 1){
            upper = guess;           
        }
        else if (input == -1){
            lower = guess;
        }
        else if (input == 0){
            break;
        }
    }
    cout << "\nDone! Your number was " << guess << "\n";
    

    return 0;
}


