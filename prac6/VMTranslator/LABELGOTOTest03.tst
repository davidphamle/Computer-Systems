// Sample Test file for LABELGOTOTest03.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load LABELGOTOTest03.asm,
output-file LABELGOTOTest03.out,
compare-to LABELGOTOTest03.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 RAM[261]%D2.6.2 RAM[262]%D2.6.2 RAM[263]%D2.6.2 RAM[264]%D2.6.2 RAM[265]%D2.6.2;

set PC 0,
set RAM[0] 256,
set RAM[256] 0,
set RAM[257] 0,
set RAM[258] 0,
set RAM[259] 0,
set RAM[260] 0,
set RAM[261] 0,
set RAM[262] 0;

repeat 300 {
  ticktock;  // Run for 300 clock cycles
}

output;
