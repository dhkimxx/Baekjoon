#include <iostream>
#include <vector>
using namespace std;

vector <vector <int>> v(9);
int arr[9] = { 1,2,3,4,5,6,7,8,9 };
bool Row[10][10];
bool Col[10][10];
bool Square[10][10];
int blank_x[81] = { 0 };
int blank_y[81] = { 0 };
int Count = 0;

int check() {
	vector <vector <int>> v_temp(9);
	int x, y;
	x = blank_x[Count];
	y = blank_y[Count];
	if (Count != 0 && x == 0 && y == 0 || Count == 81) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << v[i][j] << " ";
			}
			cout << "\n";
		}
		exit(0);
		return 0;
	}

	for (int i = 1; i <= 9; i++)
	{
		if (Row[x][i] == false && Col[y][i] == false && Square[(x / 3) * 3 + (y / 3)][i] == false)
		{
			Row[x][i] = true;
			Col[y][i] = true;
			Square[(x / 3) * 3 + (y / 3)][i] = true;
			v[x][y] = i;
			Count++;
			check();
			Count--;
			v[x][y] = 0;
			Row[x][i] = false;
			Col[y][i] = false;
			Square[(x / 3) * 3 + (y / 3)][i] = false;
		}
	}
	return 0;
}

int main() {
	int temp;
	int cnt = 0;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> temp;
			v[i].push_back(temp);
			if (!v[i][j]) {
				blank_x[cnt] = i;
				blank_y[cnt] = j;
				cnt++;
			}
			else {
				Row[i][v[i][j]] = true;
				Col[j][v[i][j]] = true;
				Square[(i / 3) * 3 + (j / 3)][v[i][j]] = true;
			}
		}
	}
	check();
}