// Test file for POPTest01

@10
D=A
@SP
AM=M+1
A=A-1
M=D

@2
D=A
@LCL
D=M+D
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

@1
D=A
@ARG
D=M+D
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

@0
D=A
@THIS
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

@40
D=A
@SP
AM=M+1
A=A-1
M=D

@1
D=A
@THAT
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D