import prisma
import prisma.models
from pydantic import BaseModel


class UpdateErrorResponseModel(BaseModel):
    """
    Response model that includes the updated error message details.
    """

    id: int
    errorMessage: str
    resolution: str
    code: int


async def update_error(id: int, code: int, message: str) -> UpdateErrorResponseModel:
    """
    This endpoint updates an existing error message by its ID. It accepts a JSON object with updated 'code' and 'message' fields and the ID of the error to update in the URL path. The expected response is the updated error object.

    Args:
    id (int): The ID of the error to update.
    code (int): The updated error code.
    message (str): The updated error message.

    Returns:
    UpdateErrorResponseModel: Response model that includes the updated error message details.

    Example:
        updated_error = await update_error(1, 404, 'Not Found')
        print(updated_error)
        # Output: UpdateErrorResponseModel(id=1, errorMessage='Not Found', resolution='Resolution', code=404)
    """
    existing_error = prisma.models.ErrorHandlingModule.prisma().find_unique(
        where={"id": id}
    )
    if not existing_error:
        raise ValueError(f"Error with ID {id} does not exist.")
    updated_error = prisma.models.ErrorHandlingModule.prisma().update(
        where={"id": id}, data={"code": code, "errorMessage": message}
    )
    return UpdateErrorResponseModel(
        id=updated_error.id,
        errorMessage=updated_error.errorMessage,
        resolution=updated_error.resolution,
        code=updated_error.code,
    )  # TODO(autogpt): Cannot access attribute "id" for class "Coroutine[Any, Any, ErrorHandlingModule | None]"


#     Attribute "id" is unknown. reportAttributeAccessIssue
