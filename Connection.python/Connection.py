import snap7.client as c
from snap7.util import *
from snap7.types import *
import time
from datetime import datetime
import os

def ReadMemory(plc,byte,bit,datatype,area1,comeco):
    result = plc.read_area(area1,comeco,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte:
        return get_sint(result,0)
    elif datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dint(result,0)
    else:
        return None

# def ReadMemory2(plc,byte,bit,datatype,area1,comeco):
#     result = plc.read_area(area1,comeco,byte,datatype)
#     if datatype==S7WLBit:
#         return get_bool(result,0,bit)
#     elif datatype==S7WLByte:
#         return get_sint(result,0)
#     elif datatype==S7WLWord:
#         return get_uint(result,0)
#     elif datatype==S7WLReal:
#         return get_real(result,0)
#     elif datatype==S7WLDWord:
#         return get_dword(result,0)
#     else:
#          return None


if __name__=="__main__":
    plc = c.Client()
    plc.connect('10.32.22.85',0,2)
    while(True):
        os.system('cls')
        # Ler Memorias (MK)
        ar = ReadMemory(plc,27,6,S7WLBit,Areas.MK,0)
        agua = ReadMemory(plc,27,1,S7WLBit,Areas.MK,0)
        dreno = ReadMemory(plc,27,0,S7WLBit,Areas.MK,0)
        soda = ReadMemory(plc,27,2,S7WLBit,Areas.MK,0)
        retSoda = ReadMemory(plc,27,3,S7WLBit,Areas.MK,0)
        acido = ReadMemory(plc,27,4,S7WLBit,Areas.MK,0)
        retAcido = ReadMemory(plc,27,5,S7WLBit,Areas.MK,0)
        #c = ReadMemory(plc,0,2,S7WLBit,Areas.MK,0)
        #d = ReadMemory(plc,10,0,S7WLByte,Areas.MK,0)
        #e = ReadMemory(plc,14,0,S7WLWord,Areas.MK,0)
        #f = ReadMemory(plc,16,0,S7WLDWord,Areas.MK,0)
        #g = ReadMemory(plc,20,0,S7WLReal,Areas.MK,0)
        # Ler Inputs (PE)
        #h = ReadMemory(plc,0,0,S7WLBit,Areas.PE,0)
        #i = ReadMemory(plc,0,1,S7WLBit,Areas.PE,0)
        # Ler Outputs (PA)
        #j = ReadMemory(plc,0,0,S7WLBit,Areas.PA,0)
        # Ler DB (DB)
        #k = ReadMemory(plc,0,0,S7WLBit,Areas.DB,120)
        #l = ReadMemory(plc,0,1,S7WLBit,Areas.DB,120)
        #m = ReadMemory(plc,0,2,S7WLBit,Areas.DB,120)
        #n = ReadMemory(plc,8,0,S7WLWord,Areas.DB,120)
        #o = ReadMemory(plc,10,0,S7WLWord,Areas.DB,120)
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        
        print("Processo de Lavagem Barril - CHOPP")
        print(date_time)
        print("\narLavagem(M27.6):", ar, "\naguaLavagem(M27.1): ", agua, "\nDrenoLavagem(M27.0):", dreno, "\nsodaLavagem(M27.2):",soda, "\nretornoSodaLavagem(M27.3):",retSoda,
        "\nacidoLavagem(M27.4):",acido, "\nretornoAcidoLavagem(M27.5):",retAcido )
        print("-----------")
        
        print("-----------")
        #print("Liga(DB120.DBX0.0):", k, "\nDesliga(DB120.DBX0.1):", l, "\nMotor(DB120.DBX0.2):", m, "\nContador Ligado(DB120.DBW8):", n, "\nContador Desligado(DB120.DBW10):", o)

        time.sleep(1)