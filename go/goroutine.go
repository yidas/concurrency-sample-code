package main

import (
	"fmt"
	"runtime"
	"sync"
)

func generateWorkers(n int) {
	var wg sync.WaitGroup

	wg.Add(n)
	for i := 0; i < n; i++ {
		go func(i int) {
			defer wg.Done()
			sum := 0
			// For monitoring usage of CPU cores
			for i := 0; i < 10000000000; i++ {
				sum += i
			}
			fmt.Printf("Worker %d Done\n", i)
		}(i)
	}

	wg.Wait()
	return
}

func main() {
	// Create workers according to core count
	generateWorkers(runtime.NumCPU())
	fmt.Println("All Done")
}
