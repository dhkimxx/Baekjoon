#include <iostream>
const double PI = 3.1415926535897932384626433832;
int main() {
	int R;
	double U, T;
	std::cin >> R;
	U = R * R * PI;
	T = R * R * 2;
	printf("%lf \n %lf", U, T);
}