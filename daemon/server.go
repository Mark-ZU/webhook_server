package main

import (
	"fmt"
	"net/http"
)

var port = ":4567"

func myfunc(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "hi")
	fmt.Printf("get req\n")
}
func main() {
	http.HandleFunc("/", myfunc)
	fmt.Printf("listen %s\n", port)
	http.ListenAndServe(":4567", nil)
}
