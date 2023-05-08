# --- TELA INICIAL (CURSES) --- 
import curses
import random

#Funções externas 
def main():
    
    #Inicialização do Curses (Tela Inicial)
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.beep()

    #Variaveis de Definição
    maximo_y, maximo_x = stdscr.getmaxyx() 
    y = maximo_y       #Valor da Altura (Max) = 51
    x = maximo_x         #Valor da Largura (Max) = 225

    #Definição de Pares de cores com o curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) #Verde
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE) #Branco
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN) #Preto
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_GREEN)  #Azul
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_GREEN)  #Vermelho
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_GREEN)  #Amarelo
    curses.init_pair(9, curses.COLOR_MAGENTA, curses.COLOR_GREEN)  #Magenta
    curses.init_pair(10, curses.COLOR_CYAN, curses.COLOR_GREEN)  #Ciano 
    curses.init_pair(11, curses.COLOR_CYAN, curses.COLOR_WHITE)

    #Define o tamanho da nova janela e sua cor de fundo
    newwin = curses.newwin(round(y/2), round(x/2), 0, 0)  
    newwin.bkgd(curses.color_pair(3))

    #Coloca os objetos na janela nescessaria
    newwin.clear()  
    newwin.box(curses.ACS_VLINE | curses.color_pair(1) , curses.ACS_HLINE | curses.color_pair(1))                              
    newwin.addstr(round(y/4) - 2,round(x/4) - 10,  "| LOGO TURTLE GAME |" , curses.color_pair(1))       #Cria o texto

    newwin.addstr(round(y/4) + 2,round(x/4) - 8,  "Pressione ESPAÇO" , curses.color_pair(1) | curses.A_BLINK)      #Cria o texto

    newwin.addstr(round(y/2) - 3, 1,  "2023, PythonOn.Inc" , curses.color_pair(1))      #Cria o texto
    newwin.refresh()
    newwin.keypad(True)

    #Espera o input (até então) do usuario 
    newwin.getch()
    curses.beep()

    # --- MENU ---

    #Definição do Menu
    itens_Do_Menu = ["|ESCOLHA SEU MODO DESEJADO|", "Modo Clássico", "Modo Sandbox", "Modo Snake", "Tutoriais", "Créditos", "Sair do Jogo" ]

    #O menu propriamente dito (usando Enumerate)
    newwin.box(curses.ACS_VLINE | curses.color_pair(3) , curses.ACS_HLINE | curses.color_pair(3))            # |               

    #Função que cria o menu (Depende da definição do Menu)    
    def expor_menu(newwin, selected_row_idx):
        newwin.clear()

        for idx, row in enumerate(itens_Do_Menu):      #OBS: (Idx é o termo selecionado no momento)
            x = maximo_x // 4 - len(row) // 2   
            y = maximo_y // 4 - len(itens_Do_Menu) // 2 + idx
            if idx == selected_row_idx:
                newwin.attron(curses.color_pair(2))
                newwin.addstr(y, x, row, curses.color_pair(2))
                newwin.attroff(curses.color_pair(2))
            else:
                newwin.addstr(y, x, row, curses.color_pair(1))
        newwin.refresh()
        return itens_Do_Menu[selected_row_idx]

    #Ativação do menu + Interação do usuario
    row_atual = 1
    opcao_escolhida = expor_menu(newwin, row_atual)
    expor_menu

    while 1:
            key = stdscr.getch()

            if key == ord('w') and row_atual > 1:
                row_atual -= 1
                expor_menu(newwin, row_atual)  # chamada da função para exibir o menu atualizado
            elif key == ord('s') and row_atual < len(itens_Do_Menu) - 1:
                row_atual += 1
                expor_menu(newwin, row_atual)  # chamada da função para exibir o menu atualizado
            elif key == curses.KEY_ENTER or key in [10, 13] or key == ord('d'):
                opcao_escolhida = expor_menu(newwin, row_atual)
                newwin.keypad(True)
                #If`s que definem o que cada opção faz
                #if row_atual == 1 and key == curses.KEY_ENTER or key in (10, 13):
                if opcao_escolhida == "Modo Clássico":
                    newwin.clear()                             
                    modo_classico()  
                    break
                if opcao_escolhida == "Modo Sandbox":
                    newwin.clear()
                    newwin.box(curses.ACS_VLINE | curses.color_pair(3) , curses.ACS_HLINE | curses.color_pair(3))                              
                    newwin.addstr(round(y/4) - 3,round(x/4) - 23,  "|Pressione o numero da cor que você deseja usar|" , curses.color_pair(1))
                    newwin.addstr(round(y/4) - 1,round(x/4) - 5,  "1-Verde" , curses.color_pair(1))
                    newwin.addstr(round(y/4) - 0,round(x/4) - 5,  "2-Ciano" , curses.color_pair(1))
                    newwin.addstr(round(y/4) + 1,round(x/4) - 5,  "3-Preto" , curses.color_pair(1))
                    newwin.addstr(round(y/4) + 2,round(x/4) - 5,  "4-Azul" , curses.color_pair(1))
                    newwin.addstr(round(y/4) + 3,round(x/4) - 5,  "5-Vermelho" , curses.color_pair(1))
                    newwin.addstr(round(y/4) + 4,round(x/4) - 5,  "6-Magenta" , curses.color_pair(1))
                    newwin.addstr(round(y/4) + 5,round(x/4) - 5,  "7-Amarelo" , curses.color_pair(1))
                    escolha_de_cor = newwin.getch()
                    if escolha_de_cor == ord("1"):
                        modo_sandbox(4)
                    elif escolha_de_cor == ord("2"):
                        modo_sandbox(10)
                    elif escolha_de_cor == ord("3"):
                        modo_sandbox(2)
                    elif escolha_de_cor == ord("4"):
                        modo_sandbox(6)
                    elif escolha_de_cor == ord("5"):
                        modo_sandbox(7)
                    elif escolha_de_cor == ord("6"):
                        modo_sandbox(9)
                    elif escolha_de_cor == ord("7"):
                        modo_sandbox(8)
                    else:
                        modo_sandbox(2)

                    newwin.refresh()
                    break
                if opcao_escolhida == "Modo Snake":
                    newwin.clear()
                    newwin.box(curses.ACS_VLINE | curses.color_pair(3) , curses.ACS_HLINE | curses.color_pair(3))                              
                    newwin.refresh()
                    newwin.clear
                    modo_snake()
                    newwin.refresh()
                    break
                if opcao_escolhida == "Tutoriais":
                    newwin.clear()
                    modo_tutoriais()
                    newwin.refresh()
                    
                    break
                if opcao_escolhida == "Créditos":
                    newwin.clear()
                    modo_creditos()
                    newwin.refresh()
                    break
                if opcao_escolhida == "Sair do Jogo":
                    newwin.clear()
                    quit()
                    newin.refresh()
                    break

            expor_menu(newwin, row_atual)  # chamada da função para exibir o menu atualizado

    newwin.refresh()
    newwin.keypad(True)

