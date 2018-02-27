from etudiants import *

COURTE_LISTE = L_ETUDIANTS[:5]
NBRE_FICHES = len(L_ETUDIANTS)
NIP = 11800422

#Q3
FICHE_RANDOM = L_ETUDIANTS[NIP % NBRE_FICHES]


def pour_tous(seq_bool):
    """
    Renvoie True si il n'y a que des valeurs True dans seq_bool, sinon False
    :param seq_bool: (itérable) séquence de booléens
    :return: (bool) True si seq_bool ne contient que des valeurs True, False sinon

    CU: any
    
    Exemples:
    >>> pour_tous([])
    True
    >>> pour_tous((True, True, True))
    True
    >>> pour_tous((True, False, True))
    False
    """
    for i in seq_bool:
        if i == False:
            return False
    return True
    
    
def il_existe(seq_bool):
    """
    Renvoie True si il y a au moins une valeur True dans seq_bool, sinon False
    :param seq_bool: (itérable) séquence de booléens
    :return: (bool) True si seq_bool contient une valeur True, False sinon

    CU: any
    
    Exemples:
    >>> il_existe([])
    False
    >>> il_existe((False, True, False))
    True
    >>> il_existe((False, False))
    False>>> pour_tous([])
    True
    """
    for i in seq_bool:
        if i == True:
            return True
    return False
#Q0
def est_liste_d_etudiants(x):
    """
    Renvoie True si x est une liste de fiches d’étudiant, False dans le cas contraire.
    :param x: (any) 
    :return: (bool) 
    
    Cu : any
    
    Exemples:
    >>> est_liste_d_etudiants(COURTE_LISTE)
    True
    >>> est_liste_d_etudiants("Timoleon")
    False
    >>> est_liste_d_etudiants([('12345678', 'Calbuth', 'Raymond', 'Danse', '12') ])
    False
    """
    for i in x:
        if (not ("nip" in i
                and "nom" in i
                and "prenom" in i
                and "formation" in i
                and "groupe" in i)
            or len(i) != 5
            or type(i) != type({})):
            
            return False
        
    return True

#Q4
def ensemble_des_formations(liste):
    """
    Renvoie l'ensemble des formations dans la liste
    :param liste: (list) une liste de fiches d’étudiants
    :return: (set) un ensemble de chaînes de caractères donnant les formations présentes dans les fiches d’étudiants
    
    CU : liste ne contient que des fiches d’étudiants
    
    Exemples :
    >>> Liste_demo = [{'nip' : '1174520', 'nom' : 'ERARD', 'prenom' : 'ANNAELLE', 'formation' : 'SESI', 'groupe' : '21'}]
    >>> Liste_demo.append({'nip' : '1171680', 'nom' : 'VASSEUR', 'prenom' : 'AGATHE', 'formation' : 'PEIP', 'groupe' : '12'})
    >>> Liste_demo.append({'nip' : '1170249', 'nom' : 'CARDOSO MORENO', 'prenom' : 'INEIDA', 'formation' : 'MASS', 'groupe' : '2'})
    >>> ensemble_des_formations(Liste_demo) == { 'SESI','PEIP','MASS' }
    True
    >>> ensemble_des_formations(Liste_demo[0:2]) == { 'SESI','PEIP' }
    True

    """
    ensemble = set()
    for i in liste:
        ensemble.add(i['formation'])
    return ensemble
    
#Q5   
def nbre_prenom(liste, prenom):
    """
    Renvoie le nombre d'étudiants dont le prénom (second paramètre) est dans la liste (premier parametre)
    :param liste: (list) une liste de fiche d'étudiants
    :param prenom: (str) un prénom
    :return: (int) le nombre d'occurences du prénom dans les fiches
    
    CU: any
    
    Exemples:
    >>> nbre_prenom(COURTE_LISTE, 'MOHAMED')
    1
    >>> nbre_prenom(COURTE_LISTE, 'ZENOBE')
    0
    """
    prenom = prenom.upper()
    B = [i["prenom"] for i in liste]
    C = B.count(prenom)
    return C

