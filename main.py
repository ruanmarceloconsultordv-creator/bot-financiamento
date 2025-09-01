import os
import telebot

# pega o token salvo no Railway (em Variables)
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# ---- COEFICIENTES ----
COEFICIENTES = {
    12: 0.1350,
    24: 0.0650,
    36: 0.0510,
    48: 0.0450,
    60: 0.0370
}

# ---- INÍCIO ----
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Olá! Eu sou o Bot de Financiamento. Me diga:\n\n"
                          "👉 Qual o valor do veículo?\n"
                          "👉 Qual o valor da entrada?\n\n"
                          "E eu calculo a média das parcelas pra você 😉")

# ---- CÁLCULO ----
@bot.message_handler(func=lambda m: m.text and m.text.replace(".", "").isdigit())
def calcular(message):
    try:
        valor = float(message.text)
        resposta = f"📊 Simulação para R$ {valor:,.2f} financiados:\n\n"
        for prazo, coef in COEFICIENTES.items():
            parcela = valor * coef
            resposta += f"{prazo}x: R$ {parcela:,.2f}/mês\n"
        bot.reply_to(message, resposta)
    except Exception as e:
        bot.reply_to(message, "⚠️ Ocorreu um erro na simulação. Tente novamente.")

print("Bot rodando no Railway...")
bot.infinity_polling()
