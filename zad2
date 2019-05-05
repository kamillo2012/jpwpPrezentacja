    def possible_movements(self, chessboard):
        movements_list = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                x = self.x_pos + i
                y = self.y_pos + j
                if abs(i) is not abs(j) and x in range(1, 9) and y in range(1, 9):
                    if chessboard[moves.position_to_number((x, y))] == '':
                        # pole jest puste
                        movements_list.append((x, y))
                    elif chessboard[moves.position_to_number((x, y))].colour != self.colour:
                        # na polu stoi figura przeciwnika
                        movements_list.append((x, y))
        return movements_list
