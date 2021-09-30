package hello

import "strconv"

// Greet func return string
func Greet() string {
	return "Hello Mark!"
}

// Greet2 func return string
func Greet2(in int) string {
	return "Hello " + strconv.Itoa(in)
}
