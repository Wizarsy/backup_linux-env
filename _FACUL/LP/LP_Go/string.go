package main

import (
	"bufio"
	f "fmt"
	"os"
)

var original, copia string

func main() {
	f.Print("Digite uma string: ")
	read := bufio.NewReader(os.Stdin)
	original, _ = read.ReadString('\n')
	for _, c := range original[:len(original)-1] {
		if c >= 97 && c <= 122 {
			copia += string(c - 32)
		} else if c >= 48 && c <= 57 || c >= 65 && c <= 90 {
			copia += string(c)
		}
	}
	f.Println(copia)
}
