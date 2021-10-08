package hello_fail

import "testing"

func TestGreet(t *testing.T) {
	var expected = "Hello Mark!"
	res := Greet()
	if res != expected {
		t.Errorf("Greet return not expected!")
	}
}

func TestGreet2(t *testing.T) {
	var tests = []struct {
		in       int
		expected string
	}{
		{1, "Hello 1"},
	}
	for _, tt := range tests {
		res := Greet2(tt.in)
		if res != tt.expected {
			t.Errorf("%s expected, got %s", tt.expected, res)
		}
	}
}
