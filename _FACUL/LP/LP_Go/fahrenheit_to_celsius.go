package main

import (
	f "fmt"
)

var F, celsius float64

func main() {
	f.Print("Digite uma temp: ")
	f.Scanf("%f", &F)
	celsius = ((F - 32) * 5) / 9
	f.Printf("%f", celsius)
}
