// Sample Test file for PUSHTest01.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load PUSHTest02.asm,
output-file PUSHTest02.out,
compare-to PUSHTest02.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[300] 10, // Set local[0] to 10
set RAM[301] 20, // Set local[1] to 20
set RAM[302] 30; // Set local[2] to 30

repeat 10 {
  ticktock;    // Run for 10 clock cycles
}

output;
