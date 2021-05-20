#!/usr/bin/env python3
import time
import platform
from typing import NewType
import shutil, errno
import urllib.request, json 
import subprocess

class NodeCreator:

    # Raise Amounts
    NodeID = 0
    RaiseAmount = 1.00
    Multi = 1.15
    Index = 1
    CPU_Hour = 0.1
    ENV_Hour = 0.02
    StartFee = 0.0

    def __init__(self):
        type (self).NodeID +=1
        if self.NodeID <= 1:
            self.LOGO()
            self.quest()
            self.confNode()
            self.Run()
            self.changeRaise(self.RaiseAmount)
            self.Looper()
        else:
            self.setRaise()
            self.changer()
            self.changeRaise(self.RaiseAmount)
            self.Looper

    @classmethod
    def quest(cls):
        cls.NodeName = str(input("Enter your Node Name:  "))
       	cls.Wallet = str(input("Enter your Wallet Address:   "))
        cls.NODE_NUM = int(input("Enter Number of Nodes you want to Start:  "))
        cls.CPU = int(input("Enter your CPU amount to use:   "))
        cls.MEM = int(input("Enter Memory in GIB:   "))
        cls.DISK = int(input("Enter DISKSPACE in GIB:   "))
        cls.CPU_Hour = float(input("Enter CPU COSTS PER HOUR:   "))
        cls.ENV_Hour = float(input("Enter ENV COSTS PER HOUR:   "))
        cls.StartFee = float(input("ENTER PRICE FOR START JOBS:   "))
        print("Setup Price Raise Amount: set it like this: |15% = 1.15|30% = 1.30| ")
        print("Leave it Empty if you want the !!!SAME PRICE ON ALL NODES!!")
        cls.Multi = float(input("Enter the Multiplikator you want:   "))

    @classmethod
    def confNode(self):

        file = open('.env', 'w')
        #Mainnet Settings
        file.write("#This file contains all settings change to your needs")
        file.write("\n")
        file.write("\nYA_PAYMENT_NETWORK=mainnet")
        file.write("\nNODE_SUBNET=public-beta")

        #NODE Settings
        file.write("\n")
        file.write("\n# run settings")
        file.write("\nNODE_NAME=" + str(self.NodeName))
        file.write("\nYA_ACCOUNT="+ str(self.Wallet))
        file.write("\nNODE_CPU_THREADS=" + str(self.CPU))
        file.write("\nNODE_MEM_GIB=" + str(self.MEM))
        file.write("\nNODE_STORAGE_GIB=" + str(self.DISK))
        file.write("\nNODE_COSTS_CPU_HOUR=" + str(self.CPU_Hour))
        file.write("\nNODE_COSTS_HOUR=" + str(self.ENV_Hour))
        file.write("\nNODE_COSTS_START=" + str(self.StartFee))
        
        # Run Settings
        file.write("\n")
        file.write("\nNODE_NUM=" + str(self.NODE_NUM))
        file.write("\nNICENESS=20\n")

        # AutoHeal Settings
        file.write("AUTOHEAL_CONTAINER_LABEL=all\n")
        file.write("AUTOHEAL_START_PERIOD=300\n")
        file.write("AUTOHEAL_INTERVAL=5\n")
  
        # Docker-Compose Name Settings

        file.write("\nCOMPOSE_PROJECT_NAME=" + str(self.NodeName))


        # Uncoment for Debug LOG on discord @Philip_golem

        #file.write("RUST_LOG=debug\n")
        #file.write("ya_market=info\n")
        #file.write("trust_dns_proto=info\n")
        #file.write("trust_dns_resolver=info\n")
        #file.write("a_sb_router=trace\n")
        #file.write("ya_net=trace\n")
        #file.write("ya_service_bus=trace\n")

        file.close()
        
    def Looper(self):
        while self.NodeID < self.NODE_NUM:
            main()
        else:
            pass

    def changeRaise(self, Multi):
        type(self).RaiseAmount *=self.Multi
        type(self).CPU_Hour *=self.Multi
        type(self).ENV_Hour *=self.Multi
        type(self).StartFee *=self.Multi

    def setRaise(self, RaiseAmount=RaiseAmount):
        self.RaiseAmount = RaiseAmount
        self.CPU_Hour = float(self.CPU_Hour * self.RaiseAmount)
        self.ENV_Hour = float(self.ENV_Hour * self.RaiseAmount)
        self.StartFee = float(self.StartFee * self.RaiseAmount)
    
    @classmethod
    def changer(cls):
        
        index = "index=" + str(cls.NodeID)
        cpuPrice = "cpuh=" + str(cls.CPU_Hour)
        envPrice = "envh=" + str(cls.ENV_Hour)
        startPrice = "sfee=" + str(cls.StartFee)
        
        cpuh = subprocess.run(['make', 'cpuh', index , cpuPrice])

        envh = subprocess.run(['make', 'envh', index , envPrice])
        
        sfee = subprocess.run(['make', 'sfee', index , startPrice]) 

    @classmethod
    def Run(cls):
        subprocess.run('make presets', shell=True)
        subprocess.run('make upd', shell=True)
        print("Nodes are Starting")
        time.sleep(1)
        print("Node Price changes will start soon")
        time.sleep(2)

    @classmethod
    def LOGO(cls):
        print("   **** welcome To GLMAutoNODE ****")
        time.sleep(0.1)
        print(" __                         __  __  __ ")
        time.sleep(0.1)
        print("/ _ |  |\/| /\    |_ _ |\ |/  \|  \|_  ")
        time.sleep(0.1)
        print("\__)|__|  |/--\|_||_(_)| \|\__/|__/|__ ")


def main():
    
    create = NodeCreator()

    # Comming soon auto change Price by averange price
    # https://api.golemstats.com/v1/provider/average/earnings
    # https://api.golemstats.com/v1/network/pricing/average
    def worker():
        pass

   
main()
