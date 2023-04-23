import ply.lex as lex
from lexico import *

# Interface
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

root = tk.Tk() #cria a tela
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.Menus()
        root.mainloop()

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, END)
        for i in self.saida.get_children():
            self.saida.delete(i)
        saidas.clear()
        global erros
        erros = 0
        self.frame_1.update()
        self.frame_2.update()
        root.update()

    def tela(self):
        self.root.title("Compilador")
        self.root.configure(background="white")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width=550, height=350)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#DCDCDC",highlightbackground="grey", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.07, relwidth=0.96, relheight=0.55)
        self.frame_2 = Frame(self.root, bd=4, bg="#DCDCDC",highlightbackground="grey", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.70, relwidth=0.96, relheight=0.20)

    def chama_analisador(self):
        columns = ('linha', 'posicao', 'token', 'lexema', 'notificacao')
        self.saida = ttk.Treeview(self.frame_2, height=5, columns=columns, show='headings')
        self.saida.heading("linha", text='Linha')
        self.saida.heading("posicao", text='Posicao referente ao inicio da entrada')
        self.saida.heading("token", text='Token')
        self.saida.heading("lexema", text='Lexema')
        self.saida.heading("notificacao", text='Notificacao')

        data = self.codigo_entry.get(1.0, "end-1c")
        # data.lower()
        lexer = lex.lex()
        lexer.input(data)

        
        # Tokenizar a entrada para passar para o analisador léxico
        for tok in lexer:
            print(tok.value)

            if tok.type in reserved.values():
                add_lista_saida(tok, f"palavra reservada")
            else:
                add_lista_saida(tok, f" ")

        saida = open('saida.txt', 'w+')

        for retorno in saidas:
            self.saida.insert('', tk.END, values=retorno)
            saida.write(str(retorno) + '\n')

        self.saida.place(relx=0.001, rely=0.01, relwidth=0.999, relheight=0.95)

        self.scrollAnalise = ttk.Scrollbar(self.frame_2, orient='vertical',command=self.saida.yview)
        self.scrollAnalise.place(relx=0.979, rely=0.0192, relwidth=0.02, relheight=0.92)
        self.saida['yscrollcommand'] = self.scrollAnalise

    def botoes(self):
        # botao limpar
        self.bt_limpar = Button(text="Limpar", bd=2, bg="#FF6347", font=('', 11), command=self.limpa_telaentrada)
        self.bt_limpar.place(relx=0.74, rely=0.92, relwidth=0.1, relheight=0.05)

        # botao executar
        self.bt_executar = Button(text="Executar", bd=2, bg="lightgreen", font=('', 11), command=self.chama_analisador)
        self.bt_executar.place(relx=0.85, rely=0.92, relwidth=0.1, relheight=0.05)

        # criação da label e entrada do código
        self.lb_codigo = Label(text="Código Fonte", bg="white", font=('', 12))
        self.lb_codigo.place(relx=0.001, rely=-0.001, relwidth=0.2, relheight=0.07)

        # criação da label da analise lexica
        self.lb_analise = Label(text="Análise Léxica e Sintática", bg="white", font=('', 12))
        self.lb_analise.place(relx=0.001, rely=0.62, relwidth=0.2, relheight=0.07)

        self.codigo_entry = tk.Text(self.frame_1)
        self.codigo_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_1, orient='vertical', command=self.codigo_entry.yview)
        self.scroll_bar.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        def onOpen():
            tf = fd.askopenfilename(
                initialdir="C:/Users/MainFrame/Desktop/",
                title="Open Text file",
                filetypes=(("Text Files", "*.txt"),)
            )
            tf = open(tf, 'r')
            entrada = tf.read()
            self.codigo_entry.insert(END, entrada)
            tf.close()

        def onSave():
            files = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            t = self.codigo_entry.get(0.0, END)
            files.write(t.rstrip())

        def tokens():
            newWindow = Toplevel(root)
            newWindow.title("Tabela de Tokens")
            newWindow.configure(background="white")
            newWindow.geometry("800x800")
            newWindow.resizable(True, True)
            newWindow.minsize(width=550, height=350)

            newWindow = ttk.Treeview(newWindow, height=3, column=('col1', 'col2', 'col3', 'col4'))
            newWindow.heading("#0", text='')
            newWindow.heading("#1", text='Tokens')
            newWindow.heading("#2", text='Lexemas')
            newWindow.heading("#3", text='Expressão Regular')
            newWindow.heading("#4", text='Descrição')

            newWindow.column("#0", width=1, stretch=NO)
            newWindow.column("#1", width=50, )
            newWindow.column("#2", width=200)
            newWindow.column("#3", width=125)
            newWindow.column("#4", width=125)

            newWindow.place(relx=0.001, rely=0.01, relwidth=0.999, relheight=0.95)

            newWindow.insert("", 1, text="", values=("ifsuldeminas", "ifsuldeminas", "ifsuldeminas", "Palavra Reservada ifsuldeminas"))
            newWindow.insert("", 3, text="", values=("INICIO", "INICIO", "INICIO", "Palavra Reservada INICIO"))
            newWindow.insert("", 4, text="", values=("FIM", "FIM", "FIM", "Palavra Reservada FIM"))
            newWindow.insert("", 5, text="", values=("COMPILADORES", "COMPILADORES", "COMPILADORES", "Palavra Reservada COMPILADORES"))
            newWindow.insert("", 6, text="", values=("mover_esquerda", "mover_esquerda", "mover_esquerda", "Palavra Reservada mover_esquerda"))
            newWindow.insert("", 7, text="", values=("LER", "LER", "LER", "Palavra Reservada LER"))
            newWindow.insert("", 8, text="", values=("IMPRIMIR", "IMPRIMIR", "IMPRIMIR", "Palavra Reservada IMPRIMIR"))
            newWindow.insert("", 9, text="", values=("RETORNA", "RETORNA", "RETORNA", "Palavra Reservada RETORNA"))
            newWindow.insert("", 10, text="", values=("SE", "SE", "SE", "Palavra Reservada SE"))

            newWindow.insert("", 11, text="", values=("SENAO", "SENAO", "SENAO", "Palavra Reservada SENAO"))
            newWindow.insert("", 12, text="", values=("SENAO_SE", "SENAO_SE", "SENAO_SE", "Palavra Reservada SENAO_SE"))
            newWindow.insert("", 13, text="", values=("PARA", "PARA", "PARA", "Palavra Reservada PARA"))
            newWindow.insert("", 14, text="", values=("ENQUANTO", "ENQUANTO", "ENQUANTO", "Palavra Reservada ENQUANTO"))
            newWindow.insert("", 15, text="", values=("FACA", "FACA", "FACA", "Palavra Reservada FACA"))
            newWindow.insert("", 16, text="", values=("FUNCAO", "FUNCAO", "FUNCAO", "Palavra Reservada FUNCAO"))
            newWindow.insert("", 17, text="", values=("CASO_FOR", "CASO_FOR", "CASO_FOR", "Palavra Reservada CASO_FOR"))
            newWindow.insert("", 18, text="", values=("SAIR", "SAIR", "SAIR", "Palavra Reservada SAIR"))
            newWindow.insert("", 20, text="", values=("aux", "aux", "aux", "Palavra Reservada aux"))

            newWindow.insert("", 21, text="", values=("mais", "+", "+", "Operador Matemático mais"))
            newWindow.insert("", 22, text="", values=("menos", "-", "-", "Operador Matemático menos"))
            newWindow.insert("", 23, text="", values=("vezes", "*", "*", "Operador Matemático vezes"))
            newWindow.insert("", 24, text="", values=("dividir", "/", "/", "Operador Matemático divide"))
            newWindow.insert("", 25, text="", values=("modulo", "%", "%", "Operador Matemático modulo"))

            newWindow.insert("", 26, text="", values=("abre_parenteses", "(", "(", "Operador de Prioridade abre parenteses"))
            newWindow.insert("", 27, text="", values=("fecha_parenteses", ")", ")", "Operador de Prioridade fecha parenteses"))
            newWindow.insert("", 28, text="", values=("abre_chaves", "{", "{", "Operador de Prioridade abre chaves"))
            newWindow.insert("", 29, text="", values=("fecha_chaves", "}", "}", "Operador de Prioridade fecha chaves"))
            newWindow.insert("", 30, text="", values=("abre_colchetes", "[", "[", "Operador de Prioridade abre colchetes"))
            newWindow.insert("", 31, text="", values=("fecha_colchetes", "]", "]", "Operador de Prioridade fecha colchetes"))

            newWindow.insert("", 32, text="", values=("menor", "<", "<", "Operador Relacional menor"))
            newWindow.insert("", 33, text="", values=("maior", ">", ">", "Operador Relacional maior"))
            newWindow.insert("", 34, text="", values=("menor_igual", "<=", "<=", "Operador Relacional menor igual"))
            newWindow.insert("", 35, text="", values=("maior_igual", ">=", ">=", "Operador Relacional maior igual"))
            newWindow.insert("", 36, text="", values=("exatamente_igual", "==", "==", "Operador Relacional duplo igual"))
            newWindow.insert("", 37, text="", values=("diferente", "!=", "!=", "Operador Relacional diferente"))
            newWindow.insert("", 38, text="", values=("e", "&", "&", "Operador Relacional e"))
            newWindow.insert("", 39, text="", values=("ou", "|", "|", "Operador Relacional ou"))

            newWindow.insert("", 40, text="", values=("inteiro", "0,1,2,3,4,5,6,7,8,9", "0|1|2|3|4|5|6|7|8|9", "Dígito Númerico Inteiro"))
            newWindow.insert("", 41, text="", values=("flutuante", "0.009...9.9999", "0.00|9.999", "Dígito Númerico Double"))
            newWindow.insert("", 42, text="", values=("texto", "a,b,c...x,y,z", "a|b|c...x|y|z", "Char"))
            newWindow.insert("", 43, text="", values=("variavel", "char(char,inteiro)*", "[char]{1}[char|inteiro]{*}", "Variável Criada"))
            newWindow.insert("", 44, text="", values=("aspas_simples",  "'", "'", "Operação de Impressão aspa simples"))

            newWindow.insert("", 45, text="", values=("virgula", ",", ",", "Operador de Execução Vírgula"))
            newWindow.insert("", 46, text="", values=("ponto_virgula", ";", ";", "Operador de Execução ponto e vírgula"))
            newWindow.insert("", 47, text="", values=("dois_pontos", ":", ":", "Operador de Execução dois pontos"))
            newWindow.insert("", 48, text="", values=("ponto", ".", ".", "Operador de Execução ponto"))

            newWindow.insert("", 49, text="", values=("aspas", '"' , '"', "Operação de Impressão aspa duplas"))

            newWindow.insert("", 50, text="", values=("comentario_uma_linha", "#", "#", "Operador de Comentário de uma linha"))
            

            newWindow.insert("", 51, text="", values=("negacao", "~", "~", "Operador de Atribuição negação"))
            newWindow.insert("", 52, text="", values=("igual", "=", "=", "Comando de Atribuição igual"))
            newWindow.insert("", 53, text="", values=("mais_igual", "+=", "+=", "Comando de Atribuição mais igual"))
            newWindow.insert("", 54, text="", values=("menos_igual", "-=", "-=", "Comando de Atribuição menos igual"))
            newWindow.insert("", 55, text="", values=("vezes_igual", "*=", "*=", "Comando de Atribuição vezes igual"))
            newWindow.insert("", 56, text="", values=("divide_igual", "/=", "/=", "Comando de Atribuição divide igual"))

            label.pack(pady=10)
            mainloop()

        menubar.add_cascade(label="Arquivo", menu=filemenu)
        menubar.add_cascade(label="Tabela de Tokens", menu=filemenu2)

        filemenu.add_command(label="Abrir Script", command=onOpen)
        filemenu.add_command(label="Salvar Como", command=onSave)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=Quit)
        filemenu2.add_command(label="Tokens", command=tokens)

Application()