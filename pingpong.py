from pygame import*
# oyun penceresinin oluşturulması
pencere = display.set_mode((600,500))
#pencere arka plan rengi RGB kod
pencere.fill((200,255,255))
game = True
FPS = 60
clock = time.Clock()
while game:
    # Eğer çarpı işaretine basılırsa pencereyi kapa
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)