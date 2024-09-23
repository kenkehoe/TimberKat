from __future__ import annotations


class TimberKat:
    def __init__(self, base_text=None):
        self.base_text = base_text

    def timberify(self):
        """"TimberKat a given string."""
        timberified = self.base_text + '_timber'
        self.base_text = timberified
        return timberified

    def untimberify(self):
        stripped_text = self.base_text.replace('_timber', '')
        self.base_text = stripped_text
        return stripped_text
