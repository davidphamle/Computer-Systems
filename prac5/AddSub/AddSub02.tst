load AddSub.asm,
output-file AddSub02.out,
compare-to AddSub02.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

set PC 0,
set RAM[1] 6,  // Set R1
set RAM[2] 10,  // Set R2
set RAM[3] 5;  // Set R3
repeat 100 {
  ticktock;
}
set RAM[1] 6,  // Restore values
set RAM[2] 10,
set RAM[3] 5,
output;
