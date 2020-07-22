#!/usr/bin/env python3

import os, threading, socket

def scan(ip,tn):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Starting Socket for thread %d" %(tn))
    for i in range(2,1024):
        suc = s.connect_ex((ip, i)) #Usamos connect_ex en lugar de connect porque si no marca error, connect_ex retorna 0 si es exitoso
        #data = s.recv(1024)
        if(suc == 0):
            print("port: %d - %s" %(i, 'open'))
            #s.timeout(0.02)
        else:
            print("port: {0} closed".format(i))

    s.close()

def main():
    
    if len(os.sys.argv) != 2:
        print("usage: {0} [IP]".format(os.sys.argv[0]))
    else:
        threads = [] # esta lista va a servir para "encolar" los hilos generados
        print("starting threads")
        for i in range(2): #el rango es el numero de hilos que deseamos crear, en este caso 2
            t = threading.Thread(target=scan, args=(os.sys.argv[1],i,))
            # creaos un objeto "t" que va a servir para inicializar los hilos
            # target debe ser la funcion que creamos
            # los argumentos son enviados a la funcion como lo es la IP y el numero del hilo
            threads.append(t) # generamos la cola de hilos creados
            t.start()


if __name__=="__main__":
    main()
