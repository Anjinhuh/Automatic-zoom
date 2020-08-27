import pyautogui
import time
import datetime
import schedule
import os
import PySimpleGUI as sg
import sys



def entrar_na_aula():
    
    digitarSenha = pyautogui.typewrite
    moverPara = pyautogui.moveTo
    clicar = pyautogui.leftClick
    time.sleep(10)
    moverPara(940, 518, duration=0)
    clicar()
    print('CliqueiParaEntrar')
    time.sleep(1)
    moverPara(1105, 481, duration=0)
    clicar()
    print('SelecionandoAula')
    time.sleep(1)
    moverPara(899, 533, duration=0)
    clicar()
    time.sleep(1)
    moverPara(968, 676, duration=0)
    clicar()
    print('EntrandoNaAula!')
    time.sleep(1)
    moverPara(909, 485)
    clicar()
    digitarSenha('484302')
    print('BotandoSenha')
    time.sleep(1)
    moverPara(959, 682)
    clicar()
    print('EntrandoNaAula')

##########################################
#               HORARIOS                 #
#             SEGUNDA-FEIRA              #
##########################################
schedule.every().monday.at("08:05").do(entrar_na_aula)
schedule.every().monday.at("08:55").do(entrar_na_aula)
schedule.every().monday.at("09:55").do(entrar_na_aula)
schedule.every().monday.at("10:45").do(entrar_na_aula)
schedule.every().monday.at("11:35").do(entrar_na_aula)
schedule.every().monday.at("12:25").do(entrar_na_aula)

##########################################
#               HORARIOS                 #
#             TERÇA-FEIRA                #
##########################################
schedule.every().tuesday.at("08:05").do(entrar_na_aula)
schedule.every().tuesday.at("08:55").do(entrar_na_aula)
schedule.every().tuesday.at("09:55").do(entrar_na_aula)
schedule.every().tuesday.at("10:45").do(entrar_na_aula)
schedule.every().tuesday.at("11:35").do(entrar_na_aula)
schedule.every().tuesday.at("12:25").do(entrar_na_aula)

##########################################
#               HORARIOS                 #
#             QUARTA-FEIRA               #
##########################################
schedule.every().wednesday.at("08:05").do(entrar_na_aula)
schedule.every().wednesday.at("08:55").do(entrar_na_aula)
schedule.every().wednesday.at("09:55").do(entrar_na_aula)
schedule.every().wednesday.at("10:45").do(entrar_na_aula)
schedule.every().wednesday.at("11:35").do(entrar_na_aula)
schedule.every().wednesday.at("12:25").do(entrar_na_aula)

##########################################
#               HORARIOS                 #
#             QUINTA-FEIRA               #
##########################################
schedule.every().thursday.at("08:05").do(entrar_na_aula)
schedule.every().thursday.at("08:55").do(entrar_na_aula)
schedule.every().thursday.at("09:55").do(entrar_na_aula)
schedule.every().thursday.at("10:45").do(entrar_na_aula)
schedule.every().thursday.at("11:35").do(entrar_na_aula)
schedule.every().thursday.at("12:25").do(entrar_na_aula)

##########################################
#               HORARIOS                 #
#             SEXTA-FEIRA                #
##########################################
schedule.every().friday.at("08:05").do(entrar_na_aula)
schedule.every().friday.at("08:55").do(entrar_na_aula)
schedule.every().friday.at("09:55").do(entrar_na_aula)
schedule.every().friday.at("10:45").do(entrar_na_aula)
schedule.every().friday.at("11:35").do(entrar_na_aula)
schedule.every().friday.at("12:25").do(entrar_na_aula)
schedule.every().tuesday.at("21:20").do(entrar_na_aula)




def printarSequencia():
    print('1')

schedule.every().tuesday.at("23:47").do(entrar_na_aula)
schedule.every().tuesday.at("22:26").do(printarSequencia)
while 1:
    schedule.run_pending()
    time.sleep(1)




    










'''
def printar():
    print('OkFuncionou')


schedule.every().tuesday.at("12:21").do(printar)
while 1:
    schedule.run_pending()
    time.sleep(1)
'''

       
    


