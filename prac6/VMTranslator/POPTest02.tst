// Sample Test file for POPTest02.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load POPTest02.asm,
output-file POPTest02.out,
compare-to POPTest02.cmp,
output-list RAM[0]%D2.6.2 RAM[3]%D2.6.2 RAM[5]%D2.6.2 RAM[16]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[3]   600,  // Set THIS to RAM[600]
set RAM[5]   5,    // Temp 0
set RAM[6]   6,    // Temp 1
set RAM[16]  16,   // Static 0;

repeat 200 {
  ticktock;    // Run for 200 clock cycles
}

output;
