#include <iostream>

int count0[41], count1[41];

void fibonacci(int n) {
    if (n > 40)
        return;
    else if (n == 0) {
        count0[n] = 1;
        count1[n] = 0;
        fibonacci(n + 1);
    }
    else if (n == 1) {
        count0[n] = 0;
        count1[n] = 1;
        fibonacci(n + 1);
    }
    else {
        count0[n] = count0[n - 1] + count0[n - 2];
        count1[n] = count1[n - 1] + count1[n - 2];
        fibonacci(n + 1);
    }
}


int main() {
    int T, N;
    std::cin >> T;
    fibonacci(0);
    for (int i = 0; i < T; i++) {
        std::cin >>  N;       
        std::cout << count0[N] << " " << count1[N] << "\n";
    }

}