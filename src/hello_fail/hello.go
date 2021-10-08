package hello_fail

import "strconv"

// Greet func return string
func Greet() string {
	return "Hello World!"
}

// Greet2 func return string
func Greet2(in int) string {
	return "Hello " + strconv.Itoa(in)
}
