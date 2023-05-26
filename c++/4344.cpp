#include <iostream>

int main()
{
	int case_n, student_n, sum, avg, above_avg;
	double prcnt;
	int i,j;

	std::cin >> case_n;

	for (i = 1; i <= case_n; i++) {
		std::cin >> student_n;

		int* score = new int[student_n];

		sum = 0;
		avg = 0;
		above_avg = 0;
		
		for (j = 0; j < student_n; j++) {
			std::cin >> score[j];
			sum += score[j];
		}
		avg = sum / (double)student_n;

		for (j = 0; j < student_n; j++) {
			if (score[j] > avg) {
				above_avg++;
			}
		}

		prcnt = above_avg / double(student_n) * 100;

		std::cout.precision(3);
		std::cout << std::fixed << prcnt << "%\n";
	}
}