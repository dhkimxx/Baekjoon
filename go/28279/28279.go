package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

func main() {
	var stdio = bufio.NewReadWriter(
		bufio.NewReader(os.Stdin),
		bufio.NewWriter(os.Stdout),
	)
	defer stdio.Flush()

	var N int
	fmt.Fscanln(stdio, &N)

	deque := list.New()

	for i := 0; i < N; i++ {
		var a, b int
		fmt.Fscanln(stdio, &a, &b)

		switch a {
		case 1:
			deque.PushFront(b)
		case 2:
			deque.PushBack(b)
		case 3:
			if deque.Len() > 0 {
				front := deque.Remove(deque.Front())
				fmt.Fprintln(stdio, front)
			} else {
				fmt.Fprintln(stdio, -1)
			}
		case 4:
			if deque.Len() > 0 {
				back := deque.Remove(deque.Back())
				fmt.Fprintln(stdio, back)
			} else {
				fmt.Fprintln(stdio, -1)
			}
		case 5:
			fmt.Fprintln(stdio, deque.Len())
		case 6:
			if deque.Len() == 0 {
				fmt.Fprintln(stdio, 1)
			} else {
				fmt.Fprintln(stdio, 0)
			}
		case 7:
			if deque.Len() > 0 {
				fmt.Fprintln(stdio, deque.Front().Value)
			} else {
				fmt.Fprintln(stdio, -1)
			}
		case 8:
			if deque.Len() > 0 {
				fmt.Fprintln(stdio, deque.Back().Value)
			} else {
				fmt.Fprintln(stdio, -1)
			}
		}
	}
}
