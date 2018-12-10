#include <iostream>
#include <math.h>

float discriminant(float a, float b, float c){
    std::cout << "Your equation: ";
    std::cout << a << "x^2 + " << b << "x + " << c << "\n";
    return (b*b) - (4 * a * c);
}

float quadsolve(float a, float b, float c){
    float disc = discriminant(a, b, c);
    if (disc < 0){
        std::cout << "Discriminant is below 0\n";
        return 0;
    }
    return ((-b) + sqrt(disc)) / (2 * a);


}

int main()
{
    std::cout << "\nTesting Discriminant Function. Outputs are discriminants.\n";
    std::cout << discriminant(4,5,6) << "\n";
    std::cout << discriminant(2, -14, -13) << "\n";
    std::cout << discriminant(2, 0, 0) << "\n";
    std::cout << discriminant(1, 5, 6) << "\n";
    std::cout << discriminant(1, -5, 6) << "\n";
    std::cout << "==============================\n";
    std::cout << "\nTesting quadsolve. Outputs are positive roots, but not necessarily positive (see README file). If returned 0 AND error message is shown, discriminant is negative.\n";
    std::cout << quadsolve(4,5,6) << "\n";
    std::cout << quadsolve(2, -14, -13) << "\n";
    std::cout << quadsolve(2.5, -14, -13) << "\n";
    std::cout << quadsolve(2, 0, 0) << "\n";
    std::cout << quadsolve(1, 5, 6) << "\n";
    std::cout << quadsolve(1, -5, 6) << "\n";
    return 0;
}


