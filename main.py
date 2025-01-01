import numpy as np
from operationclass import IntArray
from operationclass import min_productivity,max_productivity

#first 'from nameoffile' then 'import nameofclass'

def file_handling():
    lines = []

    with open('company.txt','r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val)for val in values]
            lines.append(int_values)

        data_frame = np.array([np.array(row) for row in lines], dtype = int)

        return data_frame
def main():
    data_frame = file_handling()

    print(data_frame)
    print(type(data_frame))


    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()

    max_productivity(data_frame)
    min_productivity(data_frame)

main()

