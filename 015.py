n1= float(input("Digite quanto você ganha por hora: "))
n2= float(input("Digite quantas horas você trabalhou esse mês: "))
salario= n1 * n2
impostorenda= salario * (11/100)
inss= salario * (8/100)
sindicato= salario * (5/100)
salarioliq= salario - impostorenda - inss - sindicato
print("o salario bruto é {}, o imposto de renda é {}, o inss é {}, o sindicato é {}, o salario liquido é {}".format(salario,impostorenda,inss, sindicato,salarioliq))
