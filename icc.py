import math
import cmath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')
xz1= float(input("Digite O Numero real Z1: "))
yz1= float(input("Digite O Numero imaginario Z1: "))
z1= complex(xz1,yz1)
xz0= float(input("Digite O Numero real Z0: "))
yz0= float(input("Digite O Numero imaginario Z0: "))
tensao= float(input("Digite a tensão do local: "))
z0= complex(xz0,yz0)

print(f"\nZ0:{z0}")
print(f"Z1:{z1}\n")
vazio=" "
#relação entre produtos da impedancias dividido pela soma das impedancias
relacaoZ= (z1*z0)/(z1+z0)
#Primario TC
TC=450
Ri=0.012
Rf=0.078
RRF=0.073
RRN=0.073
ExatidaoTc=50
ResistenciaFase=Ri+Rf+RRF
ResistenciaNeutro=Rf+RRN
#rais quadrada de 3
raiz3=math.sqrt(3)
ib=(100*1000)/(tensao*raiz3)
#caculo curto trifasico fase A
icc3A=ib/z1

#print(f"Icc3:{icc3}")
#print(f"ICC3A: {cmath.polar(icc3A)}")
moduloicc3a=abs(icc3A)
faseicc3A=cmath.phase(icc3A)
anguloicc3a=(math.degrees(faseicc3A))

#calculo curto trifasico fase B
icc3B=icc3A*(-0.5+0.866025403784j)
#print(f"ICC3B: {cmath.polar(icc3B)}")
moduloicc3b=abs(icc3B)
faseicc3B=cmath.phase(icc3B)
anguloicc3b=(math.degrees(faseicc3B))

#calculo trifasico fase C
icc3C=icc3B*(-0.5+0.866025403784j)
#print(f"ICC3C: {cmath.polar(icc3C)}")
moduloicc3c=abs(icc3C)
faseicc3C=cmath.phase(icc3C)
anguloicc3c=(math.degrees(faseicc3C))
#print (math.degrees(icc3))
icc2=(icc3A*raiz3*5)/TC

#Calculo bifasico a terra fase A
icc2A= (1/(z1+((relacaoZ+z1))))+((((1/(z1+(relacaoZ+z1)))*-1)*z0)/(z1+z0))+((((1/(z1+(relacaoZ+z1)))*-1)*z1)/(z1+z0))
#print(f"ICC2A: {cmath.polar(icc2A)}")
moduloicc2a=abs(icc2A)
faseicc2A=cmath.phase(icc2A)
anguloicc2a=(math.degrees(faseicc2A))

#Calculo bifasico a terra fase B
icc2B1=(1/(z1+relacaoZ)*(-0.5-0.866025403784j))+((1/(z1+relacaoZ)*-1*z1)/(z1+z0))+((1/(z1+relacaoZ)*-1*z0)/(z1+z0)*(-0.5+0.866025403784j))
icc2B=ib*icc2B1
#print(f"ICC2B: {cmath.polar(icc2B)}")
moduloicc2b=abs(icc2B)
faseicc2B=cmath.phase(faseicc3A)
faseicc2B=cmath.phase(icc2B)
anguloicc2b=(math.degrees(faseicc2B))

#Calculo bifasico a terra fase C
icc4=((1/(z1+relacaoZ))*(-0.5+0.866025403784j))+((1/(z1+relacaoZ)*-1*z0)/(z1+z0)*(-0.5-0.866025403784j))+((1/(z1+relacaoZ)*-1*z1)/(z1+z0))
icc2C=icc4*ib
#print(f"ICC2C: {cmath.polar(icc2C)}")
moduloicc2c=abs(icc2C)
faseicc2C=cmath.phase(icc2C)
anguloicc2c=(math.degrees(faseicc2C))

#Icc bifasico terra neutro
icc2n=icc2A+icc2B+icc2C
#print(f"ICC2N: {cmath.polar(icc2n)}")
moduloicc2n=abs(icc2n)
faseicc2n=cmath.phase(icc2n)
anguloicc2n=(math.degrees(faseicc2n))

#Calculo curto monofasico
iccma=(3*ib)/((2*z1)+z0)
#print(f"Monofasico: {cmath.polar(iccma)}")
moduloiccma=abs(iccma)
faseiccma=cmath.phase(iccma)
anguloiccma=(math.degrees(faseiccma))

