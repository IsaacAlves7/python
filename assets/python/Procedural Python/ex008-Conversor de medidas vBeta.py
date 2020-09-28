print('-----------------------------------------------')
print('Conversor de Unidades de Medidas de Comprimento')
print('-----------------------------------------------')
Km=float(input('Digite o valor da distancia em quilometros (Km):'))
print('hm-dam-m-dm-cm-mm')
print('-----------------')
print('A conversão de quilometros para;')
HM=Km*10
DAM=Km*100
M=Km*1000
DM=Km*10000
CM=Km*100000
MM=Km*1000000
print(' hm = {:.2f}'.format(HM))
print(' dam = {:.2f}'.format(DAM))
print(' m = {:.2f}'.format(M))
print(' dm = {:.2f}'.format(DM))
print(' cm = {:.2f}'.format(CM))
print(' mm = {:.2f}'.format(MM))
print('===================================================')
m=float(input('Digite o valor da distancia em metros (m):'))
print('km-hm-dam-dm-cm-mm')
print('------------------')
print('A conversão de metros para;')
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm= m*100
mm=m*1000
print(' km = {:.2f}'.format(km))
print(' hm = {:.2f}'.format(hm))
print(' dam = {:.2f}'.format(dam))
print(' dm = {:.2f}'.format(dm))
print(' cm = {:.2f}'.format(cm))
print(' mm = {:.2f}'.format(mm))