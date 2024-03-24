// Test file for LABELGOTOTEST04
@5
D=A
@SP
AM=M+1
A=A-1
M=D

(outer_loop)

@3
D=A
@SP
AM=M+1
A=A-1
M=D

@1
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

(inner_loop)

@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
AM=M+1
A=A-1
M=D

@1
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
@TRUE0
D;JEQ
@SP
A=M-1
M=0
@CONTINUE0
0;JMP
(TRUE0)
@SP
A=M-1
M=-1
(CONTINUE0)

@SP
AM=M-1
D=M
@inner_break
D;JNE

@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
AM=M+1
A=A-1
M=D

@1
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
M=M-D

@1
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

@inner_loop
0;JMP

(inner_break)

@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
AM=M+1
A=A-1
M=D

@1
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
M=M-D

@0
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

@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
AM=M+1
A=A-1
M=D

@-1
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

@SP
AM=M-1
D=M
@outer_loop
D;JNE