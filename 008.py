salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_total = salario_hora * horas_trabalhadas_mes
print(
    "Ganhando R${} a hora, tendo trabalhado "
    "{} horas no mês, seu salário este mês "
    "é de R${}.".format(salario_hora,horas_trabalhadas_mes)
)
