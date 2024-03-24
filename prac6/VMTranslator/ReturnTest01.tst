// Sample Test file for ReturnTest01.asm
load ReturnTest01.asm,
output-file ReturnTest01.out,
compare-to ReturnTest01.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0] 256,  // Set R0
set RAM[256] 0;  // Initialize stack with 0

repeat 200 {
  ticktock;  // Run for 200 clock cycles
}

output;
