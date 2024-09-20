from __future__ import annotations
from crcmod.predefined import PredefinedCrc


def get_timberkat_crc_calculator() -> PredefinedCrc:
    return PredefinedCrc("crc-ccitt-false")


class TimberKat:
    def __init__(self, base_text: str):
        self.base_text = base_text
        self.crc_calculator = PredefinedCrc("crc-ccitt-false")

    def timberify(self) -> str:
        """"TimberKat a given string. Also updates internal CRC calculator with timberkat data."""
        timberified = self.base_text + 'timber'
        self.crc_calculator.new()
        self.crc_calculator.update(timberkat.encode())
        return timberified

    @classmethod
    def untimberify(cls, timberkat_text: str) -> TimberKat:
        """Generates a new :py:class:`TimberKat` instance from a timberkat text.
        """
        stripped_text = timberkat_text.rstrip('timber')
        instance = cls(stripped_text)
        instance.crc_calculator.update(timberkat_text.encode())
        return instance
