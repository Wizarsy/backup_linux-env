package main

import (
	"fmt"
)

var fim, resto int

func main() {
	fim = 1000
	for num := 0; num < fim; num++ {
		if num == 1 {
			continue
		} else {
			if num%2 != 0 || num == 2 {
				for div := 2; div < num; div++ {
					resto = num % div
					if resto == 0 {
						break
					}
				}
				if resto != 0 || num == 2 {
					fmt.Printf("%d\t", num)
				}
			}
		}
	}
}
