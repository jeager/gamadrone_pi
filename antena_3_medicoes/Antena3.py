import numpy
import matplotlib.pyplot as plt

# ANTENA 3

# Distancia = 1.0 m
dbm_10 = numpy.loadtxt('antena_3_10_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_10 = numpy.mean(dbm_10) # calcula a media
print dbm_mean_10 

# Distancia = 1.5 m
dbm_15 = numpy.loadtxt('antena_3_15_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_15 = numpy.mean(dbm_15) # calcula a media
print dbm_mean_15

# Distancia = 2.0 m
dbm_20 = numpy.loadtxt('antena_3_20_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_20 = numpy.mean(dbm_20) # calcula a media
print dbm_mean_20

# Distancia = 2.5 m
dbm_25 = numpy.loadtxt('antena_3_25_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_25 = numpy.mean(dbm_25) # calcula a media
print dbm_mean_25

# Distancia = 3.0 m
dbm_30 = numpy.loadtxt('antena_3_30_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_30 = numpy.mean(dbm_30) # calcula a media
print dbm_mean_30

# Distancia = 3.5 m
dbm_35 = numpy.loadtxt('antena_3_35_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_35 = numpy.mean(dbm_35) # calcula a media
print dbm_mean_35

# Distancia = 4.0 m
dbm_40 = numpy.loadtxt('antena_3_40_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_40 = numpy.mean(dbm_40) # calcula a media
print dbm_mean_40

# Distancia = 4.5 m
dbm_45 = numpy.loadtxt('antena_3_45_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_45 = numpy.mean(dbm_45) # calcula a media
print dbm_mean_45

# Distancia = 5.0 m
dbm_50 = numpy.loadtxt('antena_3_50_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_50 = numpy.mean(dbm_50) # calcula a media
print dbm_mean_50

# Distancia = 5.5 m
dbm_55 = numpy.loadtxt('antena_3_55_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_55 = numpy.mean(dbm_55) # calcula a media
print dbm_mean_55

# Distancia = 6.0 m
dbm_60 = numpy.loadtxt('antena_3_60_parsed.txt', skiprows=1, unpack=True) # Carrega os dados que estao no arquivo txt
dbm_mean_60 = numpy.mean(dbm_60) # calcula a media
print dbm_mean_60

# Vetor das medias 
DBM_mean = numpy.array([dbm_mean_10, dbm_mean_15, dbm_mean_20, dbm_mean_25, dbm_mean_30, dbm_mean_35, dbm_mean_40, dbm_mean_45,
 dbm_mean_50, dbm_mean_55, dbm_mean_60])
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
plt.title('Antena 3') # titulo
plt.xlabel('Potencia (dBm)')
plt.ylabel('Distancia (m)')
plt.legend(loc='upper left') # legenda
plt.ylim(0, d[-1]+1) # limite dos eixos
plt.show()
