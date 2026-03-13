"""
TP 03 — Les Tris Simples
Toutes les fonctions trient en place (modifient arr).
"""
import random
import time

def bubble_sort(arr: list) -> None:
    """
    Tri à bulles avec optimisation flag swapped.
    Complexité : O(n²) pire, O(n) meilleur (tableau déjà trié).
    TODO
    """
    lst = len(arr)
    
    for e in range(lst):
        swapped = False
        for i in range(lst - e - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break


def selection_sort(arr: list) -> None:
    """
    Tri par sélection du minimum.
    Complexité : toujours O(n²), au plus n-1 échanges.
    TODO
    """
    lst = len(arr)
 
    for i in range(lst - 1):
        min_index = i
        for j in range(i + 1, lst):
            if arr[j] < arr[min_index]:
                min_index = j

def insertion_sort(arr: list) -> None:
    """
    Tri par insertion.
    Complexité : O(n²) pire, O(n) meilleur.
    TODO : pour i=1..n-1 : key=arr[i], décaler droite tant que arr[j]>key
    """
    lst = len(arr)
 
    for i in range(1, lst):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_generic(arr: list, key=None, reverse: bool = False) -> None:
    """
    Tri par insertion avec comparateur.
    key   : fonction d'extraction de clé (défaut : identité)
    reverse : si True, tri décroissant
    Complexité : O(n²)
    TODO
    """
    if key is None:
        key = lambda x: x
 
    lst = len(arr)
 
    for i in range(1, lst):
        key_val = arr[i]
        key_i   = key(arr[i])
        j = i - 1
        while j >= 0:
            key_j = key(arr[j])
            if (not reverse and key_j > key_i) or (reverse and key_j < key_i):
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key_val

def stabilite():
    valeurs = [random.randint(0, 9) for _ in range(8)]
    data = [(v, i) for i, v in enumerate(valeurs)]

    arr_bubble    = data[:]
    arr_selection = data[:]
    arr_insertion = data[:]

    insertion_sort_generic(arr_bubble,    key=lambda x: x[0])
    insertion_sort_generic(arr_selection, key=lambda x: x[0])
    insertion_sort_generic(arr_insertion, key=lambda x: x[0])

    print("Données initiales :", data)
    print("Après Tri avec bubble_sort: ", arr_bubble)
    print()
    print("Données initiales :", data)
    print("Après Tri avec selection_sort: ", arr_selection)
    print()
    print("Données initiales :", data)
    print("Après Tri avec insertion_sort: ", arr_insertion)

def benchmark():
    tailles = [500, 2000, 5000]
    tris = [
        ("bubble_sort",    bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
    ]

    for taille in tailles:
        print(f"\n{'─'*40}")
        print(f"nombre de données = {taille}")
        print(f"{'─'*40}")

        aleatoire = random.sample(range(taille * 10), taille)
        trie      = list(range(taille))
        inverse   = list(range(taille, 0, -1))

        for nom_tri, fonction_tri in tris:
            print(f"\n  {nom_tri}")
            for nom_tab, tableau in [("aléatoire", aleatoire), ("trié", trie), ("inversé", inverse)]:
                copie = tableau[:]
                debut = time.perf_counter()
                fonction_tri(copie)
                fin   = time.perf_counter()
                duree = (fin - debut) * 1000
                print(f"    {nom_tab:<12} : {duree:>7.1f}ms")

if __name__ == "__main__":

    print("=== Test de stabilité ===")
    stabilite()
    print("=== Test de benchmark ===")
    benchmark()