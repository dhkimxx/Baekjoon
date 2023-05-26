#include <iostream>

int main() {

	int x, sum , n = 2, flag = 1,count;

	std::cin >> x;

	for (sum = 1; sum < x; n++) {
		sum += n;
		flag = n % 2;	
	}
	

	count = sum - x + 1;
	if (flag)
		std::cout << count << "/" << n - count;
	else
		std::cout << n - count << "/" << count;

}