import prisma
import prisma.models
from pydantic import BaseModel


class HealthCheckDeleteRequest(BaseModel):
    """
    Request model for the DELETE /health endpoint. This endpoint is used to delete an existing health status entry from the logging system and is intended for administrative clean-up purposes.
    """

    pass


class HealthCheckDeleteResponse(BaseModel):
    """
    Response model for the DELETE /health endpoint, confirming the deletion of the health status entry.
    """

    confirmation_message: str


async def delete_health_status(
    request: HealthCheckDeleteRequest,
) -> HealthCheckDeleteResponse:
    """
    This endpoint allows deletion of the existing health status entry from the logging system. Expected response is a confirmation message that the health status was deleted. It is intended for administrative clean-up purposes.

    Args:
        request (HealthCheckDeleteRequest): Request model for the DELETE /health endpoint. This endpoint is used to delete an existing health status entry from the logging system and is intended for administrative clean-up purposes.

    Returns:
        HealthCheckDeleteResponse: Response model for the DELETE /health endpoint, confirming the deletion of the health status entry.

    Example:
        request = HealthCheckDeleteRequest(id=1)
        response = await delete_health_status(request)
        > HealthCheckDeleteResponse(confirmation_message="Health status with id 1 has been deleted")
    """
    await prisma.models.HealthCheckModule.prisma().delete(
        where={"id": request.id}
    )  # TODO(autogpt): Cannot access attribute "id" for class "HealthCheckDeleteRequest"
    #     Attribute "id" is unknown. reportAttributeAccessIssue
    confirmation_message = f"Health status with id {request.id} has been deleted"  # TODO(autogpt): Cannot access attribute "id" for class "HealthCheckDeleteRequest"
    #     Attribute "id" is unknown. reportAttributeAccessIssue
    return HealthCheckDeleteResponse(confirmation_message=confirmation_message)
