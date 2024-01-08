# Baby Rev JohnSon (REV)

This challenge is kinda have to deal with edge cases a little logical program.
```
Welcome to the Johnson's family!
You have gotten to know each person decently well, so let's see if you remember all of the facts.
(Remember that each of the members like different things from each other.)
Please choose Alice's favorite color:
```

To know the inputs we can look through the code via disassembly with IDA.

Binary file disassembly:
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+4h] [rbp-7Ch]
  int v5; // [rsp+4h] [rbp-7Ch]
  int v6; // [rsp+8h] [rbp-78h]
  int v7; // [rsp+Ch] [rbp-74h]
  char s1[104]; // [rsp+10h] [rbp-70h] BYREF
  unsigned __int64 v9; // [rsp+78h] [rbp-8h]

  v9 = __readfsqword(0x28u);
  puts("Welcome to the Johnson's family!");
  puts("You have gotten to know each person decently well, so let's see if you remember all of the facts.");
  puts("(Remember that each of the members like different things from each other.)");
  v4 = 0;
  while ( v4 <= 3 )
  {
    printf("Please choose %s's favorite color: ", (&names)[v4]);
    __isoc99_scanf("%99s", s1);
    if ( !strcmp(s1, colors) )
    {
      v6 = 1;
      goto LABEL_11;
    }
    if ( !strcmp(s1, s2) )
    {
      v6 = 2;
      goto LABEL_11;
    }
    if ( !strcmp(s1, off_4050) )
    {
      v6 = 3;
      goto LABEL_11;
    }
    if ( !strcmp(s1, off_4058) )
    {
      v6 = 4;
LABEL_11:
      if ( v6 == chosenColors[0] || v6 == chosenColors_1 || v6 == chosenColors_2 || v6 == chosenColors_3 )
        puts("That option was already chosen!");
      else
        chosenColors[v4++] = v6;
    }
    else
    {
      puts("Invalid color!");
    }
  }
  v5 = 0;
  while ( v5 <= 3 )
  {
    printf("Please choose %s's favorite food: ", (&names)[v5]);
    __isoc99_scanf("%99s", s1);
    if ( !strcmp(s1, foods) )
    {
      v7 = 1;
      goto LABEL_28;
    }
    if ( !strcmp(s1, off_4068) )
    {
      v7 = 2;
      goto LABEL_28;
    }
    if ( !strcmp(s1, off_4070) )
    {
      v7 = 3;
      goto LABEL_28;
    }
    if ( !strcmp(s1, off_4078) )
    {
      v7 = 4;
LABEL_28:
      if ( v7 == chosenFoods[0] || v7 == dword_40A4 || v7 == chosenFoods_2 || v7 == chosenFoods_3 )
        puts("That option was already chosen!");
      else
        chosenFoods[v5++] = v7;
    }
    else
    {
      puts("Invalid food!");
    }
  }
  check();
  return 0;
}
```
We can see that our input will be compared with colors and foods,  and calls check function which is kinda logic puzzle.

```c
int check()
{
  bool v0; // dl
  _BOOL4 v1; // eax
  _BOOL4 v2; // edx

  v0 = chosenFoods_2 != 2 && chosenFoods_3 != 2;
  v1 = v0 && chosenColors_1 != 1;
  v2 = chosenColors[0] != 3 && chosenColors_1 != 3;
  if ( !v2 || !v1 || chosenFoods[0] != 4 || chosenFoods_3 == 3 || chosenColors_2 == 4 || chosenColors_3 != 2 )
    return puts("Incorrect.");
  puts("Correct!");
  return system("cat flag.txt");
}
```

In data section we can see these values:
```
.data:0000000000004040 ; char *colors
.data:0000000000004040 colors          dq offset aRed          ; DATA XREF: main+96↑r
.data:0000000000004040                                         ; "red"
.data:0000000000004048 ; char *s2
.data:0000000000004048 s2              dq offset aBlue         ; DATA XREF: main:loc_13D2↑r
.data:0000000000004048                                         ; "blue"
.data:0000000000004050 ; char *off_4050
.data:0000000000004050 off_4050        dq offset aGreen        ; DATA XREF: main:loc_13F5↑r
.data:0000000000004050                                         ; "green"
.data:0000000000004058 ; char *off_4058
.data:0000000000004058 off_4058        dq offset aYellow       ; DATA XREF: main:loc_1418↑r
.data:0000000000004058                                         ; "yellow"
.data:0000000000004060                 public foods
.data:0000000000004060 ; char *foods
.data:0000000000004060 foods           dq offset aPizza        ; DATA XREF: main+1E9↑r
.data:0000000000004060                                         ; "pizza"
.data:0000000000004068 ; char *off_4068
.data:0000000000004068 off_4068        dq offset aPasta        ; DATA XREF: main:loc_1525↑r
.data:0000000000004068                                         ; "pasta"
.data:0000000000004070 ; char *off_4070
.data:0000000000004070 off_4070        dq offset aSteak        ; DATA XREF: main:loc_1548↑r
.data:0000000000004070                                         ; "steak"
.data:0000000000004078 ; char *off_4078
.data:0000000000004078 off_4078        dq offset aChicken      ; DATA XREF: main:loc_156B↑r
.data:0000000000004078 _data           ends                    ; "chicken"
```

```
└─$ ./main       
Welcome to the Johnson's family!
You have gotten to know each person decently well, so let's see if you remember all of the facts.
(Remember that each of the members like different things from each other.)
Please choose Alice's favorite color: red
Please choose Emma's favorite color: blue
Please choose James's favorite color: green
Please choose William's favorite color: yellow
Please choose Alice's favorite food: pizza
Please choose Emma's favorite food: pasta
Please choose James's favorite food: steak
Please choose William's favorite food: chicken
Incorrect.
```
Our input passes but it's incorrect and doesn't show the flag since we didn't pass in the check function.


Interpretation of the check function:
```
red = 1
blue = 2
green = 3
yellow = 4

pizza = 1
pasta = 2
steak = 3
chicken = 4

chosenFoods_2 != pasta && chosenFoods_3 != pasta
chosenColors_1 != red
chosenColors[0] != green && chosenColors_1 != green
chosenFoods[0] != chicken || chosenFoods_3 == steak || chosenColors_2 == blue || chosenColors_3 != blue
```
As we can see we can generate the correct input by using the above logic.

color1 = red
color2 = yellow
color3 = green
color4 = blue

food1 = chicken
food2 = pasta
food3 = steak
food4 = pizza

```
└─$ nc babyrevjohnson.chal.irisc.tf 10002                                                                                                                                                     1 ⨯
== proof-of-work: disabled ==
Welcome to the Johnson's family!
You have gotten to know each person decently well, so let's see if you remember all of the facts.
(Remember that each of the members like different things from each other.)
Please choose Alice's favorite color: red
gPlease choose Emma's favorite color:yellow
Please choose James's favorite color: green
Please choose William's favorite color: blue
Please choose Alice's favorite food: chicken
Please choose Emma's favorite food: pasta
Please choose James's favorite food: steak
Please choose William's favorite food: pizza
Correct!
irisctf{m0r3_th4n_0n3_l0g1c_puzzl3_h3r3} 
```

