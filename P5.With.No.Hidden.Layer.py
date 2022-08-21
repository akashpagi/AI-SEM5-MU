#P5 : With No Hidden Layer
import numpy as np
def activfunc_sigmoid(x,deriv=False): 
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x)) 
   
X = np.array([ [1,1,0,1], [0,0,0,0], [0,1,1,1], [1,1,1,1] ,
                      [0,1,0,1], [0,1,0,0], [1,0,0,1], [0,1,0,0] ])

y = np.array([[0,0,1,0,1,0,1,0]]).T

np.random.seed(1) 
w0 = 2*np.random.random((4,1)) - 1
print("initial weights - \n", w0)
for n in range(1000):
    l_input = X  # x    
    l_output = activfunc_sigmoid(l_input.dot(w0))   
    l_output_error = y - l_output 
    l_output_delta = l_output_error * activfunc_sigmoid(l_output,True)        
    w0 = w0 + 2*l_input.T.dot(l_output_delta)
    
print("final weights - \n", w0)
print( "Output After Training:")
print (l_output)
print ("Loss: \n" + str(np.mean(np.square(y - l_output))))


