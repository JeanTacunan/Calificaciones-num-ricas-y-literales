class Calificacion:
    def __init__(self, calificacion: float):
        self.calificacion = calificacion

    def obtener_letra(self) -> str:
        if self.calificacion > 9.0:
            return "La calificación es A."
        elif self.calificacion > 8.0:
            return "La calificación es B."
        elif self.calificacion >= 7.5:
            return "La calificación es C."
        else:
            return "La calificación es R."

def main():
    try:
        calificacion_input = float(input("Ingrese la calificación: "))
        calificacion_obj = Calificacion(calificacion_input)
        resultado = calificacion_obj.obtener_letra()
        print(resultado)
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
