"""Example of writing a function to process a list."""


def main() -> None:
    """Entrypoint of program"""
    names: list[str] = ["Kris", "Kaki"]
    print(conatains("Kevin", names))


def conatains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in the haystack, False otherwise"""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False


if __name__ == "__main__":
    main()
