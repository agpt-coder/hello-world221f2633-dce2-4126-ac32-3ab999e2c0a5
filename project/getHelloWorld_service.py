from typing import Optional

import prisma
import prisma.models
from pydantic import BaseModel


class HelloWorldRequestModel(BaseModel):
    """
    The request model for the HelloWorld endpoint has no parameters as it just returns a 'Hello, World!' message.
    """

    pass


class HelloWorldResponseModel(BaseModel):
    """
    The response model for the HelloWorld endpoint contains a plain text message 'Hello, World!'.
    """

    message: str


async def getHelloWorld(request: HelloWorldRequestModel) -> HelloWorldResponseModel:
    """
    This endpoint returns a simple 'Hello, World!' message in plain text. It doesn't accept any parameters and is accessible to all users and admins.

    Args:
    request (HelloWorldRequestModel): The request model for the HelloWorld endpoint has no parameters as it just returns a 'Hello, World!' message.

    Returns:
    HelloWorldResponseModel: The response model for the HelloWorld endpoint contains a plain text message 'Hello, World!'.

    Example:
    request = HelloWorldRequestModel()
    response = getHelloWorld(request)
    print(response.message)  # 'Hello, World!'
    """
    hello_world_module: Optional[
        prisma.models.HelloWorldModule
    ] = await prisma.models.HelloWorldModule.prisma().find_first()
    if hello_world_module is None:
        message = "Hello, World!"
    else:
        message = hello_world_module.message
    response = HelloWorldResponseModel(message=message)
    return response
