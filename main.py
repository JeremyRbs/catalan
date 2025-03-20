import random

# Dictionnaire des mots français et leur traduction en catalan
dictionnaire_verbes_francais_catalan = {
    'être': 'ser/ésser',
    'avoir': 'haver',
    'tenir': 'tenir',
    'venir': 'venir',
    'aller': 'anar',
    'donner': 'donar',
    'voir': 'veure',
    'savoir': 'saber',
    'devoir': 'deure',
    'pouvoir': 'poder',
    'vouloir': 'voler',
    'croire': 'creure',
    'faire': 'fer',
    'dire': 'dir',
    'sortir': 'sortir',
    'vivre': 'viure',
    'mériter': 'meréixer',
    'boire': 'beure',
    'fuir': 'fugir',
    'cuisiner': 'coure',
    'tenir (s’adapter)': 'cabre',
    'maintenir': 'mantenir',
    'courir': 'Córrer',
    'comprendre': 'entendre',
    'vendre': 'vendre',
    'écrire': 'escriure',
    'bouger': 'moure',
    'mourir': 'morrer',
    'connaître': 'conèixer',
    'naître': 'néixer',
    'émouvoir': 'commoure',
    'ouvrir': 'obrir',
    's’asseoir': 'seure',
    'faire mal': 'doldre',
    'tomber': 'caure',
    'obtenir': 'obtenir',
    'porter': 'dur',
    'conclure': 'concloure',
    'respecter': 'complir',
    'offrir': 'oferir',
    'attendre': 'atendre',
    'fondre': 'fondre',
    'rire': 'riure',
    'sourire': 'somriure',
    'mentir / se reposer': 'jeure',
    'récolter': 'collir',
    'briller': 'lluïr',
    'plaire': 'complaure',
    'valoir': 'valer',
    'sortir': 'eixir',
    'promettre': 'prometre',
    'vaincre': 'vèncer',
    'chanter': 'cantar',
    'aimer': 'estimar',
    'écouter': 'escoltar',
    'porter': 'portar',
    'chercher': 'buscar',
    'toucher': 'tocar',
    'arriver': 'arribar',
    'attendre / espérer': 'esperar',
    'acheter': 'comprar',
    'payer': 'pagar',
    'regarder': 'mirar',
    'attraper': 'agafar',
    'crier': 'cridar',
    'étudier': 'estudiar',
    'travailler': 'treballar',
    'demander': 'preguntar',
    'voyager': 'viatjar',
    'terminer': 'acabar',
    'aider': 'ajudar',
    'parler': 'parlar',
    'oublier': 'oblidar',
    'gagner': 'guanyar',
    'utiliser': 'utilitzar',
    'marcher': 'caminar',
    'avoir besoin de': 'necessitar',
    'essayer': 'intentar',
    'entrer': 'entrar',
    'enseigner': 'ensenyar',
    'rendre': 'tornar',
    'manger': 'menjar',
    'partir': 'marxar',
    'débatte': 'debatre',
    'appartenir': 'pertànyer',
    'perdre': 'perdre',
    'rendre (quelque chose)': 'retre',
    'presser': 'prémer',
    'craindre': 'témer',
    'abattre': 'abatre',
    'casser': 'rompre',
    'décider': 'decidir',
    'choisir': 'escollir',
    'dormir': 'dormir',
    'traduire': 'traduir',
    'discuter': 'discutir',
    'lire': 'llegir',
    'partager': 'compartir',
    'produire': 'produir',
}


def poser_questions(dico):
    mots_posés = list(dico.keys())
    random.shuffle(mots_posés)  # Mélange les mots de manière aléatoire
    score = 0
    mauvaises_reponses = []

    for mot_francais in mots_posés:
        traduction_attendue = dico[mot_francais]
        reponse = input(f"Traduisez '{mot_francais}' en catalan: ").strip()

        if reponse.lower() == traduction_attendue.lower():
            # Afficher la bonne réponse en vert
            print(f"\033[32mBonne réponse: {traduction_attendue}\033[0m")  # Code ANSI pour vert
            score += 1
        else:
            # Afficher la mauvaise réponse en rouge
            print(f"\033[31mMauvaise réponse: {traduction_attendue}\033[0m")  # Code ANSI pour rouge
            mauvaises_reponses.append((mot_francais, traduction_attendue))

    print(f"\nVotre score final est: {score}/{len(dico)}")
    if mauvaises_reponses:
        print("\nMauvaises réponses:")
        for mot, traduction in mauvaises_reponses:
            print(f"'{mot}' -> '{traduction}'")

    return mauvaises_reponses


def recommencer_sur_mauvaises_reponses(mauvaises_reponses, dico):
    dico_mauvaises_reponses = {mot: dico[mot] for mot, _ in mauvaises_reponses}
    if dico_mauvaises_reponses:
        print("\nRecommençons avec les mots que vous n'avez pas trouvés :")
        return poser_questions(dico_mauvaises_reponses)
    else:
        print("\nVous avez répondu correctement à toutes les questions !")
        return []


def main():
    print("Bienvenue dans le quiz de traduction !")
    mauvaises_reponses = poser_questions(dictionnaire_verbes_francais_catalan)

    if mauvaises_reponses:
        recommencer = input(
            "\nVoulez-vous recommencer avec les mots que vous n'avez pas trouvés ? (oui/non): ").strip().lower()
        if recommencer == 'oui':
            recommencer_sur_mauvaises_reponses(mauvaises_reponses, dictionnaire_verbes_francais_catalan)
        else:
            print("Merci d'avoir joué !")
    else:
        print("Bravo, vous avez répondu correctement à tous les mots !")


if __name__ == "__main__":
    main()
