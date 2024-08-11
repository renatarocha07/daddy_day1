from flask import Flask, render_template, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

def criar_pdf(nome_pai):
    print("Criando PDF...")
    pdf_path = f"carta_{nome_pai}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    texto = [
        f"Querido {nome_pai},",
        "Quero agradecer profundamente por me ensinar que a vida é sobre conhecimento e dedicação,",
        "e por sempre me inspirar a correr atrás dos meus sonhos." "Além de tudo, sou grato por você",
        "ser um pai incrível, sempre fez o seu melhor por mim. Obrigado por tudo!" ,
        "Te amo muito!",
        "",
        "Com amor,",
        "[Renata]"
    ]

    x = 72
    y = 750

    for linha in texto:
        c.drawString(x, y, linha)
        y -= 14

    c.save()
    print("PDF criado.")
    return pdf_path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_pdf():
    nome_pai = "Pai"
    pdf_path = criar_pdf(nome_pai)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
