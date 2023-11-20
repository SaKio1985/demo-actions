def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a // b

if __name__ == "__main__":
    try:
        resultado = division(5, 3)
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")