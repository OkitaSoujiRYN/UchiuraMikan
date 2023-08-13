define heros = Character("[nomduheros]", color="#f4cbd5")
define MN = Character("Milim Naza", color="#ff33b8")
define OC = Character("You Watanabe", color="#16c9ff")
define N = Character("Narrateur", color="#ff0000")


label start:
    $ nomduheros = renpy.input("Entrez un nom")
    $ nomduheros = nomduheros.strip()

    if not nomduheros:
        $ nomduheros = "Ryn"

        heros "Hey c'est moi [nomduheros]"

        scene sakura_field

        show Milim Naza
    "Vous vous appelez [nomduheros] !"
    scene sakura_field
    show image "sakura_field.png"
    show milim_naza   
    MN"Ohayo [nomduheros]"
    heros "Ohayo Milim"
    MN "Tu vas vivre une histoire incroyable dans Uchiura mais tu ne t'en rendras compte que plus tard alors je te souhaite que du bonheur lors de tes choix"
    
    heros "Merci Milim"
    MN "De rien [nomduheros]"
    heros "Je vais aller voir mes amis"
    MN "D'accord, à plus tard"
    heros "A plus tard"
    hide milim_naza
    hide image "sakura_field.png"
    scene maison
    heros "Ouhh je vient de me réveiller, j'ai l'impreession d'avoir fait un rêve, bon j'ai faim je vais aller manger"
    heros "Bonjour Onee chan"
    OC "Bonjour [nomduheros], comment vas tu ?"
    heros "Je vais bien et toi ?" 
    OC "Je vais bien aussi"
    heros "Je vais aller manger"
    OC "Moi aussi hehe donnes une part à ta grande soeur chérie nn ?"
    heros "Onee chan tu es trop gourmande !"
    OC "Je sais hehe"
    heros " Bon allons manger"
    OC "Oui allons y teehee ~"
    N "dit elle en rougissant"
    heros "Onee chan tu rougis ?"
    OC "N..non je ne rougis pas !"
    heros "Si si tu rougis"
    OC "Je ne rougis pas !"
    heros "Si si tu rougis"
    OC "Je ne rougis pas !"
    heros "Bon d'accord tu ne rougis pas "
    OC "Oui je ne rougis pas. Tu dois me donner une grande part vu que tu as fais de fausses accusations envers ta grande soeur chérie"
    heros "Tu es toujours gagnante à la fin hein ?"
    OC "Oui hehe"
    play audio chomusuke
    play audio high_tension volume 0.4
    
    scene maison
    stop music fadeout 2.0


    