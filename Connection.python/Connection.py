import snap7.client as c
from snap7.util import *
from snap7.types import *
import time
from datetime import datetime
import os
import pyodbc

#dados_conexão = ("Driver={SQL SERVER};"
#                 "Server=maquina alocada;"
#                 "Database=Nome do Banco;")
#conexao = pyodbc.connect(dados_conexão)

#Conexão ao banco de dados
dados_conexão = ("Driver = {SQl Server};"
                 "Server = SANTBS;"
                 "Database = monitoramentoPreditivo")
conexao = pyodbc.connect(dados_conexão)
print("Conexão DB Realizada com sucesso!")

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

#Leitura de memoria PLC
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
    
#Escrita de memoria no PLC  (Caso necessário)
#def writeMemory(plc,byte,bit,datatype,value):
#    result = plc.read_area(Areas.MK,0,byte, datatype)
#    if datatype==S7WLBit:
#        set_bool(result,0,bit,value)
#    elif datatype==S7WLByte or datatype==S7WLWord:
#        set_int(result,0,value)
#    elif datatype==S7WLReal: 
#        set_real(result,0,value)
#    elif datatype==S7WLDWord:
#        set_dword(result,0,value)
#    plc.write_area(Areas.MK,0,byte,result)

#plc = c.Client()
#plc.connect('ip da maquina',rack,slot)

# Conexão com o PLC 
plc = c.Client()
plc.connect('10.32.22.85',0,2)

#Looping p/acompanhamento das variaveis e falhas
while True:
    os.system('cls')
    
# Ler Memorias (MK)
#c = ReadMemory(plc,0,2,S7WLBit,Areas.MK,0)
# Ler Inputs (PE)
#h = ReadMemory(plc,0,0,S7WLBit,Areas.PE,0)
# Ler Outputs (PA)
#j = ReadMemory(plc,0,0,S7WLBit,Areas.PA,0)
# Ler DB (DB)
#k = ReadMemory(plc,0,0,S7WLBit,Areas.DB,120)

    #Processo da Cabeça de Lavagem
    ar = ReadMemory(plc,27,6,S7WLBit,Areas.MK,0)
    agua = ReadMemory(plc,27,1,S7WLBit,Areas.MK,0)
    dreno = ReadMemory(plc,27,0,S7WLBit,Areas.MK,0)
    soda = ReadMemory(plc,27,2,S7WLBit,Areas.MK,0)
    retSoda = ReadMemory(plc,27,3,S7WLBit,Areas.MK,0)
    acido = ReadMemory(plc,27,4,S7WLBit,Areas.MK,0)
    retAcido = ReadMemory(plc,27,5,S7WLBit,Areas.MK,0)
    
    #Processo da Cabeça de Enchimento
    agua2 =  ReadMemory(plc,28,0, S7WLBit,Areas.MK,0)
    alivioVapor = ReadMemory(plc,28,1, S7WLBit,Areas.MK,0)
    vapor2 = ReadMemory(plc,28,2,S7WLBit,Areas.MK,0)
    entradaCO2 = ReadMemory(plc,28,3,S7WLBit,Areas.MK,0)
    ar2 =  ReadMemory(plc,28,4,S7WLBit,Areas.MK,0)
    entradaProduto= ReadMemory(plc,28,5,S7WLBit,Areas.MK,0)
    entradaCerveja = ReadMemory(plc,28,6,S7WLBit,Areas.MK,0)
    
    #Junção das memórias para variaveis
    Var = [ar,agua,dreno,soda,retSoda,acido,retAcido,agua2,alivioVapor,vapor2,entradaCO2,ar2,entradaProduto,entradaCerveja]
    
    #envio das Variaveis para TXT (Manipulação do dash)
    f = open('dashBoard.txt', 'w')
    f.write(str(Var))
    
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    #Retorno ao terminal das variaveis para o monitoramento           
    print("Processo de Lavagem Barril - CHOPP")
    print("Data e Hora", date_time)
    print("\nAr Comprimido - (M27.6):", ar, 
              "\nÁgua Quente - (M27.1): ", agua,
              "\nDreno - (M27.0):", dreno,
              "\nSoda Cáustica - (M27.2):",soda, 
              "\nRetorno Soda - (M27.3):",retSoda,
              "\nÁcido - (M27.4):",acido, 
              "\nRetorno Ácido - (M27.5):",retAcido )
    print("\n")
    print("----------//----------")
    print("\n")
    print("Processo de Enchimento Barril - CHOPP")
    print("Data e Hora", date_time)
    print("\nÁgua Quente - (M28.0):", agua2, 
              "\nAlívio Vapor - (M28.1):",alivioVapor, 
              "\nVapor - (M28.2):",vapor2, 
              "\nEntrada CO2 - (M28.3):", entradaCO2,
              "\nAr Comprimido - (M28.4):",ar2,
              "\nEntrada Produto - (M28.5):", entradaProduto, 
              "\nEntrada Cerveja - (M28.6):",entradaCerveja) 
    time.sleep(1)