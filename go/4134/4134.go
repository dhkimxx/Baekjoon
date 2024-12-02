package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var stdio = bufio.NewReadWriter(bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout))

func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	if n == 2 {
		return true
	}

	if n%2 == 0 {
		return false
	}

	sqrtN := math.Sqrt(float64(n))
	for i := 3; i <= int(sqrtN); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	defer stdio.Flush()
	var N int
	fmt.Fscan(stdio, &N)

	for i := 0; i < N; i++ {
		var n int
		fmt.Fscan(stdio, &n)
		for {
			if isPrime(n) == true {
				fmt.Fprintln(stdio, n)
				break
			} else {
				n++
			}
		}
	}
}
