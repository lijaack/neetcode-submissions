class CountSquares:

    def __init__(self):
        # ptsCount[x][y] = how many times point (x, y) was added
        self.ptsCount = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        # Get the x and y coordinates
        x, y = point

        # Increase the count for this exact point
        # Duplicates are allowed, so we keep track of how many exist
        self.ptsCount[x][y] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        # Try every point that has the same x-coordinate
        # This point can be the opposite corner of the square
        for y2 in self.ptsCount[x1]:

            # Distance between the query point and this point
            # This becomes the side length of the square
            side = y2 - y1

            # Same point / zero-length side can't make a square
            if side == 0:
                continue

            # Two possible x-coordinates for the other side
            # One square can extend right, the other can extend left
            x3, x4 = x1 + side, x1 - side

            # Square extending to the right
            #
            # Need these three points:
            # (x1, y2)
            # (x3, y1)
            # (x3, y2)
            #
            # Multiply counts because each combination of duplicate
            # points represents a different way to form the square
            res += (
                self.ptsCount[x1][y2]
                * self.ptsCount[x3][y1]
                * self.ptsCount[x3][y2]
            )

            # Square extending to the left
            #
            # Need:
            # (x1, y2)
            # (x4, y1)
            # (x4, y2)
            res += (
                self.ptsCount[x1][y2]
                * self.ptsCount[x4][y1]
                * self.ptsCount[x4][y2]
            )

        return res