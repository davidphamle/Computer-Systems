// Sample Test file for IFGotoTest02.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load IFGOTOTest02.asm,
output-file IFGOTOTest02.out,
compare-to IFGOTOTest02.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2;

set PC 0,
set RAM[0] 256,
set RAM[256] 0,
set RAM[257] 0;

repeat 200 {
  ticktock;  // Run for 200 clock cycles
}

output;
