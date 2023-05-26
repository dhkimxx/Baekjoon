#include <iostream>
#include <cmath>

int main(){
	
	int A, B, V, day;

	std::cin >> A >> B >> V;

	day = ceil((double)(V - A) / (A - B)) + 1;
	std::cout << day;

}