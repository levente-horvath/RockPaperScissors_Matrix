import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"""
1: kő
2: papír
3: olló
"""
stone_img = mpimg.imread('stone.png')
paper_img = mpimg.imread('paper.png')
scissors_img = mpimg.imread('scissors.png')


def fight(a, b):
    # papír > kő
    if a == 1 and b == 2:
        return b
    
    if a == 2 and b == 1:
        return a
    
    # kő > olló
    if a == 1 and b == 3:
        return a 
    
    if a == 3 and b == 1:
        return b


    # olló > papir
    if a == 2 and b == 3:
        return b

    if a == 3 and b == 2:
        return a
 


matrix = np.random.randint(1, 4, size=(10, 10))
sor_len = len(matrix)
oszlop_len = len(matrix[0])

#print(matrix)

changing_positions = []

def check_positions(i, j, matrix):

    def not_in(i, j):
        for pos in changing_positions:
            if(pos[0] == (i,j)):
                return False
            if(pos[1] == (i,j)):
                return False

        return True

    if not_in(i,j) and j+1 < oszlop_len:
        if matrix[i][j] != matrix[i][j+1]:
            changing_positions.append( ((i,j), (i,j+1)) )
            return 0

    if not_in(i,j) and i+1 < sor_len:
        if matrix[i][j] != matrix[i+1][j]:
            changing_positions.append( ((i,j), (i+1,j)) )
            return 0
    
    

print("0. Generation")
print(matrix)


def simulation_loop(sim_len):

    for gen in range(sim_len):

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                check_positions(i, j, matrix)

        new_m = matrix.copy()
        for pos in changing_positions:
            c_value = fight(matrix[pos[0][0]][pos[0][1]], matrix[pos[1][0]][pos[1][1]])

            new_m[pos[0][0]][pos[0][1]] = c_value
            new_m[pos[1][0]][pos[1][1]] = c_value

        print("\n")
        print(f"{gen+1}. Generation")
        print(new_m)


        """
        def plot_icon(ax, x, y, value):
            if value == 1:
                ax.imshow(stone_img, extent=(x, x+1, y, y+1))
            elif value == 2:
                ax.imshow(paper_img, extent=(x, x+1, y, y+1))
            elif value == 3:
                ax.imshow(scissors_img, extent=(x, x+1, y, y+1))

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.axis('off')

        for i in range(10):
            for j in range(10):
                plot_icon(ax, j, 10-i-1, new_m[i, j])

        plt.savefig(f'{gen}_generacio.png')  # Saves the plot as a PNG file
        """

        matrix[:] = new_m.copy()
        changing_positions[:] = []


simulation_loop(12)