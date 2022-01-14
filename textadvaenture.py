#### Projekt Mini Text-Adventure-Game ####
 
'''
import sys # Modul um Pfade neu zu definieren, damit das Programm weis woher es z.B. Ascii Arts nehmen soll. 
sys.path.append('/Users/melissa/Desktop/Pyhon/Resource') 
# Wenn die beiden Datein nicht im selben Ordner liegen, 
# sondern unter den Pfaden /Users/melissa/Desktop/Python/Resource, 
# muss man diesen Pfad angeben: sys.path.append('/Users/melissa/Desktop/Python/Resource') 

'''
# Lösungsweg 1: K (N) K (N) K (W)  w K (W) K (W) K (W) w K (O) K (N) w K (O) K (O)
# Lösungsweg 2: K (O) K (N) w K (S) w K (O) K (O)

#####AUSLAGERUNGEN########
# Das Modul importiert die Datei mit den ausgelagerten Bildern.
import sa_bild_in_text 
# Das Modul importiert die Datei mit dem ausgelagerten Text.
import sa_gametext 
# Für die Sekunden zwischen der Textanzeige.

###  Library ###
import time
# Für die Farben. 
import color

######## 1. Variablen Definition ###########


# Dictionary (Ansammlung von Key Value Paaren).
# Key: N S W O Möglichkeiten (als String).
# Value: Besuchten Orte,  Erfahrungsnotizen (je als String im Array).

