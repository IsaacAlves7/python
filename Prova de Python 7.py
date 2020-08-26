preço= input ('Digite o preço:')
if preço < 1000:
    novo = preço + 50
else:
    novo = preço - 35

    novo = if preço < 1000 preço + 50 else preço - 35
    print(preço)