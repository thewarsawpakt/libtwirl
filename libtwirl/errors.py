class TwirlException(Exception):
    pass


class IncorrectArgumentFormatError(TwirlException):
    def __init__(self, *args):
        print(f"Incorrect argument(s): {args[0]}")


class PackageNotFoundError(TwirlException):
    def __init__(self, package):
        print(f"Package {package} Not found")
