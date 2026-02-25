from __future__ import annotations

from typing import Sequence, TypeVar

T = TypeVar("T")


def shell_sort(values: Sequence[T]) -> list[T]:
    """Return a new list sorted using the Shell sort algorithm."""
    arr = list(values)
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j > gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def main() -> None:
    sample = [9, 3, 7, 1, 5]
    print("Original:", sample)
    print("Sorted:", shell_sort(sample))


if __name__ == "__main__":
    main()
