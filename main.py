import random

# Dictionnaire des mots français et leur traduction en catalan
dictionnaire_verbes_francais_catalan = {
    'accepter': 'acceptar',
    'acheter': 'comprar',
    'aider': 'ajudar',
    'ajouter': 'afegir',
    'aller': 'anar',
    'allumer': 'per illuminar',
    'appeler': 'trucar',
    'apporter': 'portar',
    'apprendre': 'aprendre',
    's_arrêter': 'parar',
    'attendre': 'esperar',
    'avoir': 'tenir',
    'casser': 'trencar',
    'chanter': 'cantar',
    'chercher': 'cercar',
    'choisir': 'tria',
    'commencer': 'començar',
    'comprendre': 'entendre',
    'compter': 'comptar',
    'conduire': 'conduir',
    'confirmer': 'per confirmar',
    'connaître': 'saber',
    'contacter': 'contacte',
    'continuer': 'continua',
    'couper': 'tallar',
    'courir': 'correr',
    'crier': 'cridar',
    'croire': 'creure',
    'cuisiner': 'cuinar',
    'décider': 'decidir',
    'demander': 'preguntar',
    'descendre': 'per baixar',
    'devenir': 'convertirse en',
    'devoir': 'haver de',
    'dire': 'dir',
    'discuter': 'discutir',
    'donner': 'donar',
    'dormir': 'dormir',
    'écouter': 'escoltar',
    'entrer': 'entrar',
    'envoyer': 'enviar',
    'essayer': 'provar',
    'éteindre': 'apagar',
    'empêcher': 'prevenir',
    'entendre': 'escoltar',
    'être': 'ser',
    'exister': 'existir',
    'expliquer': 'explicar',
    'fermer': 'tanca',
    'finir': 'acabar',
    'gagner': 'guanyar',
    'garder': 'conservar',
    'jeter': 'llançar',
    'jouer': 'jugar',
    'laisser': 'deixar',
    'laver': 'rentar',
    'lire': 'llegir',
    'manger': 'menjar',
    'marcher': 'caminar',
    'mettre': 'posar',
    'montrer': 'mostrar',
    'nettoyer': 'netejar',
    'oublier': 'oblidar',
    'ouvrir': 'obert',
    'parler': 'parlar',
    'partager': 'compartir',
    'payer': 'pagar',
    'penser': 'pensar',
    'perdre': 'perdre',
    'permettre': 'permetre',
    'pleurer': 'plorar',
    'porter': 'portar',
    'poser': 'posar',
    'pouvoir': 'poder',
    'prendre': 'prendre',
    'prévenir': 'prevenir',
    'quitter': 'marxar',
    'raconter': 'per parlar ne',
    'rappeler': 'recordar',
    'recevoir': 'rebre',
    'reconnaître': 'reconeixer',
    'refuser': 'refusar',
    'regarder': 'mirar',
    'rencontrer': 'trobar',
    'rendre': 'tornar',
    'répéter': 'repetir',
    'répondre': 'resposta',
    'rester': 'quedar se',
    'retrouver': 'per recuperar',
    'réussir': 'per tenir èxit',
    'revenir': 'torna',
    'rire': 'riure',
    's en aller': 'marxar',
    's assoir': 'seure',
    's endormir': 'adormir se',
    'savoir': 'saber',
    'se rappeler': 'recordar',
    'se réveiller': 'despertar',
    'suivre': 'segueix',
    'téléphoner': 'anomenada',
    'tenir': 'aguantar',
    'tirer': 'estirar',
    'tomber': 'caure',
    'toucher': 'tocar',
    'tourner': 'torn',
    'traduire': 'traduir',
    'travailler': 'treballar',
    'trouver': 'trobar',
    'utiliser': 'utilitzar',
    'vendre': 'venda',
    'venir': 'vine',
    'vivre': 'viu',
    'voir': 'veure',
    'voler (ciel)': 'volar al cel',
    'voler': 'robar',
    'vouloir': 'voler',

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
