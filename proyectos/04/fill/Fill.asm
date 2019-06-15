// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Implementacion comentada con pseudocodigo en base al cual fue escrita

(CICLO)
	@SCREEN
	D=A            
	@dir            
	M=D           // pixelActual = pixelInicio
	@8192       
	D=D+A
	@dirfin       // pixelFin
	M=D
	@KBD          // getKBD
	D=M           
	@BLANCO      
	D;JEQ         // if KBD = 0 goto Blanco
	@color        // else setColor Negro
	M=-1 
	@DIBUJAR      // goto dibujar
	0;JMP 
(BLANCO)
	@color        // setColor Blanco
	M=0
(DIBUJAR)
	@dirfin       
	D=M
	@dir         
	D=D-M         // dif = pixelFin - pixelActual
	@CICLO       
	D;JEQ         // if dif=0 goto Inicio
	@color        // else getColor
	D=M
	@dir        
	A=M          // pix = getPixel(dir)
	M=D          // pix.setColor(color)
	@dir        
	M=M+1       //  dir++
	@DIBUJAR     
	0;JMP       //  goto dibujar