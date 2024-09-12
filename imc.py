from customtkinter import *

def imc():
    getalt = altura_inp.get()
    getpes = peso_inp.get()
    
    if getalt !=0 and getpes!=0:
    
        pes = float(getpes)
        alt = float(getalt)
        
        if alt > 2.40:
            alt = alt/100
    
        global resultado
        resultado = pes/alt**2
        resultado = round(resultado,1)
        
        text_resul.configure(text=resultado)
        
        if resultado < 18.5:
            text_alt.configure(text="Magreza", )
        
        elif resultado < 24.9:
            text_alt.configure(text="Normal")
        
        elif resultado < 29.9:
            text_alt.configure(text="Sobrepeso")
        
        elif resultado < 39.9:
            text_alt.configure(text="Obesidade")
        
        else:
            text_alt.configure(text="Obesidade Grave")
        

root = CTk()
root.title("IMC Calculator")
root.iconbitmap("calcular.ico")

root.geometry("480x720")#("720x1280")
root.resizable(False, False)
root.config(bg="#1f1f1f")

#Label


text_title = CTkLabel(root, text="Calculo IMC", font=("Roboto", 40), bg_color = "#1f1f1f")
text_title.place(anchor="center", relx=0.5, rely=0.065)

text_resul = CTkLabel(root, text="", font=("Roboto", 150), bg_color = "#1f1f1f")
text_resul.place(anchor="center", relx=0.5, rely=0.25)

text_alt = CTkLabel(root, text="", font=("Roboto", 30), bg_color = "#1f1f1f")
text_alt.place(anchor="center", relx=0.5, rely=0.4)


#Interativos

text_tuto = CTkLabel(root, text="Insira seus dados:", font=("Roboto", 20), bg_color = "#1f1f1f")
text_tuto.place(anchor="center", relx=0.5, rely=0.575)

peso_inp = CTkEntry(root, placeholder_text="Insira seu Peso",width=270, height=50, justify="center")
peso_inp.place(anchor="center", relx=0.5, rely=0.65)

altura_inp = CTkEntry(root, placeholder_text="Insira sua Altura", width=270, height=50, justify="center")
altura_inp.place(anchor="center", relx=0.5, rely=0.75)

botao = CTkButton(root, command=imc, text="Calcular",width=150, height=50)
botao.place(anchor="center", relx=0.5, rely=0.85)

root.mainloop()
