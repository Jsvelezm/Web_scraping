### arreglando los datos descargados de mercado libre

library(readxl)
datos =  read_excel("botines.xlsx")

precio = as.numeric(datos$price)

ventas =  gsub("\r\nventas en los últimos 4 meses.","",datos$infoVentas)

ventas = as.numeric(ventas)


data = cbind(precio,ventas)

plot(precio,ventas)

summary(data)

lm1 = lm(ventas~precio)
summary(lm1)


plot(lm1)


data2 = data[ventas > 800 & precio >800,]

plot(data2[,1],data2[,2])


filtrado = datos[!ventas > 2000 & !precio >600,]
precio2 = precio[!ventas > 2000 & !precio >600]
ventas2 = ventas[!ventas > 2000 & !precio >600]
sum(filtrado[,1],na.rm = T)/4



ve = ventas2^2
ve2 = ventas2^3
ve3 = ventas2^4
ve4 = ventas2^5
ve5 = ventas2^6
ve6 = ventas2^7
ve7 = ventas2^8



lm2 =  lm(precio2~ventas2 +ve +ve2+ve3 +ve4 + ve5 +ve6 +ve7)
summary(lm2)

x = seq(0,600)

y = cbind(1,x,x^2,x^3,x^4,x^5,x^6,x^7,x^8) %*% lm2$coefficients

plot(precio2,ventas2)
lines(x,y)
abline(h=c(150,120),col=c(2,3))

250*80
200*123
