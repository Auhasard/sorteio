import random

opcoes = ['Filmes', 'Séries', 'Animes', 'Jogos', 'Cafés', 'Restaurantes']
print('Escolha uma opção: ')
for i, opcao in enumerate(opcoes):
    print(f'{i+1}, {opcao}')
escolha = input('Digite o número da opção escolhida: ')
while not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(opcoes):
    print("Escolha inválida. Tente novamente.")
    escolha = input("Digite o número da opção escolhida: ")

escolha = int(escolha) - 1

if opcoes[escolha] == "Filmes":
    resultado = random.choice(['Atlantis', 'Viagem de Chihiro',
                               'Castelo Animado', 'A Ilha', 'Ex Machina', "Koe No Katachi", 'Meu amigo Totoro', 'O Túmulo dos Vagalumes'])
elif opcoes[escolha] == "Séries":
    resultado = random.choice(['Cobra Kai', 'Brooklin 99'])
elif opcoes[escolha] == "Animes":
    resultado = random.choice(
        ['Kaguya Sama', 'Fullmetal Alchemist', 'Nana', 'Ice guy and his cool female colleague', 'Oshi no Ko'])
elif opcoes[escolha] == "Jogos":
    resultado = random.choice(['The Last Of Us', 'The Last Of Us 2', 'Resident Evil 4', 'Slay the Spire',
                               'Overcooked', 'It takes Two', 'Nier', "Don't Starve Together", 'Danganronpa', 'Helltaker', "Mario", 'Stray'])
elif opcoes[escolha] == "Cafés":
    resultado = random.choice(['Negrita Bar Café', 'Nanica', 'Arte & Letra, Livraria e Café',])
elif opcoes[escolha] == "Restaurantes":
    resultado = random.choice(['Nayme Culinária Árabe', 'NUU NIKKEI','Famiglia Fadanelli','Ícaro Casual Greek Food', 'Pata Negra Bar & Cocina', 
                               'Thai Restaurante Tailandês', "C'La Vie Restaurante Francês", 'Chez Margot Restaurante Francês', 'Strô', 'Taisho',
                               'Jack Pizzaria', 'Green Dog'])

print(
    f"Você escolheu '{opcoes[escolha]}' e o resultado do sorteio foi: '{resultado}'")
