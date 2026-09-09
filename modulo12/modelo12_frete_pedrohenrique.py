def calcular_frete(peso, distancia):
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")

    if distancia < 0:
        raise ValueError("A distância não pode ser negativa.")

    valor = 10.00 + (peso * 2.00) + (distancia * 0.05)
    return round(valor, 2)
