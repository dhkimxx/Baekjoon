#include <iostream>

int main() {
    int N, temp, min_index; std::cin >> N;
    int* arr = new int[N];
    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }
    for (int i = 0; i < N; i++) {
        min_index = i;
        for (int j = i + 1; j < N; j++) {
            if (arr[min_index] > arr[j])
                min_index = j;                 
        }
        temp = arr[min_index];
        arr[min_index] = arr[i];
        arr[i] = temp;       
    }
    for (int i = 0; i < N; i++) {
        std::cout << arr[i] << "\n";
    }
}