// Sample Test file for NEGTest01.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load NEGTest01.asm,
output-file NEGTest01.out,
compare-to NEGTest01.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[256] 0,

repeat 10 {
  ticktock;    // Run for 10 clock cycles
}

output;
