

from ..utils import Object


class InputFileGenerated(Object):
    """
    A file generated by the client 

    Attributes:
        ID (:obj:`str`): ``InputFileGenerated``

    Args:
        original_path (:obj:`str`):
            Local path to a file from which the file is generated; may be empty if there is no such file
        conversion (:obj:`str`):
            String specifying the conversion applied to the original file; should be persistent across application restartsConversions beginning with '#' are reserved for internal TDLib usage
        expected_size (:obj:`int`):
            Expected size of the generated file; 0 if unknown

    Returns:
        InputFile

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputFileGenerated"

    def __init__(self, original_path, conversion, expected_size, **kwargs):
        
        self.original_path = original_path  # str
        self.conversion = conversion  # str
        self.expected_size = expected_size  # int

    @staticmethod
    def read(q: dict, *args) -> "InputFileGenerated":
        original_path = q.get('original_path')
        conversion = q.get('conversion')
        expected_size = q.get('expected_size')
        return InputFileGenerated(original_path, conversion, expected_size)
