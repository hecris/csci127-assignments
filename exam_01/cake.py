def divide(A, B, u):
    return B * u // A

# to test the divide function
def my_print(A, B, u):
    print('{0} cakes of {1} slices, each person gets {2} slices'.format(u, B, A))
    print('you should invite ' + str(divide(A, B, u)) + ' people')

my_print(5, 10, 1)
my_print(2, 3, 2)
