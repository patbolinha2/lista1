altura = float(input("Digite sua altura em metros: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
print(
    f"O peso ideal para sua altura é:\n{peso_ideal_homem:.2f}Kg para homens.\n"
    f"{peso_ideal_mulher:.2f}Kg para mulheres."
)
