class Soduku:
    def __init__(self, soduku: list[list[int]]):
        self.soduku = soduku
        self._non_viable = None  # https://stackoverflow.com/a/63954409
        self.category = self._get_category()

    def _get_category(self) -> str:
        """
        Returns:
            str: Will be either "complete" or "incomplete but viable" or "non-viable"
        """

        # https://stackoverflow.com/a/1589209 -- helper for _get_category
        def find_non_viability(ls: list[int], belongs_to: str, index: int):
            repeaters = {r for r in ls if r != 0 and ls.count(r) > 1}
            # all the repeating elements except 0
            if repeaters:
                self.non_viable = belongs_to, index

        # Checking all the rows
        for i in range(9):
            ls = self.soduku[i]
            find_non_viability(ls, "row", i)

        # Checking all the columns
        for i in range(9):
            ls = [self.soduku[j][i] for j in range(0, 9)]
            find_non_viability(ls, "columns", i)

        # Checking all the sub-matrices
        j = 0
        k = -1
        for i in range(9):
            # generate a sub-matrix
            ls = []
            for _ in range(9):
                k += 1
                ls.append(self.soduku[j][k])

                if k in (2, 5, 8) and j not in (2, 5, 8):
                    j += 1
                    k -= 3

            find_non_viability(ls, "sub-matrices", i)

            if ((i + 1) % 3 == 0):
                j += 1
                k = -1
            else:
                j -= 2

        # Returning the category
        try:
            if self.non_viable:
                return "non-viable"
        except AttributeError:
            for row in self.soduku:
                if 0 in row:
                    return "incomplete but viable"

        return "complete"

    @property
    def non_viable(self) -> dict[str, list[int]]:
        if self._non_viable is None:
            raise AttributeError("Attribute not yet initalised")
        return self._non_viable

    @non_viable.setter
    def non_viable(self, violate: tuple[str, int]):
        """
        Args:
            violate (tuple[str, str]):
                violate[0] must be either "rows" or "columns" or 'sub-matrices"
                violate[1] must be b/w 0 to 8
        """
        if self._non_viable is None:
            self._non_viable = {"rows": [], "columns": [], "sub-matrices": []}
        if 0 <= violate[1] <= 8:
            if violate[0] in self._non_viable.keys():
                self._non_viable[violate[0]].append(violate[1])
            else:
                raise KeyError("Key must be either \"rows\" or \"columns\" or \"sub-matrices\"")
        else:
            raise ValueError("The value must be between 0 to 8")


class Sodukus():
    def __init__(self, soduku: list[list[list[int]]]):
        self.items = [Soduku(s) for s in soduku]


def inp_soduku():
    soduku = []
    while True:
        try:
            tmp = [int(i) for i in input().strip().split()]
        except ValueError:
            print("All the values should be integers")
            continue

        if len(tmp) == 0:
            continue  # For the empty line
        if len(tmp) != 9:
            print("There should be exactly nine integers in each row")
            continue

        soduku.append(tmp)

        if len(soduku) == 9:
                break

    return soduku

def inp_sodukus() -> list[list[list[int]]]:
    while True:
        try:
            n = int(input())
            if not n > 0:
                raise ValueError()
            break
        except ValueError:
            print("Please enter a integer greater than 0")
            continue

    res = []
    for _ in range(n):
        res.append(inp_soduku())
    
    return res


def output(sodukus: Sodukus):
    for s in sodukus.items:
        print("\n{}".format(cat := s.category))
        if cat == "non-viable":
            for k, v in s.non_viable.items():
                print(f"  {k}:", *[i + 1 for i in v])


def main():
    sodukus = Sodukus(inp_sodukus())
    output(sodukus)


if __name__ == "__main__":
    main()
