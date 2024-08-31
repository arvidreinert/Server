from setup import *
from rectangle import Rectangle
import pickle
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9000  # The port used by the server
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_s.connect((HOST, PORT))
#the rectangles position in the middle
def send_pos(rectobject):
    my_pos = rectobject.get_pos()
    my_pos = (my_pos[0],my_pos[1],rectobject.z_position)
    l = pickle.dumps(my_pos)
    server_s.sendall(l)

def get_others_players_pos():
    server_s.sendall(b"get_me_the_others_location")
    data = server_s.recv(1024)
    data = pickle.loads(data)
    return data

def statue(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*44,16*18,32,64)),True)
    statue.z_position = location[2]
    statue.set_size((50,100))
    return statue

def street_horizontal(location=(0,height/2,0),lenght=750):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_details.image_at((16*5,16*38,32,32)),True)
    statue.z_position = 10000000
    statue.set_size((lenght,200))
    return statue

def street_vertical(location=(0,height/2,0),lenght=750):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_details.image_at((16*7,16*38,32,32)),True)
    statue.z_position = 10000000
    statue.set_size((200,lenght))
    return statue

def street_curve_right_up(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_details.image_at((16*9,16*38,32,32)),True)
    statue.z_position = 10000000
    statue.set_size((200,200))
    return statue

def skyscraper(location=(0,height/2,0)):
    v = location[2]+100
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_houses.image_at((16*3,16*45,48,128)),True)
    statue.z_position = location[2]
    statue.set_size((150,310))
    return statue 

def cosy_shop(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_houses.image_at((16*2,16*62,65,80)),True)
    statue.z_position = location[2]
    statue.set_size((150,150))
    return statue 

def mini_house(location=(0,height/2,0)):
    v = location[2]-10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_houses.image_at((16*2,16*25,48,96)),True)
    statue.z_position = location[2]
    statue.set_size((100,200))
    return statue 

def house(location=(0,height/2,0)):
    v = location[2]-10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*32,16*18,48,64)),True)
    statue.z_position = location[2]
    statue.set_size((75,100))
    return statue

def tree(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*51,16*6,32,48)),True)
    statue.z_position = location[2]
    statue.set_size((100,125))
    return statue

def register_books(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_interiosrs.image_at((16*7,16*35,48,48)),True)
    statue.z_position = location[2]
    statue.set_size((200,200))
    return statue

pressed =False
my_sprite_sheet = SpriteSheet("16_p_tileset.png")
my_walks = SpriteSheet("Basic Charakter Spritesheet.png")
my_houses = SpriteSheet("BD001.png")
my_details = SpriteSheet("CP_V1.0.4.png")
my_interiosrs = SpriteSheet("Interiors_free_48x48.png")
walk_idle = [1]
for i in range(3):
    walk_idle.append(my_walks.image_at((50,50*(i+1),40,40)))
walk_back = [1]
for i in range(3):
    walk_back.append(my_walks.image_at((50*(i+1),50,40,40)))
walk_front = [1]
for i in range(3):
    walk_front.append(my_walks.image_at((50*(i+1),0,40,40)))
walk_left = [1]
for i in range(3):
    walk_left.append(my_walks.image_at((50*(i+1),100,40,40)))
walk_right = [1]
for i in range(3):
    walk_right.append(my_walks.image_at((50*(i+1),150,40,40)))

my_walk = walk_idle
p = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),"Basic Charakter Spritesheet.png")
p.set_image(walk_front[1],True)
p.set_size((100,100))
p.z_position = 0
my_sprites = {}
living_house = mini_house((width/2-200,height/2,85))
tanne = tree((width/2-100,height/2,40))
street1 = street_horizontal((width/2+450,height/2,-100),1500)
street2 = street_vertical((width/2-300,height/2,0),200)
players_house = skyscraper((width/2,height/2,100))
my_sprites["player_home_transp"] = players_house
my_sprites["street1"] = street1
my_sprites["tree1"] = tanne
my_sprites["street3"] = street_horizontal((width/2+450,height/2,100),1500)
my_sprites["stret2"] = street2
my_sprites["house1_transp"] = living_house
my_sprites["turn"] = street_curve_right_up((width/2-300,height/2,-100))
my_sprites["turn1"] = street_curve_right_up((width/2-400,height/2,100))
my_sprites["shop1"] = cosy_shop((width/2+100,height/2,300))
my_sprites["register"] = register_books((width/2-500,height/2,0))
my_sprites["p"] = p
my_out_world_sprites = my_sprites
my_shop1_sprites = {"p":p}
out_of_charakter = False
my_sprites["turn1"].set_rotation(-90)
#you have to summand y+(z+z:4)*-1
printing_row = []

