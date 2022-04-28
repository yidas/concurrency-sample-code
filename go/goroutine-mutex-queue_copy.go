package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	mu      sync.Mutex
	queue   []string
	popList []string
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	for {
		// Detect queue without lock
		if len(c.queue) <= 0 {
			break
		}
		c.mu.Lock()
		if len(c.queue) > 0 {
			// Pop up first element from queue
			task := c.queue[0]
			c.queue = c.queue[1:]
			// Poplist log
			c.popList = append(c.popList, task)
		}
		// Lock so only one goroutine at a time can access the map c.v.
		c.mu.Unlock()
	}
}

func main() {
	var queue []string
	jobAmount := 200
	for i := 0; i < jobAmount; i++ {
		queue = append(queue, strconv.Itoa(i))
	}
	c := SafeCounter{queue: queue}
	for i := 0; i < 10; i++ {
		go c.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(c.popList)
}
