// Test file for IFGOTOTest02
@0
D=A
@SP
AM=M+1
A=A-1
M=D

@SP
AM=M-1
D=M
@not_zero
D;JNE

@3
D=A
@SP
AM=M+1
A=A-1
M=D

(not_zero)

@4
D=A
@SP
AM=M+1
A=A-1
M=D