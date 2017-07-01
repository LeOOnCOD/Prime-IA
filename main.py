from gtts import gTTS
from Chatbot import Chatbot
import os

a = """
		 	 _______  _______    _________    _______     _______ 
			(  ____ )(  ____ )   \__   __/   (       )   (  ____ \ 
			| (    )|| (    )|      ) (      | () () |   | (    \/
			| (____)|| (____)|      | |      | || || |   | (__    
			|  _____)|     __)      | |      | |(_)| |   |  __)   
			| (      | (\ (         | |      | |   | |   | (      
			| )_     | ) \ \__ _ ___) (___ _ | )   ( | _ | (____/\ 
			|/(_)    |/   \__/(_)\_______/(_)|/     \|(_)(_______/
		                                                   

[*] P.R.I.M.E Ainda está em desenvolvimento
[*] Bugs e erros podem vir a acontecer
[*] CODADO POR: LeOOnCOD

-----------------------------------------------------------------------------		
		                                                                  """
print(a)		                                                                  

ola = gTTS("Olá, tudo bem?",lang="pt")
ola.save("ola.mp3")
os.startfile('ola.mp3')

prazer = gTTS("Prazer em te conhecer!",lang="pt")
prazer.save("prazer.mp3")
os.startfile('prazer.mp3')

Bot = Chatbot("Prime")
while True:
	frase = Bot.escuta()
	resposta = Bot.pensa(frase)
	Bot.fala(resposta)
	if resposta == 'tchau':
		break