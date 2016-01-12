from random import *

def new_game(L_1, L_2, L_3, L_4):
    global Locations, l_mark, t_mark, r_mark, b_mark, Loc_Marks, N
    E = ' '
    l_mark = [E, E, E, E, E, E, E, E]
    r_mark = [E, E, E, E, E, E, E, E]
    t_mark = [E, E, E, E, E, E, E, E]
    b_mark = [E, E, E, E, E, E, E, E]
    Locations = [L_1, L_2, L_3, L_4]
    Loc_Marks = []
    N = 0

def one_step(current_P): # ((row, column), direction)
    (r, c), direction = current_P
    global Locations
    Obstacle = {'b': [(r - 1, c), (r - 1, c - 1), (r - 1, c + 1)],
                't': [(r + 1, c), (r + 1, c - 1), (r + 1, c + 1)],
                'l': [(r, c + 1), (r + 1, c + 1), (r - 1, c + 1)],
                'r': [(r, c - 1), (r + 1, c - 1), (r - 1, c - 1)]}
    Next = {'b': [(r - 1, c), 'l', 'r'],
            't': [(r + 1, c), 'l', 'r'],
            'l': [(r, c + 1), 'b', 't'],
            'r': [(r, c - 1), 'b', 't']}
    
    if Obstacle[direction][0] in Locations:
        return None
    for i in [1, 2]:
        if Obstacle[direction][i] in Locations:
            return (r, c), Next[direction][i]
    return Next[direction][0], direction

def shoot(entry):
    x, direction = int(entry[0]) - 1, entry[1]
    Starts = {'l': (x, -1), 'r': (x, 8), 't':(-1, x), 'b':(8, x)}
    position = Starts[direction], direction
    position = one_step(position)
    if position == None:
        return None
    if position[1] != direction:
        return entry
    while position != None:
        if position[0][1] == -1:
            return str(position[0][0] + 1) + 'l'
        if position[0][1] == 8:
            return str(position[0][0] + 1) + 'r'
        if position[0][0] == -1:
            return str(position[0][1] + 1) + 't'
        if position[0][0] == 8:
            return str(position[0][1] + 1) + 'b'
        position = one_step(position)
    return None

def mark(entry):
    global l_mark, t_mark, r_mark, b_mark, N
    Marks = {'l':l_mark, 't':t_mark, 'r':r_mark, 'b':b_mark}
    out = shoot(entry)
    if out == None:
        Marks[entry[1]][int(entry[0]) - 1] = 'H'
    elif out == entry:
        Marks[entry[1]][int(entry[0]) - 1] = 'R'
    elif out != entry:
        Marks[entry[1]][int(entry[0]) - 1] = chr(ord('a') + N)
        Marks[out[1]][int(out[0]) - 1] = chr(ord('a') + N)
        N += 1   
        
def toggle(row, column):
    global Loc_Marks
    if (row - 1, column - 1) in Loc_Marks:
        Loc_Marks.remove((row - 1, column - 1))
    else:
        Loc_Marks.append((row - 1, column - 1))

def score():
    global Locations, l_mark, t_mark, r_mark, b_mark, Loc_Marks
    score = 100
    for i in l_mark + t_mark + r_mark + b_mark:
        if i != ' ':
            score -= 1
    for i in Locations:
        if i not in Loc_Marks:
            score -= 10
    for i in Loc_Marks:
        if i not in Locations:
            score -= 10
    return score

def print_game():
    global Locations, l_mark, t_mark, r_mark, b_mark, Loc_Marks
    print("     1 2 3 4 5 6 7 8")
    print("    ", ' '.join(t_mark))
    print("    ------------------")
    ch = "1"
    for i in range(0, 8):
        print(ch, l_mark[i], "|", end='')
        for j in range(0, 8):
            if (i, j) not in Loc_Marks:
                print('-', end = ' ') 
            else:
                print('*', end = ' ')
        print("|", r_mark[i], ch)
        ch = chr(ord(ch) + 1)
    print("    ------------------")
    print("    ", ' '.join(b_mark))
    print("     1 2 3 4 5 6 7 8")
    print()

def print_instructions():
    print()
    print("To make a shoot:")
    print("Enter a number 1 to 8, followed by a letter L for left,")
    print("R for right, T for top, and B for bottom.")
    print("To mark or unmark where you think an atom may be:")
    print("Enter a row number followed by a column number")
    print("To finish the game:")
    print('Please enter "finish"')
    print()

def start():
    global Loc_Marks, Locations, l_mark, t_mark, r_mark, b_mark, N
    R = [0, 1, 2, 3, 4, 5, 6, 7]
    while True:
        L_1, L_2, L_3, L_4 = 0, 0, 0, 0
        while len({L_1, L_2, L_3, L_4}) != 4:
            L_1, L_2 = (choice(R), choice(R)), (choice(R), choice(R)) 
            L_3, L_4 = (choice(R), choice(R)), (choice(R), choice(R))
        new_game(L_1, L_2, L_3, L_4)
        while True:       
            print_game()
            print_instructions()
            Move = ''.join(input().split()).lower()
            if Move == 'finish':
                print("Your score is:")
                print(score())
                Loc_Marks = Locations
                print("The correct solution is:")
                print_game()
                break
            elif Move[0] in '12345678' and Move[1] in 'rltb':
                mark(Move)
            elif Move[0] in '12345678' and Move[1] in '12345678':
                toggle(int(Move[0]), int(Move[1]))
            else:
                print('Input not legal, please try again.\n')
        M = input("Do you want another round? Yes/No\n")
        if M.lower() == 'no':
            break

if __name__ == "__main__":
    start()
            
