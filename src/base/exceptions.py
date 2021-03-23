"""Custom error types to unify the exception behaviour across all APIs."""


from typing import Optional


class TradingApiException(Exception):
    """Exception raised for general errors while communication with APIs.

    Attributes:
        message (str): The message. Defaults to "".
    """

    def __init__(self, message: Optional[str] = ""):
        """Exception raised for general errors while communication with APIs.

        Args:
            message (str, optional): The message. Defaults to "".
        """
        self.message = message
        super().__init__(self.message)


class TradingApiHttpException(Exception):
    """Exception raised for HTTP errors while communication with APIs."""

    def __init__(
        self,
        http_status_code: int,
        http_status_code_name: str,
        message: Optional[str] = "",
    ):
        """Exception raised for HTTP errors while communication with APIs.

        Args:
            http_status_code (int): The HTTP status code.
            http_status_code_name (str): The name of the HTTP status code.
            message (str, optional): The message. Defaults to "".
        """
        self.http_status_code = http_status_code
        self.http_status_code_name = http_status_code_name
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """String representation of the error.

        Returns:
            str: The string representation of the error.
        """
        return f"{self.http_status_code_name} ({self.http_status_code}): {self.message}"
