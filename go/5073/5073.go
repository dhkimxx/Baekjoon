package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	Equilateral = "Equilateral"
	Isosceles   = "Isosceles"
	Scalene     = "Scalene"

	Invalid = "Invalid"
)

func printResult(x, y, z int64) {
	if x+y <= z || y+z <= x || x+z <= y {
		fmt.Fprintln(stdio, Invalid)
	} else if x == y && y == z {
		fmt.Fprintln(stdio, Equilateral)
	} else if x == y || y == z || z == x {
		fmt.Fprintln(stdio, Isosceles)
	} else {
		fmt.Fprintln(stdio, Scalene)
	}
}

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer stdio.Flush()

	for {
		var a, b, c int64
		fmt.Fscan(stdio, &a, &b, &c)

		if a*b*c == 0 {
			break
		} else {
			printResult(a, b, c)
		}

	}

}
