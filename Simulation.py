import random
import sys
import numpy as np
import scipy.linalg as la
import scipy.integrate as integrate
import matplotlib.pyplot as plt


parameters=open("Simulation_parameters.txt","r")
all_lines=parameters.readlines()
parameters.close()

#This function generates hi coefficients in order to generate the later Hamiltonians
def coefficient_hi_generator(number_of_particles,random_or_not):
    if abs(number_of_particles)>8 or abs(number_of_particles)==0:
        sys.exit("You must insert as number of particles a positive integer lower than 8 and higher than 0.")
    elif random_or_not not in [0,1]:
        sys.exit("The second line of the file containing the parameters must be 0 or 1.")
    else:
        if random_or_not==0:
            #Create both Jij and hi arrays with 0s to give them value later
            hi=np.zeros(number_of_particles)
            i=0
            while i<number_of_particles:
                hi[i]=float(input("Introduce the element h{}: ".format(i+1)))
                i=i+1
            i=0
            return(hi)
        elif random_or_not==1:
            #Create both Jij and hi arrays with 0s to give them value later
            hi=np.zeros(number_of_particles)
            i=0
            while i<number_of_particles:
                random.seed()
                hi[i]=random.random()
                i=i+1
            return(hi)  
 
    
    
    
    