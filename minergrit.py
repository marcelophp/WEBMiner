#!/usr/bin/evn python3
# encoding: utf-8
#
# [Github] www.github.com/Xdwnff-04x
# [Telegram - Channel] https://telegram.me/ZWDChannel
# [Telegram - PV] @nZwdeff
# [Doacoes]
#   Minegrate: 04xxxxBackdoor.ZWD@gmail.com
#   Carteira Bitcoin: 17FSQYQWUMmDhKYoXLFFzNVN7PojVPxqNm
#   PicPay: @04xxxx 5/100
#
# [Modo de Mineracao Utilizada] cpuminer-multi
#   Github: github.com/wolf9466/cpuminer-multi
#
# [Modo de Reabrir]
#   Para reabrir o progama apos feixar a conexao com o servidor ..
#   Utilize o comando: screen -r
# [License]
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
import os
from os import system
from sys import *
from time import *

n0='\033[90m'
n1='\033[91m'
n2='\033[92m'
n3='\033[93m'
n4='\033[94m'
n5='\033[95m'
n6='\033[96m'
n7='\033[97m'

u1='\033[31m'
u2='\033[32m'
u3='\033[33m'
u4='\033[34;1m'
u5='\033[35m'
u6='\033[36m'
u0='\033[m'

__author__ = 'Zwdeff'
__version__ = '0.5'

if version_info < (3, 0):
   print(u1+'Error: Progama suportado somente em python3x.'+u0)
   sleep(2)
   exit()
if os.path.isfile('/usr/local/bin/minerd') == False:
   print(u1+'Dependencias Desinstaladas.'+u0)
   sleep(1)
   print(n2+'Instalando Dependencias. Aguarde ..'+u0)
   sleep(2)
   system('apt-get update && clear')
   system('apt-get install libcurl4-openssl-dev -y && clear')
   if os.path.isfile('/usr/bin/git') == False:
      system('apt-get install git -y && clear')
   if os.path.isfile('/usr/bin/autoconf') == False:
      system('apt-get install autoconf -y && clear')
   system('apt-get install build-essential -y && clear')
   system('apt-get install autotools-dev -y && clear')
   system('apt-get install libcurl3 -y && clear')
   system('apt-get install libcurl4-gnutls-dev -y && clear')
   system('mkdir /home/download')
   system('cd /home/download && git clone https://github.com/LucasJones/cpuminer-multi')
   system('clear')
   system('cd /home/download/cpuminer-multi && ./autogen.sh && clear')
   system('cd /home/download/cpuminer-multi && CFLAGS="-march=native" ./configure && clear')
   system('cd /home/download/cpuminer-multi && make && clear && make install && clear')
   system('rm -rf /home/download')
   print(u6+'\nConcluido .. Dependencias Instaladas.'+u0)
   sleep(2)
   
if os.path.isfile('/etc/Zw/s0') == False:
   # Abrindo o Progama em segundo Plano.
   system('mkdir /etc/Zw')
   system('touch /etc/Zw/s0')
   system('screen -d -m -t minergrit.py python3 minergrit.py')
   system('screen -r')
   exit()

# Inicializacao da mineracao.
minerando = u3+'Concluido. Pode feixar a conexao com o seu Seridor ..\n'\
            +'Para reabrir o progama, Utilize: screen -r' + u0
# Menu de Mineracao multipla.
__main2__ ='\n'\
+u2+'1) = XMR+XDN\n' + u0\
+u2+'2) = XMR+FCN\n' + u0\
+u2+'3) = FCN+QCN\n' + u0\
+u2+'4) = FCN+DSH\n' + u0\
+u2+'5) = FCN+INF8\n' + u0\
+u2+'6) = MCN+QCN\n' + u0\
+u2+'7) = MCN+DSH\n' + u0\
+u2+'8) = MCN+INF8\n' + u0\
+u2+'0) = Home\n' + u0

# Menu de Mineracao.
__main1__ ='\n'\
+u2+'1) = Bytecoin\n' + u0\
+u2+'2) = QuazarCoin\n' + u0\
+u2+'3) = Monero\n' + u0\
+u2+'4) = FantomCoin\n' + u0\
+u2+'5) = DigitalNote\n' + u0\
+u2+'6) = MonetaVerde\n' + u0\
+u2+'7) = Dashcoin\n' + u0\
+u2+'8) = Infinium-8\n' + u0\
+u2+'9) = Mais Opcoes\n' + u0\
+u2+'^C = exit\n' + u0

