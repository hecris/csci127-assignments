#include <iostream>
#include <string>

int sumofsquares(int a, int b){
    std::cout << a << " to " << b << "\n";
    if (b < a){
        std::cout << "Not a valid range. Error ";
        return -1;
    }
    int result = 0;
    while (a <= b){
        int square = a * a;
        std::cout << square;
        if (a != b){
            std::cout << "+";
        }
        else {
            std::cout << "=";
        }
        result += square;
        a++;
    }
    return result;

}

int main(){
    std::cout << sumofsquares(5, 10) << "\n\n";
    std::cout << sumofsquares(10, 5) << "\n\n";
    std::cout << sumofsquares(-10, 5) << "\n\n";
    std::cout << sumofsquares(0, 5) << "\n\n";
    std::cout << sumofsquares(0, 0) << "\n\n";
    std::cout << sumofsquares(-10, -5) << "\n\n";
    std::cout << sumofsquares(50, 100) << "\n\n";
    return 0;
}
