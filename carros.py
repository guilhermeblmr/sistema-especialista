# Função para recomendar os top 5 carros com base nas respostas do usuário
def sistema_especialista():
    print("Bem-vindo ao Sistema Especialista em Carros!")
    print("Vou te ajudar a escolher o carro ideal para você.")
    print("--------------------------------------------------\n")

    # Perguntas sobre preferências do usuário
    estilo = input("Qual estilo de carro você prefere (esportivo, sedan, SUV, hatchback)? ").lower()
    print("----------------------------------------------------------------------------------")
    desempenho = input("Quão importante é o desempenho do carro para você (baixo, médio, alto)? ").lower()
    print("----------------------------------------------------------------------------------")
    espaco = input("Você precisa de bastante espaço interno (sim/não)? ").lower()
    print("----------------------------------------------------------------------------------")
    eficiencia = input("Quão importante é a eficiência de combustível para você (baixa, média, alta)? ").lower()
    print("----------------------------------------------------------------------------------")
    preco = input("Qual é o seu orçamento para o carro (baixo, médio, alto)? ").lower()
    print("----------------------------------------------------------------------------------")
    marca = input("Você tem alguma marca de carro preferida? (Digite apenas o nome da marca, deixe em branco se não tiver preferência) ").lower()
    print("----------------------------------------------------------------------------------")

    # Critérios de seleção baseados nas respostas
    recomendacoes = []

    # Estilo
    if estilo == "esportivo":
        recomendacoes += ["Chevrolet Corvette", "Porsche 911", "Ford Mustang", "BMW M4", "Audi R8"]
    elif estilo == "sedan":
        recomendacoes += ["Toyota Camry", "Honda Accord", "Nissan Altima", "BMW 7 Series", "Mercedes-Benz S-Class"]
    elif estilo == "suv":
        recomendacoes += ["Toyota RAV4", "Honda CR-V", "Ford Escape", "Chevrolet Equinox", "Subaru Outback"]
    elif estilo == "hatchback":
        recomendacoes += ["Volkswagen Gol", "Chevrolet Onix", "Ford Ka", "Honda Fit", "Peugeot 208"]
    else:
        print("Estilo de carro não reconhecido. Escolha entre 'esportivo', 'sedan', 'SUV' ou 'hatchback'.")

    # Desempenho
    if desempenho == "alto":
        recomendacoes += ["Chevrolet Corvette", "Ford Mustang", "Porsche 911", "BMW M4", "Audi R8", "Mercedes-AMG GT", "BMW 7 Series", "Audi A8", "Lexus LS", "Porsche Panamera", "Jaguar XJ", "Cadillac CT6", "Maserati Quattroporte", "Bentley Flying Spur", "Rolls-Royce Ghost"]
    elif desempenho == "médio":
        recomendacoes += ["Toyota Camry", "Toyota Corolla", "Honda Accord", "Hyundai Elantra", "Nissan Sentra", "Honda Civic", "Volkswagen Polo", "Nissan Altima", "Toyota RAV4", "Honda CR-V", "Ford Escape", "Volkswagen Gol", "Chevrolet Onix", "Ford Ka", "Honda Fit", "Peugeot 208"]
    elif desempenho == "baixo":
        recomendacoes += ["Toyota Prius", "Toyota Yaris", "Honda Insight", "Kia Forte", "Ford Fiesta", "Chevrolet Sonic", "Renault Sandero", "Fiat Cronos", "Hyundai HB20S", "Toyota Etios", "Chevrolet Prisma", "Ford EcoSport", "Chevrolet Spin", "Nissan Kicks", "Honda WR-V", "Renault Captur", "Hyundai Creta", "Volkswagen T-Cross", "Ford Territory"]

    # Espaço
    if espaco == "sim":
        recomendacoes += ["Toyota RAV4", "Honda CR-V", "Ford Escape", "Chevrolet Equinox", "Jeep Grand Cherokee", "Subaru Outback", "Hyundai Tucson", "Mazda CX-5", "Kia Sportage", "Toyota Camry", "Honda Accord", "Nissan Altima", "Hyundai Sonata", "Ford Fusion", "Chevrolet Malibu", "Subaru Legacy", "Mazda6", "Kia Optima", "Volkswagen Passat"]
    elif espaco == "não":
        recomendacoes += ["Chevrolet Corvette", "Porsche 911", "Ford Mustang", "BMW M4", "Audi R8", "Toyota Camry", "Honda Accord", "Nissan Altima", "Volkswagen Gol", "Chevrolet Onix", "Ford Ka", "Honda Fit", "Peugeot 208"]

    # Eficiência de combustível
    if eficiencia == "alta":
        recomendacoes += ["Toyota Prius", "Toyota Corolla Hybrid", "Toyota Yaris Hybrid", "Honda Insight Hybrid", "Honda Civic Hatchback", "Hyundai Ioniq Hybrid", "Kia Niro", "Toyota Avalon Hybrid", "Lexus ES Hybrid", "Toyota RAV4 Hybrid", "Honda CR-V Hybrid", "Ford Escape Hybrid", "Chevrolet Equinox Diesel", "Toyota Camry Hybrid", "Honda Accord Hybrid"]
    elif eficiencia == "média":
        recomendacoes += ["Toyota Corolla", "Toyota Yaris", "Honda Civic", "Hyundai Elantra", "Kia Forte", "Nissan Sentra", "Ford Fiesta", "Chevrolet Sonic", "Volkswagen Polo", "Renault Sandero", "Fiat Cronos", "Hyundai HB20S", "Chevrolet Prisma", "Ford EcoSport", "Chevrolet Spin", "Nissan Kicks", "Honda WR-V", "Renault Captur", "Hyundai Creta", "Volkswagen T-Cross", "Ford Territory"]
    elif eficiencia == "baixa":
        recomendacoes += ["Chevrolet Corvette", "Porsche 911", "Ford Mustang", "BMW M4", "Audi R8", "BMW 7 Series", "Mercedes-Benz S-Class", "Audi A8", "Lexus LS", "Porsche Panamera", "Jaguar XJ", "Cadillac CT6", "Maserati Quattroporte", "Bentley Flying Spur", "Rolls-Royce Ghost"]

    # Preço
    if preco == "baixo":
        recomendacoes += ["Volkswagen Gol", "Chevrolet Onix", "Ford Ka", "Fiat Argo", "Renault Kwid", "Toyota Etios", "Hyundai HB20", "Nissan March", "Honda Fit", "Peugeot 208"]
    elif preco == "médio":
        recomendacoes += ["Toyota Corolla", "Honda Civic", "Hyundai Elantra", "Kia Forte", "Nissan Sentra", "Ford Fiesta", "Chevrolet Sonic", "Volkswagen Polo", "Renault Sandero", "Fiat Cronos", "Hyundai HB20S", "Chevrolet Prisma", "Ford EcoSport", "Chevrolet Spin", "Nissan Kicks", "Honda WR-V", "Renault Captur", "Hyundai Creta", "Volkswagen T-Cross", "Ford Territory"]
    elif preco == "alto":
        recomendacoes += ["Mercedes-AMG GT", "BMW M4", "Audi R8", "BMW 7 Series", "Mercedes-Benz S-Class", "Audi A8", "Lexus LS", "Porsche Panamera", "Jaguar XJ", "Cadillac CT6", "Maserati Quattroporte", "Bentley Flying Spur", "Rolls-Royce Ghost"]

    # Marca preferida
    if marca:
        recomendacoes = [carro for carro in recomendacoes if marca in carro.lower()]

    # Remover duplicatas da lista de recomendações
    recomendacoes = list(set(recomendacoes))

    # Imprimir as top 5 recomendações
    print("\nCom base nas suas respostas, as melhores opções de carros para você são:")
    for i in range(min(5, len(recomendacoes))):
        print(f"{i+1}. {recomendacoes[i]}")

# Chamada da função principal
sistema_especialista()
