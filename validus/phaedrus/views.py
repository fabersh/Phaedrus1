from django.http import HttpResponse
from . import stats

import statistics
import numpy


# Sample below is used to test the code. It will be replaced with a call
#to the database
samplex = [1.446,1.453,1.446,1.448,1.449,1.452,1.446]
sampley = [1.446,1.453,1.446,1.448,4.636,1.452,1.446]

#Original home for this function is the stats.py file.
def correlation(samplex, sampley):
    corrxy =stats. covariance(samplex, sampley) / stats.standard_dev(samplex)*stats.standard_dev(sampley)
    return corrxy



#This line is used to test the statistical functions on the browser using a small subset shown above (samplex, sampley)
#The code was brought into the views.py ONLY FOR TESTING PURPOSES; otherwise the MVC model would be broken. The
#ideal home for these functions are in the stats.py file.
def index(request):
    return HttpResponse(stats.correlation(samplex, sampley) )