def modo_sandbox(cor_escolhida):
    # Configurações iniciais da janela
    screen = curses.initscr()

    #Definição de Pares de cores com o curses (Temporario pois já existe no outro código)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLUE)  #Azul
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_RED)  #Vermelho
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_YELLOW)  #Amarelo
    curses.init_pair(9, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)  #Magenta
    curses.init_pair(10, curses.COLOR_CYAN, curses.COLOR_CYAN)  #Ciano 


    # Continuação das Confirgurações iniciais da janela
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    screen_height, screen_width = screen.getmaxyx()
    
    win = curses.newwin(screen_height, screen_width, 0, 0)
    win.keypad(1)
    win.attrset(curses.color_pair(3))
    win.bkgd(curses.color_pair(3))
    win.box() #-----> Desenho da Box no jogo
    win.addstr(0,57,  "Desenhe! ----------- Pressione R para resetar e M para voltar ao Menu ----------- Mova com W A S D" , curses.color_pair(1))

    # Configurações iniciais da tartaruga
    turtle_x = screen_width // 2 
    turtle_y = screen_height // 2
    turtle_body = [[turtle_y, turtle_x], [turtle_y, turtle_x], [turtle_y, turtle_x]]
    turtle_direction = curses.KEY_RIGHT

    # Função que faz a tartaruga aparecer
    def tartaruga(cor_tartaruga,cor_rastro):
            for i, body_part in enumerate(turtle_body):
                if i == 0:
                    win.addch(body_part[0], body_part[1], curses.ACS_CKBOARD | curses.color_pair(cor_tartaruga))
                else:
                    win.addch(body_part[0], body_part[1], ' ', curses.color_pair(cor_rastro))

    # Loop principal do jogo
    box = curses.newwin(screen_height, screen_width, 0, 0)
    box.box()
    box.bkgd(curses.color_pair(5))

    while True:
        curses.curs_set(0)
        next_key = win.getch()
        if next_key == -1:
            continue
        elif next_key == ord("a") and turtle_direction != curses.KEY_RIGHT:
            turtle_direction = curses.KEY_LEFT
        elif next_key == ord("d") and turtle_direction != curses.KEY_LEFT:
            turtle_direction = curses.KEY_RIGHT
        elif next_key == ord("w") and turtle_direction != curses.KEY_DOWN:
            turtle_direction = curses.KEY_UP
        elif next_key == ord("s") and turtle_direction != curses.KEY_UP:
            turtle_direction = curses.KEY_DOWN
        elif next_key == ord("r"):
            win.clear()
            modo_sandbox(cor_escolhida)
        elif next_key == ord("m"):
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)
            box.clear()
            box.refresh()
            win.clear()
            win.refresh()
            box = curses.newwin(int(screen_height/2), int(screen_width/2), 0, 0)
            win= curses.newwin(int(screen_height/2), int(screen_width/2), 0, 0) 
            win.clear()
            box.clear()
            box.refresh()
            win.erase()
            box.erase()
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.endwin 
            main()
            
        else:
            continue

    # Move a tartaruga
        new_head = [turtle_body[0][0], turtle_body[0][1]]
        if turtle_direction == curses.KEY_LEFT:
            new_head[1] -= 1
        elif turtle_direction == curses.KEY_RIGHT:
            new_head[1] += 1
        elif turtle_direction == curses.KEY_UP:
            new_head[0] -= 1
        elif turtle_direction == curses.KEY_DOWN:
            new_head[0] += 1
        turtle_body.insert(0, new_head)

        # Verifica se a tartaruga colidiu com as bordas da tela
        if new_head[0] == 0 or new_head[0] == screen_height - 1 or new_head[1] == 0 or new_head[1] == screen_width - 1:
            curses.beep()
            curses.endwin()
            main()
            quit()

        tartaruga(5, cor_escolhida)
        #box.refresh()
        win.refresh()

