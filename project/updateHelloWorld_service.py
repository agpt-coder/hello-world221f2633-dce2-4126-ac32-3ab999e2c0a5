import prisma
import prisma.models
from pydantic import BaseModel


class UpdateHelloWorldResponse(BaseModel):
    """
    Response model reflecting the updated 'Hello, World!' message.
    """

    message: str


async def updateHelloWorld(message: str) -> UpdateHelloWorldResponse:
    """
    This endpoint allows updating the 'Hello, World!' message. It expects a JSON payload with an updated 'message' field. Like the creation endpoint, this is restricted to admin users.

    Args:
        message (str): The new 'Hello, World!' message to be updated.

    Returns:
        UpdateHelloWorldResponse: Response model reflecting the updated 'Hello, World!' message.

    Example:
        response = await updateHelloWorld("Hello, Universe!")
        > UpdateHelloWorldResponse(message="Hello, Universe!")
    """
    hello_world_instance = await prisma.models.HelloWorldModule.prisma().find_first()
    if hello_world_instance:
        await prisma.models.HelloWorldModule.prisma().update(
            where={"id": hello_world_instance.id}, data={"message": message}
        )
    else:
        await prisma.models.HelloWorldModule.prisma().create(data={"message": message})
    return UpdateHelloWorldResponse(message=message)
