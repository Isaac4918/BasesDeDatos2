def obtener_lineas_letra(letra, frase):
    lineas = letra.split('\n')
    lineas_coincidentes = []
    primera_coincidencia = False

    for linea in lineas:
        for palabra in frase.split():
            if palabra.lower() in linea.lower():
                lineas_coincidentes.append(linea)
                primera_coincidencia = True
                break

        if primera_coincidencia:
            lineas_coincidentes.append(linea)
            if len(lineas_coincidentes) == 4:
                break

    return lineas_coincidentes[:4]

# Ejemplo de uso
letra_cancion = "Parte1\nDaddy's flown across the ocean\nLeaving just a memory\nSnapshot in the family album\nDaddy what else did you leave for me?\nDaddy, what'd'ja leave behind for me?!?\nAll in all it was just a brick in the wall.\nAll in all it was all just bricks in the wall.\n\n\"You! Yes, you behind the bikesheds, stand still lady!\"\n\nWhen we grew up and went to school\nThere were certain teachers who would\nHurt the children in any way they could\n(oof!)\nBy pouring their derision\nUpon anything we did\nAnd exposing every weakness\nHowever carefully hidden by the kids\nBut in the town it was well known\nWhen they got home at night, their fat and\nPsychopathic wives would thrash them\nWithin inches of their lives.\n\nParte 2\n\nWe don't need no education\nWe dont need no thought control\nNo dark sarcasm in the classroom\nTeachers leave them kids alone\nHey! Teachers! Leave them kids alone!\nAll in all it's just another brick in the wall.\nAll in all you're just another brick in the wall.\n\nWe don't need no education\nWe don't need no thought control\nNo dark sarcasm in the classroom\nTeachers leave us kids alone\nHey! Teachers! Leave us kids alone!\nAll in all it's just another brick in the wall.\nAll in all you're just another brick in the wall.\n\n\"Wrong, Guess again! 2x\nIf you don't eat yer meat, you can't have any pudding.\nHow can you have any pudding if you don't eat yer meat?\nYou! Yes, you behind the bikesheds, stand still laddie!\"\n\nParte 3\n\nI don't need no arms around me\nAnd I don't need no drugs to calm me\nI have seen the writing on the wall\nDon't think I need anything at all\n\nNo! Don't think I'll need anything at all\nAll in all it was all just bricks in the wall.\nAll in all you were all just bricks in the wall."

frase_busqueda = 'Leave us kids alone'

resultado = obtener_lineas_letra(letra_cancion, frase_busqueda)
for linea in resultado:
    print(linea)