# Orte mit Fundstücken werden in gelb angezeigt und tödliche Orte sind rot.
Orte = {

    # Anfangsrichtungen:
    "N"  : [color.CBLUE2 + color.CBOLD + "Du stehst vor einem großen Felsen mit einem Eingang zu einer tiefen Höhle." + color.CEND, ""], 
    "W"  : [color.CBLUE2 + color.CBOLD + "Hier ist ein langer, einsamer und wirklich traumhafter Strand aus weißem Puderzuckersand und das Wasser ist türkis-blau." + color.CEND, "" ],
    "S" :  [color.CYELLOW + color.CBOLD + "Dein kaputtes Schiffswrack ist hier gestrandet und du findest darin noch eine alte Flasche Piraten-Rum deiner früheren Besatzung." + color.CEND, "Rum" ],
    "O":   [color.CBLUE2 + color.CBOLD + "Hier geht es in den Dschungel." + color.CEND, "" ],

    # Weitere Fundstücke:  
    "NNW" :[color.CYELLOW + color.CBOLD + "Hier ist ein goldener Schatz. Nur mit dem passenden Schlüssel kann man ihn öffnen." + color.CEND, "Schatz" ],
    "WWW" :[color.CYELLOW + color.CBOLD + "Im Westen geht der Strand weiter, wo Du einen goldenen Schlüssel im Sand findest." + color.CEND, "Schluessel" ],
    "OO" : [color.CYELLOW + color.CBOLD + "Du stößt auf ein kleines Bambushütten-Dorf mit friedlichen Ureinwohnern. Für eine Gegenleistung sind sie bereit mit dir ein Boot zu bauen."  + color.CEND, "Ureinwohner"],
    "ON" :[color.CYELLOW + color.CBOLD + "Du findest unter einigen Büschen einen alten Werkzeugkasten." + color.CEND, "Werkzeugkasten" ],

   # tödliche Wege:
    "NNN" :[color.CRED2 + color.CBOLD + "Hier ist befindet sich eine riesige Schlange in der Höhle." + color.CEND, "Tod"],
    "NNO" :[color.CRED2 + color.CBOLD + "Dich beißt eine giftige Schlange in der Dunkelheit." + color.CEND, "Tod"],
    "ONN"  :[color.CRED2 + color.CBOLD + "Du befindest dich in einer Lichtung, dort liegt die Leiche von einem deiner Besatzungsmitglieder. Ein schwarzer Panther greift dich an." + color.CEND, "Tod" ],
    "OON": [color.CRED2 + color.CBOLD + "Der Dschungel wird immer dunkler und du siehst nicht mal mehr die Hand vor Augen, aus der Dunkelheit erscheint eine unheimliche Gestalt." + color.CEND, "Tod"],
    "OOW": [color.CRED2 + color.CBOLD + "Im Urwald verirrst du dich und du wirst von einer unbekannten Schlange gebissen." + color.CEND, "Tod"],
    "OOO": [color.CRED2 + color.CBOLD + "Im Urwald verirrst du dich und du wirst von einer unbekannten Schlange gebissen." + color.CEND, "Tod"],
    "SSS": [color.CRED2 + color.CBOLD + "Das Meer wird hier tiefer und dunkler, hier lauern gefährliche Haie. Ohne ein Boot, kannst du hier nicht lebend entlang!" + color.CEND, "Tod"],
    "SSWS":[color.CRED2 + color.CBOLD + "Das Meer wird hier tiefer und dunkler, die Strömung wird stärker und sie zieht dich in die Tiefe." + color.CEND, "Tod"],
    "SSOS":[color.CRED2 + color.CBOLD + "Das Meer wird hier tiefer und dunkler, hier lauern gefährliche Haie. Ohne ein Boot, kannst du hier nicht lebend entlang!" + color.CEND, "Tod"],
    "OOSS":[color.CRED2 + color.CBOLD + "Das Meer wird hier tiefer und dunkler, hier lauern gefährliche Haie. Ohne ein Boot, kannst du hier nicht lebend entlang!" + color.CEND, "Tod"],
    "WSS":[color.CRED2  + color.CBOLD + "Das Meer wird hier tiefer und dunkler, hier lauern gefährliche Haie. Ohne ein Boot, kannst du hier nicht lebend entlang!" + color.CEND, "Tod"],
    "WWWW":[color.CRED2 + color.CBOLD + "Du triffst auf unheimliche Kanibalen am Strand!" + color.CEND, "Tod"],
    "WWSS":[color.CRED2 + color.CBOLD + "Das Meer wird hier tiefer und dunkler, hier lauern gefährliche Haie. Ohne ein Boot, kannst du hier nicht lebend entlang!" + color.CEND, "Tod"],

 # Weitere normale Wege ohne Fundstücke:
    "NN" : [color.CBLUE2 + color.CBOLD + "Hier ist ein dunkler Weg durch die Höhle." + color.CEND, "" ],
    "NW" :[color.CBLUE2  + color.CBOLD + "Hier ist nichts außer einer langen und hohen Felsenwand." + color.CEND, "" ],
    "NNWN" :[color.CBLUE2 + color.CBOLD + "Hier ist nichts außer Dunkelheit und eine Felswand." + color.CEND, "" ],
    "WN" :[color.CBLUE2  + color.CBOLD + "Hier ist nichts außer einer langen und hohen Felsenwand." + color.CEND, "" ],
    "WW" : [color.CBLUE2 + color.CBOLD + "Hier ist weiterhin ein langer, malerischer Strand aus weißem Pudersand und das Wasser ist türkis-blau." + color.CEND, "" ],
    "WWS" :[color.CBLUE2 + color.CBOLD + "Das Wasser ist warm, klar und türkis-blau. Ansonsten ist hier nichts." + color.CEND, "" ],
    "WS" : [color.CBLUE2 + color.CBOLD + "Das Wasser ist warm, klar und türkis-blau. Ansonsten ist hier nichts." + color.CEND, "" ],
    "SS":  [color.CBLUE2 + color.CBOLD + "Das Wasser hinter dem Schiffswrack sieht herrlich blau und klar aus - hier kann man gut schwimmen." + color.CEND, ""],
    "SSW": [color.CBLUE2 + color.CBOLD + "Das Wasser hinter dem Schiffswrack sieht herrlich blau und klar aus - hier kann man gut schwimmen." + color.CEND, ""],
    "SSO": [color.CBLUE2 + color.CBOLD + "Das Wasser hinter dem Schiffswrack sieht herrlich blau und klar aus - hier kann man gut schwimmen." + color.CEND, ""],
    "SOS": [color.CBLUE2 + color.CBOLD + "Das Wasser hinter dem Schiffswrack sieht herrlich blau und klar aus - hier kann man gut schwimmen." + color.CEND, ""],
    "OOS": [color.CBLUE2 + color.CBOLD + "Hier ist nichts außer Palmen und Strand." + color.CEND, ""],
    "OOSW":[color.CBLUE2 + color.CBOLD + "Hier kann man gut schwimmen." + color.CEND, ""],
    "OOSO":[color.CBLUE2 + color.CBOLD + "Hier kann man gut schwimmen." + color.CEND, ""],
    "OOS": [color.CBLUE2 + color.CBOLD + "Du befindest dich im tiefsten Dschungel, hier findest du nichts außer Bäume und Insekten. " + color.CEND, ""],
   
     
}

