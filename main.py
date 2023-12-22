from abc import ABC, abstractmethod
from typing import List


# Абстрактний клас для MoveRules
class MoveRules(ABC):
    def __init__(self, position: List[int]):
        self.position = position

    @abstractmethod
    def get_all_moves(self) -> List[List[int]]:
        pass


# Клас конкретних правил руху для коня
class KnightMove(MoveRules):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        moves = [
            (x + 2, y + 1), (x + 1, y + 2),
            (x - 1, y + 2), (x - 2, y + 1),
            (x - 2, y - 1), (x - 1, y - 2),
            (x + 1, y - 2), (x + 2, y - 1)
        ]
        return [(i, j) for i, j in moves if 1 <= i <= 8 and 1 <= j <= 8]


# Клас конкретних правил руху для слона
class BishopMove(MoveRules):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        moves = [(x + i, y + i) for i in range(1, 8)] + [(x - i, y + i) for i in range(1, 8)]
        return [(i, j) for i, j in moves if 1 <= i <= 8 and 1 <= j <= 8]


# Клас конкретних правил руху для короля
class KingMove(MoveRules):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        moves = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x + 1, y - 1),
            (x - 1, y + 1), (x - 1, y - 1)
        ]
        return [(i, j) for i, j in moves if 1 <= i <= 8 and 1 <= j <= 8]


# Абстрактний клас для шахової фігури
class Piece(ABC):
    def __init__(self, position: List[int], color: str, move_rule: MoveRules):
        self.position = position
        self.color = color
        self.number_of_moves = 0
        self.move_rule = move_rule

    def validate_position(self, position: List[int]):
        return all(1 <= coord <= 8 for coord in position)

    def move(self, new_position: List[int]) -> dict:
        if not self.validate_position(new_position):
            return {"status": "failure", "message": "Invalid position coordinates. Each coordinate should be between 1 and 8."}

        self.position = new_position
        self.number_of_moves += 1
        return {"status": "success", "message": f"Переміщено на {new_position}"}

    def get_position(self) -> List[int]:
        return self.position

    def __str__(self):
        return f"{self.color} {self.__class__.__name__} at {self.position} with {self.number_of_moves} moves"

    def get_all_moves(self) -> List[List[int]]:
        return self.move_rule.get_all_moves()


# Клас конкретної фігури "Кінь"
class Knight(Piece):
    def __init__(self, position: List[int], color: str):
        move_rule = KnightMove(position)
        super().__init__(position, color, move_rule)


# Клас конкретної фігури "Слон"
class Bishop(Piece):
    def __init__(self, position: List[int], color: str):
        move_rule = BishopMove(position)
        super().__init__(position, color, move_rule)


# Клас конкретної фігури "Король"
class King(Piece):
    def __init__(self, position: List[int], color: str):
        move_rule = KingMove(position)
        super().__init__(position, color, move_rule)


# Приклад використання та тестування:
knight = Knight([2, 3], 'Білий')
print(knight)  # Виведе: Білий Knight at [2, 3] with 0 moves
print("All moves:", knight.get_all_moves())  # Виведе всі можливі ходи для коня

bishop = Bishop([4, 5], 'Чорний')
print(bishop)  # Виведе: Чорний Bishop at [4, 5] with 0 moves
print("All moves:", bishop.get_all_moves())  # Виведе всі можливі ходи для слона

king = King([1, 1], 'Білий')
print(king)  # Виведе: Білий King at [1, 1] with 0 moves
print("All moves:", king.get_all_moves())  # Виведе всі можливі ходи для короля
