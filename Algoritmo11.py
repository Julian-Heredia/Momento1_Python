Titulo_de_bachiller = str(input("Usted posee un titulo de bachiller?: "))

if (Titulo_de_bachiller == "si"):print("Felicidades, puede acceder al grado superior!!")

else:print("Debido a que no tiene un titulo, debe respnder una serie de preguntas: \n")
pregunta1 = int(input("Cuantos años dura una tecnica en CESDE?: "))

if (pregunta1 != 2):print("Ha fallado, suerte en la proxima")

else:print("Felicidades, siguiente pregunta: \n")
pregunta2 = str(input("Que es GIT?: "))

if (pregunta2 == "un controlador de versiones"):print("Felicidades, puede acceder al grado superior!!")

else:print("Ha fallado, suerte en la proxima")