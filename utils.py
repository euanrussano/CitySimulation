def is_point_in_rectangle(point_x, point_y, rect_x1, rect_y1, rect_x2, rect_y2):
    """
    Checks if a point is inside an axis-aligned rectangle.

    Args:
        point_x, point_y: Coordinates of the point.
        rect_x1, rect_y1: Coordinates of one corner of the rectangle.
        rect_x2, rect_y2: Coordinates of the opposite corner of the rectangle.

    Returns:
        True if the point is inside or on the boundary, False otherwise.
    """
    min_x = min(rect_x1, rect_x2)
    max_x = max(rect_x1, rect_x2)
    min_y = min(rect_y1, rect_y2)
    max_y = max(rect_y1, rect_y2)

    return min_x <= point_x <= max_x and min_y <= point_y <= max_y

# Example usage:
# point = (5, 5)
# rectangle_corners = (0, 0, 10, 10)
# if is_point_in_rectangle(point[0], point[1], *rectangle_corners):
#     print("Point is inside the rectangle.")
# else:
#     print("Point is outside the rectangle.")