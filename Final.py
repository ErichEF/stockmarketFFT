import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

#snp1=np.loadtxt('S&P2001-2010.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
#snp11=np.loadtxt('S&P2011-2020.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
dji1=np.loadtxt('DJI2001-2010.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
dji11=np.loadtxt('DJI2011-2020.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)

dax1=np.loadtxt('DAX2001.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
dax11=np.loadtxt('DAX2011.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
jse7=np.loadtxt('JSE2007.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)
jse11=np.loadtxt('JSE2011.csv',dtype='float',delimiter=',',usecols=(4),unpack=True)

time1 = pd.read_csv("DJI2001-2010.csv",parse_dates=["#Date"],usecols=[0]).values
time11 = pd.read_csv("DJI2011-2020.csv",parse_dates=["#Date"],usecols=[0]).values
timedax1 = pd.read_csv("DAX2001.csv",parse_dates=["#Date"],usecols=[0]).values
timedax11 =  pd.read_csv("DAX2011.csv",parse_dates=["#Date"],usecols=[0]).values
timejse7 = pd.read_csv("JSE2007.csv",parse_dates=["#Date"],usecols=[0]).values
timejse11 =  pd.read_csv("JSE2011.csv",parse_dates=["#Date"],usecols=[0]).values

plt.figure()
plt.plot(time1,dji1,'b',label='DOW Index')
plt.plot(timedax1,dax1,'r',label='DAX Index')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones and DAX Stock Price 2001 - 2010')
plt.legend()
plt.annotate("September 11 Attacks",xy=(pd.Timestamp('2001-9-11'), 9473.73),xytext=(pd.Timestamp('2001-2-11'), 12000),arrowprops=dict(arrowstyle='-|>'))
plt.annotate("Lehman Brothers Collapse",xy=(pd.Timestamp('2008-9-15'), 10926.2),xytext=(pd.Timestamp('2007-2-15'), 10000),arrowprops=dict(arrowstyle='-|>'))
plt.grid()

plt.figure()
plt.plot(time11,dji11,'b',label='DOW Index')
plt.plot(timedax11,dax11,'r',label='DAX Index')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones and DAX Stock Price 2011 - April 7, 2020')
plt.legend()
plt.grid()

plt.figure()
plt.plot(timejse7,jse7,'g',label='JSE Index')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('JSE Stock Price 2007 - 2010')
plt.legend()
plt.annotate("FIFA World Cup",xy=(pd.Timestamp('2010-6-11'), 8.5),xytext=(pd.Timestamp('2010-1-11'), 10),arrowprops=dict(arrowstyle='-|>'))
plt.grid()

plt.figure()
plt.plot(timejse11,jse11,'g',label='JSE Index')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('JSE Stock Price 2011 - 2020')
plt.legend()
plt.grid()

dji1fft = np.fft.rfft(dji1) # Using real because imaginary values from normal fft contribute nothing
dji11fft = np.fft.rfft(dji11)
dax1fft = np.fft.rfft(dax1)
dax11fft = np.fft.rfft(dax11)
jse7fft = np.fft.rfft(jse7)

threshfreq1 = 1/90 # Tri-monthly
threshfreq2 = 1/180 # Half-year
threshfreq3 = 1/60 # Bi monthly
threshfreq4 = 1/5 # Weekly, because stock market closed on weekends
threshfreq5 = 1/120 # Per quarter

def lowfreq1(x):
    for i in range(len(x)):
        if freq1[i]>threshfreq5:
            x[i]=0
    return x

def highfreq1(x):
    for i in range(len(x)):
        if freq1[i]<threshfreq4:
            x[i]=0
    return x

def lowfreq11(x):
    for i in range(len(x)):
        if freq11[i]>threshfreq5:
            x[i]=0
    return x

def highfreq11(x):
    for i in range(len(x)):
        if freq11[i]<threshfreq4:
            x[i]=0
    return x

def lowfreqdax1(x):
    for i in range(len(x)):
        if freqdax1[i]>threshfreq5:
            x[i]=0
    return x

def highfreqdax1(x):
    for i in range(len(x)):
        if freqdax1[i]<threshfreq4:
            x[i]=0
    return x

def lowfreqdax11(x):
    for i in range(len(x)):
        if freqdax11[i]>threshfreq5:
            x[i]=0
    return x

def highfreqdax11(x):
    for i in range(len(x)):
        if freqdax11[i]<threshfreq4:
            x[i]=0
    return x

def lowfreq7(x):
    for i in range(len(x)):
        if freqjse7[i]>threshfreq5:
            x[i]=0
    return x

def highfreq7(x):
    for i in range(len(x)):
        if freqjse7[i]<threshfreq4:
            x[i]=0
    return x

freq1=np.fft.rfftfreq(len(dji1))
freq11=np.fft.rfftfreq(len(dji11))
freqdax1=np.fft.rfftfreq(len(dax1))
freqdax11=np.fft.rfftfreq(len(dax11))
freqjse7=np.fft.rfftfreq(len(jse7))

lowdji1 = lowfreq1(dji1fft)
lowdax1 = lowfreqdax1(dax1fft)
plt.figure()
plt.plot(time1[1::],np.fft.irfft(lowdji1),'b')
plt.plot(timedax1[1::],np.fft.irfft(lowdax1),'r')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones and DAX Stock Price 2001-2010 (Smoothed out)')
plt.grid()

lowdji11 = lowfreq11(dji11fft)
lowdax11 = lowfreqdax11(dax11fft)
plt.figure()
plt.plot(time11[1::],np.fft.irfft(lowdji11),'b')
plt.plot(timedax11,np.fft.irfft(lowdax11),'r')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones and DAX Stock Price 2011-2020 (Smoothed out)')
plt.grid()

dji1fft = np.fft.rfft(dji1) #Refreshing since for some reason the previous ffts mess up the following code
dji11fft = np.fft.rfft(dji11)
dax1fft = np.fft.rfft(dax1)
dax11fft = np.fft.rfft(dax11)

highdji1 = highfreq1(dji1fft)
highdax1 = highfreqdax1(dax1fft)
plt.figure()
plt.plot(time1[1::],np.fft.irfft(highdji1),'b')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones Stock Price 2001-2010 (Stability)')
plt.grid()

plt.figure()
plt.plot(timedax1[1::],np.fft.irfft(highdax1),'r')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('DAX Stock Price 2001-2010 (Stability)')
plt.grid()

highdji11 = highfreq11(dji11fft)
highdax11 = highfreqdax11(dax11fft)
plt.figure()
plt.plot(time11[2:-1],np.fft.irfft(highdji11)[1:-1],'b')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones Stock Price 2011-2020 (Stability)')
plt.grid()

plt.figure()
plt.plot(timedax11[1:-1],np.fft.irfft(highdax11)[1:-1],'r')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('DAX Stock Price 2011-2020 (Stability)')
plt.grid()

jse7fft = np.fft.rfft(jse7)
lowjse7 = lowfreq7(jse7fft)
plt.figure()
plt.plot(timejse7,np.fft.irfft(lowjse7),'g')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('JSE Stock Price 2007-2010 (Smoothed out)')
plt.grid()

jse7fft = np.fft.rfft(jse7)
highjse7 = highfreq7(jse7fft)
plt.figure()
plt.plot(timejse7[1:-1],np.fft.irfft(highjse7)[1:-1],'g')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('JSE Stock Price 2007-2010 (Stability)')
plt.grid()

corr1 = np.convolve(dax11,dji11)

plt.figure()
plt.plot(corr1)
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Dow Jones Stock Price 2011-2020 (Smoothed out)')
plt.grid()
