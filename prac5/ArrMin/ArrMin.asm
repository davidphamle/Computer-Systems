// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


// Initialize R0 with the first array element
@R1
A = M
D = M
@R0
M = D

// Initialize counter R3 to R1 (starting index)
@R1
D = M
@R3
M = D

// Start of loop
(LOOP)
// Check if R3 is equal to R1+R2 (one past the last element)
@R3
D = M
@R1
D = D - M  // D = R3 - R1
@R2
D = D - M  // D = R3 - R1 - R2
@END
D;JEQ

// Get the element at RAM[R3]
@R3
A = M
D = M

// Compare with R0 and update R0 if the element is smaller
@R0
D = D - M
@UPDATE_MIN
D;JLT  // changed JGT to JLT to update the min if the element is smaller

// Increment R3 and jump back to the loop
@R3
M = M + 1
@LOOP
0;JMP

// Update minimum value in R0
(UPDATE_MIN)
@R3
A = M
D = M
@R0
M = D

// End of program
(END)
@END
0;JMP
