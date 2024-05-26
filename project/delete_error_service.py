import prisma
import prisma.models
from pydantic import BaseModel


class DeleteErrorResponseModel(BaseModel):
    """
    Response model indicating the success of the error message deletion.
    """

    message: str


async def delete_error(id: int) -> DeleteErrorResponseModel:
    """
    This endpoint deletes an existing error message by its ID. It is mainly used by administrators to clean up old or resolved errors.

    Args:
        id (int): The ID of the error message to be deleted.

    Returns:
        DeleteErrorResponseModel: Response model indicating the success of the error message deletion.

    Example:
        delete_error(1)
        > DeleteErrorResponseModel(message='Error message deleted successfully')
    """
    await prisma.models.ErrorHandlingModule.prisma().delete(where={"id": id})
    return DeleteErrorResponseModel(message="Error message deleted successfully")
