# coding: utf-8
import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button, font
from datetime import *
from ics import Calendar, Event
from PIL import Image, ImageDraw, ImageFont

def data_atual():
    data_atual =  data_ultima_sessao.get()
    data_atual = date.today()
    proxima_sessao = data_atual + timedelta(+45)
    dia_para_agendar = proxima_sessao + timedelta(-30)
    cal = Calendar()
    event1 = Event()
    event1.name = "Dia ideal para agendar a sessão no app"
    event1.begin = f"{dia_para_agendar}"
    event1.all_day
    cal.events.add(event1)
    event2 = Event()
    event2.name = "Dia da próxima sessão"
    event2.begin = f"{proxima_sessao}"
    event2.all_day
    cal.events.add(event2)
    with open(f"{date.today()}-lembrete_laser.ics", "w") as f:
        f.write(str(cal))
    proxima_sessao = '{}/{}/{}'.format(proxima_sessao.day, proxima_sessao.month,proxima_sessao.year)
    dia_para_agendar = '{}/{}/{}'.format(dia_para_agendar.day, dia_para_agendar.month,dia_para_agendar.year)
    opcao_escolhida = messagebox.askokcancel(
            title="Finalizando...",
            message=f"Próxima sessão é: {proxima_sessao}\n"
                    f"Dia para agendar: {dia_para_agendar}\n"
                    f"Pronto para salvar?")

    if opcao_escolhida:
            fnt = ImageFont.truetype('Fonts\ArialTh.ttf', 20)
            qr1 = qrcode.QRCode(version=1, box_size=10, border=5)
            qr1.add_data(event1)
            qr1.make(fit=True)
            img1 = qr1.make_image(fill_color=(153, 204, 204), back_color='white')
            d1 = ImageDraw.Draw(img1)
            d1.text((200,20),"Dia ideal para agendar a sessão no app", font=fnt, fill=(0, 0, 0))
            img1.save('Dia ideal para agendar a sessão no app.png')
            
            qr2 = qrcode.QRCode(version=1, box_size=10, border=5)
            qr2.add_data(event2)
            qr2.make(fit=True)
            img2 = qr2.make_image(fill_color=(153, 204, 204), back_color='white')
            d2 = ImageDraw.Draw(img2)
            d2.text((220,20),"Dia da próxima sessão", font=fnt, fill=(0, 0, 0))
            img2.save('Dia da próxima sessão.png')
    

def gera_qr_code():
    data =  data_ultima_sessao.get()

    if len(data) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma data válida")
    else:
        data = datetime.strptime(data, '%d/%m/%Y').date()
        proxima_sessao = data + timedelta(+45)
        dia_para_agendar = proxima_sessao + timedelta(-30)
        cal = Calendar()
        event1 = Event()
        event1.name = "Dia ideal para agendar a sessão no app"
        event1.begin = f"{dia_para_agendar}"
        event1.all_day
        cal.events.add(event1)
        event2 = Event()
        event2.name = "Dia da próxima sessão"
        event2.begin = f"{proxima_sessao}"
        event2.all_day
        cal.events.add(event2)
        with open(f"{date.today()} - lembrete_laser.ics", "w") as f:
            f.write(str(cal))
        proxima_sessao = '{}/{}/{}'.format(proxima_sessao.day, proxima_sessao.month,proxima_sessao.year)
        dia_para_agendar = '{}/{}/{}'.format(dia_para_agendar.day, dia_para_agendar.month,dia_para_agendar.year)
        opcao_escolhida = messagebox.askokcancel(
                title="Finalizando...",
                message=f"Próxima sessão é: {proxima_sessao}\n"
                        f"Dia para agendar: {dia_para_agendar}\n"
                        f"Pronto para salvar?")
        if opcao_escolhida:
                fnt = ImageFont.truetype('Fonts\ArialTh.ttf', 20)
                qr1 = qrcode.QRCode(version=1, box_size=10, border=5)
                qr1.add_data(event1)
                qr1.make(fit=True)
                img1 = qr1.make_image(fill_color=(153, 204, 204), back_color='white')
                d1 = ImageDraw.Draw(img1)
                d1.text((200,20),"Dia ideal para agendar a sessão no app", font=fnt, fill=(0, 0, 0))
                img1.save('Dia ideal para agendar a sessão no app.png')
                
                qr2 = qrcode.QRCode(version=1, box_size=10, border=5)
                qr2.add_data(event2)
                qr2.make(fit=True)
                img2 = qr2.make_image(fill_color=(153, 204, 204), back_color='white')
                d2 = ImageDraw.Draw(img2)
                d2.text((220,20),"Dia da próxima sessão", font=fnt, fill=(0, 0, 0))
                img2.save('Dia da próxima sessão.png')

if __name__ == '__main__':
    window = Tk()
    window.title("Calcular laser")
    window.config(padx=10, pady=100, background='#99CCCC' )

    label_font = font.Font( size=13)
    website_label = Label(font = label_font, text="Data da última sessão:", background='#99CCCC')
    website_label.grid(row=0, column=1, columnspan=3)
    website_label2 = Label(text="(DD/MM/AAAA)", background='#99CCCC')
    website_label2.grid(row=1, column=1, columnspan=3)

    data_ultima_sessao = Entry(width=45)
    data_ultima_sessao.grid(row=4, rowspan=5, column=1, columnspan=3)
    data_ultima_sessao.focus()
    
    botão = Button(text="Foi Hoje!", width=20, command= data_atual)
    botão.grid(row=10, column=1, columnspan=1)
    botão2 = Button(text="Gerar Lembrete", width=20, command=gera_qr_code)
    botão2.grid(row=10, column=2, columnspan=2)

    window.mainloop()
    