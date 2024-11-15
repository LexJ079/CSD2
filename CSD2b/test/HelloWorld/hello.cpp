#include <iostream>

int main () {

	std::cout << "Hello what is your name?" << std::endl;

	std::string yourName;
	std::cin >> yourName;
	std::cout << "Hi, " << yourName << std::endl;

	std::cout << "and what is your age?" << std::endl;

	std::string yourAge;
	std::cin >> yourAge;
	std::cout << "Age = " << yourAge << std::endl;


}
