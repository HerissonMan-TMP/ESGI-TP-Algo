"""
TP 01 — Analyse de Complexité & Benchmarks
Complétez les sections marquées TODO
"""
import time
import random


# ── Exercice 1 ────────────────────────────────────────────────────────────────

def func_a(n: int) -> int:
    """
    Complexité : O(n²) car deux boucles imbriquées
    """
    s = 0
    for i in range(n):
        for j in range(i, n):
            s += 1
    return s


def func_b(n: int) -> int:
    """
    Complexité : O(n) car une seule boucle et des additions
    """
    c, i = 0, 1
    while i < n:
        c += 1
        i *= 2
    return c


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def find_pair_naive(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n²)
    TODO: deux boucles imbriquées
    """
    n = len(arr)
    for i in range(n):
        # On commence j à i + 1 pour éviter les doublons et le test i != j
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


def find_pair_fast(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n)
    TODO: une passe avec un set — pour chaque x, chercher (target-x)
    """
    seen = set()
    for x in arr:
        if target - x in seen:
            return True
        seen.add(x)
    return False


# ── Exercice 3 ────────────────────────────────────────────────────────────────

def run_benchmark():
    """Mesure et affiche les temps d'exécution des deux versions."""
    print(f"{'n':>8}  {'naïf (ms)':>12}  {'rapide (ms)':>12}")
    print("-" * 40)
    for n in [1_000, 5_000, 10_000, 50_000]:
        arr = random.sample(range(n * 10), n)
        target = arr[n-2] + arr[n-1]

        # TODO: mesurez find_pair_naive avec time.perf_counter()
        t1_naive = time.perf_counter()
        find_pair_naive(arr, target)
        t2_naive = time.perf_counter()
        t_naive = t2_naive - t1_naive  

        # TODO: mesurez find_pair_fast
        t1_fast = time.perf_counter()
        find_pair_fast(arr, target)
        t2_fast = time.perf_counter()
        t_fast = t2_fast - t1_fast

        print(f"{n:>8}  {t_naive * 1000:>12.3f}  {t_fast * 1000:>12.3f}")


if __name__ == "__main__":
    run_benchmark()
