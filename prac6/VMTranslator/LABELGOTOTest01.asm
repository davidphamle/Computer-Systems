// Test file for LABELGOTOTest01: Basic Conditional Jump

@1
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

@0
D=A
@SP
AM=M+1
A=A-1
M=D

(not_zero)

@2
D=A
@SP
AM=M+1
A=A-1
M=D