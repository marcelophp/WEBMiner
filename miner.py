#/usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
from os import system, path
from time import sleep

ail = input('Coloque seu email :: ')
if path.isfile('cpuminer-multi/autogen.sh') == False:
  system('apt-get update && clear')
  system('apt-get install libcurl4-openssl-dev -y && clear')
  system('apt-get install git && clear')
  system('apt-get install build-essential -y && clear')
  system('apt-get install autotools-dev autoconf -y && clear')
  system('apt-get install libcurl3 libcurl4-gnutls-dev -y && clear')
  system('mkdir download')
  system('git clone https://github.com/wolf9466/cpuminer-multi && clear')
  system('cd cpuminer-multi && ./autogen.sh && clear &&\
         CFLAGS="-march=native" ./configure && clear && make && clear && make install && clear')
  print('\033[33mConcluido. Mineracao iniciada.. ficarar Rodando em segundo Plano.\033[m')
  system('minerd -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45560 -u %s -p x' %(ail))
else:
  print('\033[33mConcluido. Mineracao iniciada ficarar Rodando em segundo Plano.\033[m')
  system('minerd -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45560 -u %s -p x' %(ail))