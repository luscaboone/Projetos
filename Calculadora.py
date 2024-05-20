import customtkinter

customtkinter.set_appearance_mode("dark") #MODO ESCURO PARA JANELA
    
calculadora = customtkinter.CTk()
calculadora.geometry("349x430") #TAMANHO DA JANELA
#calculadora.iconbitmap("teste.ico")

calculadora.title("Calculadora") #TITULO DA JANELA

def calcular():
    calculo = saidanumeros.get('0.0', 'end')
    resultado = eval(calculo)
    saidanumeros.delete('0.0', 'end')
    saidanumeros.insert('0.0', resultado)

saidanumeros = customtkinter.CTkTextbox(calculadora, #LOCAL PARA DIGITAR OS NUMEROS
                                      width=340, #LARGURA DO TERMINAL
                                      height=80, #ALTURA DO TERMINAL
                                      font=(('Arial', 60))) #FONTE QUE FICARA NO TERMINAL
saidanumeros.grid(row=0, column=0, columnspan=4, padx=5, pady=3)

numero7 = customtkinter.CTkButton(calculadora, 
                                  width=80, #LARGURA DO BOTÃO
                                  height=80, #ALTURA DO BOTÃO
                                  fg_color="gray", #COR DO BOTAO
                                  hover_color="#a9a9a9", #COR DO BOTÃO QUANDO O MOUSE PASSAR POR CIMA
                                  corner_radius=0, #BORDA DO BOTÃO(QUADRADA OU REDONDA)
                                  command= lambda:saidanumeros.insert('end', 7),
                                  text="7") #TEXTO QUE FICA NO BOTÃO
numero7.grid(row=2, column=0, padx=1, pady=3) #CONFIGURAÇÕES DA POSIÇÃO DO BOTÃO

numero8 = customtkinter.CTkButton(calculadora,
                                  width=80,
                                  height=80,
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 8),
                                  text="8")
numero8.grid(row=2, column=1, padx=1, pady=3)

numero9 = customtkinter.CTkButton(calculadora, 
                                  width=80,
                                  height=80,
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 9),
                                  text="9")
numero9.grid(row=2, column=2, padx=1, pady=3)

vezes = customtkinter.CTkButton(calculadora, 
                                width=80,
                                height=80,
                                fg_color="gray", 
                                hover_color="#a9a9a9", 
                                corner_radius=0,
                                command= lambda:saidanumeros.insert('end', "*"),
                                text="X")
vezes.grid(row=2, column=3, padx=1, pady=3)

numero4 = customtkinter.CTkButton(calculadora, 
                                  width=80, 
                                  height=80, 
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 4),
                                  text="4")
numero4.grid(row=3, column=0, padx=1, pady=3)

numero5 = customtkinter.CTkButton(calculadora, 
                                  width=80, 
                                  height=80, 
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 5),
                                  text="5")
numero5.grid(row=3, column=1, padx=1, pady=3)

numero6 = customtkinter.CTkButton(calculadora, 
                                  width=80,
                                  height=80, 
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 6),
                                  text="6")
numero6.grid(row=3, column=2, padx=1, pady=3)

menos = customtkinter.CTkButton(calculadora,
                                width=80,
                                height=80, 
                                fg_color="gray", 
                                hover_color="#a9a9a9", 
                                corner_radius=0,
                                command= lambda:saidanumeros.insert('end', "-"),
                                text="-")
menos.grid(row=3, column=3, padx=1, pady=3)

numero1 = customtkinter.CTkButton(calculadora, 
                                  width=80,
                                  height=80, 
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 1),
                                  text="1")
numero1.grid(row=4, column=0, padx=1, pady=3)

numero2 = customtkinter.CTkButton(calculadora, 
                                  width=80,
                                  height=80, 
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 2),
                                  text="2")
numero2.grid(row=4, column=1, padx=1, pady=3)

numero3 = customtkinter.CTkButton(calculadora, 
                                  width=80,
                                  height=80,
                                  fg_color="gray", 
                                  hover_color="#a9a9a9", 
                                  corner_radius=0,
                                  command= lambda:saidanumeros.insert('end', 3),
                                  text="3")
numero3.grid(row=4, column=2, padx=1, pady=3)

mais = customtkinter.CTkButton(calculadora, 
                               width=80, 
                               height=80,
                               fg_color="gray",
                               hover_color="#a9a9a9", 
                               corner_radius=0,
                               command= lambda:saidanumeros.insert('end', "+"),
                               text="+")
mais.grid(row=4, column=3, padx=1, pady=3)

zero = customtkinter.CTkButton(calculadora, 
                               width=80,
                               height=80, 
                               fg_color="gray",
                               hover_color="#a9a9a9", 
                               corner_radius=0,
                               command= lambda:saidanumeros.insert('end', 0),
                               text="0")
zero.grid(row=5, column=1, padx=1, pady=3)

ponto = customtkinter.CTkButton(calculadora,
                                width=80,
                                height=80, 
                                fg_color="gray",
                                hover_color="#a9a9a9", 
                                corner_radius=0,
                                command= lambda:saidanumeros.insert('end', "."),
                                text=".")
ponto.grid(row=5, column=2, padx=1, pady=3)

igual = customtkinter.CTkButton(calculadora, 
                                width=80, 
                                height=80, 
                                fg_color="gray", 
                                hover_color="#a9a9a9",
                                corner_radius=0,
                                command= calcular,
                                text="=")
igual.grid(row=5, column=3, padx=1, pady=3)

apagar = customtkinter.CTkButton(calculadora,
                                 width=80, 
                                 height=80, 
                                 fg_color="gray", 
                                 hover_color="#a9a9a9", 
                                 corner_radius=0,
                                command= lambda:saidanumeros.delete("0.0", "end"),
                                 text="Apagar")
apagar.grid(row=5, column=0, padx=1, pady=3)

calculadora.mainloop()
