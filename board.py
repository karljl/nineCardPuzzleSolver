from card import Card
from collections import defaultdict


class Board:

    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = cards
        self.board: list[Card] = []
        self.considered_starts = defaultdict(list)  # {card: [rotations]}

    def __repr__(self):
        return self.board

    def is_valid_starting_card(self, card) -> bool:
        return len(self.considered_starts[card]) < 4

    def place_starting_card(self, card) -> None:
        while card.current_rotation in self.considered_starts[card]:
            card.rotate()
        self.considered_starts[card].append(card.current_rotation)

        self.board.append(card)
        card.in_use = True

    def is_valid_middle_card(self, card, position) -> bool:
        if card.in_use:
            return False

        match position:
            case 1 | 2:
                left_card: Card = self.board[position - 1]
                return -left_card.right in card.sides
            case 3 | 6:
                upper_card: Card = self.board[position - 3]
                return -upper_card.down in card.sides
            case 4 | 5 | 7 | 8:
                left_card: Card = self.board[position - 1]
                upper_card: Card = self.board[position - 3]
                return card.contains_consecutive_values(-left_card.right, -upper_card.down)

    def place_middle_card(self, card, position) -> None:
        match position:
            case 1 | 2:
                left_card: Card = self.board[position - 1]
                while not card.compare_left_to_right(left_card):
                    card.rotate()
            case 3 | 6:
                upper_card: Card = self.board[position - 3]
                while not card.compare_up_to_down(upper_card):
                    card.rotate()
            case 4 | 5 | 7 | 8:
                left_card: Card = self.board[position - 1]
                upper_card: Card = self.board[position - 3]
                while not card.compare_left_to_right_and_up_to_down(left_card, upper_card):
                    card.rotate()

        self.board.append(card)
        card.in_use = True

    def remove_last_card(self):
        card = self.board.pop()
        card.in_use = False

    def place_cards(self, position: int = 0) -> None:
        if position == len(self.cards):
            print(self.board)
            return

        for card in self.cards:
            if position == 0:
                if self.is_valid_starting_card(card):
                    self.place_starting_card(card)
                    self.place_cards(position + 1)
            else:
                if self.is_valid_middle_card(card, position):
                    self.place_middle_card(card, position)
                    self.place_cards(position + 1)

        self.remove_last_card()
