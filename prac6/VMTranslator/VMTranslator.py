class VMTranslator:
    call_counter = 0

    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        asm_code = ""
        if segment == "constant":
            asm_code += f"@{offset}\n"
            asm_code += "D=A\n"
        elif segment == "local":
            asm_code += "@LCL\nD=M\n"  
            asm_code += f"@{offset}\nD=D+A\n"  
            asm_code += "A=D\nD=M\n" 

        elif segment == "argument":
            asm_code += "@ARG\nD=M\n" 
            asm_code += f"@{offset}\nD=D+A\n" 
            asm_code += "A=D\nD=M\n" 
            
        elif segment == "this":
            asm_code += "@THIS\nD=M\n"
            asm_code += f"@{offset}\nD=D+A\n"
            asm_code += "A=D\nD=M\n"
        
        elif segment == "that":
            asm_code += "@THAT\nD=M\n"
            asm_code += f"@{offset}\nD=D+A\n"
            asm_code += "A=D\nD=M\n"
            
        elif segment == "temp":
            asm_code += f"@{5 + offset}\nD=M\n"
            
        elif segment == "static":
            asm_code += f"@filename.{offset}\nD=M\n"

        elif segment == "pointer":
            asm_code += f"@{'THIS' if offset == 0 else 'THAT'}\nD=M\n"
        # push D register to stack
        asm_code += "@SP\nAM=M+1\nA=A-1\nM=D\n"
        return asm_code

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        asm_code = ""
        if segment == "local":
            asm_code += f"@{offset}\nD=A\n@LCL\nD=M+D\n@R13\nM=D\n" 
        elif segment == "argument":
            asm_code += f"@{offset}\nD=A\n@ARG\nD=M+D\n@R13\nM=D\n"  
        elif segment == "this":
            asm_code += f"@{offset}\nD=A\n@THIS\nD=M+D\n@R13\nM=D\n" 
        elif segment == "that":
            asm_code += f"@{offset}\nD=A\n@THAT\nD=M+D\n@R13\nM=D\n" 
        elif segment == "temp":
            asm_code += f"@{offset}\nD=A\n@5\nD=A+D\n@R13\nM=D\n" 
        elif segment == "static":
            asm_code += f"@{16+offset}\nD=A\n@R13\nM=D\n" 
        elif segment == "pointer":
            asm_code += f"@{3+offset}\nD=A\n@R13\nM=D\n" 

        # pop from stack into D
        asm_code += "@SP\nAM=M-1\nD=M\n"

        # store D into the address previously computed (in R13)
        asm_code += "@R13\nA=M\nM=D\n"

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        asm_code = "@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n"
        return asm_code

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nM=M-D\n"
        return asm_code

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        asm_code = "@SP\nA=M-1\nM=-M\n"
        return asm_code

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nD=M-D\n@TRUE\nD;JEQ\n@SP\nA=M-1\nM=0\n@CONTINUE\n0;JMP\n(TRUE)\n@SP\nA=M-1\nM=-1\n(CONTINUE)\n"
        return asm_code

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nD=M-D\n@TRUE\nD;JGT\n@SP\nA=M-1\nM=0\n@CONTINUE\n0;JMP\n(TRUE)\n@SP\nA=M-1\nM=-1\n(CONTINUE)\n"
        return asm_code

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nD=M-D\n@TRUE\nD;JLT\n@SP\nA=M-1\nM=0\n@CONTINUE\n0;JMP\n(TRUE)\n@SP\nA=M-1\nM=-1\n(CONTINUE)\n"
        return asm_code

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nM=D&M\n"
        return asm_code

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nM=D|M\n"
        return asm_code

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        asm_code = "@SP\nA=M-1\nM=!M\n"
        return asm_code

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        asm_code = f"({label})\n"
        return asm_code

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        asm_code = f"@{label}\n0;JMP\n"
        return asm_code

    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        asm_code = "@SP\nAM=M-1\nD=M\n@" + label + "\nD;JNE\n"
        return asm_code

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        asm_code = f"({function_name})\n"
        for _ in range(n_vars):
            asm_code += "@SP\nA=M\nM=0\n@SP\nM=M+1\n"
        return asm_code

    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        return_label = f"RETURN_LABEL_{VMTranslator.call_counter}"
        VMTranslator.call_counter += 1

        asm_code = (
            # Push return address
            f"@{return_label}\n"
            "D=A\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "M=M+1\n"
            
            # Push LCL, ARG, THIS, THAT
            "@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
            
            # ARG = SP - 5 - n_args
            f"@{5 + n_args}\n"
            "D=A\n"
            "@SP\n"
            "D=M-D\n"
            "@ARG\n"
            "M=D\n"
            
            # LCL = SP
            "@SP\n"
            "D=M\n"
            "@LCL\n"
            "M=D\n"
            
            # Goto function
            f"@{function_name}\n"
            "0;JMP\n"
            
            # Declare a label for the return address
            f"({return_label})\n"
        )
        return asm_code

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        asm_code = "@LCL\nD=M\n@R13\nM=D\n@5\nA=D-A\nD=M\n@R14\nM=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@R13\nAM=M-1\nD=M\n@THAT\nM=D\n@R13\nAM=M-1\nD=M\n@THIS\nM=D\n@R13\nAM=M-1\nD=M\n@ARG\nM=D\n@R13\nAM=M-1\nD=M\n@LCL\nM=D\n@R14\nA=M\n0;JMP\n"
        return asm_code

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        