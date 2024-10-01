
class Option[T]:
    def __init__(self, value: T = None):
        self.__value = value

    def is_some(self) -> bool:
        if self.__value is None:
            return False

        return True

    def is_none(self) -> bool:
        return not self.is_some()

    def unwrap(self) -> T:
        if self.is_none():
            raise ValueError("Called unwrap on a None value")

        return self.__value

    def unwrap_or(self, default: T) -> T:
        if self.is_none():
            return default

        return self.__value