def modo_snake(): 

    # Configurações iniciais da janela
    screen = curses.initscr()

    #Definição de Pares de cores com o curses (Temporario pois já existe no outro código)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Continuação das Confirgurações iniciais da janela
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    screen_height, screen_width = screen.getmaxyx()
    screen_height //= 4 
    screen_height += 1
    screen_width //= 4
    win = curses.newwin(screen_height, screen_width, 0, 0)
    win.keypad(1)
    win.attrset(curses.color_pair(3))
    win.bkgd(curses.color_pair(3))
    win.box() #-----> Desenho da Box no jogo
    win.attrset(curses.color_pair(2))

    # Configurações iniciais da tartaruga
    turtle_x = screen_width // 2
    turtle_y = screen_height // 2
    turtle_body = [[turtle_y, turtle_x], [turtle_y, turtle_x], [turtle_y, turtle_x]]
    turtle_direction = curses.KEY_RIGHT

    # Cria a comida aleatoriamente
    food = [random.randint(1, screen_height - 2), random.randint(1, screen_width - 2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    # Cria a janela de score e desenha a box
    score_win = curses.newwin(3, screen_width, screen_height, 0)
    score_win.box()

    # Loop principal do jogo
    score = 0
    win.addstr(0, 0,  "Score: {}".format(score) , curses.color_pair(2))
    box = curses.newwin(screen_height+5, screen_width+2, 0, 0)
    box.box()

    while True:
        curses.curs_set(0)
        win.attrset(curses.color_pair(3))
        next_key = win.getch()
        if next_key == -1:
            continue
        elif next_key == ord("a") and turtle_direction != curses.KEY_RIGHT:
            turtle_direction = curses.KEY_LEFT
        elif next_key == ord("d") and turtle_direction != curses.KEY_LEFT:
            turtle_direction = curses.KEY_RIGHT
        elif next_key == ord("w") and turtle_direction != curses.KEY_DOWN:
            turtle_direction = curses.KEY_UP
        elif next_key == ord("s") and turtle_direction != curses.KEY_UP:
            turtle_direction = curses.KEY_DOWN
        elif next_key == ord("m"):
            win.clear()
            win.refresh()
            box.clear()
            box.refresh()
            main()
        else:
            continue

    # Move a tartaruga
        new_head = [turtle_body[0][0], turtle_body[0][1]]
        if turtle_direction == curses.KEY_LEFT:
            new_head[1] -= 1
        elif turtle_direction == curses.KEY_RIGHT:
            new_head[1] += 1
        elif turtle_direction == curses.KEY_UP:
            new_head[0] -= 1
        elif turtle_direction == curses.KEY_DOWN:
            new_head[0] += 1
        turtle_body.insert(0, new_head)

        # Verifica se a tartatuga colidiu com o proprio corpo
        if new_head in turtle_body[1:]:
            curses.beep()
            curses.endwin()
            game_over()
            quit()

        # Verifica se a tartaruga colidiu com as bordas da tela
        if new_head[0] == 0 or new_head[0] == screen_height - 1 or new_head[1] == 0 or new_head[1] == screen_width - 1:
            curses.beep()
            curses.endwin()
            game_over()
            quit()

        # Verifica se a tartaruga comeu a comida
        if new_head == food:
            curses.beep()
            score += 1
            food = None
            while food is None:
                new_food = [random.randint(1, screen_height - 2), random.randint(1, screen_width - 2)]
                food = new_food if new_food not in turtle_body else None
            win.addch(food[0], food[1], curses.ACS_PI)
            win.attrset(curses.color_pair(2))
            win.addstr(0, 0, "Score: {}".format(score), curses.color_pair(2))
        
        else:
            tail = turtle_body.pop()
            win.addch(tail[0], tail[1], ' ')    
        
        # Desenha a tartaruga
        for i, body_part in enumerate(turtle_body):
            if i == 0:
                win.addch(body_part[0], body_part[1], curses.ACS_CKBOARD | curses.color_pair(5))
            else:
                win.addch(body_part[0], body_part[1], '*', curses.color_pair(1))

def modo_classico():
    
    screen = curses.initscr()
    
    # Configurações iniciais da janela
    curses.echo()
    curses.curs_set(1)
    
    # Inicia a cor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_GREEN, curses.COLOR_GREEN)

    #Criando janela
    altura, largura = screen.getmaxyx()
    janela_altura, janela_largura = altura-4, largura - 2
    window = curses.newwin(janela_altura, janela_largura,0, 0)
    window.border()
    window.refresh()
    
    #Posição da turtle
    y,x= altura//2, largura//2
    
    #criando a janela de comandos
    texto_y, texto_x = altura - 2, 2
    texto_largura = largura-6
    texto_janela = curses.newwin(1,texto_largura, texto_y,texto_x)
    texto_janela.clear()
    texto_janela.addstr(0,0,"Digite um comando: ",  curses.color_pair(1))
    texto_janela.refresh()

    while True:
        texto = texto_janela.getstr(0, len("Digite um comando: "), texto_largura).decode("utf-8")
        if texto.startswith("d "):
            try: 
                direction = texto.split(" ")[1]
                distance = int(texto.split(" ")[2])
                if direction == "o": 
                    if x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y,x-i,"*")
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            x-= 1
                            if x == 0:
                                x = janela_largura - 2
                            window.addstr(y,x, "@")
                            window.refresh()

                elif direction == "l":
                    if x + distance < janela_largura :
                        for i in range(distance):
                            window.addstr(y,x+i,"*")
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range (distance):
                            window.addstr(y,x,"*")
                            x += 1
                            if x == janela_largura - 1:
                                x = 1
                            window.addstr(y,x, "@")
                            window.refresh()

                if direction == "s":
                    if y + distance < janela_altura:
                        for i in range(distance):
                            window.addstr(y+i,x,"*")
                        y += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range (distance):
                            window.addstr(y,x,"*")
                            y += 1
                            if y == janela_altura:
                                y = 1
                            window.addstr(y,x, "@")
                            window.refresh()

                if direction == "n":
                    if y - distance >=0:
                        for i in range(distance):
                            window.addstr(y-i, x, "*")
                        y -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            y-= 1
                            if y == 0:
                                y = janela_altura - 1
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "ne":
                    if x + distance < janela_largura and y - distance >0:
                        for i in range(distance):
                            window.addstr(y-i, x+i, "*")
                        y -= distance
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            y -= 1
                            x += 1
                            if y == 0:
                                x= x + 1
                                y = janela_altura - 1
                            if x == janela_largura - 1:
                                x = 1 
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "se":
                    if  x + distance < janela_largura and  y + distance < janela_altura:  
                        for i in range(distance):
                            window.addstr(y+i, x+i, "*")
                        y += distance
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else: 
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            y += 1
                            x += 1
                            if y == janela_altura:
                                x = x - 1
                                y = 1
                            if x == janela_largura - 1:
                                x = 1
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "no":
                    if y - distance >=0 and x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y-i, x-i, "*")
                        y -= distance
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else: 
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            y -= 1
                            x -= 1
                            if y == 0:
                              x = x - 1 
                              y = janela_altura - 1
                            if x == 0 :
                                x = janela_largura - 2
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "so":
                    if y + distance < janela_altura and x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y+i, x-i, "*")
                        y += distance
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh() 
                    else: 
                        for i in range(distance):
                            window.addstr(y,x,"*")
                            y += 1
                            x -= 1
                            if y == janela_altura:
                                x = x - 1 
                                y = 1
                            if x == 0:
                                x = janela_largura - 2

                            window.addstr(y,x, "@")
                            window.refresh() 


            except:
                window.addstr(0,0, "Lembre de digitar um comando válido!", curses.A_REVERSE)
                window.refresh()
                
        if texto.startswith("b "):
            try: 
                direction = texto.split(" ")[1]
                distance = int(texto.split(" ")[2])
                if direction == "o": 
                    if x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y,x-i," ")
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x," ")
                            x-= 1
                            if x == 0:
                                x = janela_largura - 2
                            window.addstr(y,x, "@")
                            window.refresh()

                elif direction == "l":
                    if x + distance < janela_largura :
                        for i in range(distance):
                            window.addstr(y,x+i," ")
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range (distance):
                            window.addstr(y,x," ")
                            x += 1
                            if x == janela_largura - 1:
                                x = 1
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "s":
                    if y + distance < janela_altura:
                        for i in range(distance):
                            window.addstr(y+i,x," ")
                        y += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range (distance):
                            window.addstr(y,x," ")
                            y += 1
                            if y == janela_altura:
                                y = 1
                            window.addstr(y,x, "@")
                            window.refresh()
                
                if direction == "n":
                    if y - distance >=0:
                        for i in range(distance):
                            window.addstr(y-i, x, " ")
                        y -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x," ")
                            y-= 1
                            if y == 0:
                                y = janela_altura - 1
                            window.addstr(y,x, "@")
                            window.refresh()
                
                
                if direction == "ne":
                    if x + distance < janela_largura and y - distance >0:
                        for i in range(distance):
                            window.addstr(y-i, x+i, " ")
                        y -= distance
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else:
                        for i in range(distance):
                            window.addstr(y,x," ")
                            y -= 1
                            x += 1
                            if y == 0:
                                x= x + 1
                                y = janela_altura - 1
                            if x == janela_largura - 1:
                                x = 1 
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "se":
                    if  x + distance < janela_largura and  y + distance < janela_altura:  
                        for i in range(distance):
                            window.addstr(y+i, x+i, " ")
                        y += distance
                        x += distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else: 
                        for i in range(distance):
                            window.addstr(y,x," ")
                            y += 1
                            x += 1
                            if y == janela_altura:
                                x = x - 1
                                y = 1
                            if x == janela_largura - 1:
                                x = 1
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "no":
                    if y - distance >=0 and x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y-i, x-i, " ")
                        y -= distance
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh()
                    else: 
                        for i in range(distance):
                            window.addstr(y,x," ")
                            y -= 1
                            x -= 1
                            if y == 0:
                              x = x - 1 
                              y = janela_altura - 1
                            if x == 0 :
                                x = janela_largura - 2
                            window.addstr(y,x, "@")
                            window.refresh()
                if direction == "so":
                    if y + distance < janela_altura and x - distance >= 0:
                        for i in range(distance):
                            window.addstr(y+i, x-i, " ")
                        y += distance
                        x -= distance
                        window.addstr(y,x, "@")
                        window.refresh() 
                    else: 
                        for i in range(distance):
                            window.addstr(y,x," ")
                            y += 1
                            x -= 1
                            if y == janela_altura:
                                x = x - 1 
                                y = 1
                            if x == 0:
                                x = janela_largura - 2

                            window.addstr(y,x, "@")
                            window.refresh()    

            except:
                window.addstr(0,0, "Lembre de digitar um comando válido!", curses.A_REVERSE)
                window.refresh()

        if texto.startswith("sair"):
            window.clear()
            window.refresh()
            texto_janela.clear()
            texto_janela.refresh()
            main()
            break
        if texto.startswith("resetar"):
            window.clear()
            window.border()
            y,x = altura//2, largura//2
            window.addstr(y,x,"@")
            window.refresh() 

