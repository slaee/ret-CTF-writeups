# Whats a rune (REV)

This challenge is written in go and we can see this challenge is to reverse the encrypted flag inside "the" file.

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

var flag = "irisctf{this_is_not_the_real_flag}"

func init() {
	runed := []string{}
	z := rune(0)

	for _, v := range flag {
		fmt.Println(z, v, z+v)
		runed = append(runed, string(v+z))
		z = v
	}

	flag = strings.Join(runed, "")
}

func main() {
	file, err := os.OpenFile("the2", os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer file.Close()
	if _, err := file.Write([]byte(flag)); err != nil {
		fmt.Println(err)
		return
	}
}
```

the:
```
iÛÛÜÖ×ÚáäÈÑ¥gebªØÔÍãâ£i¥§²ËÅÒÍÈä
```

To reverse we can just subtract the previous rune from the current rune. Since we have the first rune `i` and use it as the first previous rune, we can just subtract the first rune from the second rune and so on.

```py
try:
    with open("the", "r") as file:
        orig_flag = file.read()

    runed = []
    z = ord(orig_flag[0])

    for v in orig_flag[1:]:
        runed.append(chr(ord(v) - z))
        z = ord(v) - z

    flag = ''.join(runed)  

    print('i' +flag)


except Exception as e:
    print(e)
```

```
└─$ python3 main.py
irisctf{i_r3411y_1ik3_num63r5}Nw[rV
```