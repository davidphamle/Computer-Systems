// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Initialize R1 and R2 based on test setup
@R1 // the address of arr[0]
D=M-1 // subtract 1 because the array starts from arr[0]
@R2 // the length
M=M+D // now R2 is the address of the last element

(OUTER_LOOP)
@R1
D=M
@R2
D=D-M
@FINISH
D;JGT
@R1
D=M
@R3 // use R3 as the index of the inner loop.
M=D+1 

(INNER_LOOP)
@R3
D=M
@R2
D=D-M
@INNER_FINISH
D;JGT
@R3 // use inner index to locate the element.
A=M
D=M // now D contains the element pointed by the inner index.

@R1
A=M
D=D-M // compare with the outer index
@SKIP
D;JGE

// Swap the elements
@R1
A=M
D=M
@temp
M=D
@R3
A=M
D=M
@R1
A=M
M=D
@temp
D=M
@R3
A=M
M=D

(SKIP)
@R3
M=M+1
@INNER_LOOP
0;JMP

(INNER_FINISH)
@R1
M=M+1
@OUTER_LOOP
0;JMP

(FINISH)
@R0
M=-1 // Set R0 to True (-1) when complete
(END)
@END
0;JMP