#Calculo bifasico
bifasico=((ib/z1)*(raiz3/2))
#print(f"Bifasico: {cmath.polar(bifasico)}")
moduloicc2=abs(bifasico)
faseicc2=cmath.phase(bifasico)
anguloicc2=(math.degrees(faseicc2))

#Calculo fase terra minimo
zc=40/(tensao*tensao/100)
icc1min=(3*ib)/((2*z1)+z0+(3*zc))
#print(f"ICC1min: {cmath.polar(icc1min)}")
moduloicc1min=abs(icc1min)
faseicc1min=cmath.phase(icc1min)
anguloicc1min=(math.degrees(faseicc1min))

#Queda tensao trifasico fase A
qttfa=(((ib/z1)*5)/TC)*ResistenciaFase
#print(f"Queda de tensão Trifasico fase A: {cmath.polar(qttfa)}")
moduloqttfa=abs(qttfa)
faseqttfa=cmath.phase(qttfa)
anguloqttfa=(math.degrees(faseqttfa))

#Queda tensao trifasico fase B
qttfb=((((ib/z1)*5)/TC)*(-0.5+0.866025403784j))*ResistenciaFase
#print(f"Queda de tensão Trifasico fase B: {cmath.polar(qttfb)}")
moduloqttfb=abs(qttfb)
faseqttfb=cmath.phase(qttfb)
anguloqttfb=(math.degrees(faseqttfb))

#Queda tensao trifasico fase C
qttfc=((((ib/z1)*5)/TC)*(-0.5+0.866025403784j)*(-0.5+0.866025403784j))*ResistenciaFase
#print(f"Queda de tensão Trifasico fase B: {cmath.polar(qttfc)}")
moduloqttfc=abs(qttfc)
faseqttfc=cmath.phase(qttfc)
anguloqttfc=(math.degrees(faseqttfc))

#Queda tensao bifasico Terra fase A
qtba=(ResistenciaFase*icc2A)+(ResistenciaNeutro*((icc2n*5)/TC))
#print(f"Queda de tensão Bifasico Terra fase A: {cmath.polar(qtba)}")
moduloqtba=abs(qtba)
faseqtba=cmath.phase(qtba)
anguloqtba=(math.degrees(faseqtba))

#Queda tensao bifasico Terra fase B
qtbb=(ResistenciaFase*((icc2B*5/TC)))+(ResistenciaNeutro*((icc2n*5)/TC))
#print(f"Queda de tensão Bifasico Terra fase B: {cmath.polar(qtbb)}")
moduloqtbb=abs(qtbb)
faseqtbb=cmath.phase(qtbb)
anguloqtbb=(math.degrees(faseqtbb))

#Queda tensao bifasico Terra fase C
qtbc=(ResistenciaFase*((icc2C*5/TC)))+(ResistenciaNeutro*((icc2n*5)/TC))
#print(f"Queda de tensão Bifasico Terra fase C: {cmath.polar(qtbc)}")
moduloqtbc=abs(qtbc)
faseqtbc=cmath.phase(qtbc)
anguloqtbc=(math.degrees(faseqtbc))

#Queda tensao monofasico Terra fase A
qtma=(ResistenciaFase*((iccma*5/TC)))+(ResistenciaNeutro*((iccma*5)/TC))
#print(f"Queda de tensão Monofasico Terra fase A: {cmath.polar(qtma)}")
moduloqtma=abs(qtma)
faseqtma=cmath.phase(qtma)
anguloqtma=(math.degrees(faseqtma))

#Queda tensao monofasico Terra fase B
qtmb=(ResistenciaNeutro*((iccma*5)/TC))
#print(f"Queda de tensão Monofasico Terra fase B: {cmath.polar(qtmb)}")
moduloqtmb=abs(qtmb)
faseqtmb=cmath.phase(qtmb)
anguloqtmb=(math.degrees(faseqtmb))

#Queda tensao monofasico Terra fase C
qtmc=(ResistenciaNeutro*((iccma*5)/TC))
#print(f"Queda de tensão Monofasico Terra fase C: {cmath.polar(qtmc)}")
moduloqtmc=abs(qtmc)
faseqtmc=cmath.phase(qtmc)
#answer = str(round(answer, 2))
anguloqtmc=str(round((math.degrees(faseqtmc)),2))


