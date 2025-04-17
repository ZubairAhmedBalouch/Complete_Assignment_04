# graphics.py - Minimal graphics module for Canvas usage
import tkinter

class Canvas:
    def __init__(self, width, height):
        self._tk = tkinter.Tk()
        self._tk.title("Canvas")
        self._canvas = tkinter.Canvas(self._tk, width=width, height=height)
        self._canvas.pack()
        self._mouse_x = 0
        self._mouse_y = 0
        self._click_x = None
        self._click_y = None
        self._canvas.bind("<Motion>", self._on_mouse_move)
        self._canvas.bind("<Button-1>", self._on_click)
        self._tk.update()

    def _on_mouse_move(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_click(self, event):
        self._click_x = event.x
        self._click_y = event.y

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def set_color(self, obj, color):
        self._canvas.itemconfig(obj, fill=color, outline=color)

    def find_overlapping(self, x1, y1, x2, y2):
        return self._canvas.find_overlapping(x1, y1, x2, y2)

    def moveto(self, obj, x, y):
        bbox = self._canvas.bbox(obj)
        if bbox:
            current_x, current_y = bbox[0], bbox[1]
            dx = x - current_x
            dy = y - current_y
            self._canvas.move(obj, dx, dy)
        self._tk.update()

    def get_mouse_x(self):
        return self._mouse_x

    def get_mouse_y(self):
        return self._mouse_y

    def wait_for_click(self):
        self._click_x = None
        self._click_y = None
        while self._click_x is None or self._click_y is None:
            self._tk.update()
        return

    def get_last_click(self):
        return self._click_x, self._click_y
