#include <iostream>

int main() {
	int case_n;
	int  H, W, N;
	int X, Y;
	std::cin >> case_n;
	for (int i = 1; i <= case_n; i++) {

		std::cin >> H >> W >> N;
		X = N / H + 1;
		if (!(N % H))
			X -= 1;

		Y = N % H;
		if (Y == 0)
			Y = H;
		
		std::cout << Y * 100 + X << std::endl;

	}
	return 0;
}