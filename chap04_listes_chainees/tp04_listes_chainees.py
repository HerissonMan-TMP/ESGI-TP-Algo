"""
TP 04 — Listes Doublement Chaînées
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Liste doublement chaînée avec head, tail et taille."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, val) -> None:
        """Insertion en tête — O(1). TODO"""
        raise NotImplementedError

    def push_back(self, val) -> None:
        """Insertion en queue — O(1). TODO"""
        raise NotImplementedError

    def pop_front(self):
        """
        Suppression et retour de la valeur en tête — O(1).
        Lève IndexError si vide.
        TODO
        """
        raise NotImplementedError

    def pop_back(self):
        """
        Suppression et retour de la valeur en queue — O(1).
        Lève IndexError si vide.
        TODO
        """
        raise NotImplementedError

    def insert_after(self, node: Node, val) -> Node:
        """
        Insère val après node, retourne le nouveau nœud — O(1).
        TODO
        """
        raise NotImplementedError

    def remove(self, node: Node) -> None:
        """Supprime node de la liste — O(1). TODO"""
        raise NotImplementedError

    def find(self, val) -> Node | None:
        """Retourne le premier nœud avec data==val, ou None — O(n). TODO"""
        raise NotImplementedError

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        """Parcours de head vers tail. TODO"""
        raise NotImplementedError

    def to_list(self) -> list:
        return list(self)


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def reverse_iterative(lst: DoublyLinkedList) -> None:
    """
    Inverse la liste en place — O(n) temps, O(1) espace.
    Pour chaque nœud, échange prev et next, puis swap head et tail.
    TODO
    """
    raise NotImplementedError


# ── Exercice 3 — Algorithme de Floyd ─────────────────────────────────────────

class SNode:
    """Nœud de liste simplement chaînée pour l'exercice Floyd."""
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head: SNode | None) -> bool:
    """
    Détecte un cycle dans une liste simplement chaînée.
    Algorithme du lièvre et de la tortue — O(n) temps, O(1) espace.
    TODO : slow avance de 1, fast avance de 2
    """
    raise NotImplementedError


# ── Exercice 4 ────────────────────────────────────────────────────────────────

def kth_from_end(head: SNode | None, k: int) -> int:
    """
    Retourne la valeur du k-ième élément depuis la fin (k=1 = dernier).
    Un seul parcours, deux pointeurs distants de k.
    Lève ValueError si k > longueur.
    TODO
    """
    raise NotImplementedError
