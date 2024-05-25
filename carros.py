def perguntar(pergunta, opcoes):
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    escolha = int(input("Escolha uma opção (número): "))
    return escolha

def coletar_respostas():
    respostas = {}
    
    # Pergunta sobre o estilo do carro
    respostas['estilo'] = perguntar(
        "Qual estilo de carro você prefere?",
        ["Esportivo", "Sedan", "SUV", "Hatchback"]
    )
    
    # Pergunta se o carro deve ser elétrico
    respostas['eletrico'] = perguntar(
        "Você está interessado em um carro elétrico?",
        ["Sim", "Não"]
    )
    
    # Pergunta sobre o desempenho do carro
    respostas['desempenho'] = perguntar(
        "Quão importante é o desempenho do carro para você?",
        ["Baixo", "Médio", "Alto"]
    )
    
    # Pergunta sobre o espaço interno (se não for SUV ou esportivo)
    if respostas['estilo'] not in [1, 3]:  # 1: Esportivo, 3: SUV
        respostas['espaco'] = perguntar(
            "Você precisa de bastante espaço interno?",
            ["Sim", "Não"]
        )
    
    # Se não for elétrico, perguntar sobre eficiência de combustível
    if respostas['eletrico'] == 2:
        respostas['combustivel'] = perguntar(
            "Quão importante é a eficiência de combustível para você?",
            ["Baixa", "Média", "Alta"]
        )
    
    # Pergunta sobre o orçamento
    respostas['orcamento'] = perguntar(
        "Qual é o seu orçamento para o carro?",
        ["Baixo", "Médio", "Alto"]
    )
    
    return respostas

def recomendar_carro(respostas):
    estilo = respostas['estilo']
    desempenho = respostas['desempenho']
    eletrico = respostas['eletrico']
    espaco = respostas.get('espaco', 2)  # Padrão para "Não" se não existir
    combustivel = respostas.get('combustivel', 2)  # Padrão para "Média" se não existir
    orcamento = respostas['orcamento']
    
    if eletrico == 1:
        if estilo == 3:  # SUV elétrico
            return "Considere um SUV elétrico como o Volvo EX30."
        elif estilo == 2:  # Sedan elétrico
            return "Um sedan elétrico como o JAC E-J7 seria ideal."
        elif estilo == 4:  # Hatchback elétrico
            return "Um hatchback elétrico como o Nissan Leaf seria uma boa escolha."
        else:  # Estilo esportivo elétrico
            return "Carros esportivos elétricos são raros, mas o Rimac Nevera pode ser considerado."
    
    # Baseado nas respostas, vamos fazer algumas recomendações simples
    if estilo == 1:  # Esportivo
        if desempenho == 3:  # Alto desempenho
            return "Você deve considerar um carro esportivo de alto desempenho, como um Porsche 911."
        else:
            return "Você pode gostar de um carro esportivo como um Ford Mustang."
    
    elif estilo == 2:  # Sedan
        if espaco == 1:  # Precisa de bastante espaço
            return "Um sedan espaçoso como o Toyota Camry seria uma boa escolha."
        else:
            return "Um sedan compacto como o Honda Civic pode ser adequado."
    
    elif estilo == 3:  # SUV
        if orcamento == 1:  # Baixo orçamento
            return "Considere um SUV econômico como o Ford EcoSport."
        else:
            return "Um SUV como o BMW X5 pode ser uma boa escolha."
    
    elif estilo == 4:  # Hatchback
        if combustivel == 3:  # Alta eficiência de combustível
            return "Um hatchback econômico como o Toyota Prius seria ideal."
        else:
            return "Um hatchback versátil como o Volkswagen Golf pode ser uma boa escolha."
    
    return "Com base nas suas respostas, não temos uma recomendação específica, mas sugerimos consultar um especialista."

# Função principal para executar o sistema
def main():
    print("Bem-vindo ao sistema especialista de escolha de carro!")
    respostas = coletar_respostas()
    recomendacao = recomendar_carro(respostas)
    print(f"Recomendação: {recomendacao}")

if __name__ == "__main__":
    main()
