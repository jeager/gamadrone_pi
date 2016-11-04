import subprocess
import time
import argparse
import re


def set_antena(code, wlan):
"""
Descrição: 
Esta é uma função que seta o nome das antenas 
utilizando o atributo hardware address de cada uma delas,
dessa forma o posicionamento das antenas fica fixo em relação ao drone.

Parâmetros:
code - hardware address da antena.
wlan - nome da antena.
"""
        if code == '79':
                global antena_2
                antena_2 = wlan
        elif code == 'd6':
                global antena_1
                antena_1 = wlan
        elif code == 'ba':
                global antena_3
                antena_3 = wlan

def calc_med(list):
"""
Descrição: 
Está é uma função que calcula a média das medições
de potência das antenas de acordo com a posição
do usuário.

Parâmetros:
list - Lista que contém as medições de potência 
das antenas. 
"""
	med = 0
	for a in list:
		med += a
	if len(list) > 0:
		return med/len(list)	
	else:
		return 0
def setup():
"""
Descrição:
Função que executa os comandos no cmd para acessar
os dados de cada antena e tomando como base no hardware
address chamar o método set_antena() para
definir a posição de cada uma delas.
"""
        cmd = subprocess.Popen('ifconfig wlan0', shell=True,
                           stdout=subprocess.PIPE)
        cmd1 = subprocess.Popen('ifconfig wlan1', shell=True,
                           stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen('ifconfig wlan2', shell=True,
                           stdout=subprocess.PIPE)
        for line in cmd.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan0')
        for line in cmd1.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan1')
        for line in cmd2.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan2')
                        
def read_antenas():
"""
Descrição:
Realiza a execução dos comandos no cmd para medir
as potências das antenas 100 vezes e calcular a média
dessas medições. Em seguida ele define o quadrante que o 
usuário se encontra a partir de comparações entre as 
potências das antenas.
"""
        while True:
                cmd = subprocess.Popen('iwconfig ' + antena_1, shell=True,
                                   stdout=subprocess.PIPE)
                cmd1 = subprocess.Popen('iwconfig ' + antena_2, shell=True,
                                   stdout=subprocess.PIPE)
                cmd2 = subprocess.Popen('iwconfig ' + antena_3, shell=True,
                                   stdout=subprocess.PIPE)           
                count = 0
                wlan0_list = []
                wlan1_list = []
                wlan2_list = []

                while count < 100:
                        if cmd:
                                for line in cmd.stdout:
                                        if 'Link Quality' in line:
                                                wlan0_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'

                        if cmd1:
                                for line in cmd1.stdout:
                                        if 'Link Quality' in line:
                                                wlan1_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'
                        if cmd2:
                                for line in cmd2.stdout:
                                        if 'Link Quality' in line:
                                                wlan2_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'
                                
                        count += 1
                        if count == 100:
                                w0 = calc_med(wlan0_list)
                                w1 = calc_med(wlan1_list)
                                w2 = calc_med(wlan2_list)

                                #print 'antena_1: ' + str(w0) + " antena_2: " + str(w1) + " antena_3: " + str(w2)
                                wlan0_list = []
                                wlan1_list = []
                                wlan2_list = []
                                """
                                Encontrar o quadrante
                                w0 média da antena esquerda do drone
                                w1 média da antena direita do drone
                                wl média da antena de trás do drone
                                """        
                                if ((w1>w0)and(w0>w2)):
                                        print "primeiro quadrante, visão frontal"
                                
                                if ((w0>w1)and(w1>w2)):
                                        print "segundo quadrante, visão frontal"

                                if ((w0>w1)and(w2>w1)):
                                        print "terceiro quadrante, visão traseira"
                                        
                                if ((w1>w0)and(w2>w0)):
                                        print "quarto quadrante, visão traseira"

                                if ((w1>w0)and(w1>w2)):
                                        print "zona morta, lado direito"

                                if ((w0>w1)and(w0>w2)):
                                        print "zona morta, lado esquerdo"

                        time.sleep(0.0001)
                count = 0
def main():
        setup()
        print antena_1 + " " + antena_2 + " " + antena_3
        read_antenas()
        
if __name__ == "__main__": main()
        
