def safe_pawns(pawns: set) -> int:
    result = []
    count = 0
    coordinates_set = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                       'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                       'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                       'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                       'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                       'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                       'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    def verify_coord(pawn,):
        if 1 < int(pawn[1]) < 8:
            for i in range(len(coordinates_set)):
                if coordinates_set[i] == pawn:
                    if coordinates_set[i + 7] or coordinates_set[i + 9] in pawns:
                        count += 1
        if 1 == int(pawn[1]):
            for i in range(len(coordinates_set)):
                if coordinates_set[i] == pawn:
                    if coordinates_set[i + 9] in pawns:
                        count += 1
            if int(pawn[1]) == 8:
                for i in range(len(coordinates_set)):
                    if coordinates_set[i] == pawn:
                        if coordinates_set[i + 7] in pawns:
                            count += 1
    for pawn in pawns:
        verify_coord(pawn)
    print(count)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")