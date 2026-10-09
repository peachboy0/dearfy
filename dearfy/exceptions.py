
# ! Dearfy Exceptions

class DearfyNoContentException(Exception):
    """Item must contain child items."""

class DearfyAppNoInited(Exception):
    """The application has not yet been initialized."""