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

func lcm(a, b int64) int64 {
	return (a * b) / gcd(a, b)
}

func main() {
	defer stdio.Flush()

	var a, b int64
	var c, d int64
	fmt.Fscan(stdio, &a, &b)
	fmt.Fscan(stdio, &c, &d)

	lcm := lcm(b, d)

	child := lcm/b*a + lcm/d*c
	parent := lcm

	fmt.Println(child/gcd(child, parent), parent/gcd(child, parent))
}
