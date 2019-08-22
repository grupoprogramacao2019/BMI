alturaFloat = input("Digite sua altura: ")
pesoFloat = input("Digite seu peso: ")

imc = pesoFloat/(alturaFloat**2)
print(imc)

if imc < 17.0:
    print("Muito abaixo do peso!")
elif imc >= 17.0 and imc <= 18:
    print("Abaixo do peso normal!")
elif imc > 18.5 and imc <= 25.0:
    print("Peso dentro do normal!")
elif imc > 25.0 and imc <= 30.0:
    print("Acima do peso normal !")
else:
    print("Muito acima do peso ? ")