def modo_tutoriais():
    stdscr = curses.initscr()
    maximo_y, maximo_x = stdscr.getmaxyx() 
    y = maximo_y      
    x = maximo_x 
    newwin = curses.newwin(round(y/2), round(x/2), 0, 0)
    newwin.bkgd(curses.color_pair(3))
    newwin.box(curses.ACS_VLINE | curses.color_pair(3) , curses.ACS_HLINE)                              
    newwin.addstr(round(y/4) - 8, round(x/4) - 7, "Tutoriais", curses.color_pair(2))
    newwin.addstr(round(y/4) - 7,1,  "| Modo Clássico |" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 6,1 ,  "- Inicie o comando com 'd' para DESENHO,'b' para BORRACHA e'sair' para ir ao menu" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 5,1 ,  "- Após um espaçamento escolha a direção desejada entre as seguintes:" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 4,1 , "n (Norte), s (Sul), l (Leste), o (Oeste), ne (Nord.), no (Noro.), se (Sude.)..." , curses.color_pair(11))
    newwin.addstr(round(y/4) - 3,1 ,  "- Após mais um espaçamento indique a quantidade de passos que a tartaruga dará!" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 2,1 ,  "Exemplos:" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 1,1 ,  "Digite um comando: d ne 7 | Digite um comando: b s 11" , curses.color_pair(1))
    newwin.addstr(round(y/4) + 0,1 ,  "| Modo Sandbox |" , curses.color_pair(1))
    newwin.addstr(round(y/4) + 1,1 ,  "- Escolha a cor desejada como indicado e mova a tartaruga com W A S D " , curses.color_pair(1))
    newwin.addstr(round(y/4) + 2,1 ,  "| Modo Snake |" , curses.color_pair(1))
    newwin.addstr(round(y/4) + 3,1 ,  "- Mova a cobra com W A S D, coma as frutas e não colida a cobra!" , curses.color_pair(1))
    newwin.addstr(round(y/4) + 5,1 ,  "OBS: Pressione -->M<-- para retornar ao menu" , curses.color_pair(11))

    next_key = newwin.getch()
    if next_key == ord("m"):
        newwin.clear()
        newwin.refresh()
        main()
    curses.endwin()

