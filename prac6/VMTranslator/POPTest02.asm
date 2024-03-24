// Test file for POPTest02

@10
D=A
@SP
AM=M+1
A=A-1
M=D

@0
D=A
@5
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

@20
D=A
@SP
AM=M+1
A=A-1
M=D

@16
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

@30
D=A
@SP
AM=M+1
A=A-1
M=D

@3
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D