import os
import time
import os.path
from typing import NewType
import shutil, errno

class Node:

    # NODE INFOS
    NodeName = ""
    Wallet = ""
    NODE_NUM = 1
    NodeID = 0

    # HW SPECS
    CPU = 3
    MEM = 2
    DISK = 20
    # CPU COSTS
    CPU_Hour = 0.1
    ENV_Hour = 0.02
    StartFee = 0.0

    # Raise Amounts
    RaiseAmount = 1.00
    Multi = 1.15

    # Path Vars
    DockerDIR = ""
    NEWDIR = ""

    def __init__(self):

        type (self).NodeID +=1
        if self.NodeID <= 1:
            self.quest()
            self.confNode()
            self.Run()
            self.changeRaise(self.RaiseAmount)
            self.Looper()
        else:
            if self.RaiseAmount < self.Multi:
                self.dockerDIR()
                self.confNode()
                self.Run()
                self.Looper()    
            else:            
                self.dockerDIR()
                self.confNode()
                self.Run()
                self.changeRaise(self.RaiseAmount)
                self.Looper()
            
    @classmethod
    def quest(cls):
        cls.NodeName = str(input("Enter your Node Name:(default:BannanaNode):  "))
       	cls.Wallet = str(input("Enter your Wallet Address:(default:DevWallet):   "))
        cls.NODE_NUM = int(input("Enter Number of Nodes you want to Start:(default: 1 Node):  "))
        cls.CPU = int(input("Enter your CPU amount to use:(default:3 CORES):   "))
        cls.MEM = int(input("Enter Memory in GIB:(default:2 GB):   "))
        cls.DISK = int(input("Enter DISKSPACE in GIB:(default:20 GB):   "))
        cls.CPU_Hour = float(input("Enter CPU COSTS PER HOUR:(default:0.1 GLM):   "))
        cls.ENV_Hour = float(input("Enter ENV COSTS PER HOUR:(default:0.02 GLM):   "))
        cls.StartFee = float(input("ENTER PRICE FOR START JOBS:(default:0.0 GLM):   "))
        print("Setup Price Raise Amount: set it like this: |15% = 1.15|30% = 1.30| ")
        cls.Multi = float(input("Enter the Multiplikator you want:(default:0%):   "))

    @classmethod
    def confNode(self):

        self.DockerDIR = os.getcwd()
        file = open('.env', 'w')
        #Mainnet Settings
        file.write("#This file contains all settings change to your needs")
        file.write("\nYA_PAYMENT_NETWORK=mainnet")
        file.write("\nNODE_SUBNET=public-beta")

        #NODE Settings
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
        file.write("NODE_NUM=1\n")
        file.write("NICENESS=20\n")

        # AutoHeal Settings
        file.write("AUTOHEAL_CONTAINER_LABEL=all\n")
        file.write("AUTOHEAL_START_PERIOD=300\n")
        file.write("AUTOHEAL_INTERVAL=5\n")
  
        # Docker-Compose Name Settings

        file.write("\nCOMPOSE_PROJECT_NAME=" + str(self.NodeName + str(self.NodeID)))


        # Uncoment for Debug LOG on discord @Philip_golem

        #file.write("RUST_LOG=debug\n")
        #file.write("ya_market=info\n")
        #file.write("trust_dns_proto=info\n")
        #file.write("trust_dns_resolver=info\n")
        #file.write("a_sb_router=trace\n")
        #file.write("ya_net=trace\n")
        #file.write("ya_service_bus=trace\n")

        file.close()
    
    def changeRaise(self, Multi):
        type(self).RaiseAmount *=self.Multi
        type(self).CPU_Hour *=self.Multi
        type(self).ENV_Hour *=self.Multi
        type(self).StartFee *=self.Multi

    def dockerDIR(self):
        
        self.NEWDIR = str(("Node" + str(self.NodeID)))
        shutil.copytree(self.DockerDIR, self.NEWDIR)
        os.chdir(self.NEWDIR)
 
    def changeDIR(self):
        os.system("cd ..")
        
    def Run(self):
        print("RUN NODE"+ str(self.NodeID))
        os.system('make presets')
        os.system('make upd')
        self.changeDIR()

    def Looper(self):
        while self.NodeID < self.NODE_NUM:
            main()
        else:
            pass


def main():
    
    Start = Node()
    print(Start.__dict__)
    
main()
