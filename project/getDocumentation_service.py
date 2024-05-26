import prisma
import prisma.enums
import prisma.models
from pydantic import BaseModel


class GetApiDocsRequest(BaseModel):
    """
    This request doesn't require any parameters as it serves static documentation for the 'Hello, World!' endpoint.
    """

    pass


class GetApiDocsResponse(BaseModel):
    """
    This response provides the documentation details for the 'Hello, World!' API endpoint, including the endpoint, method, and description.
    """

    id: int
    endpoint: str
    method: prisma.enums.HttpMethod
    description: str


async def getDocumentation(request: GetApiDocsRequest) -> GetApiDocsResponse:
    """
    This endpoint provides the documentation for the 'Hello, World!' API.
    It interacts with the HelloWorldModule to fetch endpoint details and returns them in a structured format.
    It's designed to be publicly accessible, allowing users and developers to understand how to interact with the API.

    Args:
    request (GetApiDocsRequest): This request doesn't require any parameters as it serves static documentation for the 'Hello, World!' endpoint.

    Returns:
    GetApiDocsResponse: This response provides the documentation details for the 'Hello, World!' API endpoint, including the endpoint, method, and description.

    Example:
        request = GetApiDocsRequest()
        response = await getDocumentation(request)
        > GetApiDocsResponse(id=1, endpoint='/hello', method='GET', description='Returns Hello, World message')
    """
    documentation_entry = await prisma.models.DocumentationModule.prisma().find_first()
    if not documentation_entry:
        raise ValueError("No documentation entry found.")
    return GetApiDocsResponse(
        id=documentation_entry.id,
        endpoint=documentation_entry.endpoint,
        method=documentation_entry.method,
        description=documentation_entry.description,
    )
