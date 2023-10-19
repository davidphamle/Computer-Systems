// Sample Test file for LABELGOTOTest01.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load LABELGOTOTest01.asm,
output-file LABELGOTOTest01.out,
compare-to LABELGOTOTest01.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[256] 0,
set RAM[257] 0,
set RAM[258] 0;

repeat 200 {
  ticktock;    // Run for 10 clock cycles
}

output;
