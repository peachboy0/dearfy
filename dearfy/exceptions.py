
# ! Dearfy Exceptions

class DearfyNoContentError(Exception):
    """Item must contain child items."""

class DearfyAppNoInitedError(Exception):
    """The application has not yet been initialized."""

class DearfyNotItemError(Exception):
    pass