def who_is_winner(pieces_position_list):
    # Your code here!
    columns = [[0] * 6 for _ in range(7)]
    lengths = [0]  * 7
    edge = ord("A")
    for piece in pieces_position_list:
        column, color = piece.split("_")
        column = ord(column) - edge
        columns[column][lengths[column]] = color
        if control(columns, column, lengths[column], color):
            print_table(columns)

            return color
        lengths[column] += 1
    print_table(columns)
    return "Draw"

        
def control(table, column, row , color):
    count = 4
    for x in range(6):
        if table[column][x] == color:
            count -= 1
            if count == 0:
                print("column", column, "xrow", row, "color", color)
                return True
        else:
            count = 4
    count = 4
    for x in range(7):
            if table[x][row] == color:
                count -= 1
                print("ycolumn", x, "row", row, "color", end="|" )
                if count == 0:
                    print("xcolumn", column, "row", row, "color", color)
                    
                    return True
            else:
                print("")
                count = 4
    return False

def print_table(table):
    print( " ".join([chr(i+ord("A")) for i in range(7)]))
    for j in range(6):
        for i in range(7):
            if table[i][j] != 0:
                print(table[i][j][0], end=" ")
            else:
                print( table[i][j], end=" ")
        print(" ")
        
print(who_is_winner([ 
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]))