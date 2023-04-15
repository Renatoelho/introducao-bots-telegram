
import telebot
import dotenv
from os import getenv

dotenv.load_dotenv()

TOKEN_TELEGRAM = getenv("TOKEN_TELEGRAM")

bot = telebot.TeleBot(TOKEN_TELEGRAM)

comandos = (
    "/opcao1 - Essa é a primeira opção.",
    "/opcao2 - Essa é a segunda opção."
)

@bot.message_handler(commands=["start"])
def mensagem_boas_vindas(message):
    bot.send_message(message.chat.id, "Olá, tudo bem? Escolha uma das seguintes opções:")
    bot.send_message(message.chat.id, comandos[0])
    bot.send_message(message.chat.id, comandos[1])

@bot.message_handler(commands=["opcao1"])
def opcao1(message):
    bot.send_message(message.chat.id, "Você escolheu a primeira opção.")

@bot.message_handler(commands=["opcao2"])
def opcao2(message):
    bot.send_message(message.chat.id, "Você escolheu a segunda opção.")

@bot.message_handler(func=lambda message: "Bom dia" in message.text)
def responde_usuario(message):
        nome_usuario = message.from_user.first_name
        resposta = f"Olá, {nome_usuario}. Em que posso ajudar?"
        bot.reply_to(message, resposta)

if __name__ == "__main__":
    bot.polling()