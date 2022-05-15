from turtle import color


class Button:
    def __init__(self, position, input_text, font, base_color, hovering_color):
        self.x_position = position[0]
        self.y_position = position[1]
        self.input_text = input_text
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(self.input_text, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_position, self.y_position))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.text_rect.left, self.text_rect.right) and position[
            1
        ] in range(self.text_rect.top, self.text_rect.bottom):
            return True
        else:
            return False

    def changeColor(self, position):
        if position[0] in range(self.text_rect.left, self.text_rect.right) and position[
            1
        ] in range(self.text_rect.top, self.text_rect.bottom):
            self.text = self.font.render(self.input_text, True, self.hovering_color)
        else:
            self.text = self.font.render(self.input_text, True, self.base_color)
