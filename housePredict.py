import pickle
import numpy as np

f = open("data_params.pkl","rb")
pickleListe = pickle.load(f)

#scan all indexes for numerical and categorical variables 
def findFeatures(pL):
    catList = []
    numList = []
    posDic = {}
    n=0
    for i in pL:
        idx = i[0]
        coe = i[1]
        posDic[idx] = n
        n +=1
    return posDic

numList = ['sqft_living', 'sqft_lot', 'sqft_above','sqft_basement', 'yr_built','sqft_living15', 'sqft_lot15']
catList = ["bedrooms","bathrooms","floors","view","condition","grade","zipcode","date"]


def catPosSearch(cat, inp):
    if cat == "date":
        return "date[T." + inp.strip() + "]"
    else:
        return "C(" + cat + ")[T." + inp + "]"

#please insert your data as below
print("date	\t10/13/2014")  
print("bedrooms\t3")
print("bathrooms \t1.0")	
print("sqft_living \t1180")	
print("sqft_lot \t5650")
print("floors \t\t1.0")
print("view	\t0.0")
print("condition \t3")	
print("grade \t\t7")
print("sqft_above \t1180")
print("sqft_basement \t0.0")
print("yr_built \t1955")
print("zipcode \t98178")
print("sqft_living15 \t1340")
print("sqft_lot15 \t5650")


inputVector = [0 for i in range(0, len(pickleListe))]
coefVector = [i[1] for i in pickleListe]

inputVector[0] = 1.0

posDic = findFeatures(pickleListe)

for i in (numList + catList):
    inp = input("Please insert the value for feature " + i+" : ")
    if i in numList:
        pos = posDic[i]
        inputVector[pos] = float(inp)
    else:
        s = catPosSearch(i, inp)
        if s in posDic and i != "date":
            pos = posDic[s]
            inputVector[pos] = 1.0
        elif s in posDic:
            pos = posDic[s]
            inputVector[pos] = 1.0


result = np.dot(coefVector, inputVector)


print('Predicted value:'+str(result))






