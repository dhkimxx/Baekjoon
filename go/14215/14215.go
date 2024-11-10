package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func sum(arr []int) int {
	total := 0
	for _, num := range arr {
		total += num
	}
	return total
}

func main() {
	defer stdio.Flush()

	arr := make([]int, 3)

	for i := 0; i < 3; i++ {
		fmt.Fscan(stdio, &arr[i])
	}

	sort.Ints(arr)

	for {
		if arr[0]+arr[1] > arr[2] {
			break
		} else {
			arr[2]--
		}
	}

	fmt.Fprintln(stdio, sum(arr))

}
