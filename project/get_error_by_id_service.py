import prisma
import prisma.models
from pydantic import BaseModel


class ErrorResponseModel(BaseModel):
    """
    The response model containing the details of a specific error message. This includes the error message, resolution, and code.
    """

    id: int
    errorMessage: str
    resolution: str
    code: int


async def get_error_by_id(id: int) -> ErrorResponseModel:
    """
    This endpoint retrieves a specific error message by its ID. It is useful for viewing detailed information about a single error. The expected response is a JSON object containing the error details.

    Args:
    id (int): The ID of the error message to be retrieved.

    Returns:
    ErrorResponseModel: The response model containing the details of a specific error message. This includes the error message, resolution, and code.

    Example:
        error = await get_error_by_id(1)
        print(error)
        # ErrorResponseModel(id=1, errorMessage="Example error", resolution="Example resolution", code=500)
    """
    error = await prisma.models.ErrorHandlingModule.prisma().find_unique(
        where={"id": id}
    )
    if error is None:
        raise ValueError(f"No error found with ID {id}")
    return ErrorResponseModel(
        id=error.id,
        errorMessage=error.errorMessage,
        resolution=error.resolution,
        code=error.code,
    )