#####Festlegung der Ende Möglichkeiten#####

#Wir müssen den Werkzeukasten finden um das Boot bauen zu können, den Schatz finden, einen Schlüssel finden um die Truhe zu öffnen, 
# die Ureinwohner finden und mit Gold bestechen damit sie uns beim Bootbau helfen um von der Insel heil zu entkommen.
Ende_1 =["Werkzeugkasten", "Schluessel", "Schatz", "Ureinwohner"] 

#Wir müssen den Werkzeugkasten und den Rum finden um die Ureinwohner abzufüllen, damit sie helfen das Boot zu bauen um von der Insel heil abzuhauen.
Ende_2 =["Werkzeugkasten", "Rum" , "Ureinwohner"] 



###Navigation####

# Navigation_Notiz als Liste um die Richtungen in N S W O zu notieren.
Navigation_Notiz=[] 

# Erfahrungsnotizen als Liste um die gesammelten Erfahrungen (Items) zu speichern.
Erfahrungsnotizen=[]



######## 2) Functionsdefinition ############

### Hier sind einige Funktionen deklariert. ###

def nach_dem_namen_fragen():  
    # \n in einem String ist eine neue Zeile. input speichert String in Variable Username.
    username = input(color.CBLUE + color.CBOLD + "Wie heißt Du ? \n" + color.CEND) 
    print()
    time.sleep(1)
    #.upper() Zugehörigkeit zu dem Username, um ihn groß zu schreiben.
    print (color.CBLUE + color.CBOLD + "Hallo Kapitän", username.upper(), "- Das Abenteuer möge beginnen!" + color.CEND)   
    print()
    time.sleep(1)

def nach_dem_weg_fragen():
    print (sa_bild_in_text.compass)
    auswahl_navigation = input(color.CBLUE + color.CBOLD + "Kompass: Du kannst nach (N)orden, (O)sten, (S)üden, (W)esten gehen, wo willst du hin ? : \n" + color.CEND)
    if auswahl_navigation == "N" or auswahl_navigation == "O" or auswahl_navigation =="S" or auswahl_navigation =="W":
        return auswahl_navigation
    else:
        return nach_dem_weg_fragen()    
  
def ein_schritt_zurueck():
    print ()
    print (color.CBEIGE + color.CBOLD +"Du bist wieder zurückgegangen" + color.CEND)
    print ()
    time.sleep(1)
        
