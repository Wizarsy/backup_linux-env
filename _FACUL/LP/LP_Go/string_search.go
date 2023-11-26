package main

import (
	"bufio"
	f "fmt"
	"os"
	s "strings"
)

var str, busca, temp string
var vezes int = 0

func main() {
	f.Print("Digite uma frase: ")
	read := bufio.NewReader(os.Stdin)
	str, _ = read.ReadString('\n')
	f.Print("Qual a busca: ")
	busca, _ = read.ReadString('\n')
	str = s.TrimSpace(str)
	busca = s.TrimSpace(busca)

	for i := 0; i < len(str); i++ {
		temp += string(str[i])
		if temp == busca {
			vezes++
		}
		if len(temp) == len(busca) {
			temp = ""
			i -= (len(busca) - 1)
		}
	}
	f.Printf("A palavra '%s' aparece %d vezes", busca, vezes)
}
