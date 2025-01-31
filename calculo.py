def inverter_string(texto):
    if texto is None:
        raise ValueError("O parâmetro 'texto' não pode ser None.")

    if not isinstance(texto, str):
        raise TypeError("O parâmetro 'texto' deve ser do tipo string.")

    if len(texto.strip()) == 0:
        raise ValueError("A string fornecida está vazia.")

    chars = list(texto)
    
    inicio = 0
    fim = len(chars) - 1
    
    while inicio < fim:
        chars[inicio], chars[fim] = chars[fim], chars[inicio]
        inicio += 1
        fim -= 1
    
    return "".join(chars)


def main():
    try:
        texto_digitado = input("Digite a string que deseja inverter: ")

        resultado = inverter_string(texto_digitado)

        print(f"String original: {texto_digitado}")
        print(f"String invertida: {resultado}")

    except (TypeError, ValueError) as e:
        print(f"Erro ao inverter string: {e}")


if __name__ == "__main__":
    main()



