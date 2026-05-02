import pygame

class Text():
    def __init__(self, text, font, fsize, colText, textX, textY, win):
        self.text = text
        self.font = font
        self.fsize = fsize
        self.colText = colText
        self.textX = textX
        self.textY = textY
        self.win = win # окно типа виндоу
    def drawText(self):
        txt = pygame.font.Font(self.font, self.fsize).render(self.text, True, self.colText)
        self.win.blit(txt, (self.textX, self.textY))
    def setText(self, text):
        self.text = text
        self.drawText()

class SysText():
    def __init__(self, text, font, fsize, colText, textX, textY, win):
        self.text = text
        self.font = font
        self.fsize = fsize
        self.colText = colText
        self.textX = textX
        self.textY = textY
        self.win = win # окно типа виндоу
    def drawText(self):
        txt = pygame.font.SysFont(self.font, self.fsize).render(self.text, True, self.colText)
        self.win.blit(txt, (self.textX, self.textY))
    def setText(self, text):
        self.text = text
        self.drawText()

class SquareArea():
    def __init__(self, bg, x, y, wid, hid, col):
        self.bg = bg
        self.x = x
        self.y = y
        self.wid = wid
        self.hid = hid
        self.col = col

        self.rect = pygame.rect.Rect(self.x, self.y, self.wid, self.hid)
    def drawArea(self):
        pygame.draw.rect(self.bg, self.col, self.rect)

class Button(SquareArea, Text):
    def __init__(self, bg, x, y, wid, hid, col, text, font, fsize, colText, textX, textY):
        SquareArea.__init__(self, bg, x, y, wid, hid, col)
        Text.__init__(self, text, font, fsize, colText, textX, textY, bg)
    def drawButton(self, textTrue):
        self.drawArea()
        if textTrue:
            self.drawText()

class ButtonSysText(SquareArea, SysText):
    def __init__(self, bg, x, y, wid, hid, col, text, font, fsize, colText, textX, textY):
        SquareArea.__init__(self, bg, x, y, wid, hid, col)
        SysText.__init__(self, text, font, fsize, colText, textX, textY, bg)
    def drawButton(self, textTrue):
        self.drawArea()
        if textTrue:
            self.drawText()

class CircleArea():
    def __init__(self, bg):
        self.bg = bg