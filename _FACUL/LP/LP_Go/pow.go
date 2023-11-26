package main

import (
	f "fmt"
)

func main() {
	x, a, p := 0, 0, 1
	for x <= 0 {
		f.Print("Digite um numero inteiro positivo: ")
		f.Scanf("%d\n", &x)
	}
	f.Print("Digite o expoente: ")
	f.Scanf("%d\n", &a)
	for a > 0 {
		p *= x
		a--
	}
	f.Println(p)
}
