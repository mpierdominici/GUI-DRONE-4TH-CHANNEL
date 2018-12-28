#!/usr/apps/Python/bin/python

from tkinter import *
import serial.tools.list_ports
import re
from tkinter import ttk, font


class DroneControl:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("ISME drone control")

        self.portList = Listbox(self.gui)
        self.update_port_list()

        self.portLabel = ttk.Label(self.gui, text="Dispositivos conectados:")

        self.portLabel.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.portList.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)

        self.gui.mainloop()

    def update_port_list(self):
        portListString = list(serial.tools.list_ports.comports())  # lista de los puertos conectados a la pc

        for i in range(len(portListString)):
            port = portListString.pop(0)
            self.portList.insert(i + 1, port.__str__().split("-", 1)[0])

        self.portList.pack()  # mando la informacion agregada al list box




g = DroneControl()

