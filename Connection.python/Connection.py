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


plc = c.Client()
plc.connect('10.32.22.85',0,2)
while(True):
    os.system('cls')
    ar = ReadMemory(plc,27,6,S7WLBit,Areas.MK,0)
    agua = ReadMemory(plc,27,1,S7WLBit,Areas.MK,0)
    dreno = ReadMemory(plc,27,0,S7WLBit,Areas.MK,0)
    soda = ReadMemory(plc,27,2,S7WLBit,Areas.MK,0)
    retSoda = ReadMemory(plc,27,3,S7WLBit,Areas.MK,0)
    acido = ReadMemory(plc,27,4,S7WLBit,Areas.MK,0)
    retAcido = ReadMemory(plc,27,5,S7WLBit,Areas.MK,0)
    agua2 =  ReadMemory(plc,28,0, S7WLBit,Areas.MK,0)
    alivioVapor = ReadMemory(plc,28,1, S7WLBit,Areas.MK,0)
    vapor2 = ReadMemory(plc,28,2,S7WLBit,Areas.MK,0)
    entradaCO2 = ReadMemory(plc,28,3,S7WLBit,Areas.MK,0)
    ar2 =  ReadMemory(plc,28,4,S7WLBit,Areas.MK,0)
    entradaProduto= ReadMemory(plc,28,5,S7WLBit,Areas.MK,0)
    entradaCerveja = ReadMemory(plc,28,6,S7WLBit,Areas.MK,0)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        # Ler Memorias (MK)
        #c = ReadMemory(plc,0,2,S7WLBit,Areas.MK,0)
        # Ler Inputs (PE)
        #h = ReadMemory(plc,0,0,S7WLBit,Areas.PE,0)
        # Ler Outputs (PA)
        #j = ReadMemory(plc,0,0,S7WLBit,Areas.PA,0)
        # Ler DB (DB)
        #k = ReadMemory(plc,0,0,S7WLBit,Areas.DB,120)
        
    print("Processo de Lavagem Barril - CHOPP")
    print(date_time)
    print("\nAr Comprimido - (M27.6):", ar, 
              "\nÁgua Quente - (M27.1): ", agua,
              "\nDreno - (M27.0):", dreno,
              "\nSoda Cáustica - (M27.2):",soda, 
              "\nRetorno Soda - (M27.3):",retSoda,
              "\nÁcido - (M27.4):",acido, 
              "\nRetorno Ácido - (M27.5):",retAcido )
    
    print("----------//----------")
    print("----------//----------")
    
    print("Processo de Enchimento Barril - CHOPP")
    print(date_time)
    print("\nÁgua Quente - (M28.0):", agua2, 
              "\nAlívio Vapor - (M28.1):",alivioVapor, 
              "\nVapor - (M28.2):",vapor2, 
              "\nEntrada CO2 - (M28.3):", entradaCO2,
              "\nAr Comprimido - (M28.4):",ar2,
              "\nEntrada Produto - (M28.5):", entradaProduto, 
              "\nEntrada Cerveja - (M28.6):",entradaCerveja) 
    time.sleep(1)
                
        #print("Liga(DB120.DBX0.0):", k, 
        # "\nDesliga(DB120.DBX0.1):", l, 
        # "\nMotor(DB120.DBX0.2):", m, 
        # "\nContador Ligado(DB120.DBW8):", n, 
        # "\nContador Desligado(DB120.DBW10):", o)
        #time.sleep(0.0)