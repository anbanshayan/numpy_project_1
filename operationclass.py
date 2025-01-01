import numpy as np
import matplotlib.pyplot as plt

#This will have some useful methods.
#This will use to display the data to some operations and plot our data or create new file name

def productivity_of_company(order,data_frame):
    
    num_products = 0
    for element in data_frame[order]:
        num_products += element

    return num_products
    
def max_productivity(data_frame):
    i = 0
    best_company = i + 1

    num_of_products = 0
     
    for i in range (len(data_frame)):
        result = productivity_of_company(i,data_frame)

        if result>num_of_products:
            num_of_products = result
            best_company = i +1

    print(f"The best company is the {best_company}. company with {num_of_products}")


def min_productivity(data_frame):
    i = 0
    worst_company = i +1
    num_of_products = productivity_of_company(0,data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i,data_frame)
        if result <= num_of_products:
            num_of_products = result
            worst_company = i+1

    print(f"The worst company is the {worst_company}. company with {num_of_products} products made.")

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

    def show_data(self):
        x =np.arange(len(self.int_array))
        plt.plot(x,self.int_array,marker='o')
        plt.title("Productivity of Employee")
        plt.xlabel('Rank of employee')
        plt.ylabel('Products/month')
        # plt.xticks()
        plt.grid()
        plt.show()