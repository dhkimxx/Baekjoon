#include <iostream>

int main() {
	int M = 0, n,i;
	double avg, sum = 0;
	std::cin >> n;
	int* score = new int[n];
	double* newscore = new double[n];
	
	
	for (i = 0; i < n; i++) {
		std::cin >> score[i];
		if (score[i] > M)
			M = score[i];
	}
	for (i = 0; i < n; i++) {
		newscore[i] = score[i] / (float)M * 100;
		sum += newscore[i];
	}
	avg = sum / n;
	std::cout << avg;
}