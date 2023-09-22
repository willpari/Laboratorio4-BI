# Datos
frecuencia <- c(80, 50, 100, 26, 12)
sectores <- c("x1", "x2", "x3", "x4", "x5")

# Crear el gráfico horizontal
barplot(frecuencia, names.arg = sectores, horiz = TRUE, col = "blue",
        main = "Gráfico Horizontal de Frecuencia por Sectores",
        xlab = "Frecuencia", ylab = "Sectores")