#Micah Kennedy
#Pd 1-2

#Two By Two Grid
def draw_grid():
    def draw_horiz():
        print('+', '- ' * 4, '+', '- ' * 4, '+')
    def draw_vert():
        print('|', ' ' * 8, '|', ' ' * 8, '|')
    draw_horiz()
    for i in range(4):
        draw_vert()
    draw_horiz()
    for i in range(4):
        draw_vert()
    draw_horiz()
draw_grid()

#4 by 4 grid
def draw_sec_grid():
    def draw_horiz():
        print('+', ('- ' * 4 + '+') * 4)
    def draw_vert():
        print('|', (' ' * 8 + '|') * 4)
    for i in range(4):
        draw_horiz()
        for i in range(4):
            draw_vert()
    draw_horiz()
draw_sec_grid()
