package main

import (
	"bufio"
	"fmt"
	"os"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func gcd(x, y int64) int64 {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	defer stdio.Flush()

	var a, b int64
	fmt.Fscan(stdio, &a, &b)

	gcd := gcd(a, b)

	var res int64 = a * b / gcd

	fmt.Fprintln(stdio, res)
}