def nach_dem_weg_fragen_und_erfahrung_notieren(): 
    
    weg = nach_dem_weg_fragen()

    global Erfahrungsnotizen
    global Navigation_Notiz
    global Orte
     
    # Wenn / Dann Möglichkeit 
    # Wir nehmen hier zurückgemachte Schritte nicht mit in die Liste (Navigation_Notiz) auf:
    # Mit .pop() entfernen wir den letzen Eintrag der Liste.
    if weg == "S" and len(Navigation_Notiz) >0 and Navigation_Notiz[-1] == "N":
        Navigation_Notiz.pop()
        ein_schritt_zurueck()

    elif weg == "N" and len(Navigation_Notiz) >0 and Navigation_Notiz[-1] == "S":
        Navigation_Notiz.pop()
        ein_schritt_zurueck()

    elif weg == "O" and len(Navigation_Notiz) >0 and Navigation_Notiz[-1] == "W":
        Navigation_Notiz.pop()
        ein_schritt_zurueck()

    elif weg == "W" and len(Navigation_Notiz) >0 and Navigation_Notiz[-1]== "O":
        Navigation_Notiz.pop()    
        ein_schritt_zurueck()

    # Ansonsten füge die zurückgelegte Richtung an die Navigation_Notiz hinzu mit .append
    else:
        Navigation_Notiz.append(weg)

    # mit "".join werden die Strings im Array Navigation_Notiz zusammen zu einem einzigen String gepackt.
    zusammengefasste_richtungen = "".join(Navigation_Notiz)
    print()
    # Dem User wird die zurückgelegte Richtung angezeigt.
    print( color.CBEIGE + color.CBOLD + "Du bist in diese Richtung gegangen : " + color.CEND, zusammengefasste_richtungen )
    print()
    time.sleep(1)

    # Boolean (Wenn / Dann) um Zustände zu erfassen und max. zurückgelegte Schritte festzulegen.
    if len(zusammengefasste_richtungen) > 5:
        if "Müde" not in Erfahrungsnotizen:
            # Bei mehr als 5 Orten wird man müde  (wenn "Müde" noch nicht in Erfahrung_Notiz ist)
            Erfahrungsnotizen.append("Müde")
    if len(zusammengefasste_richtungen) > 10:
        # Bei mehr als 10 Orten bekommt man Hunger  (wenn "Hunger" noch nicht in Erfahrung_Notiz ist)
        if "Hunger" not in Erfahrungsnotizen:
            Erfahrungsnotizen.append("Hunger")
    if len(zusammengefasste_richtungen) > 15:
        # Bei mehr als 15 Orten wird man verzweifelt (wenn "Verzwiflung" noch nicht in Erfahrung_Notiz ist)
        if "Verzweiflung" not in Erfahrungsnotizen:
            Erfahrungsnotizen.append("Verzweiflung")
    if len(zusammengefasste_richtungen) > 20:
        # Bei mehr als 20 Orten wird man sterben vor Erschöpfung (wenn "Tod" noch nicht in Erfahrung_Notiz ist ist Game Over!)
        if "Tod" not in Erfahrungsnotizen:
            Erfahrungsnotizen.append("Tod")
    
    if zusammengefasste_richtungen in Orte:
        # Mit Orte.get  holen wir den Value "Array" (Ortsbeschreibung ist unter Index [0]) aus dem Dictionary 
        print(Orte.get(zusammengefasste_richtungen)[0])
        # Mit Orte.get holen wir den Value "Array" (Erfahrung oder Items oder nichts  unter Index [1]) aus dem Dictionary 
        if Orte.get(zusammengefasste_richtungen)[1]:

            if "Müde" in Erfahrungsnotizen:
                Erfahrungsnotizen.remove("Müde")
            if "Hunger" in Erfahrungsnotizen:
                Erfahrungsnotizen.remove("Hunger")
            if "Verzweiflung" in Erfahrungsnotizen:
                Erfahrungsnotizen.remove("Verzweiflung")
            if "Tod" in Erfahrungsnotizen:
                Erfahrungsnotizen.remove("Tod")

            Erfahrungsnotizen.append(Orte.get(zusammengefasste_richtungen)[1])
            # list ist eine Methode um aus einem set eine norale Liste zu machen (returnen)
            Erfahrungsnotizen = list(set(Erfahrungsnotizen)) # set ist eine Methode und sie returnt Erfahrungswerte in ein unique array. 
    else:
        print(color.CBEIGE + color.CBOLD + "Hier ist nichts mehr zu finden." + color.CEND)
        print()
        time.sleep(1)

    weiter_fragen = erfahrungsnotize_schauen_und_weiter_fragen()
    return weiter_fragen

