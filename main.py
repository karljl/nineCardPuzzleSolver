from card import Card
from board import Board


# cards = [
#     Card([-4, -1, 2, -3]),
#     Card([-2, 1, 4, 3]),
#     Card([-1, -3, -4, 3]),
#     Card([-1, 2, 4, 3]),
#     Card([-1, -4, -3, 2]),
#     Card([4, -4, -2, -1]),
#     Card([2, -3, -4, -1]),
#     Card([-4, 1, -2, 3]),
#     Card([-2, -3, 1, 2])
# ]

cards = [
    Card([-4, 1, -3, 2]),
    Card([-2, 4, 3, -2]),
    Card([-3, 1, -2, 4]),
    Card([2, -1, -4, 3]),
    Card([2, -1, 4, -3]),
    Card([-4, 1, 3, -2]),
    Card([-3, -2, 2, 1]),
    Card([-1, -4, 2, 3]),
    Card([-2, 1, 2, -1]),
]


def main():
    board = Board(cards)
    try:
        board.place_cards()
    except IndexError:
        print("This puzzle has no valid solution.")


if __name__ == '__main__':
    main()
