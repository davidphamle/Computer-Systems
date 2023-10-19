// Sample Test file for FunctionTest02.asm
load FunctionTest02.asm,
output-file FunctionTest02.out,
compare-to FunctionTest02.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0] 256,
set RAM[256] 0;

repeat 200 {
  ticktock;  // Run for 200 clock cycles
}

output;

