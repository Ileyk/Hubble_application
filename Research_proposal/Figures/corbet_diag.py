import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import math
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from itertools import product, combinations
from numpy import linspace
import re
from matplotlib.patches import Rectangle

# below is a method which compute, for each disc, its area which overlaps another disc.
# IT DOES ACCOUNT FOR MORE THAN DOUBLE OVERLAP since we now compute this area (or rather its complement)
# in a Monte-Carlo way

font = {'family' : 'normal',
'weight' : 'bold',
'size'   : 25}

plt.rc('font', **font)

Ncol=5

Nsys=75
mdot = np.zeros((1+Nsys,Ncol))

fichier = 'corbet_data.txt'
f = open(fichier, "r")
words2 = f.read()
words = filter(None, re.split(r'[\n ]',words2))

markers=['o','s','^','x','p','D','+']#,'v']
colors=['b','g','r','c','m','k','y']

Po = []#np.zeros(Nsys)
Ps = []#np.zeros(Nsys)
noSpin = []
noPer = []
typ = []
gal = []
for i in range(0,Nsys):
	print 'ici', words[(i+1)*Ncol], words[(i+1)*Ncol+1]#(i+1)*Ncol
	if   (words[(i+1)*Ncol+1]=='--' and words[(i+1)*Ncol]!='--'): # no spin
		noSpin.append(float(words[(i+1)*Ncol]))
	elif (words[(i+1)*Ncol]=='--' and words[(i+1)*Ncol+1]!='--'): # no period
		noPer.append(float(words[(i+1)*Ncol+1]))
	elif (words[(i+1)*Ncol]=='--' and words[(i+1)*Ncol+1]=='--'): # no period nor spin
		print i
	elif ('#' in words[(i+1)*Ncol]):
		print i
	else:
		Po.append(float(words[(i+1)*Ncol]))
		Ps.append(float(words[(i+1)*Ncol+1]))
		typ.append(words[(i+1)*Ncol+2])
		gal.append(words[(i+1)*Ncol+3])
		#Ps[i]=words[(i+1)*Ncol+1]

# print np.asarray(noPer), np.ones(np.size(noPer))
# print noPer, [200]*np.size(noPer)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

ax.set_yscale('log')
ax.set_xscale('log')

xmin, xmax, ymin, ymax = 0.5*np.amin(np.asarray(Po, dtype='float')), 2*np.amax(np.asarray(Po, dtype='float')), 0.5*np.amin(np.asarray(Ps, dtype='float')), 2*np.amax(np.asarray(Ps, dtype='float'))
xmin=1
ymin=1
xmax=1000
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

# plt.scatter(*zip(*[(a, b) for a,b in zip(Po,Ps) if (a<2000 and b > -100)]))
for i in range(0,np.size(Po)):
	if (typ[i]=='Sg'):
		marker=markers[0]
		color=colors[0]
	elif (typ[i]=='Be'):
		marker=markers[1]
		color=colors[1]
	elif (typ[i]=='SFXT'):
		marker=markers[2]
		color=colors[2]
	elif (typ[i]=='RLOF'):
		continue
		# marker=markers[3]
		# color=colors[3]
	elif (typ[i]!='Sg' and typ[i]!='Be' and typ[i]!='SFXT' and typ[i]!='RLOF'):
		continue
		# marker=markers[4]
		# color=colors[4]
	plt.scatter(Po[i],Ps[i],marker=marker,color=color,s=120)
	if (marker=='x'):
		plt.scatter(Po[i],Ps[i],marker=marker,color=color,s=120, lw=5)
# add a frame to the 3 systems we consider in the article SgXB_1
# a X-1 :
# XTE J1855-026 :
# IGR J18027-2016 :
# ax.plot((8.96),(238),'o',color='y',markerfacecolor='none',markeredgecolor=colors[0],ms=20,markeredgewidth=4)
# ax.plot((6.07),(361),'o',color='y',markerfacecolor='none',markeredgecolor=colors[0],ms=20,markeredgewidth=4)
# ax.plot((4.47),(140),'o',color='y',markerfacecolor='none',markeredgecolor=colors[0],ms=20,markeredgewidth=4)
# plt.axvline(x=5.6, ymin=0.0001, ymax = 61500, linewidth=2, linestyle='--', color='k', alpha=0.4)
# plt.axvline(x=3.9, ymin=0.0001, ymax = 61500, linewidth=2, linestyle='--', color='k', alpha=0.4)
# plt.text(0.5, 0.5, 'matplotlib', rotation=90, horizontalalignment='center',verticalalignment='center', transform=ax.transAxes, fontsize=4)
# plt.text(5.1, 9500, 'Cyg X-1', rotation=90, horizontalalignment='center',verticalalignment='center',fontsize=13)
# plt.text(3.6, 9500, 'LMC X-1', rotation=90, horizontalalignment='center',verticalalignment='center',fontsize=13)

