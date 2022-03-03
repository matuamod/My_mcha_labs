import math

A = []
B = []
res = []
b = []
d = []

print()
a = int(input("Enter number of rows : ")) 
c = int(input("Enter number of colums : "))

def Get_Matrix_A_b(_A, _B, _a, _c, _b, _d, _res):
    print("\nEnter all elements of matrix\n")
    for i in range(_a):
        _A.append([])
        _B.append([])
        for j in range(_c):
            _A[i].append(float(input()))
            _B[i].append(_A[i][j])
        _b.append(float(input()))
        _d.append(_b[i])
        res.append(0.0)
    
    print("\nOriginal Matrix A : \n")
    Print_Res_Matrix(_A, _b)

    return _A, _B, _b, _d, _res

def Calculated_A(_A, _B, _b, _d, _res):
    for i in range(len(_A)):
        for j in range(len(_A[i])):
            _A[i][j] = _B[i][j]
        _b[i] = _d[i]
        _res[i] = 0.0

    return _A, _b, _res

def Transformed_A(_A, _b):
    for i in range(len(_A)):
        for j in range(i + 1, len(_A[i])):
            tmp = _A[j][i] / _A[i][i]
            _b[j] -= tmp * _b[i]
            _A[j][i] = 0
            for m in range(i + 1, len(_A[i])):
                _A[j][m] -= tmp * _A[i][m]

    return _A, _b
        
def Final_Solution(_A, _b, _res):
    for i in reversed(range(len(_A))):
        for j in range(i, len(_A[i])):
            if j == len(_A[i]) - 1:
                break
            else:
                _b[i] -= _A[i][j + 1] * _res[j + 1]
        _res[i] = _b[i] / _A[i][i]

    print("The final solution of method is : \n")

    for i in range(len(_res)):
        print(round(_res[i], 4), end= '  ')
    print("\n\n")

    return _A, _b, _res

def Main_Column_Elem(_A, _b):
    for i in range(len(_A)):
        max_index = i
        max_value = _A[i][i]
        for j in range(i + 1, len(_A)):
            if math.fabs(max_value) < math.fabs(_A[j][i]):
                max_index = j
                max_value = _A[j][i]

        #Changing rows

        if i != max_index:
            _b[i], _b[max_index] = _b[max_index], _b[i]
            for m in range(i, len(_A[i])):
                _A[i][m], _A[max_index][m] = _A[max_index][m], _A[i][m]

        for j in range(i + 1, len(_A[i])):
            tmp = _A[j][i] / _A[i][i]
            _b[j] -= tmp * _b[i]
            _A[j][i] = 0
            for m in range(i + 1, len(_A[i])):
                _A[j][m] -= tmp * _A[i][m]

    print("Matrix A after transformation : \n")
    Print_Res_Matrix(_A, _b)

    return _A, _b

def Main_Matrix_Elem(_A, _b):
    for i in range(len(_A)):
        max_index = i
        max_value = _A[i][i]
        for j in range(i, len(_A)):
            for m in range(i, len(_A[i])):
                if math.fabs(max_value) < math.fabs(_A[j][m]):
                    max_index = j
                    max_value = _A[j][m]
                
        #Changing rows

        if i != max_index:
            _b[i], _b[max_index] = _b[max_index], _b[i]
            for l in range(len(_A[i])):
                _A[i][l], _A[max_index][l] = _A[max_index][l], _A[i][l]

        for j in range(i + 1, len(_A[i])):
            tmp = _A[j][i] / _A[i][i]
            _b[j] -= tmp * _b[i]
            _A[j][i] = 0
            for m in range(i + 1, len(_A[i])):
                _A[j][m] -= tmp * _A[i][m]

    print("Matrix A after transformation : \n")
    Print_Res_Matrix(_A, _b)

    return _A, _b

def Print_Res_Matrix(_A, _b):
    for i in range(len(_A)):
        for j in range(len(_A[i])):
            print("{:.4f}".format(_A[i][j]), end= '  ')
        print(" | ", "{:.4f}".format(_b[i]))

    print("\n")

#First method of solving - Gauss method
print("First method of solving - Gauss method : ")

A, B, b, d, res = Get_Matrix_A_b(A, B, a, c, b, d, res)

A, b = Transformed_A(A, b)

Print_Res_Matrix(A, b)

A, b, res = Final_Solution(A, b, res)

#Second method of solving by searching the main element of matrix in column
print("Second method of solving by searching the main element of matrix in column : ")

A, b, res = Calculated_A(A, B, b, d, res)

A, b = Main_Column_Elem(A, b)

A, b, res = Final_Solution(A, b, res)

#Third method of solving by searching the main element of matrix
print("Third method of solving by searching the main element of matrix : ")

A, b, res = Calculated_A(A, B, b, d, res)

A, b = Main_Matrix_Elem(A, b)

A, b, res = Final_Solution(A, b, res)