alturaFloat = 1.59
pesoFloat = 52.0

imc = pesoFloat/(alturaFloat**2)
print(imc)

print("imc muito abaixo do peso:", imc <17.0)
print("imc abaixo do peso:", imc>17.0 and imc<=18.5)
print("imc peso dentro do normal:", imc>18.5 and imc<=25.0)
print("imc acima do normal:", imc>25.0 and imc<=30.0)
print("imc muito acima do normal:", imc>30.0)