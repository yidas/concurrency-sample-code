package main

import (
	"fmt"
	"sync"
)

func consumeJobsWithProcesses(queue []int, n int) []int {
	var popList []int
	var wg sync.WaitGroup
	var mux sync.Mutex

	wg.Add(n)
	for i := 0; i < n; i++ {
		go func(i int) {
			defer wg.Done()
			for {
				// Detect queue without lock
				if len(queue) <= 0 {
					break
				}
				// Lock and consume
				mux.Lock()
				if len(queue) > 0 {
					qi := 0
					lastIndex := queue[qi]
					queue = append(queue[:qi], queue[qi+1:]...)
					popList = append(popList, lastIndex)
				}
				mux.Unlock()
			}
		}(i)
	}
	wg.Wait()
	return popList
}

func main() {

	// Add jobs into job queue
	var queue []int
	jobAmount := 20
	for i := 0; i < jobAmount; i++ {
		queue = append(queue, i)
	}
	// Consume jobs with goroutine
	popList := consumeJobsWithProcesses(queue, 10)
	fmt.Println("The length of job queue:", len(popList))
	fmt.Println(popList)
}