#Q6
def nombre_prenoms_diff(liste):
    """
    Renvoie le nombre de prenoms différents dans la liste de fiches d'étudiants
    :param liste: (list) une liste de fiches d'étudiants
    :return: (tuple) le nombre de prénoms différents
    
    CU: any
    >>> nombre_prenoms_diff(COURTE_LISTE)
    5
    """

    return len({i["prenom"] for i in liste})

#Q7
def prenom_plus_freq(liste):
    """
    Renvoie le prénom le plus fréquent dans la liste, accompagné de son nombre d'occurences
    :param liste: (list) une liste de fiches d'étudiants
    :return: (list, int) le(s) prénoms le(s) plus frequent(s), avec le nombre d'occurences
    
    CU: any
    
    Exemples:
##    >>> l1 = prenom_plus_freq(COURTE_LISTE)
##    >>> l2 = (['MARIEME AICHA', 'ELODIE', 'ARTHUR', 'MOHAMED', 'DANIEL'], 1)
##    >>> len(l1) == len(l2)
##    True
##    >>> for i in l1:
##    ...     i in l2
##    True
    """
    liste_prenoms = [i["prenom"] for i in liste]
    ensemble_prenoms = set(liste_prenoms)
    a = 0
    prenom_max = []
    for prenom in ensemble_prenoms:
        temp = liste_prenoms.count(prenom)
        if temp > a:
            prenom_max = [prenom]
            a = temp
        elif temp == a:
            prenom_max.append(prenom)
    return prenom_max, a

#Q8
def is_nip_distincts(liste):
    """
    Vérifie que tous les NIP sont distincts
    :param liste: (list)
    :return: (bool) True si les NIP sont disctincts, False sinon
    
    CU: any
    
    Exemples:
    >>> is_nip_distincts(COURTE_LISTE)
    True
    """
    liste_nip = [i["nip"] for i in L_ETUDIANTS]
    ensemble_nip = set(liste_nip)
    return len(liste_nip) == len(ensemble_nip)

#Q9
def nbre_etudiants_par_formation(liste):
    """
    Renvoie le nombre d'étudiants dans chaque formation
    :param liste: (list) une liste de fiches d'étudiants
    :return: (dict) Dictionnaire avec le nombre d'étudiants par formation
    
    CU: any
    
    Exemples
    >>> nbre_etudiants_par_formation(COURTE_LISTE)
    
    """
    formations = {}
    for i in liste:
        if i["formation"] not in formations:
            formations[i["formation"]] = 1
        formations[i["formation"]] += 1
    return formations
    
#Q10
def liste_formation(liste, form):
    """
    Renvoie la liste des étudiants dans une formation donnée
    :param liste: (list) une liste de fiches d'étudiants
    :param form: (str) la formation dans laquelle on veut chercher les étudiants
    :return: (list) la liste des étudiants dans la formation donnée
    
    CU: any
    
    Exemples
    >>> liste_formation(COURTE_LISTE, "MASS")
    
    """
    res = []
    for i in liste:
        if i["formation"] == form:
            res.append((i["nip"], i["nom"], i["prenom"], i["groupe"]))
    return res





#Q3
print(FICHE_RANDOM)

#Q5
print("Nombre d'occurences du prénom Alexandre: ", nbre_prenom(L_ETUDIANTS, "ALEXANDRE"),
      "\nNombre d'occurences du prénom Camille", nbre_prenom(L_ETUDIANTS, "CAMILLE"))

#Q6
prenoms_diff = nombre_prenoms_diff(L_ETUDIANTS)
print("Il y a", prenoms_diff, "noms différents dans la liste")

#Q7
prenom_frequent = prenom_plus_freq(L_ETUDIANTS)
print("Le prénom le plus fréquent est (sont):", prenom_frequent[0], "et apparaît (apparaissent)",
      prenom_frequent[1], "fois")

#Q8
nip_distincts = is_nip_distincts(L_ETUDIANTS)
if nip_distincts:
    print("Les identifiants des étudiants sont tous distincts")
else:
    print("Les identifiants des étudiants ne sont pas tous distincts")
    
#Q9
print("Nombre d'étudiants par formation:", nbre_etudiants_par_formation(L_ETUDIANTS))

if __name__ == "__main__":

     import doctest

     doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

