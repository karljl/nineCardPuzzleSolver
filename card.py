class Card:

    def __init__(self, sides: list[int]):
        self.sides = sides

        self.rotations = {
            0: (sides[0], sides[1], sides[2], sides[3]),
            1: (sides[3], sides[0], sides[1], sides[2]),
            2: (sides[2], sides[3], sides[0], sides[1]),
            3: (sides[1], sides[2], sides[3], sides[0]),
        }

        self.current_rotation = 0
        self.in_use = False

    def __repr__(self) -> str:
        return f"(UP: {self.up}, RIGHT: {self.right}, DOWN: {self.down}, LEFT: {self.left})"

    def contains_consecutive_values(self, value1: int, value2: int) -> bool:
        subset = [value1, value2]
        idx = 0
        values = self.sides + [self.sides[0]]
        for ele in values:
            if subset[idx] == ele:
                idx += 1
                if idx == len(subset):
                    return True
            else:
                idx = int(ele == subset[0])
        return False

    def rotate(self) -> None:
        self.current_rotation = (self.current_rotation + 1) % 4

    @property
    def up(self) -> int:
        return self.rotations[self.current_rotation][0]

    @property
    def right(self) -> int:
        return self.rotations[self.current_rotation][1]

    @property
    def down(self) -> int:
        return self.rotations[self.current_rotation][2]

    @property
    def left(self) -> int:
        return self.rotations[self.current_rotation][3]

    def compare_left_to_right(self, other: "Card") -> bool:
        return self.left == -other.right

    def compare_up_to_down(self, other: "Card") -> bool:
        return self.up == -other.down

    def compare_left_to_right_and_up_to_down(self, left_card: "Card", upper_card: "Card") -> bool:
        return self.left == -left_card.right and self.up == -upper_card.down
