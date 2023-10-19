// Sample Test file for LABELGOTOTest04.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load NOTTest01.asm,
output-file LABELGOTOTest04.out,
compare-to LABELGOTOTest04.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2;

set PC 0,
set RAM[0] 256,
set RAM[256] 0,
set RAM[257] 0;

repeat 300 {
  ticktock;  // Run for 300 clock cycles
}

output;
