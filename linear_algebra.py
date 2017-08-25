"""
This program allows one to row reduce matricies,
find the linearity of matricies, find the inverses
of matricies, or calculate a simple linear regression.
"""

#import various packages
from __future__ import division
import numpy as np

def createVector(elems):
    return np.transpose(np.matrix([elems], 'f'))

def makeMatrix(vlist):
    m = np.hstack(vlist)
    return m

#makes the element of operation in the row 1
def reduceRow(m, row, col):
    if not (abs(m[row, col]) < error):
        m[row] /= m[row, col]
    return m

#performs reduceRow for every row
def reduceRows(m, col):
    for row in range(m.shape[0]):
        m = reduceRow(m, row, col)
    return m

#subtracts the row of choice from each row
def pivotColumn(m, col):
    for row in range(m.shape[0]):
        if not (row == col or \
        (abs(m[row, col]) < error)):
            m[row] -= m[col]
    return m

def cleanMatrix(m):
    for col in range(np.amin(m.shape)):
        reduceRow(m, col, col)
    return m

def pivotColumns(m):
    for col in range(np.amin(m.shape)):
        m = reduceRows(m, col)
        m = pivotColumn(m, col)
    return m

#final funcion to row reduce a matrix
def reduceMatrix(m):
    m = pivotColumns(m)
    m = cleanMatrix(m)
    return m

#appends a column of zeros and reduces matrix
def findLinearity(m):
    z = np.zeros((m.shape[0], 1))
    m = np.hstack((m, z))
    m = reduceMatrix(m)
    return m

#finds the inverses of matricies
def findInverse(m):
    i = np.eye(m.shape[0])
    m = np.hstack((m, i))
    m = reduceMatrix(m)
    if np.array_equal(m[:,:i.shape[0]], i):
        return m[:,i.shape[0]:]
    else: return 'NaN'

#finds the linear regression of a data set
def findRegession(A, y):
    return np.dot(np.dot(findInverse(np.dot(np.transpose(A),A)),np.transpose(A)),y)

error = 1e-5

A =  np.matrix([[41, 62, 125],
                [71, 41, 45]], 'f')

print reduceMatrix(A)
