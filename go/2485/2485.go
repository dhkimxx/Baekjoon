package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(x, y int) int {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}

	sub := make([]int, n-1)
	for i := 1; i < n; i++ {
		sub[i-1] = arr[i] - arr[i-1]
	}

	currentGcd := sub[0]
	for i := 1; i < len(sub); i++ {
		currentGcd = gcd(currentGcd, sub[i])
	}

	res := 0
	for _, v := range sub {
		res += v/currentGcd - 1
	}

	fmt.Fprintln(writer, res)
}