def erfahrungsnotize_schauen_und_weiter_fragen():
    global Erfahrungsnotizen
    global Ende_1
    global Ende_2
    print()
    time.sleep(1)

    print(color.CBEIGE + color.CBOLD + "Schauen wir doch mal in deine Erfahrungsnotize rein : " + color.CEND, Erfahrungsnotizen)
    weiter_fragen = True
    
    #Boolean (Wenn - Dann Möglichkeit)
    if "Tod" in Erfahrungsnotizen:
        print(sa_bild_in_text.skull)
        print ()
        time.sleep(1)
        print(color.CRED2 + color.CBOLD + "GAME OVER!" + color.CEND)
        print ()
        weiter_fragen = False

    elif erfahrungsnotiz_mit_ende_vergleichen(Ende_1):
        print(sa_bild_in_text.boat)
        print (color.CYELLOW + color.CBOLD + "GEWONNEN!\n" "Du hast es geschafft von der Insel heil zu entkommen. :) \nDu hast das Werkzeug und den Schatz gefunden und ihn mit dem goldenen Schlüssel geöffnet\nund die friedlichen Ureinwohner mit Gold bestochen dir beim Bootsbau zu helfen.\n"  + color.CEND)
        weiter_fragen = False
    elif erfahrungsnotiz_mit_ende_vergleichen(Ende_2):
        print(sa_bild_in_text.boat)
        print (color.CYELLOW  + color.CBOLD + "GEWONNEN!\n Wow! Du hast es super schnell geschafft von der Insel heil zu entkommen.\nDu hast das Werkzeug und den Rum gefunden um die Ureinwohner abzufüllen\ndamit sie dir beim Bootsbau helfen." + color.CEND)
        weiter_fragen = False
    else:
        print (color.CBEIGE + color.CBOLD + "Du hast noch nicht genügend Erfahrung gesammelt." + color.CEND) 

    return weiter_fragen

def erfahrungsnotiz_mit_ende_vergleichen(Ende):
    ergebnis = False
    
    global Erfahrungsnotizen

    #        ["Ureinwohner"] 
    #Ende_1 =["Schluessel", "Werkzeugkasten", "Piratensaebel", "Schatztruhe", "Ureinwohner", "Boot"] 

    # LOOP Schleife um die Erfahrungsnotizen mit der Erfahrung zu vergleichen
    for erfahrung in Ende:
        if erfahrung in Erfahrungsnotizen:
            ergebnis = True
        else:
            ergebnis = False
            # wenn ein Item nicht vorhanden ist, kann sofort ein False als Ergebnis ausgegeben werden damit wir nicht weiter vergleichen!
            
            return ergebnis 

    return ergebnis

def spiel_beenden():
    print(color.CBEIGE+ color.CBOLD + "Das Spiel wird beendet." + color.CEND)

def moeglichkeit_treffen():
    auswahl = input(color.CBEIGE + color.CBOLD + "Möchtest du die Insel mit dem (K)ompass erkunden, die bisherigen (E)rfahrungsnotizen anschauen,\ndie bisherige Notiz (w)egschmeissen und zurück zum Start oder das Spiel mit (Q)uit beenden? : \n " + color.CEND)
    # Die globale Variable Navigation_Notiz ansprechen.
    global Navigation_Notiz

    # Boolean (richtig/falsch / Wenn - Dann Möglichkeit festgelegt): 
    if auswahl == "E":
        if erfahrungsnotize_schauen_und_weiter_fragen():
            moeglichkeit_treffen() # Die Methode ruft sich selbst nochmal auf damit sie sich solange wiederholt.   
    # wenn die Aussage oben schon zutrifft, wird die Bedingung nicht weiter geprüft mit elif.   
    elif auswahl == "Q":  
        spiel_beenden()
    # wenn die Aussage oben schon zutrifft, wird die Bedingung nicht weiter geprüft mit elif.      
    elif auswahl == "K"  :
        if nach_dem_weg_fragen_und_erfahrung_notieren():
            moeglichkeit_treffen()
    elif auswahl == "w"  :
        Navigation_Notiz=[]
        print(color.CBEIGE + color.CBOLD + "Du bist zurueck zum Startpunkt am Strand und diese Navigationsnotiz brauchst du nicht mehr." + color.CEND)
        moeglichkeit_treffen()
    else:
        print (color.CBEIGE + color.CBOLD + "Du bist wohl noch etwas verwirrt. Bitte gib eine korrekte Auswahl ein. " + color.CEND)
        moeglichkeit_treffen()


######## 3. Functionsaufruf ############


print(sa_bild_in_text.island) #Methode um das Start-Bild anzuzeigen.
print()
time.sleep(1)
print(sa_gametext.intro) #Methode um das Intro anzuzeigen.
print()
time.sleep(1)
nach_dem_namen_fragen() # Methode aufrufen nach_dem_namen_fragen.
print()
time.sleep(1)
moeglichkeit_treffen()
