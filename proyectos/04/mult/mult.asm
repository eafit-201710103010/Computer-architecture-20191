// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Implementacion comentada con pseudocodigo en base al cual fue escrita

 @R2           // sum = 0
 M=0
 @i            // i = 0
 M=0
 (LOOP)        //while ( true )
  @R1        
  D=M
  @i
  D=D-M        // dif = R1-i
  @END           
  D;JEQ        // if dif=0 goto end
  @R0          // else
  D=M
  @R2
  M=M+D        // sum = sum + R0
  @i
  M=M+1        //i++
  @LOOP
  0,JMP        // goto LOOP
  (END)
  0,JMP       // Ciclo infinito para cerrar