import statistics
import numpy

def fetch_data(number_years):
    # number_of years is either 1Y, 2Y, 3Y
    #Pending: retrieve data from the database in a list
    x = []
    return x

# Sample below is used to test the code. It will be replaced with a call
#to the database
samplex = [1.446,1.453,1.446,1.448,1.449,1.452,1.446,1.446,1.453,1.446,1.448,1.449,1.452,1.446]
sampley = [1.446,1.453,1.446,1.448,1.449,1.452,1.446,1.446,1.453,1.446,1.448,1.449,1.452,1.446]


#Border conditions are not validated at this point.
#An additional check should be put in place at the end of the array
def daily_return(samplex, i):
    if i == 0:
        return (samplex[1]/samplex[0])-1
    else:
        r = (samplex[i+1]/samplex[i]) -1
        return r



def average(samplex):
    x = statistics.mean(samplex)
    return x

def standard_dev(samplex):
    x = statistics.stdev(samplex, xbar = None)
    return x

def covariance (samplex, sampley):
    covxy = numpy.cov(samplex, sampley)
    return covxy

def correlation(samplex, sampley):
    corrxy = covariance(samplex, sampley) / standard_dev(samplex)*standard_dev(sampley)
    return corrxy