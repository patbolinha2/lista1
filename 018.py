
arqv= float(input("Digite o tamanho do arquivo em mb: "))
vlc = float(input("Digite a velocidade da conexão em mbps: "))
tmp= arqv /(vlc/8)
minutos = tmp / 60
print("{} min".format(minutos))
