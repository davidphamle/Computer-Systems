// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)

// Put your code here.
@R1
D = M

@POSITIVE // Set the address for the positive label
D;JGE     // Jump to the positive label if D >= 0

@R1
D = M
D = -D

(POSITIVE) // Positive label
@R0
M = D      // Store the absolute value in R0
0;JMP      // Jump to the end label to terminate



