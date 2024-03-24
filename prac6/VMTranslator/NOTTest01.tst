// Sample Test file for NOTTest01.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load NOTTest01.asm,
output-file NOTTest01.out,
compare-to NOTTest01.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[256] 0;

repeat 200 {
  ticktock;    // Run for 10 clock cycles
}

output;
