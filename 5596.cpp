#include <iostream>
using namespace std;

int main() {
    int A[4], sumA = 0;
    int B[4], sumB = 0;

    for(int i = 0; i < 4; i++){
        cin >> A[i];
        sumA += A[i];
    }
    for(int i = 0; i < 4; i++){
        cin >> B[i];
        sumB += B[i];
    }
    cout << max(sumA, sumB);
}
