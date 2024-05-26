from typing import List

import prisma
import prisma.models
from pydantic import BaseModel


class GetErrorsRequestModel(BaseModel):
    """
    This request model is used for retrieving error messages. It doesn't require any additional parameters since it is a GET request for listing errors.
    """

    pass


class ErrorObject(BaseModel):
    """
    Details of an individual error recorded by the system.
    """

    id: int
    errorMessage: str
    resolution: str
    code: int


class ErrorListResponseModel(BaseModel):
    """
    A response model that returns a list of error objects recorded by the ErrorHandlingModule. This is meant for admin review and management of errors.
    """

    errors: List[ErrorObject]


async def get_errors(request: GetErrorsRequestModel) -> ErrorListResponseModel:
    """
    This endpoint retrieves a list of all error messages recorded by the ErrorHandlingModule. It is meant for use by administrators to review and manage errors. The expected response is a JSON array of error objects.

    Args:
        request (GetErrorsRequestModel): This request model is used for retrieving error messages. It doesn't require any additional parameters since it is a GET request for listing errors.

    Returns:
        ErrorListResponseModel: A response model that returns a list of error objects recorded by the ErrorHandlingModule. This is meant for admin review and management of errors.

    Example:
        request = GetErrorsRequestModel()
        response = await get_errors(request)
        > response.errors  # [ErrorObject(id=1, errorMessage='Error', resolution='Resolved', code=500)]
    """
    errors = await prisma.models.ErrorHandlingModule.prisma().find_many()
    error_objects = [
        ErrorObject(
            id=error.id,
            errorMessage=error.errorMessage,
            resolution=error.resolution,
            code=error.code,
        )
        for error in errors
    ]
    return ErrorListResponseModel(errors=error_objects)
