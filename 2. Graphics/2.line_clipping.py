import matplotlib.pyplot as plt

# Cohen–Sutherland region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

# Compute region code for a point (x, y)
def compute_out_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
    return code

# Cohen–Sutherland line clipping
def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    outcode1 = compute_out_code(x1, y1, x_min, y_min, x_max, y_max)
    outcode2 = compute_out_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False

    while True:
        if not (outcode1 | outcode2):
            # Both endpoints inside: trivially accept
            accept = True
            break
        elif outcode1 & outcode2:
            # Both endpoints share an outside zone: trivially reject
            break
        else:
            # At least one endpoint is outside the rectangle
            outcode_out = outcode1 if outcode1 else outcode2

            if outcode_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif outcode_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif outcode_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif outcode_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_out_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                outcode2 = compute_out_code(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# ---- Main Program (Lab Demo) ----
if __name__ == "__main__":
    # Define clipping window
    x_min, y_min = 50, 50
    x_max, y_max = 100, 100

    # Test lines
    lines = [
        (30, 30, 70, 70),    # crosses
        (60, 20, 80, 120),   # crosses top and bottom
        (20, 80, 120, 80),   # horizontal
        (70, 70, 90, 90),    # fully inside
        (110, 110, 130, 130) # fully outside
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

    # Original lines
    ax1.set_title("Original Lines")
    for line in lines:
        ax1.plot([line[0], line[2]], [line[1], line[3]], 'b')
    ax1.plot([x_min, x_max, x_max, x_min, x_min],
             [y_min, y_min, y_max, y_max, y_min], 'r')
    ax1.set_xlim(0, 150)
    ax1.set_ylim(0, 150)
    ax1.set_aspect('equal')

    # Clipped lines
    ax2.set_title("Clipped Lines (Cohen-Sutherland)")
    for line in lines:
        clipped = cohen_sutherland_clip(*line, x_min, y_min, x_max, y_max)
        ax2.plot([line[0], line[2]], [line[1], line[3]], 'gray', linestyle='dotted')  # original (faint)
        if clipped:
            ax2.plot([clipped[0], clipped[2]], [clipped[1], clipped[3]], 'g', linewidth=2)
    ax2.plot([x_min, x_max, x_max, x_min, x_min],
             [y_min, y_min, y_max, y_max, y_min], 'r')
    ax2.set_xlim(0, 150)
    ax2.set_ylim(0, 150)
    ax2.set_aspect('equal')

    plt.tight_layout()
    # plt.savefig("cohen_sutherland_result.png", dpi=300)
    plt.show()