# for i in range(0,np.size(noPer)):
# 	plt.plot((xmin, xmax), (noPer[i], noPer[i]),color='r',linestyle='--', linewidth=1.5, alpha=1)
# 	# plt.loglog(np.arange(xmin,xmax,(xmax-xmin)/100.),[noPer[i]]*100,color='r',linestyle='--', linewidth=1.5, alpha=1)
# for i in range(0,np.size(noSpin)):
# 	plt.plot((noSpin[i], noSpin[i]), (ymin, ymax),color='g',linestyle='--', linewidth=1.5, alpha=1)
# 	plt.axvline(x=0.402, ymin=0.4, ymax = 0.615, linewidth=2, color='k')
	# ax.plot(v,noSpin[i]+v,100*v,color='b',linewidth=0.8,alpha=1)
# 	plt.loglog(np.arange(noSpin[i]-0.01,noSpin[i]+0.01,(0.01-(-0.01))/100.),(np.arange(noSpin[i]-0.01,noSpin[i]+0.01,(0.01-(-0.01))/100.)/noSpin[i])**3,color='r',linestyle='--', linewidth=1.5, alpha=1)

# plt.grid()

# xticks = [1.1,2.,4.,8.,16.]
# fig.xaxis.set_ticks( xticks )
# fig.xaxis.set_ticklabels( ['%1.1f'  % i for i in xticks] )
ax.tick_params(which='major', length=8, color='k')
ax.tick_params(which='minor', length=4, color='k')

plt.grid(which='both',color='k', linestyle='-', linewidth=1.5, alpha=0.1)

plt.xlabel('Orbital period (days)', fontweight='bold', fontsize=25)
plt.ylabel('Neutron star spin period (seconds)', fontweight='bold', fontsize=25)

# - - - - -

# Create custom artists
Sg = plt.Line2D((0,0),(0,1),   markerfacecolor=colors[0], markeredgecolor='none', marker=markers[0], linestyle='', markersize=10)
Be = plt.Line2D((0,0),(0,1),   markerfacecolor=colors[1], markeredgecolor='none', marker=markers[1], linestyle='', markersize=10)
SFXT = plt.Line2D((0,0),(0,1), markerfacecolor=colors[2], markeredgecolor='none', marker=markers[2], linestyle='', markersize=10)
# RLOF = plt.Line2D((0,0),(0,1), markeredgecolor=colors[3], marker=markers[3], markeredgewidth=5, linestyle='', linewidth=400, markersize=10)
# Other = plt.Line2D((0,0),(0,1), markerfacecolor=colors[4], markeredgecolor='none', marker=markers[4], linestyle='', markersize=10)

#Create legend from custom artist/label lists
ax.legend([Sg,Be,SFXT],['Supergiant X-ray binaries','Be X-ray binaries','Supergiant fast X-ray transients'],loc='upper right',fontsize=15,shadow=True,numpoints = 1)

# - - - - -

fig.savefig('corbet_diag.png',bbox_inches='tight',dpi=100)

# mdot[i][j]=words[select_out_adim]

# Lz=1
#
# rad=0.1
#
# Nbmax=200
# areas=np.zeros(Nbmax)
# areas_too_much=np.zeros(Nbmax)
#
# Navg=20
#
# NMC=2000
#
# for k in range(0,Nbmax): # represents the deepness of the column (ie the distance to the source)
#
# 	print k
#
# 	for p in range(0,Navg): # so as to repeat the process Navg times and get a smoother output
#
# 		Nb=1+k # the furthest the source, the more absorption balls (linearly if uniform absorption along l.o.s.)
#
# 		balls=np.zeros((Nb,2))
#
# 		for i in range(0,Nb):
# 			balls[i,0]=Lz*random.random()
# 			balls[i,1]=Lz*random.random()
#
# 		shadow=0
# 		# test-particle : is it in the shadow?
# 		for i in range(0,NMC):
# 			x=Lz*random.random()
# 			y=Lz*random.random()
# 			if (any(np.sqrt((balls[:,0]-x)**2.+(balls[:,1]-y)**2.)<rad)):
# 				shadow=shadow+1
#
# 		areas[k]=areas[k]+(shadow/float(NMC))/Navg
#
# 	areas_too_much[k]=Nb*math.pi*rad**2.
#
# 		# area_tot=0.
# 		# area_i=0.
# 		# for i in range(0,Nb):
# 		# 	print i
# 		# 	area_i=math.pi*rad**2.
# 		# 	for j in range(0,Nb):
# 		# 		d=np.sqrt((balls[i,0]-balls[j,0])**2.+(balls[i,1]-balls[j,1])**2.)
# 		# 		if (i!=j and d<2*rad):
# 		# 			overlap=(2*rad**2.)*math.acos(d/(2*rad))-0.5*d*np.sqrt(4*rad**2-d**2)
# 		# 			area_i=area_i-overlap
# 		# 	area_tot=area_tot+area_i
# 		#
# 		# areas[k]=areas[k]+area_tot/Navg.
#
#
