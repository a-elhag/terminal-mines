from .game_model import GameState, CellState
from click import clear, style, echo
from sys import exit

color_mapping = {
    CellState.FLAG: "bright_green",
    CellState.WARN1: "bright_cyan",
    CellState.WARN2: "cyan",
    CellState.WARN3: "bright_blue",
    CellState.WARN4: "bright_magenta",
    CellState.WARN5: "magenta",
    CellState.WARN6: "bright_yellow",
    CellState.WARN7: "bright_yellow",
    CellState.WARN8: "bright_yellow",
    CellState.EXPLODED: "bright_red"
}


def render(minefield, x, y):
    clear()

    def render_cell(iter_x, iter_y):
        state = minefield.get_cell(iter_x, iter_y).state

        bg = "red" if iter_x == x and iter_y == y else None
        fg = color_mapping.get(state, None)

        return style(state.value, bg=bg, fg=fg)

    echo(chr(0x250C) + chr(0x2500) * (minefield.width * 2 + 1) + chr(0x2510))
    for iter_y in range(minefield.height):
        echo(chr(0x2502) + " " + " ".join(render_cell(iter_x, iter_y) for iter_x in range(minefield.width)) + " " +
             chr(0x2502))
    echo(chr(0x2514) + chr(0x2500) * (minefield.width * 2 + 1) + chr(0x2518))

    if minefield.state == GameState.WON:
        echo(" Game won")
    elif minefield.state == GameState.LOST:
        echo(" Game lost")
    else:
        echo(" Flags remaining: {}".format(minefield.flags_remaining))

    if minefield.state != GameState.IN_PROGRESS:
        exit(0)
