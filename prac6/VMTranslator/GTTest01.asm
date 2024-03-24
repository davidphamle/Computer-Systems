// Test file for GTTest01: 20 > 10
@20
D=A
@SP
AM=M+1
A=A-1
M=D

@10
D=A
@SP
AM=M+1
A=A-1
M=D

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
@TRUE
D;JGT
@SP
A=M-1
M=0
@CONTINUE
0;JMP
(TRUE)
@SP
A=M-1
M=-1
(CONTINUE)