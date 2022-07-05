#import modułu; "pustego szablonu"
import pygame

# szerokość i wysokość okna gry
window = pygame.display.set_mode([800, 500])

# tytuł okna gry
pygame.display.set_caption("Paper, Stone, Scissors")

# wstawienie tła z pliku
tlo = pygame.image.load('tlo.jpg')

#tekst - inicjalizacja
pygame.font.init()

#import czcionki ("Nazwa rodziny czcionek", rozmiar czcionki)
font = pygame.font.SysFont("Calibri", 74)

#wpisanie tekstu (zmienna = [czcionka].render("Tekst", wygładzenie krawędzi jako True lub False, [r, g, b] - kolor czcionki)
text1 = font.render("Welcome to the game!", True, [102, 0, 51])
text2 = font.render("Give your name:", True, [102, 0, 51])

#ustawienie zmiennej logicznej
running = True

# pętla główna programu
while running:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.QUIT:
            running = False

    window.blit(tlo,(0, 0 ))
    pygame.display.update()
    #wyświetlenie tekstu [okno].blit([tekst], [x, y])
    window.blit(text1, [60, 200])
    #odświeżenie ekranu
    pygame.display.flip()
    #wyczyszczenie programu
    #win.fill((0, 0, 0))


#zakończenie zadania
pygame.quit()




