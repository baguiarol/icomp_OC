from pathlib import Path
import glob
import statistics as st
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


aq = Path('OC-Modulo3/Dados dos Intervalos/')

ar = glob.glob('*.txt')

a = 0

var = []

valores = []
desvio = []

for i in range(len(ar)):
    aqr = open(ar[i], 'r') # arquivo1
    #print(ar[i])
    
    for line in aqr:
        for k in line.split():
            var.append(k)
    for j in range(len(var)):
        if(var[j] == '#'):
            a += float(var[j+1].replace(',','.'))
            desvio.append(float(var[j+1].replace(',','.')))
    a = a/10
   
    ar[i] = ar[i].replace('.txt', '')
    ar[i] = ar[i].replace('run', '')
  
    margem_erro = st.pstdev(desvio)
    #print(margem_erro)
    valores.append((int(ar[i]), round(a,3), round(margem_erro,3)))
    a = 0
    var = []
    desvio = []
    

valores.sort()

intervalo_x = []
misses_y = []
erros = []

for i in range(len(valores)):
    intervalo_x.append(valores[i][0])
    misses_y.append(valores[i][1])
    erros.append(valores[i][2])

#print(intervalo_x)
#print(misses_y)
#print(erros)

#gerando o grafico
plt.rcParams['figure.figsize'] = (11,7)
plt.title('Média dos Intervalos do Cache Miss com Barras de Erro', fontsize=20)
plt.xlabel('Intervalos', fontsize=15)
plt.ylabel('Média dos Misses', fontsize=15)

plt.plot(intervalo_x ,misses_y, 'or')
plt.errorbar(intervalo_x,misses_y , erros,color = 'orange' ,uplims=True, lolims=True)

plt.annotate("Ponto ótimo", xy=(30, 17),xycoords='data',xytext=(400, 20),textcoords='data',arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.show()