#!/usr/apps/Python/bin/python

from tkinter import *
import serial.tools.list_ports
import re
from tkinter import ttk, font


class DroneControl:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("ISME drone control")
        self.arduino = serial.Serial()
        self.portList = Listbox(self.gui)
        self.update_port_list()

        self.portLabel = ttk.Label(self.gui, text="Dispositivos disponibles:")
        self.boton1 = ttk.Button(self.gui, text="Conectar", command=self.conectar)
        self.boton2 = ttk.Button(self.gui, text="Desconectar", command=self.desconectar)
        self.boton3 = ttk.Button(self.gui, text="GPS", command=self.gps)
        self.boton4 = ttk.Button(self.gui, text="Atti", command=self.atti)
        self.boton5 = ttk.Button(self.gui, text="Manual", command=self.manual)




        self.portLabel.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.portList.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton3.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton4.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton5.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)

        self.gui.mainloop()

    def update_port_list(self):
        portListString = list(serial.tools.list_ports.comports())  # lista de los puertos conectados a la pc

        for i in range(len(portListString)):
            port = portListString.pop(0)
            self.portList.insert(i + 1, port.__str__().split("-", 1)[0])

       # self.portList.insert(0, "hola")
        self.portList.pack()  # mando la informacion agregada al list box

    def conectar(self):

        selectedItem = self.portList.curselection()
        if selectedItem: #chequo si se selecciono algun dispositivo
           self.arduino = serial.Serial(self.portList.get(selectedItem[0]), 9600)
           #self.arduino.write(b'3')
           #print(self.portList.get(selectedItem[0]))

    def desconectar(self):
        self.arduino.close()

    def gps(self):
        self.arduino.write(b'3')

    def manual(self):
        self.arduino.write(b'7')

    def atti(self):
        self.arduino.write(b'9')






g = DroneControl()

