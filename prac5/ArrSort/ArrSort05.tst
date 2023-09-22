// Sample Test file for ArrSort.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load ArrSort.asm,
output-file ArrSort05.out,
compare-to ArrSort05.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[1000]%D2.6.2 RAM[1001]%D2.6.2 RAM[1002]%D2.6.2 RAM[1003]%D2.6.2 RAM[1004]%D2.6.2;

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  1000, // Set R1
set RAM[2]  5,  // Set R2
set RAM[1000] -1,  // Set Arr[0]
set RAM[1001] -10,  // Set Arr[1]
set RAM[1002] -100,  // Set Arr[2]
set RAM[1003] 2;  // Set Arr[3]
set RAM[1004] 0;  // Set Arr[4]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1000,  // Restore arguments in case program used them
set RAM[2] 5,
output;        // Output to file

