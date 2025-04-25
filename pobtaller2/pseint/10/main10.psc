Algoritmo main10
	Escribir ' enter entering hour'
	entering_hour <- 0
	exiting_hour <- 0
	payment <- 0
	Leer entering_hour
	Escribir ' enter exiting hour'
	Leer exiting_hour
	time <- exiting_hour-entering_hour
	Escribir time, ' hours of parking'
	payment <- 1000+((time-1)*600)
	Escribir ' bill of ', payment, ' bolivares'
FinAlgoritmo
