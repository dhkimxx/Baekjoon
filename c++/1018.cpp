#include <iostream>
#include <string>

std::string WB[8] = {
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW"
};
std::string BW[8] = {
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB"
};


int main() {
	int N, M; std::cin >> N >> M;
	int WBcount, BWcount, min = 64;
	std::string *arr = new std::string[N];
	
	for (int i = 0; i < N; i++) {
		std::cin >> arr[i];
	}

	for (int i = 0; i < N - 8 + 1; i++) {
		for (int j = 0; j < M - 8 + 1; j++) {

			WBcount = 0, BWcount = 0;
			for (int n = 0; n < 8; n++) {
				for (int m = 0; m < 8; m++) {
					if (arr[n + i][m + j] != WB[n][m]) {
						WBcount++;
					}
					if (arr[n + i][m + j] != BW[n][m]) {
						BWcount++;
					}
				}
			}
			if (min > WBcount)
				min = WBcount;
			if (min > BWcount)
				min = BWcount;
		}
	}
	std::cout << min;
}