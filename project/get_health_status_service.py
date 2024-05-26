import prisma
import prisma.models
from pydantic import BaseModel


class HealthCheckRequestModel(BaseModel):
    """
    Request model for the health check endpoint. Since this endpoint does not require any parameters, the Fields array will be empty.
    """

    pass


class HealthCheckResponseModel(BaseModel):
    """
    Response model for the health check endpoint, indicating the status of the API. If the API is operational, the status will be 'ok'. If there's an error, other status messages will be provided.
    """

    status: str


async def get_health_status(
    request: HealthCheckRequestModel,
) -> HealthCheckResponseModel:
    """
    This endpoint checks the health status of the API. When called, it returns a simple JSON object that indicates if the API is running correctly.
    Expected response is a JSON object with a 'status' key set to 'ok'. In case of failure, it interacts with the ErrorHandlingModule to return appropriate status messages.

    Args:
    request (HealthCheckRequestModel): Request model for the health check endpoint. Since this endpoint does not require any parameters, the Fields array will be empty.

    Returns:
    HealthCheckResponseModel: Response model for the health check endpoint, indicating the status of the API. If the API is operational, the status will be 'ok'. If there's an error, other status messages will be provided.

    Example:
        request = HealthCheckRequestModel()
        response = await get_health_status(request)
        print(response.status)  # Will print 'ok' if API is running correctly
    """
    try:
        health_check = await prisma.models.HealthCheckModule.prisma().find_first()
        if health_check:
            return HealthCheckResponseModel(status=health_check.statusMessage)
        else:
            return HealthCheckResponseModel(
                status="Health check module not configured."
            )
    except Exception as e:
        error_message = await prisma.models.ErrorHandlingModule.prisma().find_first()
        if error_message:
            return HealthCheckResponseModel(status=error_message.errorMessage)
        else:
            return HealthCheckResponseModel(status=f"Error Occurred: {str(e)}")
