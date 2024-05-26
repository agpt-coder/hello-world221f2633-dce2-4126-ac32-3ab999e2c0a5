import prisma
import prisma.models
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    Response model for the created error object. It includes the unique ID of the error, the error code, and the error message.
    """

    id: int
    code: int
    message: str


async def create_error(code: int, message: str) -> ErrorResponse:
    """
    This endpoint allows for the creation of a new error message. It is used internally by other modules to log errors. It accepts a JSON object with 'code' and 'message' fields as input and returns the created error object with a unique ID.

    Args:
    code (int): The error code representing the type of error.
    message (str): The detailed error message explaining the error.

    Returns:
    ErrorResponse: Response model for the created error object. It includes the unique ID of the error, the error code, and the error message.

    Example:
    > create_error(404, 'Not Found')
    > ErrorResponse(id=1, code=404, message='Not Found')
    """
    new_error = await prisma.models.ErrorHandlingModule.prisma().create(
        data={"errorMessage": message, "resolution": "", "code": code}
    )
    return ErrorResponse(
        id=new_error.id, code=new_error.code, message=new_error.errorMessage
    )
