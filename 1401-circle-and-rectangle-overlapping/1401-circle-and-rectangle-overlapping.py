class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter < x1:
            closest_x = x1
        elif xCenter > x2:
            closest_x = x2
        else:
            closest_x = xCenter

        # Find closest y-coordinate
        if yCenter < y1:
            closest_y = y1
        elif yCenter > y2:
            closest_y = y2
        else:
            closest_y = yCenter

        # Distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return dx * dx + dy * dy <= radius * radius