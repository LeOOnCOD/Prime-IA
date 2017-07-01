import telepot
from Chatbot import Chatbot

a = """	
 /$$$$$$$$ /$$$$$$$$ /$$       /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$ /$$                   /$$    
|__  $$__/| $$_____/| $$      | $$_____/ /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$| $$                  | $$    
   | $$   | $$      | $$      | $$      | $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$$$$$$   /$$$$$$  /$$$$$$  
   | $$   | $$$$$   | $$      | $$$$$   | $$ /$$$$| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$__  $$ /$$__  $$|_  $$_/  
   | $$   | $$__/   | $$      | $$__/   | $$|_  $$| $$__  $$| $$__  $$| $$  $$$| $$| $$  \ $$| $$  \ $$  | $$    
   | $$   | $$      | $$      | $$      | $$  \ $$| $$  \ $$| $$  | $$| $$\  $ | $$| $$  | $$| $$  | $$  | $$ /$$
   | $$   | $$$$$$$$| $$$$$$$$| $$$$$$$$|  $$$$$$/| $$  | $$| $$  | $$| $$ \/  | $$| $$$$$$$/|  $$$$$$/  |  $$$$/
   |__/   |________/|________/|________/ \______/ |__/  |__/|__/  |__/|__/     |__/|_______/  \______/    \___/  
                                                                                                                 
                                                                                                                     
[*] TELEGRAMbot ainda está em desenvolvimento
[*] Erros e bugs, poderão acontecer
[*] CODADO POR: LeOOnCOD                                                                                                                     
                                                                                                                             """
print(a)                                                                                                       

telegram = telepot.Bot("417145136:AAETDgB5qUvibO_U2iPGwwIFtNCzXWkiWEA")
bot = Chatbot("Prime")

def recebendoMsg(msg):
	frase = bot.escuta(frase=msg['text'])
	resp = bot.pensa(frase)
	bot.fala(resp)
	#chatID = msg['chat']['id']
	tipoMsg, tipoChat, chatID = telepot.glance(msg)
	telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
	pass