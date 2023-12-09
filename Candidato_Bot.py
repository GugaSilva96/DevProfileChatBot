import tkinter as tk

class Candidato:
    def __init__(self, nome, carreira, habilidades, preferencias=None, contato=None, telefone=None):
        self.nome = nome
        self.carreira = carreira
        self.habilidades = habilidades
        self.preferencias = preferencias if preferencias is not None else []
        self.contato = contato if contato is not None else ""
        self.telefone = telefone if telefone is not None else ""

    def gerar_resposta(self, opcao):
        if opcao == 0:
            return "Até logo!"
        elif opcao == 1:
            return f"Eu sou {self.nome}, um {self.carreira}."
        elif opcao == 2:
            habilidades_candidato = "\n".join(self.habilidades)
            preferencias_candidato = "\n".join(self.preferencias)
            return f"Essas são minhas principais habilidades:\n{habilidades_candidato}\nE minhas áreas de preferências são:\n{preferencias_candidato}."
        elif opcao == 3:
            return f"Você pode entrar em contato comigo pelo email: {self.contato}\nou pelo meu telefone {self.telefone}."
        else:
            return "Opção inválida. Por favor, escolha 0, 1, 2 ou 3."

# Função chamada quando o botão é pressionado
def responder():
    opcao_recrutador = int(entry.get())
    resposta_candidato = candidato.gerar_resposta(opcao_recrutador)
    output.config(text=resposta_candidato)

    # Verificar se a opção é zero para encerrar o programa
    if opcao_recrutador == 0:
        root.destroy()  # Fecha a janela principal

# Exemplo de uso
nome_candidato = "Gustavo Silva"
carreira_candidato = "Desenvolvedor Back-end"
habilidades_candidato = ["Lógica de programação", "Pensamento computacional", "Grande capacidade para resolução de problemas", "Git e GitHub"]
preferencias_candidato = ["Inteligência Artificial", "Desenvolvimento Back-End"]
contato_candidato = "guga.h.costaesilva@gmail.com"
telefone_candidato = "(21) 97226-2615"

candidato = Candidato(nome_candidato, carreira_candidato, habilidades_candidato, preferencias_candidato, contato_candidato, telefone_candidato)

# Criar a interface gráfica
root = tk.Tk()
root.title("Chat com Recrutador")

# Campo de entrada
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Botão para enviar a opção
button = tk.Button(root, text="Enviar Opção", command=responder)
button.pack(pady=10)

# Campo de exibição
output = tk.Label(root, text="")
output.pack(pady=10)

# Iniciar a interface
root.mainloop()
