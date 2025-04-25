Algoritmo main14
	Subtotal <- 0
	Total <- 0
	IVA <- 0
	price <- 0
	price_code <- ''
	Escribir 'enter code and price'
	Escribir 'bill'
	Repetir
		Escribir 'code'
		Leer price_code
		Si price_code<>'' Entonces
			Escribir 'price: '
			Leer price
			// Sumar al subtotal
			Subtotal <- Subtotal+price
			// Imprimir producto y precio
			Escribir price_code, ': ', price
		FinSi
	Hasta Que price_code=''
	IVA <- Subtotal*0.15
	Total <- Subtotal+IVA
	Escribir '--- Resumen ---'
	Escribir 'Sub Total: ', Subtotal
	Escribir 'IVA (15%): ', IVA
	Escribir 'Total: ', Total
FinAlgoritmo
