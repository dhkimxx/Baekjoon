package main

import "fmt"

func sum(arr []int) int {
	total := 0
	for _, num := range arr {
		total += num
	}
	return total
}

/**
(GCD, Greatest Common Divisor)
*/
func gcd(x, y int64) int64 {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

/**
(LCM, Least Common Multiple)
*/
func lcm(a, b int64) int64 {
	return (a * b) / gcd(a, b)
}

func main() {
	arr := make([]int, 10)
	arr = append(arr, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println("arr :", arr)
	fmt.Println("sum(arr) :", sum(arr))
	fmt.Println("=============================")

	var a, b int64 = 123, 345
	fmt.Println("a, b :", a, b)
	fmt.Println("gcd(a, b):", gcd(a, b))
	fmt.Println("=============================")

	fmt.Println("a, b :", a, b)
	fmt.Println("lcm(a, b):", lcm(a, b))
	fmt.Println("=============================")
}
