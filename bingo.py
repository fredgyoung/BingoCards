from capitals import *
import numpy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def print_grid(mydict):

    data = numpy.random.permutation(list(mydict.keys()))
    width, height = letter
    c.setStrokeColorRGB(0.0, 0.0, 0.0)
    border = width / 14
    square_size = width * 6 / 35

    grid_lines = []

    for x in range(6):
        grid_lines.append(border + (x * square_size))

    c.grid(grid_lines, grid_lines)

    c.setFillColor(colors.lightblue)
    c.rect(border, border + (5 * square_size), 5 * square_size, 80, fill=1)

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 56)
    c.drawString(1 * square_size - 20, 6 * square_size - 40, "B")
    c.drawString(2 * square_size - 20, 6 * square_size - 40, "I")
    c.drawString(3 * square_size - 20, 6 * square_size - 40, "N")
    c.drawString(4 * square_size - 20, 6 * square_size - 40, "G")
    c.drawString(5 * square_size - 20, 6 * square_size - 40, "O")

    # Print words
    c.setFont("Helvetica", 14)
    index = 0
    for i in range(5):
        for j in range(5):
            c.drawString(i * square_size + 60, j * square_size + 90, data[index])
            index += 1

    c.showPage()


if __name__ == '__main__':

    c = canvas.Canvas(r'C:\temp\bingo.pdf', pagesize=letter)

    for i in range(20):
        print_grid(united_states)
    c.save()
