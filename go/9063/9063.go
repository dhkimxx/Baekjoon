package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer stdio.Flush()

	var n int
	fmt.Fscan(stdio, &n)

	if n == 1 {
		fmt.Fprintln(stdio, 0)
		return
	}

	minX, maxX := int64(math.MaxInt64), int64(math.MinInt64)
	minY, maxY := int64(math.MaxInt64), int64(math.MinInt64)

	for i := 0; i < n; i++ {
		var x, y int64
		fmt.Fscan(stdio, &x, &y)

		if x < minX {
			minX = x
		}
		if x > maxX {
			maxX = x
		}
		if y < minY {
			minY = y
		}
		if y > maxY {
			maxY = y
		}
	}

	fmt.Fprintln(stdio, (maxX-minX)*(maxY-minY))

}
