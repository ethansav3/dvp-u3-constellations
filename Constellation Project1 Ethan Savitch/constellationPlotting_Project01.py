
# coding: utf-8

# In[218]:


get_ipython().magic('matplotlib notebook')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# ## Graphing The Big Dipper
# First, determining the coordinates for all stars in the constellation.

# In[219]:


#RA = [h,m,s]
#DEC = [dec,arcmin,arcsec]

AlkaidRA = [13, 48, 16.36]
AlkaidDec = [49, 13, 14.2, 1]

MizarRA = [13,24,40.24]
MizarDec = [54, 49, 42.3, 1]

AliothRA = [12, 54, 50.49]
AliothDec = [55, 51, 31.4, 1]

MegrezRA = [12, 16, 20.17]
MegrezDec = [56,55,43.2, 1]

PhecdaRA = [11, 54, 48.15]
PhecdaDec = [53, 35, 24.8, 1]

MerakRA = [11, 2, 57.27]
MerakDec = [56, 16, 50.7, 1]

DubheRA = [11,4,51.71]
DubheDec = [61, 38, 59.3, 1]

BigDipper_RA_HMS = [AlkaidRA, MizarRA, AliothRA, MegrezRA, PhecdaRA, MerakRA, DubheRA]
BigDipper_DEC_deg = [AlkaidDec, MizarDec, AliothDec, MegrezDec, PhecdaDec, MerakDec, DubheDec]
BigDipper_Distances = [103.94, 78.16, 82.55, 80.51, 83.18, 79.74, 123.64]
BigDipper_StarNames = ['Alkaid', 'Mizar', 'Alioth', 'Megrez', 'Phecda', 'Merak', 'Dubhe']


# # Convert to RA/DEC

# In[220]:


#convert right ascension hour,minute,second into a Right Ascenion in RADIANS (b/c pi/180)
def hms_To_RA(hour, minute, second):
    RA = (hour*15 + minute * (1.0/4.0) + second * (1/240.)) * (np.pi/180)
    return RA

#convert declination degree,arcmin,arcsec into a Declination in RADIANS (b/c pi/180)
#sign = 1 if northern hemisphere
#sign = -1 if southern hemisphere
def deg_To_Dec(degree, arcmin, arcsec, sign):
    if(sign == 1):
        Dec = (degree + arcmin * (1./60.) + arcsec * (1./3600.)) * (np.pi/180)
        return Dec
    if(sign == -1):
        Dec = (degree - arcmin * (1./60.) - arcsec * (1./3600.)) * (np.pi/180)
        return Dec


BigDipper_RA = [hms_To_RA(h, m, s) for (h,m,s) in BigDipper_RA_HMS]
BigDipper_DEC = [deg_To_Dec(deg, arcmin, arcsec, sign) for (deg, arcmin, arcsec, sign) in BigDipper_DEC_deg]


# # Convert to X/Y/Z

# In[221]:


#dec = declination
#ra = right ascension
#r = distance to that star
def radToX(dec, ra, r):
    x = r * np.cos(dec) * np.cos(ra)
    return x

def radToY(dec, ra, r):
    y = r * np.cos(dec) * np.sin(ra)
    return y

def radToZ(dec, ra, r):
    z = r * np.sin(dec)
    return z

BigDipper_RA_DEC = list(zip(BigDipper_RA, BigDipper_DEC, BigDipper_Distances))

BigDipper_X = [radToX(dec, ra, dist) for (ra, dec, dist) in BigDipper_RA_DEC]
BigDipper_Y = [radToY(dec, ra, dist) for (ra, dec, dist) in BigDipper_RA_DEC]
BigDipper_Z = [radToZ(dec, ra, dist) for (ra, dec, dist) in BigDipper_RA_DEC]

BigDipper = list(zip(BigDipper_StarNames, BigDipper_X, BigDipper_Y, BigDipper_Z))


# ## Plot in 2 Dimensions

# In[222]:


fig = plt.figure()
fig.add_subplot(1,1,1)
plt.scatter(BigDipper_X,BigDipper_Y)
plt.show()


# ## Plot in 3 Dimensions

# In[223]:


fig3d = plt.figure()
fig3d.add_subplot(1,1,1,projection='3d')
plt.scatter(BigDipper_X, BigDipper_Y, BigDipper_Z)
plt.xlabel('x')
plt.ylabel('y')
plt.title('The Big Dipper')
plt.show()
print(BigDipper)


# made by Ethan Savitch
# 7/8/18
