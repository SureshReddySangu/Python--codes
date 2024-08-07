from scipy.constants import pi
from numpy import linspace, arange, tan
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt


png_filename = 'beta.png'


nf = 3.48       # refractive index of the guiding film
ns = 1.444      # refractive index of the substrate
nc = 1.444      # refractive index of the cover
h =  0.22e-6     # height of the guiding film

samples = 1000  # number of kappas to sample

wavelength = 1.55*10**-6 
k = 2*pi/wavelength
kappamax = sqrt((k*nf)**2 - (k*ns)**2)
kappa = linspace(1, kappamax, num=samples)

beta = sqrt((k*nf)**2 - kappa**2)
gamma_s = sqrt(beta**2 - (k*ns)**2)
gamma_c = sqrt(beta**2 - (k*nc)**2)


y1 = tan(h*kappa)
y2 = (gamma_c + gamma_s)/(kappa*(1-(gamma_c*gamma_s/kappa**2)))



fig = plt.figure()                                      # calls a variable for the png info

# defines plot's information (more options can be seen on matplotlib website)
plt.title("Characteristic Equation for TE Modes")       # plot name
plt.xlabel('kappa')                                     # x axis label
plt.ylabel('Transcendental Funcs')                      # y axis label
#plt.xticks(arange(0,kappamax, kappamax/20))#5000))     # x axis tick marks
plt.axis([0,kappamax,-10,10])                           # x and y ranges

# defines png size
fig.set_size_inches(10.5,5.5)                           # png size in inches

# plots the characteristic equation for TE
plt.plot(kappa,y1)
plt.plot(kappa,y2)

#saves png with specific resolution and shows plot
fig.savefig(png_filename ,dpi=600, bbox_inches='tight') # saves png
plt.show()                                              # shows plot

plt.close()                                             # closes pylab