__banner__ = n2+'''\
 __  __ _                  ____      _ _
|  \/  (_)_ __   ___ _ __ / ___|_ __(_) |_
| |\/| | | '_ \ / _ \ '__| |  _| '__| | __|
| |  | | | | | |  __/ |  | |_| | |  | | |_
|_|  |_|_|_| |_|\___|_|   \____|_|  |_|\__|'''+u2+'''

---|- : MINERAR-MOEDAS-WEB |
\n''' + u0
__description__ ='\n'\
+n2+'---|- : Author :'+u1+' %s v%s\n' % (__author__, __version__) + u0\
+n2+'---|- : Github :'+u1+' www.github.com/Xdwnff-04x\n' + u0\
+n2+'---|- : Channel:'+u1+' telegram.me/ZWDChannel\n' + u0\
+u2+'---|- : Minerar:'+u1+' 04xxxxBackdoor.ZWD@gmail.com\n' + u0\
+u2+'---|- : Bitcoin:'+u1+' 17FSQYQWUMmDhKYoXLFFzNVN7PojVPxqNm\n' + u0\
+u2+'---|- : Doacoes^' + u0
print(__banner__)
print(__description__)

def case():
 try:
    print(__main1__)
    df = input(n2+'[noob]'+u2+' :: '+u0)
    while df != '1' or df != '2' or df != '3' or df != '4' or df != '5'\
     or df != '6' or df != '7' or df != '8' or df != '9':
      if df == '1' or df == '2' or df == '3' or df == '4' or df == '5'\
       or df == '6' or df == '7' or df == '8' or df == '9':
         if df == '9':
            print(__main2__)
            dj = input(n2+'[noob]'+u2+' :: '+u0)
            while dj != '1' or dj != '2' or dj != '3' or dj != '4' or dj != '5'\
             or dj != '6' or dj != '7' or dj != '8' or dj != '0':
              if dj == '1' or dj == '2' or dj == '3' or dj == '4' or dj == '5'\
               or dj == '6' or dj == '7' or dj == '8' or dj == '0':
                 if dj == '0':
                    case()
                 ss = input(u2+'[noob] Email para Minerar :: '+u0)
                 if dj == '1':
                    print(n3+'Iniciando a mineracao - XMR+XDN'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://xdn-xmr.pool.minergate.com:45790 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '2':
                    print(n3+'Iniciando a mineracao - XMR+FCN'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://fcn-xmr.pool.minergate.com:45590 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '3':
                    print(n3+'Iniciando a mineracao - FCN+QCN'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://fcn-qcn.pool.minergate.com:45600 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '4':
                    print(n3+'Iniciando a mineracao - FCN+DSH'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://fcn-dsh.pool.minergate.com:45730 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '5':
                    print(n3+'Iniciando a mineracao - FCN+INF8'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://fcn-inf8.pool.minergate.com:45760 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '6':
                    print(n3+'Iniciando a mineracao - MCN+QCN'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://mcn-qcn.pool.minergate.com:45670 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '7':
                    print(n3+'Iniciando a mineracao - MCN+DSH'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://mcn-dsh.pool.minergate.com:45740 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
                 if dj == '8':
                    print(n3+'Iniciando a mineracao - MCN+INF8'+u0)
                    sleep(2)
                    print(minerando)
                    system('minerd -a cryptonight -o '\
                          +'stratum+tcp://mcn-inf8.pool.minergate.com:45770 -u '+ss+' -p x')
                    system('rm -rf /etc/Zw')
                    exit()
              else:
                 dj = input(n2+'[noob]'+u2+' :: '+u0)
         w = input(u2+'[noob] Email para Minerar :: '+u0)
         if df == '1':
            print(n3+'Iniciando a mineracao - Bytecoin'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://bcn.pool.minergate.com:45550 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '2':
            print(n2+'Iniciando a mineracao - QuazarCoin'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://qcn.pool.minergate.com:45570 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '3':
            print(n3+'Iniciando a mineracao - Monero'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45560 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '4':
            print(n3+'Iniciando a mineracao - FantomCoin'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://fcn.pool.minergate.com:45610 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '5':
            print(n3+'Iniciando a mineracao - DigitalNote'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://xdn.pool.minergate.com:45620 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '6':
            print(n3+'Iniciando a mineracao - MonetaVerde'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://mcn.pool.minergate.com:45640 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '7':
            print(n3+'Iniciando a mineracao - Dashcoin'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://dsh.pool.minergate.com:45720 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
         if df == '8':
            print(n3+'Iniciando a mineracao - Infinium-8'+u0)
            sleep(2)
            print(minerando)
            system('minerd -a cryptonight -o stratum+tcp://inf8.pool.minergate.com:45750 -u '+w\
                  +' -p x')
            system('rm -rf /etc/Zw')
            exit()
      else:
         df = input(n2+'[noob]'+u2+' :: '+u0)
       
 except KeyboardInterrupt:
    system('rm -rf /etc/Zw')
    print(u1+'\nGoing Out ..\033[m')
    sleep(2)
    exit()
if __name__ == '__main__':
   case()
