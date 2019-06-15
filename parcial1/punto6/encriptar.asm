	@dir
	M=16  //Aqui empiezo a guardar
	@val
	M=170  //Valor por el que voy a hacer Xor
	@dib
	M=16   //Guardo pos inicial
	@pix
	M=16384   //Posicion inciio pantalla
	(LOOP)
	@dir
	D=M
	@dirfin
	M=D        //Voy guardando hasta que posicion he escrito
	@KBD
	D=M
	@128
	D=D-A    //Si la tecla es enter voy a pintar
	@MESSAGE
	D;JEQ
	@KBD
	D=M       // Sino, obtengo tecla
	@val
	D=DxM     //Tecla Xor 170
	@dir
	A=M
	M=D      //Guardo el resultado en cierta direccion
	@dir
	M=M+1    //Aumento la direccion
	@LOOP
	0;JMP
	(MESSAGE)
	@dib    // Empiexo en dir inicial
	D=M
	@dirfin
	D=D-M   //Si es mayor a la ultima termino 
	@END
	D;JGT
	@dib     //Obtengo mensaje encriptado
	A=M
	D=M
	@pix    //Lo dibujo 
	M=D	
	@dib
	M=M+1    //Aumento direccion
	@pix
	M=M+1    //Aumento direccion de dibujo 
	@MESSAGE
	O;JMP     // Vuelvo al ciclo
	(END)
	@END      // Ciclo infinito para cerrar
	0;JMP
	
	
	
	
