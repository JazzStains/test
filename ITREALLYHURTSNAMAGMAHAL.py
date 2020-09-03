import pyautogui
import time

#pip install pyautogui to work

comments = ["Kay sakit naman isipin na","Sa puso mo ako'y pangalawa","Sa tuwing makikita kitang kasama siya","Pinipikit ko ang aking mga mata","At sa gabing kasama mo siya","Halos hindi ako makahinga","Kayakap ko ang bote ng tequila","Nagmumukmok sa ibabaw ng lamesa","Naghihintay hanggang sumapit ang umaga","Nang muli kang makasama","Ano ating lagay, hindi mapalagay","Ako'y nasasaktan 'pag hawak mo kanyang kamay","Sa kanya ka sa tanghali, akin ka sa gabi","'Pag dilat sa umaga, yo, wala ka na sa tabi","Merong kahati, gusto kita na mapasa'kin","Kung pwede lang ba sana sa kanya kita nakawin","At lagi mong iisipin, kung hindi ka para sa 'kin","Huwag mo lang kakalimutin na ika'y mahal pa rin"]

time.sleep(5)
for i in range(50): #number inside is how many comments you want to write
    pyautogui.typewrite(comments[i%18])
    pyautogui.typewrite("\n")
    time.sleep(2)
