// Sample Test file for CallTest02.asm
load CallTest02.asm,
output-file CallTest02.out,
compare-to CallTest02.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0] 256,  // Set R0
set RAM[256] 0;  // Initialize stack with 0

repeat 300 {
  ticktock;  // Run for 300 clock cycles
}

output;
