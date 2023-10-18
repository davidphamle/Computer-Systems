// Sample Test file for PUSHTest03.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load PUSHTest03.asm,
output-file PUSHTest03.out,
compare-to PUSHTest03.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 RAM[261]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[2]   500,  // Set ARG to RAM[500]
set RAM[500] 100,
set RAM[501] 200,
set RAM[3]   600,  // Set THIS to RAM[600]
set RAM[600] 300,
set RAM[601] 400,
set RAM[4]   700,  // Set THAT to RAM[700]
set RAM[700] 500,
set RAM[701] 600,
set RAM[5]   5,    // Temp 0
set RAM[6]   6,    // Temp 1
set RAM[16]  16,   // Static 0

repeat 200 {
  ticktock;    // Run for 200 clock cycles
}

output;
