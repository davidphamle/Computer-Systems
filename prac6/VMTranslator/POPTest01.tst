// Sample Test file for POPTest01.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load POPTest01.asm,
output-file POPTest01.out,
compare-to POPTest01.cmp,
output-list RAM[0]%D2.6.2 RAM[302]%D2.6.2 RAM[501]%D2.6.2 RAM[600]%D2.6.2 RAM[701]%D2.6.2;

set PC 0,
set RAM[0]   256,  // Set R0
set RAM[1]   300,  // Set LCL to RAM[300]
set RAM[300] 0,
set RAM[301] 0,
set RAM[302] 0,
set RAM[2]   500,  // Set ARG to RAM[500]
set RAM[500] 100,
set RAM[501] 200,
set RAM[3]   600,  // Set THIS to RAM[600]
set RAM[600] 300,
set RAM[601] 400,
set RAM[4]   700,  // Set THAT to RAM[700]
set RAM[700] 500,
set RAM[701] 600;

repeat 200 {
  ticktock;    // Run for 200 clock cycles
}

output;
