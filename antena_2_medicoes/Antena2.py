import numpy
import matplotlib.pyplot as plt

# ANTENA 2

dbm_array = []
i = 10
# Carregar valores
for x in range(0, 11):
	values = numpy.mean(numpy.loadtxt('antena_2_' + str(i) +  '_parsed.txt', skiprows=1, unpack=True))
	dbm_array.append(values)
	print values
	i = i + 5

# Vetor das medias 
DBM_mean = numpy.array(dbm_array)
print DBM_mean

# Vetor das distancias
d = numpy.array([1,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0])

# Minimos quadrados
m = len(d)
X = numpy.matrix([numpy.ones(m), DBM_mean]).T
y = numpy.matrix(d).T
betaHat = numpy.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
d_DBM = 0.1 # delta potencia
n_DBM = (numpy.amax(DBM_mean) - numpy.amin(DBM_mean))/d_DBM # tamanho do vetor potencia 
DBM = numpy.linspace(numpy.amin(DBM_mean),numpy.amax(DBM_mean),n_DBM) # Vetor tempo [s]
dd = numpy.array(betaHat[0] + betaHat[1] * DBM) # distancia obtida pelo metodo dos minimos quadrados

# Polinomio de 3 grau
p3 = numpy.poly1d(numpy.polyfit(DBM_mean, d, 3)) # Ajuste de curva
D_p3 = p3(DBM) # Distancia obtida pelo o ajuste de curva
print p3

# Graficos 
plt.figure(1)
plt.plot(DBM, dd.T,'k',label='Minimos quadrados') # Grafico obtido pelo metodo dos minimos quadrados
plt.plot(DBM_mean,d,'o',label='Medias') # grafico obtido pelas medicoes
plt.plot(DBM, D_p3,'r', label='Polinomio grau 3')
plt.title('Antena 2') # titulo
plt.xlabel('Potencia (dBm)')
plt.ylabel('Distancia (m)')
plt.legend(loc='upper left') # legenda
plt.ylim(0, d[-1]+1) # limite dos eixos
plt.show()
