// Sample Test file for ArrSort.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load ArrSort.asm,
output-file ArrSort01.out,
compare-to ArrSort01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[300]%D2.6.2 RAM[301]%D2.6.2 RAM[302]%D2.6.2;

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  300, // Set R1
set RAM[2]  3,  // Set R2
set RAM[300] 2,  // Set Arr[0]
set RAM[301] 4,  // Set Arr[1]
set RAM[302] 1,  // Set Arr[2]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 300,  // Restore arguments in case program used them
set RAM[2] 3,
output;        // Output to file

