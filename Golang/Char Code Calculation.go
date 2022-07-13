/*
https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/go
*/

package main

import (
	"fmt"
)

func Calc(s string) int {

	var total1 string = ""
	var total2 string = ""

	for _, c := range s {
		total1 += fmt.Sprint(int(c))
	}

	for _, c := range total1 {
		if c == '7' {
			c = '1'
		}
		total2 += string(c)
	}

	sum := 0

	for i := 0; i < len(total1); i++ {
		if total1[i] != total2[i] {
			sum += 6
		}
	}

	// fmt.Printf("total1: %s\ntotal2: %s\n", total1, total2)

	// t1, _ := strconv.Atoi(total1)
	// t2, _ := strconv.Atoi(total2)

	return sum
}
