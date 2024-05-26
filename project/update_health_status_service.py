import prisma
import prisma.models
from pydantic import BaseModel


class HealthCheckUpdateResponse(BaseModel):
    """
    Response model confirming the health status update.
    """

    confirmationMessage: str


async def update_health_status(statusMessage: str) -> HealthCheckUpdateResponse:
    """
    This endpoint allows updating the existing health status entry. It would accept relevant health data in the request body and update the current status accordingly. Expected response is a confirmation message that the health status was updated. It is primarily intended for maintenance purposes.

    Args:
    statusMessage (str): The new status message for the health check update.

    Returns:
    HealthCheckUpdateResponse: Response model confirming the health status update.

    Example:
        statusMessage = "All systems functional"
        await update_health_status(statusMessage)
        > HealthCheckUpdateResponse(confirmationMessage="Health status updated to: All systems functional")
    """
    await prisma.models.HealthCheckModule.prisma().update(
        where={"id": 1}, data={"statusMessage": statusMessage}
    )
    response = HealthCheckUpdateResponse(
        confirmationMessage=f"Health status updated to: {statusMessage}"
    )
    return response
