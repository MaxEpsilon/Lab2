from astropy.io import fits
import numpy as np
from astropy.modeling.models import Gaussian2D
a = fits.open('normalizedflat.fits')
data = a[0].data

cropped = data[22:90,:]

hdu = fits.PrimaryHDU(cropped)
hdu.writeto('cropped.fits')
