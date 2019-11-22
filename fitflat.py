from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
a = fits.open('cropped.fits')

data = a[0].data
counts = np.mean(data,axis=0)

pixpos = np.array(range(1, len(counts)+1))

a, b, c = np.polyfit(x=pixpos, y=counts, deg=2)
x = np.arange(1, len(pixpos)+1, 1)
y = a * x**2 + b * x + c

newy = counts / y
plt.plot(pixpos,counts)
plt.plot(pixpos,y)
plt.show()

hdu = fits.PrimaryHDU(y)
hdu.writeto('finalnomalizedflats.fits')

