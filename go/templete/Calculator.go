package main

import "fmt"

func sum(arr []int) int {
	total := 0
	for _, num := range arr {
		total += num
	}
	return total
}

func main() {
	arr := make([]int, 10)
	arr = append(arr, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println("arr:", arr)
	fmt.Println("sum(arr):", sum(arr))
}