def make_row(key):
    c = 0
    d = True
    while d:
        if my_sprites[key].z_position >= my_sprites[printing_row[c]].z_position:
            printing_row.insert(c,key)
            d = False
        else:
            if c <= len(printing_row)-2:
                c += 1
            else:
                d = False

    if my_sprites[key].z_position <= my_sprites[printing_row[len(printing_row)-1]].z_position and key not in printing_row:
            printing_row.append(key)

for key in my_sprites:
    if printing_row != []:
        make_row(key)
    else:
        printing_row.append(key)
    print(f"loading{key}")
print("sorted reaady")
counter = 0     

while True:
    if my_sprites != my_shop1_sprites:
        if p.get_colliding_with(my_sprites["shop1"]):
            if my_sprites["shop1"].get_point_collide(pygame.mouse.get_pos()):
                my_sprites = my_shop1_sprites
                printing_row = []
                my_sprites["regal"] = register_books((width/2-300,height/2,-100))
                for key in my_sprites:
                    if printing_row != []:
                        make_row(key)
                    else:
                        printing_row.append(key)
                    print(f"loading{key}")
                    print("sorted reaady")
    if my_sprites == my_out_world_sprites:
        pass
        #why is this bullshhit not fucking working???????
        #my_sprites["turn1"].set_rotation(-90)
    for key in my_sprites:
        if "transp" in key:
            if p.get_colliding_with(my_sprites[key]):
                if my_sprites["p"].z_position >= my_sprites[key].z_position:
                    my_sprites[key].set_transparency(30)
            else:
                my_sprites[key].set_transparency(255)
        else:
            my_sprites[key].set_transparency(255)

    if counter <= 4:
        counter += 1
    else:
        p.set_image(my_walk[my_walk[0]],True)
        if my_walk[0] <= 2:
            my_walk[0] += 1
        else:
            my_walk[0] = 1
        p.set_size((100,100))
        counter = 0

    clock.tick(30)
    if pressed != False:
        if pressed == "up":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,0.7)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0,0.7)
            if out_of_charakter == True:
                my_sprites["p"].change_position(0,1.4)
            else:
                my_sprites["p"].z_position += 0.7
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "down":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,-0.7)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0,-0.7)
            if out_of_charakter == True:
                my_sprites["p"].change_position(0,-1.4)
            else:
                my_sprites["p"].z_position -= 0.7
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "right":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(-0.7,0)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(-0.7,0)
            if out_of_charakter == True:
                my_sprites["p"].change_position(-1.4,0)

        if pressed == "left":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0.7,0)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0.7,0)
            if out_of_charakter == True:
                my_sprites["p"].change_position(1.4,0)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_walk = walk_back
                pressed = "up"
            elif event.key == pygame.K_DOWN:
                my_walk = walk_front
                pressed = "down"
            elif event.key == pygame.K_LEFT:
                my_walk = walk_left
                pressed = "left"
            elif event.key == pygame.K_RIGHT:
                my_walk = walk_right
                pressed = "right"
            elif event.key == pygame.K_SPACE:
                print(get_others_players_pos())
                if out_of_charakter == True:
                    out_of_charakter = False
                else:
                    out_of_charakter = True

        if event.type == pygame.KEYUP:
            my_walk = walk_idle
            pressed = False

    screen.fill((250,250,250))
    for key in printing_row:
        my_sprites[key].update(screen)
    pygame.display.update()