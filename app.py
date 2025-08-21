import os
import random


def quiz(questions):
    total_questions_int = number_of_questions(questions)
    selected_questions = random_questions(total_questions_int, questions)

    correct_answers = 0
    wrong_answers = 0
    current_total_questions = 0

    for index_current_question, current_question in enumerate(selected_questions):
        show_question(index_current_question, current_question)

        current_total_questions += 1

        show_options(current_question)

        user_choice = get_answer()

        is_correct = validate_answer(user_choice, current_question)
        if is_correct:
            correct_answers += 1
        else:
            wrong_answers += 1

        sum_correct_answers(correct_answers, wrong_answers, current_total_questions)

    final_message(correct_answers, wrong_answers, current_total_questions)


def number_of_questions(questions):
    possible_questions = len(questions)
    number_of_questions = input(
        f"Você pode escolher até {possible_questions}.\nDigite o número de perguntas que deseja: "
    )
    number_of_questions_int = int(number_of_questions)
    return number_of_questions_int


def random_questions(total_questions_int, questions):
    randomic_questions = random.sample(questions, total_questions_int)
    return randomic_questions


def show_question(index_current_question, current_question):
    print(f"\nPergunta {index_current_question + 1}: {current_question["Pergunta"]}")


def show_options(current_question):
    for index_option, option in enumerate(current_question["Opções"]):
        print(f"{index_option + 1}) {option}")


def get_answer():
    selected_option = input("Digite a alternativa correta: ")
    selected_option_int = int(selected_option)
    return selected_option_int - 1


def validate_answer(user_choice, current_question):
    user_choice_text = current_question["Opções"][user_choice]
    if user_choice_text == current_question["Resposta"]:
        print(f"\nResposta correta ✅")
        return True
    else:
        print(f"\nResposta incorreta ❌")
        return False


def sum_correct_answers(correct_answers, wrong_answers, current_total_questions):
    print(f"\n{correct_answers} ✅ \n{wrong_answers} ❌\n")


def corrects_percentage(correct_answers, current_total_questions):
    percentage_right = (correct_answers / current_total_questions) * 100
    print(f"Porcentagem: {percentage_right:.2f}%")


def final_message(correct_answers, wrong_answers, current_total_questions):
    os.system("clear")
    sum_correct_answers(correct_answers, wrong_answers, current_total_questions)
    corrects_percentage(correct_answers, current_total_questions)