def modo_creditos(): 
    stdscr = curses.initscr()
    maximo_y, maximo_x = stdscr.getmaxyx() 
    y = maximo_y       
    x = maximo_x 
    newwin = curses.newwin(round(y/2), round(x/2), 0, 0)  
    newwin.bkgd(curses.color_pair(3))
    newwin.box(curses.ACS_VLINE | curses.color_pair(3) , curses.ACS_HLINE | curses.color_pair(3))                              
    newwin.addstr(round(y/4) - 5, round(x/4) - 35, "Trabalho da Cadeira: Fundamentos de Programação. | Professor: Joabe | UPE")
    newwin.addstr(round(y/4) - 3,round(x/4) - 10,  "Bernardo Braga" , curses.color_pair(1)) 
    newwin.addstr(round(y/4) - 2,round(x/4) - 10,  "Giulia Buonafina" , curses.color_pair(1))
    newwin.addstr(round(y/4) - 1,round(x/4) - 10,  "Mateus Ribeiro" , curses.color_pair(1))

    next_key = newwin.getch()
    if next_key == ord("m"):
        newwin.clear()
        newwin.refresh()
        main()
    
    curses.endwin()

def game_over():
    stdscr = curses.initscr()

# Calcula as coordenadas da nova janela
    maximo_y, maximo_x = stdscr.getmaxyx()  
    y = maximo_y      
    x = maximo_x        
    curses.echo()

# Define cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) #Verde
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE) #Branco
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN) #Preto
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_GREEN)  #Azul
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_GREEN)  #Vermelho
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_GREEN)  #Amarelo
    curses.init_pair(9, curses.COLOR_MAGENTA, curses.COLOR_GREEN)  #Magenta
    curses.init_pair(10, curses.COLOR_CYAN, curses.COLOR_GREEN)  #Ciano
    curses.init_pair(11, curses.COLOR_CYAN, curses.COLOR_WHITE)

    #Define o tamanho da tela
    newwin = curses.newwin(round(y/2), round(x/2), 0, 0)  
    newwin.keypad(True)
    newwin.bkgd(curses.color_pair(3))

    # Escreve "game over" na nova janela
    newwin.addstr(round(y/4) -2 , round(x/4)-6, "Game Over", curses.color_pair(2))
    newwin.addstr(round(y/4) -1 , round(x/4) -17,  "Pressione M para voltar para o Menu", curses.color_pair(1)) 
    
    while True:
        next_key = newwin.getch()
        if next_key == ord("m"):
            newwin.clear()
            newwin.refresh()
            main()
            break
    
    newwin.refresh()
    curses.endwin()

main()

