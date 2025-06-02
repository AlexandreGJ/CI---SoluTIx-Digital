def avaliar_proposta(notas):
    """
    Avalia uma proposta de licitação com base na média das notas.
    :param notas: Lista de notas (valores de 0 a 10).
    :return: Resultado da avaliação (aprovado ou reprovado).
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    media = sum(notas) / len(notas)
    return "Aprovado" if media >= 7 else "Reprovado"

# Exemplo de uso:
if __name__ == "__main__":
    notas_exemplo = [8, 7.5, 9, 6]
    print(f"Resultado: {avaliar_proposta(notas_exemplo)}")
