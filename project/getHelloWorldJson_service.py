import prisma
import prisma.models
from pydantic import BaseModel


class HelloWorldRequest(BaseModel):
    """
    Request model for the 'Hello, World!' endpoint. This endpoint does not require any request parameters.
    """

    pass


class HelloWorldResponse(BaseModel):
    """
    Response model for the 'Hello, World!' endpoint. Returns a JSON object containing the 'Hello, World!' message.
    """

    message: str


async def getHelloWorldJson(request: HelloWorldRequest) -> HelloWorldResponse:
    """
    This endpoint returns a JSON object containing the 'Hello, World!' message.
    The response format is {'message': 'Hello, World!'}. This endpoint is also open to all users and admins.

    Args:
    request (HelloWorldRequest): Request model for the 'Hello, World!' endpoint. This endpoint does not require any request parameters.

    Returns:
    HelloWorldResponse: Response model for the 'Hello, World!' endpoint. Returns a JSON object containing the 'Hello, World!' message.

    Example:
        request = HelloWorldRequest()
        response = await getHelloWorldJson(request)
        assert response.message == 'Hello, World!'
    """
    hello_world_module = await prisma.models.HelloWorldModule.prisma().find_first()
    response_message = (
        hello_world_module.message if hello_world_module else "Hello, World!"
    )
    return HelloWorldResponse(message=response_message)