questions = [
    {
        "Pergunta": "Quantas cores tem o arco-íris?",
        "Opções": ["Sete", "Oito", "Nove", "Dez"],
        "Resposta": "Sete",
    },
    {
        "Pergunta": "Primogênito é o nome dado a qual filho de um casal?",
        "Opções": [
            "Segundo filho",
            "Último filho",
            "Filho do meio",
            "Primeiro filho",
        ],
        "Resposta": "Primeiro filho",
    },
    {
        "Pergunta": "Qual é a letra que antecede a letra O no alfabeto brasileiro?",
        "Opções": ["M", "N", "P", "Q"],
        "Resposta": "N",
    },
    {
        "Pergunta": "Quantas patas uma formiga possui?",
        "Opções": ["8", "6", "4", "10"],
        "Resposta": "6",
    },
    {
        "Pergunta": "Os faraós eram governantes de qual país?",
        "Opções": ["Grécia", "Índia", "Roma", "Egito"],
        "Resposta": "Egito",
    },
    {
        "Pergunta": "Qual é o nome do único satélite natural da Terra?",
        "Opções": ["Tupã", "Lua", "Titã", "Io"],
        "Resposta": "Lua",
    },
    {
        "Pergunta": "Qual é o único país onde o animal coala vive?",
        "Opções": ["Brasil", "Estados Unidos", "Canadá", "Austrália"],
        "Resposta": "Austrália",
    },
    {
        "Pergunta": "As cores vermelho e azul misturadas formam qual cor?",
        "Opções": ["Roxo", "Amarelo", "Verde", "Laranja"],
        "Resposta": "Roxo",
    },
    {
        "Pergunta": "Quantos anos tem um século?",
        "Opções": ["100", "10", "1000", "50"],
        "Resposta": "100",
    },
    {
        "Pergunta": "Quem pintou o quadro Mona Lisa?",
        "Opções": [
            "Van Gogh",
            "Osmar de Barros",
            "Leonardo da Vinci",
            "Leonardo DiCaprio",
        ],
        "Resposta": "Leonardo da Vinci",
    },
    {
        "Pergunta": "Quem nasce em Pernambuco é o que?",
        "Opções": ["Pernambuquês", "Pernambués", "Pernambucólico", "Pernambucano"],
        "Resposta": "Pernambucano",
    },
    {
        "Pergunta": "Que nome se dá para o coletivo de lobos?",
        "Opções": ["Alcateia", "Cardume", "Vexame", "Matilha"],
        "Resposta": "Alcateia",
    },
    {
        "Pergunta": "Como é o nome da energia gerada pelo vento?",
        "Opções": ["Hídrica", "Térmica", "Eólica", "Química"],
        "Resposta": "Eólica",
    },
    {
        "Pergunta": "Qual é o maior país da América do Sul?",
        "Opções": ["Brasil", "Argentina", "Chile", "Colômbia"],
        "Resposta": "Brasil",
    },
    {
        "Pergunta": "Como é chamado o macho da cabra?",
        "Opções": ["Cabrito", "Bode", "Carneiro", "Touro"],
        "Resposta": "Bode",
    },
    {
        "Pergunta": "Como é chamado o maior osso do corpo humano?",
        "Opções": ["Fêmur", "Úmero", "Tíbia", "Costela"],
        "Resposta": "Fêmur",
    },
    {
        "Pergunta": "Qual é o sistema de governo adotado no Brasil?",
        "Opções": [
            "Monarquia parlamentarista",
            "República presidencialista",
            "Ditadura militar",
            "República parlamentarista",
        ],
        "Resposta": "República presidencialista",
    },
    {
        "Pergunta": "Qual é a floresta tropical mais extensa do mundo?",
        "Opções": [
            "Floresta Amazônica",
            "Floresta Negra",
            "Floresta de Sherwood",
            "Floresta do Congo",
        ],
        "Resposta": "Floresta Amazônica",
    },
    {
        "Pergunta": "Qual desses não é o nome de um oceano?",
        "Opções": ["Polar", "Oceano Negro", "Pacífico", "Índico"],
        "Resposta": "Oceano Negro",
    },
    {
        "Pergunta": "Qual é a fórmula da água?",
        "Opções": ["H2O", "CO2", "NaCl", "C6H12O6"],
        "Resposta": "H2O",
    },
    {
        "Pergunta": "Qual objeto costuma ser jogado pela noiva durante a festa de casamento?",
        "Opções": ["Véu", "Sapato", "Aliança", "Buquê de flores"],
        "Resposta": "Buquê de flores",
    },
    {
        "Pergunta": "Qual é o nome do famoso navio que naufragou em 1912 e foi tema de um filme?",
        "Opções": ["Queen Mary", "Enterprise", "Titanic", "Dear Rose"],
        "Resposta": "Titanic",
    },
    {
        "Pergunta": "Quantos dias tem um ano bissexto?",
        "Opções": ["365", "366", "367", "364"],
        "Resposta": "366",
    },
    {
        "Pergunta": "Qual é o maior continente do mundo?",
        "Opções": ["Europa", "América", "África", "Ásia"],
        "Resposta": "Ásia",
    },
    {
        "Pergunta": "Qual país tem como capital a cidade de Lisboa?",
        "Opções": ["Espanha", "Portugal", "França", "Itália"],
        "Resposta": "Portugal",
    },
    {
        "Pergunta": "Quem é o responsável por buscar e devolver a bola ao campo durante um jogo de futebol?",
        "Opções": ["Goleiro", "Zagueiro", "Atacante", "Gandula"],
        "Resposta": "Gandula",
    },
    {
        "Pergunta": "Você tem 36 laranjas e joga um terço fora, com quantas você fica?",
        "Opções": ["6", "24", "12", "18"],
        "Resposta": "24",
    },
    {
        "Pergunta": "Quanto é 50% de 300?",
        "Opções": ["25", "50", "100", "150"],
        "Resposta": "150",
    },
    {
        "Pergunta": "Qual é a capital da Espanha?",
        "Opções": ["Valência", "Barcelona", "Sevilla", "Madrid"],
        "Resposta": "Madrid",
    },
    {
        "Pergunta": "Quantos séculos há em um milênio?",
        "Opções": ["2 séculos", "10 séculos", "20 séculos", "15 séculos"],
        "Resposta": "10 séculos",
    },
    {
        "Pergunta": "Qual é o metal mais caro do mundo?",
        "Opções": ["Ouro", "Platina", "Ródio", "Paládio"],
        "Resposta": "Ródio",
    },
    {
        "Pergunta": "Qual é a cor do sangue arterial?",
        "Opções": ["Vermelho", "Azul", "Roxo", "Preto"],
        "Resposta": "Vermelho",
    },
    {
        "Pergunta": "Qual é o nome da haste de madeira de extremidade achatada usada para remar?",
        "Opções": ["Vela", "Timão", "Remo", "Leme"],
        "Resposta": "Remo",
    },
    {
        "Pergunta": "Qual animal é conhecido como o 'rei da selva'?",
        "Opções": ["Leopardo", "Tigre", "Leão", "Onça"],
        "Resposta": "Leão",
    },
    {
        "Pergunta": "Qual é o mineral capaz de enfraquecer o Super-Homem?",
        "Opções": ["Ametista", "Quartzo", "Diamante", "Kriptonita"],
        "Resposta": "Kriptonita",
    },
    {
        "Pergunta": "Qual é o coletivo de lobos?",
        "Opções": ["Matilha", "Bando", "Alcateia", "Manada"],
        "Resposta": "Alcateia",
    },
    {
        "Pergunta": "A moranga é uma variedade de:",
        "Opções": ["Morango", "Abóbora", "Melancia", "Ameixa"],
        "Resposta": "Abóbora",
    },
    {
        "Pergunta": "Como é chamado um ângulo de 90º?",
        "Opções": ["Reto", "Obtuso", "Agudo", "Raso"],
        "Resposta": "Reto",
    },
    {
        "Pergunta": "O tomate é um(a)…",
        "Opções": ["Fruta", "Verdura", "Legume", "Raiz"],
        "Resposta": "Fruta",
    },
    {
        "Pergunta": "Qual é o nome do primeiro presidente negro eleito nos Estados Unidos?",
        "Opções": ["George W. Bush", "Bill Clinton", "Barack Obama", "Donald Trump"],
        "Resposta": "Barack Obama",
    },
    {
        "Pergunta": "Quantos dias há em 3 semanas?",
        "Opções": ["14", "18", "21", "28"],
        "Resposta": "21",
    },
    {
        "Pergunta": "O que as abelhas fabricam?",
        "Opções": ["Seda", "Mel", "Pólen", "Algodão"],
        "Resposta": "Mel",
    },
    {
        "Pergunta": "A metade de 2 x 8 é igual a?",
        "Opções": ["12", "16", "8", "10"],
        "Resposta": "8",
    },
    {
        "Pergunta": "Qual é o animal que mata mais humanos por ano?",
        "Opções": ["Tubarão", "Crocodilo", "Mosquito", "Cobra"],
        "Resposta": "Mosquito",
    },
    {
        "Pergunta": "Um quilômetro equivale a quantos metros?",
        "Opções": ["60 metros", "100 metros", "1000 metros", "10000 metros"],
        "Resposta": "1000 metros",
    },
    {
        "Pergunta": "O azeite de oliva é feito de quê?",
        "Opções": ["Azeitona", "Milho", "Canola", "Oliveira"],
        "Resposta": "Azeitona",
    },
    {
        "Pergunta": "Como se chama a passagem da água do estado líquido para o sólido?",
        "Opções": ["Solidificação", "Vaporização", "Condensação", "Fusão"],
        "Resposta": "Solidificação",
    },
    {
        "Pergunta": "Qual é o nome da substância responsável pela cor verde das plantas?",
        "Opções": ["Melanina", "Hemoglobina", "Clorofila", "Antocianina"],
        "Resposta": "Clorofila",
    },
    {
        "Pergunta": "A música 'Livre estou' faz parte da trilha sonora de qual desenho animado?",
        "Opções": [
            "Frozen – Uma Aventura Congelante",
            "O Rei Leão",
            "Moana – Um Mar de Aventuras",
            "Enrolados",
        ],
        "Resposta": "Frozen – Uma Aventura Congelante",
    },
    {
        "Pergunta": "Complete o ditado: 'Quando a esmola é grande, o santo…'",
        "Opções": ["foge.", "desconfia.", "pede mais.", "se aproxima,"],
        "Resposta": "desconfia.",
    },
    {
        "Pergunta": "Qual é o nome do rio que corta a cidade de Paris?",
        "Opções": ["Tamisa", "Sena", "Rio de Janeiro", "Danúbio"],
        "Resposta": "Sena",
    },
    {
        "Pergunta": "Qual planeta do Sistema Solar é conhecido como “Planeta Vermelho”?",
        "Opções": ["Vênus", "Marte", "Júpiter", "Saturno"],
        "Resposta": "Marte",
    },
    {
        "Pergunta": "O Suriname está localizado em qual continente?",
        "Opções": ["América do Sul", "América Central", "África", "Europa"],
        "Resposta": "América do Sul",
    },
    {
        "Pergunta": "Qual é o principal ingrediente do prato mexicano guacamole?",
        "Opções": ["Carne", "Feijão", "Arroz", "Abacate"],
        "Resposta": "Abacate",
    },
    {
        "Pergunta": "Quantos planetas tem o Sistema Solar?",
        "Opções": ["7", "8", "9", "10"],
        "Resposta": "8",
    },
    {
        "Pergunta": "Qual é o nome verdadeiro da cantora Anitta?",
        "Opções": [
            "Anitta é o seu nome verdadeiro",
            "Larissa",
            "Maria",
            "Bruna Gabriela",
        ],
        "Resposta": "Larissa",
    },
    {
        "Pergunta": "A bile é produzida por qual órgão do corpo humano?",
        "Opções": ["Vesícula biliar", "Pâncreas", "Fígado", "Baço"],
        "Resposta": "Fígado",
    },
    {
        "Pergunta": "Qual foi a primeira capital do Brasil?",
        "Opções": ["Salvador", "São Paulo", "Rio de Janeiro", "Brasília"],
        "Resposta": "Salvador",
    },
    {
        "Pergunta": "Quantos ossos tem o corpo humano?",
        "Opções": ["206", "316", "186", "209"],
        "Resposta": "206",
    },
    {
        "Pergunta": "“Rojo” significa qual cor, em espanhol?",
        "Opções": ["Roxo", "Verde", "Vermelho", "Azul"],
        "Resposta": "Vermelho",
    },
    {
        "Pergunta": "Qual é o idioma oficial da China?",
        "Opções": ["Cantonês", "Mandarim", "Tibetano", "Mongol"],
        "Resposta": "Mandarim",
    },
    {
        "Pergunta": "Uma refeição vespertina acontece em qual período do dia?",
        "Opções": [
            "À meia-noite",
            "Na hora do almoço",
            "Pela manhã cedo",
            "Na parte da tarde",
        ],
        "Resposta": "Na parte da tarde",
    },
    {
        "Pergunta": "Qual é o menor país do mundo?",
        "Opções": ["Mônaco", "Malta", "Nauru", "Vaticano"],
        "Resposta": "Vaticano",
    },
    {
        "Pergunta": "Qual é o maior planeta do sistema solar?",
        "Opções": ["Netuno", "Saturno", "Urano", "Júpiter"],
        "Resposta": "Júpiter",
    },
    {
        "Pergunta": "Qual é a atual capital do Brasil?",
        "Opções": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "Resposta": "Brasília",
    },
    {
        "Pergunta": "Qual animal nasce do cruzamento do burro com a égua?",
        "Opções": ["Mula", "Bezerro", "Cabrito", "Cabra"],
        "Resposta": "Mula",
    },
    {
        "Pergunta": "Qual objeto é jogado no mar para fixar navios e barcos, impedindo que se movimentem?",
        "Opções": ["Leme", "Âncora", "Timão", "Remo"],
        "Resposta": "Âncora",
    },
    {
        "Pergunta": "Qual é o maior animal vivo do planeta Terra?",
        "Opções": ["Baleia Azul", "Tubarão Branco", "Elefante", "Hipopótamo"],
        "Resposta": "Baleia Azul",
    },
    {
        "Pergunta": "Quem proclamou a Independência do Brasil?",
        "Opções": [
            "D. Pedro I",
            "Napoleão Bonaparte",
            "Carlos Drummond de Andrade",
            "Jesus Cristo",
        ],
        "Resposta": "D. Pedro I",
    },
    {
        "Pergunta": "Quantos estados fazem parte da região sudeste?",
        "Opções": ["4", "5", "4", "2"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Qual material é extraído da seringueira?",
        "Opções": ["Mel", "Xarope", "Bambu", "Látex"],
        "Resposta": "Látex",
    },
    {
        "Pergunta": "Quem foi o primeiro homem a pisar na Lua?",
        "Opções": ["Van Gogh", "Barack Obama", "Donald Trump", "Neil Armstrong"],
        "Resposta": "Neil Armstrong",
    },
    {
        "Pergunta": "Quantas letras tem o alfabeto?",
        "Opções": ["19", "20", "23", "26"],
        "Resposta": "26",
    },
    {
        "Pergunta": "Como é a conjugação do verbo caber na 1.ª pessoa do singular do presente do indicativo?",
        "Opções": ["Tu cabes", "Eu coube", "Eu cabo", "Eu caibo"],
        "Resposta": "Eu caibo",
    },
    {
        "Pergunta": "Quem foi o primeiro presidente do Brasil?",
        "Opções": [
            "Getúlio Vargas",
            "Juscelino Kubitschek",
            "Deodoro da Fonseca",
            "Floriano Peixoto",
        ],
        "Resposta": "Deodoro da Fonseca",
    },
    {
        "Pergunta": "Qual evento marcou o início da Idade Média?",
        "Opções": [
            "Queda do Império Romano do Ocidente",
            "Invenção da imprensa",
            "Descobrimento da América",
            "Revolução Francesa",
        ],
        "Resposta": "Queda do Império Romano do Ocidente",
    },
    {
        "Pergunta": "Em que ano começou a Primeira Guerra Mundial?",
        "Opções": ["1910", "1914", "1917", "1920"],
        "Resposta": "1914",
    },
    {
        "Pergunta": "Em que ano ocorreu a Revolução Francesa?",
        "Opções": ["1776", "1789", "1804", "1822"],
        "Resposta": "1789",
    },
    {
        "Pergunta": "Quem liderou a marcha sobre Roma em 1922?",
        "Opções": [
            "Adolf Hitler",
            "Benito Mussolini",
            "Joseph Stalin",
            "Francisco Franco",
        ],
        "Resposta": "Benito Mussolini",
    },
    {
        "Pergunta": "Qual é o rio mais longo do mundo?",
        "Opções": ["Nilo", "Amazonas", "Mississipi", "Yangtzé"],
        "Resposta": "Amazonas",
    },
    {
        "Pergunta": "Qual o nome do autor de “Dom Quixote”?",
        "Opções": [
            "Gabriel García Márquez",
            "Miguel de Cervantes",
            "Jorge Luis Borges",
            "Pablo Neruda",
        ],
        "Resposta": "Miguel de Cervantes",
    },
    {
        "Pergunta": "Em que país foram realizados os Jogos Olímpicos de 2016?",
        "Opções": ["China", "Brasil", "Inglaterra", "Estados Unidos"],
        "Resposta": "Brasil",
    },
    {
        "Pergunta": "Quem detém o recorde mundial de velocidade nos 100 metros rasos?",
        "Opções": ["Usain Bolt", "Carl Lewis", "Michael Johnson", "Justin Gatlin"],
        "Resposta": "Usain Bolt",
    },
    {
        "Pergunta": "Qual é o maior planeta do Sistema Solar?",
        "Opções": ["Marte", "Júpiter", "Terra", "Vênus"],
        "Resposta": "Júpiter",
    },
    {
        "Pergunta": "Quantos dias tem um ano bissexto?",
        "Opções": ["365", "366", "367", "368"],
        "Resposta": "366",
    },
    {
        "Pergunta": "Qual a linguagem de programação frequentemente usada para desenvolvimento web front-end?",
        "Opções": ["JavaScript", "Python", "Java", "C++"],
        "Resposta": "JavaScript",
    },
    {
        "Pergunta": "Qual é a capital da França?",
        "Opções": ["Roma", "Berlim", "Paris", "Londres"],
        "Resposta": "Paris",
    },
    {
        "Pergunta": "Qual esporte utiliza uma raquete e uma peteca?",
        "Opções": ["Tênis", "Badminton", "Vôlei", "Squash"],
        "Resposta": "Badminton",
    },
    {
        "Pergunta": "Qual estilo musical surgiu nos Estados Unidos com influência da cultura afro-americana?",
        "Opções": ["Rock", "Jazz", "Clássico", "Eletrônica"],
        "Resposta": "Jazz",
    },
    {
        "Pergunta": "Em qual continente está localizado o deserto do Saara?",
        "Opções": ["Ásia", "África", "América do Sul", "Austrália"],
        "Resposta": "África",
    },
    {
        "Pergunta": "Qual é o nome do movimento artístico que surgiu no século XIX e que buscava retratar a realidade de forma objetiva?",
        "Opções": ["Romantismo", "Realismo", "Impressionismo", "Modernismo"],
        "Resposta": "Realismo",
    },
    {
        "Pergunta": "Quem é conhecido como o “Rei do Pop”?",
        "Opções": ["Michael Jackson", "Elvis Presley", "Madonna", "Prince"],
        "Resposta": "Michael Jackson",
    },
    {
        "Pergunta": "Quem escreveu a peça “Hamlet”?",
        "Opções": [
            "Charles Dickens",
            "William Shakespeare",
            "Jane Austen",
            "Leo Tolstoy",
        ],
        "Resposta": "William Shakespeare",
    },
    {
        "Pergunta": "Qual filme ganhou o Oscar de Melhor Filme em 1998?",
        "Opções": [
            "Titanic",
            "Shakespeare Apaixonado",
            "O Resgate do Soldado Ryan",
            "A Vida é Bela",
        ],
        "Resposta": "Shakespeare Apaixonado",
    },
    {
        "Pergunta": "Qual a cor da caixa preta dos aviões?",
        "Opções": ["Laranja", "Preta", "Azul", "Vermelha"],
        "Resposta": "Laranja",
    },
    {
        "Pergunta": "Qual é a sede da Organização das Nações Unidas (ONU)?",
        "Opções": ["Genebra", "Viena", "Nova York", "Paris"],
        "Resposta": "Nova York",
    },
    {
        "Pergunta": "Qual é o processo pelo qual as plantas produzem seu próprio alimento?",
        "Opções": ["Respiração", "Fotossíntese", "Digestão", "Transpiração"],
        "Resposta": "Fotossíntese",
    },
    {
        "Pergunta": "Qual documento declara os direitos humanos fundamentais?",
        "Opções": [
            "Constituição Federal",
            "Carta das Nações Unidas",
            "Declaração de Independência dos Estados Unidos",
            "Declaração Universal dos Direitos Humanos",
        ],
        "Resposta": "Declaração Universal dos Direitos Humanos",
    },
    {
        "Pergunta": "Qual é o livro sagrado do islamismo?",
        "Opções": ["Bíblia", "Alcorão", "Torá", "Bhagavad Gita"],
        "Resposta": "Alcorão",
    },
    {
        "Pergunta": "O que significa a sigla PIB?",
        "Opções": [
            "Produto Interno Bruto",
            "Plano Internacional de Benefícios",
            "Programa de Incentivo ao Brasil",
            "Pagamento Internacional Bancário",
        ],
        "Resposta": "Produto Interno Bruto",
    },
    {
        "Pergunta": "O que é superávit?",
        "Opções": [
            "Quando as despesas superam as receitas",
            "Quando as receitas superam as despesas",
            "Equilíbrio entre receitas e despesas",
            "Aumento da dívida pública",
        ],
        "Resposta": "Quando as receitas superam as despesas",
    },
    {
        "Pergunta": "O que é a bolsa de valores?",
        "Opções": [
            "Local de câmbio de moedas estrangeiras",
            "Instituição financeira que concede empréstimos",
            "Mercado onde se negociam ações de empresas",
            "Órgão governamental que controla a economia",
        ],
        "Resposta": "Mercado onde se negociam ações de empresas",
    },
    {
        "Pergunta": "Qual filme de animação da Disney conta a história de um leãozinho chamado Simba?",
        "Opções": ["O Rei Leão", "A Bela e a Fera", "Aladdin", "A Pequena Sereia"],
        "Resposta": "O Rei Leão",
    },
    {
        "Pergunta": "Qual é a capital da Austrália?",
        "Opções": ["Sydney", "Canberra", "Melbourne", "Perth"],
        "Resposta": "Canberra",
    },
    {
        "Pergunta": "O que é inflação?",
        "Opções": [
            "Diminuição da taxa de juros",
            "Estabilidade econômica",
            "Aumento do poder de compra",
            "Aumento geral dos preços",
        ],
        "Resposta": "Aumento geral dos preços",
    },
    {
        "Pergunta": "Qual estreito separa a Grã-Bretanha da França?",
        "Opções": [
            "Canal da Mancha",
            "Estreito de Gibraltar",
            "Estreito de Bósforo",
            "Estreito de Magalhães",
        ],
        "Resposta": "Canal da Mancha",
    },
    {
        "Pergunta": "Qual é o sistema eleitoral utilizado para eleger o Presidente do Brasil?",
        "Opções": [
            "Sistema proporcional",
            "Sistema de dois turnos",
            "Sistema majoritário simples",
            "Sistema distrital misto",
        ],
        "Resposta": "Sistema de dois turnos",
    },
    {
        "Pergunta": "Qual país é conhecido como a “Terra do Sol Nascente”?",
        "Opções": ["Japão", "China", "Coreia do Sul", "Vietnã"],
        "Resposta": "Japão",
    },
    {
        "Pergunta": "Qual religião tem como princípio a crença na reencarnação?",
        "Opções": ["Cristianismo", "Islamismo", "Hinduísmo", "Judaísmo"],
        "Resposta": "Hinduísmo",
    },
    {
        "Pergunta": "Quem dirigiu o filme “O Poderoso Chefão”?",
        "Opções": [
            "Francis Ford Coppola",
            "Martin Scorsese",
            "Steven Spielberg",
            "Quentin Tarantino",
        ],
        "Resposta": "Francis Ford Coppola",
    },
    {
        "Pergunta": "Qual é o nome da força que atrai os objetos para o centro da Terra?",
        "Opções": ["Magnetismo", "Eletricidade", "Gravidade", "Atrito"],
        "Resposta": "Gravidade",
    },
    {
        "Pergunta": "O que é taxa de juros?",
        "Opções": [
            "Valor total de um produto",
            "Percentual cobrado sobre um empréstimo ou investimento",
            "Imposto sobre produtos industrializados",
            "Valor do salário mínimo",
        ],
        "Resposta": "Percentual cobrado sobre um empréstimo ou investimento",
    },
    {
        "Pergunta": "Qual a velocidade da luz no vácuo?",
        "Opções": [
            "Aproximadamente 300.000 km/s",
            "Aproximadamente 150.000 km/s",
            "Aproximadamente 600.000 km/s",
            "Aproximadamente 100.000 km/s",
        ],
        "Resposta": "Aproximadamente 300.000 km/s",
    },
    {
        "Pergunta": "Quem esculpiu a estátua “O Pensador”?",
        "Opções": ["Michelangelo", "Donatello", "Auguste Rodin", "Leonardo da Vinci"],
        "Resposta": "Auguste Rodin",
    },
    {
        "Pergunta": "Qual foi o período da história do Brasil conhecido como “Era Vargas”?",
        "Opções": ["1930-1945 e 1951-1954", "1889-1930", "1964-1985", "1985-2002"],
        "Resposta": "1930-1945 e 1951-1954",
    },
    {
        "Pergunta": "Qual é o metal líquido à temperatura ambiente?",
        "Opções": ["Mercúrio", "Ouro", "Prata", "Chumbo"],
        "Resposta": "Mercúrio",
    },
    {
        "Pergunta": "Qual é o maior órgão interno do corpo humano?",
        "Opções": ["Coração", "Cérebro", "Fígado", "Pulmões"],
        "Resposta": "Fígado",
    },
    {
        "Pergunta": "Qual o nome do movimento artístico que valorizava a natureza e as emoções, surgido no século XIX?",
        "Opções": ["Realismo", "Romantismo", "Impressionismo", "Modernismo"],
        "Resposta": "Romantismo",
    },
    {
        "Pergunta": "Qual o nome da empresa fundada por Jeff Bezos?",
        "Opções": ["Google", "Facebook", "Amazon", "Microsoft"],
        "Resposta": "Amazon",
    },
]

quiz(questions)
