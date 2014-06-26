import numpy as np
import datetime
import sys



'''problem. need to run this on np arrays. not normal arrays. will everything behave the same way?'''
def FFT(A):
  n = len(A)
  if n == 1:
    return A
  w_n = np.exp(2*np.pi*1j/n)
  w = 1
  a_even = A[0::2]
  a_odd = A[1::2]
  y_0 = FFT(a_even) 
  y_1 = FFT(a_odd)
  y = [0]*n
  for k in range(n/2):
    y[k] = y_0[k] + (w * y_1[k])
    y[k+(n/2)] = y_0[k] - (w * y_1[k])
    w *= w_n
  return y

def DFT(A_col):
  n = len(A_col)
  w_n = np.exp(2*np.pi*1j/n)
  V = np.array([[0.+1j]*n]*n)
  for i in range(n):
    for j in range(n):
      V[i][j] = w_n**(i*j)
  return np.dot(V,A_col)

def iDFT(A_col):
  n = len(A_col)
  w_n = np.exp(2*np.pi*1j/n)
  Vinv = np.array([[0.+1j]*n]*n)
  for i in range(n):
    for j in range(n):
      Vinv[i][j] = w_n**(-i*j)/n
  return np.dot(Vinv,A_col)

def iFFT_recur(A):
  n = len(A)
  if n == 1:
    return A
  w_n = np.exp(-2*np.pi*1j/n)
  w = 1
  a_even = A[0::2]
  a_odd = A[1::2]
  y_0 = FFT(a_even)
  y_1 = FFT(a_odd)
  y = [0]*n
  for k in range(n/2):
    y[k] = y_0[k] + (w * y_1[k])
    y[k+(n/2)] = y_0[k] - (w * y_1[k])
    w *= w_n
  return y

def iFFT(A):
  n = len(A)
  A = [c/float(n) for c in A]
  # return iFFT_recur(A)
  return iFFT_recur(A)

'''defunct, use A.T where A is a np.array'''
def transpose(A):
  try:
    num_col = len(A[0])
    num_row = len(A)
    B = [[0]*num_row]*num_col
    print "A: ",A
    print "B: ",B
  except:
    print "please enter 2d array"

def FFT(A):
  num_rows = len(A)
  num_col = len(A[0])
  output = [[]*num_col]*num_rows
  for i in range(num_rows):
    output[i] = FFT(A[i])
  output = output.T
  output2 = [[]*num_rows]*num_col
  for i in range(num_col):
    output2[i] = FFT(output[i])
  return output2.T
  
  
    
def main():
  A = [[1,2,3,4],[1,2,3,4]]
  A_col = np.array([[1],[2],[3],[4]])
  '''print FFT(iFFT(A))
  print DFT(iDFT(A_col))'''
  transpose(A)
  

main()