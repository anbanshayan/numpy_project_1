import numpy as np

#This will have some useful methods.
#This will use to display the data to some operations and plot our data or create new file name


class IntArray:
    def __init__(self,int_array):
        if not isinstance(int_array,np.ndarray) or int_array.dtype != int:
            raise ValueError("Input must be a NUMPY array of integers")

        self.int_array = int_array
    
    def display(self):
        print(self.int_array)

    def salary(self):
        array_shape = self.int_array.shape
        money_per_product = np.full(array_shape,7)
        salaries = self.int_array * money_per_product

        print(f"People made {self.int_array} products and this is their salaries {salaries}")