df = pd.DataFrame({'Falta' : ["Tri", "BTerr", "Mono", "FTMin", "Bi"],
                   'IA (A)' : [str(round(moduloicc3a,2)),str(round(moduloicc2a,2)),str(round(moduloiccma,2)),str(round(moduloicc1min,2)),str(round(moduloicc2,2))],
                   'IA (°)' : [str(round(anguloicc3a,2)),str(round(anguloicc2a,2)),str(round(anguloiccma,2)),str(round(anguloicc1min,2)),str(round(anguloicc2,2))],
                   'IB (A)' : [str(round(moduloicc3b,2)),str(round(moduloicc2b,2)),vazio,vazio,vazio],
                   'IB (°)' : [str(round(anguloicc3b,2)),str(round(anguloicc2b,2)),vazio,vazio,vazio],
                   'IC (A)' : [str(round(moduloicc3c,2)),str(round(moduloicc3b,2)),vazio,vazio,vazio],
                   'IC (°)' : [str(round(anguloicc3c,2)),str(round(anguloicc2b,2)),vazio,vazio,vazio],
                   'IN (A)' : [vazio,str(round(moduloicc2n,2)),vazio,vazio,vazio],
                   'IN (°)' : [vazio,str(round(anguloicc2n,2)),vazio,vazio,vazio]})
    
print(df)
print(f"\n")

dfqueda = pd.DataFrame({'Falta' : ["Trifasico", "Bi", "Monofasico"],
                   'VA (V)' : [str(round(moduloqttfa,2)),str(round(moduloqtba,2)),str(round(moduloqtma,2))],
                   'VA (°)' : [str(round(anguloqttfa,2)),str(round(anguloqtba,2)),str(round(anguloqtma,2))],
                   'VB (V)' : [str(round(moduloqttfb,2)),str(round(moduloqtbb,2)),str(round(moduloqtmb,2))],
                   'VB (°)' : [str(round(anguloqttfb,2)),str(round(anguloqtbb,2)),str(round(anguloqtmb,2))],
                   'VC (V)' : [str(round(moduloqttfc,2)),str(round(moduloqtbc,2)),str(round(moduloqtmc,2))],
                   'VC (°)' : [str(round(anguloqttfc,2)),str(round(anguloqtbc,2)),anguloqtmc]})
    
print(dfqueda)
print(f"\n")
modulo=(moduloicc3a, moduloicc3b,moduloicc3c,moduloicc2a,moduloicc2b,moduloicc2c,moduloicc2n,moduloiccma,moduloicc2,moduloicc1min)
maiorcurto=(max(modulo))
print ("Maior curto: %.2f A.\n" % max(modulo))

angulo=(anguloicc3a,anguloicc3b,anguloicc3c,anguloicc2a,anguloicc2b,anguloicc2c,anguloicc2n,anguloiccma,anguloicc2,anguloicc1min)
anguloA=(anguloicc3a,anguloicc2a,anguloiccma)
anguloB=(anguloicc3b,anguloicc2b,vazio)
anguloC=(anguloicc3c,anguloicc2b,vazio)
anguloN=(vazio,anguloicc2n,vazio)
#cabecalho(IA Modulo,IA Angulo,IB Modulo,IB Angulo,IC Modulo,IC Angulo,IN Modulo,IN Angulo)
quedatensao=(moduloqttfa,moduloqttfb,moduloqttfc,moduloqtba,moduloqtbb,moduloqtbc,moduloqtma,moduloqtmb,moduloqtmc)
print ("Maior Queda de Tensão: %.2f V.\n" % max(quedatensao))

primariotc=(max(modulo)/TC)
print ("Relação maior ICC por primario TC:%.2f.\n" % primariotc)

queda=(max(quedatensao)/ExatidaoTc)

print ("Relação maior Queda de tensão por primario TC: %.2f .\n" % queda)
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

if queda <= 0.8:
    print(bcolors.OK + 'Cálculo OK'+ bcolors.RESET)
else:
    print(bcolors.FAIL+'Rever Cálculo, relação maior Queda de tensão pela classe de exatidão do TC maior que 0,8\n'+ bcolors.RESET)

if primariotc <= 20:
    print(bcolors.OK + 'Cálculo OK'+ bcolors.RESET)
else:
    
    print(bcolors.FAIL+'Rever Cálculo, relação maior ICC pelo primario do TC maior que 20'+ bcolors.RESET)
    


# In[ ]:




