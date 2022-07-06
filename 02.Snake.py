#import modułu; "pustego szablonu"
import pygame

#import modułu liczb pseudolosowych
import random

# szerokość i wysokość okna gry
window = pygame.display.set_mode([600, 400])

# tytuł okna gry
pygame.display.set_caption("Snake")

#kolor tła zapisany w tupli
tlo = (224, 224, 224)

#tekst - inicjalizacja
pygame.font.init()

#import czcionki ("Nazwa rodziny czcionek", rozmiar czcionki)
font1 = pygame.font.SysFont("Calibri", 60)
font2 = pygame.font.SysFont("Calibri", 30)
font3 = pygame.font.SysFont("Calibri", 15)

#wpisanie tekstu (zmienna = [czcionka].render("Tekst", wygładzenie krawędzi jako True lub False, [r, g, b] - kolor czcionki)
text1 = font1.render("Welcome to the game!", True, [102, 0, 51])
text2 = font2.render("Press SPACE to start", True, [102, 0, 51])

#zmienne do rysowania obiektu
x = 300
y = 200
szerokosc = 20
wysokosc = 20
krok = 20
run = 0
w = random.randrange(0, 580, 20)
z = random.randrange(0, 380, 20)
wszerokosc = 20
zwysokosc = 20
wynik = 0

#ustawienie zmiennej logicznej
running = True

# pętla główna programu
while running:

    # opóźnienie w grze
    pygame.time.delay(50)

    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.QUIT:
            running = False

    #okno początkowe
    if run == 0:
        window.fill(tlo)
        window.blit(text1, [25, 140])
        window.blit(text2, [170, 250])
        pygame.display.update()

    #przejście z okna początkowego do gry - naciśnięcie spacji
    #włączenie obsługi zdarzeń
    start = pygame.key.get_pressed()
    # warunki do przejścia do okna gry
    if start[pygame.K_SPACE] :
        run += 1

    #okno gry
    if run >= 1:
        #włączenie obsługi zdarzeń
        keys = pygame.key.get_pressed()
        # warunki do zmiany pozycji obiektu
        if keys[pygame.K_LEFT] :
            x -= krok
        if keys[pygame.K_RIGHT] :
            x += krok
        if keys[pygame.K_UP] :
            y -= krok
        if keys[pygame.K_DOWN] :
            y += krok

        #blokada okna - aby wąż nie wychodził poza obraz okna
        if x < 0:
            x = 0
        elif x > 580:
            x = 580
        elif y < 0:
            y = 0
        elif y > 380:
            y = 380

        #czyszczenie ekranu
        window.fill(tlo)

        #prezentacja wyniku
        label = font3.render('Wynik: ' + str(wynik), True, (0, 0, 0))
        window.blit(label, [0, 0])

        #rysowanie prostąkąta
        pygame.draw.rect(window, (0, 0, 0), (x, y, szerokosc, wysokosc))
        pygame.draw.rect(window, (255, 0,0), (w, z, wszerokosc, zwysokosc))

        #odświeżanie ekranu
        pygame.display.update()

        if x == w and y == z:
            wynik += 1
            w = random.randrange(0, 580, 20)
            z = random.randrange(0, 380, 20)

#zakończenie zadania
pygame.quit()
