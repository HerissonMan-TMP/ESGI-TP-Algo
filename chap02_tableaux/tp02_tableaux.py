"""
TP 02 — Les Tableaux
Complétez les fonctions marquées TODO
"""


def rotate(arr: list, k: int) -> None:
    """
    Rotation circulaire droite de k positions, en place.
    Complexité attendue : O(n) temps, O(1) espace.
    Astuce : triple reverse.
    TODO
    """
    n = len(arr)
    if n == 0:
        return
    k = k % n

    def rev(lo, hi):
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)


def remove_duplicates(arr: list) -> int:
    """
    Supprime les doublons d'un tableau TRIÉ en place.
    Retourne la nouvelle longueur.
    Complexité attendue : O(n).
    TODO
    """
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


def merge_arrays(a: list, b: list) -> list:
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    Complexité attendue : O(n+m).
    TODO
    """
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def binary_search(arr: list, target: int) -> int:
    """
    Recherche binaire dans un tableau trié.
    Retourne l'indice de target ou -1 si absent.
    Complexité attendue : O(log n).
    TODO
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] >= target.
    Retourne len(arr) si target > tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] > target.
    Retourne len(arr) si target >= tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def transpose(m: list) -> None:
    """
    Transposée d'une matrice n×n en place.
    Complexité attendue : O(n²).
    TODO : échanger m[i][j] et m[j][i] pour j > i
    """
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]


def rotate_90(m: list) -> None:
    """
    Rotation 90° sens horaire en place.
    Étapes : transposer, puis inverser chaque ligne.
    TODO
    """
    transpose(m)
    for row in m:
        row.reverse()


def max_subarray(arr: list) -> int:
    """
    Sous-tableau contigu de somme maximale (algorithme de Kadane).
    Complexité attendue : O(n).
    TODO : cur = max(arr[i], cur + arr[i]) ; best = max(best, cur)
    """
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
