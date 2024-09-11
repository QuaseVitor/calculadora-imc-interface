from customtkinter import *


resultado = 0

def imc():
    getalt = int(altura_inp.get())
    getpes = int(peso_inp.get())
    
    if getalt !=0 and getpes!=0:
    
        pes = float(getpes)
        alt = float(getalt)
        
        if alt > 2.40:
            alt = alt/100
    
        global resultado
        resultado = pes/alt**2
        resultado = round(resultado,1)
        
        text_resul.configure(text=resultado)
    


root = CTk()
root.title("IMC Calculator")
root.iconbitmap("calcular.ico")

root.geometry("480x720")#("720x1280")
root.resizable(False, False)
root.config(bg="#1f1f1f")



peso_inp = CTkEntry(root, placeholder_text="Insira seu Peso",width=350, height=50)
peso_inp.place(anchor="center", relx=0.5, rely=0.65)

altura_inp = CTkEntry(root, placeholder_text="Insira sua Altura", width=350, height=50)
altura_inp.place(anchor="center", relx=0.5, rely=0.75)

botao = CTkButton(root, command=imc, text="Calcular",width=150, height=50)
botao.place(anchor="center", relx=0.5, rely=0.85)

text_resul = CTkLabel(root, text="", font=("Roboto", 150), bg_color = "#1f1f1f")
text_resul.place(anchor="center", relx=0.5, rely=0.2)


root.mainloop()
