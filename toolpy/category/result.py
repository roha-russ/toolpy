from typing import Callable


class Result[T]:
    def __init__(self, value: T = None, error: Exception = None):
        self.__value = value
        self.__error = error

    @staticmethod
    def ok(value: T) -> "Result[T]":
        return Result(value, None)

    @staticmethod
    def err(error: Exception) -> "Result[T]":
        return Result(None, error)

    def is_ok(self) -> bool:
        return self.__value is not None

    def is_err(self) -> bool:
        return self.__error is not None

    def unwrap(self) -> T:
        if self.is_err():
            raise ValueError("Called unwrap on an error value")

        return self.__value

    def unwrap_or(self, default: T) -> T:
        if self.is_err():
            return default

        return self.__value

    def unwrap_or_none(self) -> T:
        return self.__value

    def unwrap_err(self) -> Exception:
        if self.is_ok():
            raise ValueError("Called unwrap_err on a value")

        return self.__error

    def unwrap_err_or(self, default: Exception) -> Exception:
        if self.is_ok():
            return default

        return self.__error

    def unwrap_err_or_none(self) -> Exception:
        return self.__error


def wrap[T](runnable: Callable[[], T]) -> Result[T]:
    try:
        return Result.ok(runnable())
    except Exception as e:
        return Result.err(e)

