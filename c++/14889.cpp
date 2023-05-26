#include <iostream>
#include <vector>
using namespace std;

vector <vector <int>> s(20);
vector <int> p;
int teamPlayer;
int Min;

int teamMaker(int player, int last) {
	if (player == teamPlayer) {
		int stat1 = 0, stat2 = 0;
		for (int i : p) {
			for (int j : p) {
				stat1 += s[i][j];
			}
		}
		vector <int> p_temp;
		for (int i = 0; i < teamPlayer * 2; i++) {
			p_temp.push_back(i);
			for (int j : p) {
				if (i == j)
					p_temp.pop_back();
			}
		}
		for (int i : p_temp) {
			for (int j : p_temp) {
				stat2 += s[i][j];
			}
		}
		if (Min > abs(stat1 - stat2))
			Min = abs(stat1 - stat2);
		return 0;
	}
	for (int i = last; i < teamPlayer * 2; i++) {
		p.push_back(i);
		teamMaker(player + 1, i + 1);
		p.pop_back();
	}
	return 0;
}

int main() {
	int N; cin >> N;
	teamPlayer = N / 2;
	Min = 100 * N * N;
	int temp;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> temp;
			s[i].push_back(temp);
		}
	}
	teamMaker(0, 0);
	cout << Min;
}