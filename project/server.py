import logging
from contextlib import asynccontextmanager

import prisma
import prisma.enums
import project.create_error_service
import project.create_health_status_service
import project.createHelloWorld_service
import project.delete_error_service
import project.delete_health_status_service
import project.deleteHelloWorld_service
import project.get_error_by_id_service
import project.get_errors_service
import project.get_health_status_service
import project.get_hello_world_service
import project.getDocumentation_service
import project.getHelloWorld_service
import project.getHelloWorldJson_service
import project.update_error_service
import project.update_health_status_service
import project.updateHelloWorld_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="hello world",
    lifespan=lifespan,
    description="create an api that returns just hello world.",
)


@app.post(
    "/helloworld",
    response_model=project.createHelloWorld_service.HelloWorldPostResponse,
)
async def api_post_createHelloWorld(
    message: str, responseType: prisma.enums.ResponseType
) -> project.createHelloWorld_service.HelloWorldPostResponse | Response:
    """
    This endpoint allows the creation of a new 'Hello, World!' message. It accepts a JSON payload with a 'message' field. This new message can then be fetched via the GET endpoints. Only admin users can create new messages.
    """
    try:
        res = project.createHelloWorld_service.createHelloWorld(message, responseType)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.put(
    "/api/errors/{id}",
    response_model=project.update_error_service.UpdateErrorResponseModel,
)
async def api_put_update_error(
    id: int, code: int, message: str
) -> project.update_error_service.UpdateErrorResponseModel | Response:
    """
    This endpoint updates an existing error message by its ID. It accepts a JSON object with updated 'code' and 'message' fields and the ID of the error to update in the URL path. The expected response is the updated error object.
    """
    try:
        res = await project.update_error_service.update_error(id, code, message)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/hello", response_model=project.get_hello_world_service.HelloWorldResponse
)
async def api_get_get_hello_world(
    request: project.get_hello_world_service.HelloWorldRequest,
) -> project.get_hello_world_service.HelloWorldResponse | Response:
    """
    This endpoint returns a simple 'Hello World' message. It doesn't require any input parameters and returns a JSON object containing the message. The purpose is to verify that the API is working correctly.
    """
    try:
        res = project.get_hello_world_service.get_hello_world(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.delete(
    "/api/errors/{id}",
    response_model=project.delete_error_service.DeleteErrorResponseModel,
)
async def api_delete_delete_error(
    id: int,
) -> project.delete_error_service.DeleteErrorResponseModel | Response:
    """
    This endpoint deletes an existing error message by its ID. It is mainly used by administrators to clean up old or resolved errors. The expected response is a success message indicating the error has been deleted.
    """
    try:
        res = await project.delete_error_service.delete_error(id)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post(
    "/health", response_model=project.create_health_status_service.HealthCheckResponse
)
async def api_post_create_health_status(
    statusMessage: str, adminId: int
) -> project.create_health_status_service.HealthCheckResponse | Response:
    """
    This endpoint is meant for updating or initiating new health status entry for the API logging purpose. Expected response is a confirmation message that the health status entry was created. Generally, this won't be typically used frequently and is kept primarily for administrative use.
    """
    try:
        res = project.create_health_status_service.create_health_status(
            statusMessage, adminId
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.delete(
    "/helloworld",
    response_model=project.deleteHelloWorld_service.DeleteHelloWorldResponseModel,
)
async def api_delete_deleteHelloWorld(
    request: project.deleteHelloWorld_service.DeleteHelloWorldRequestModel,
) -> project.deleteHelloWorld_service.DeleteHelloWorldResponseModel | Response:
    """
    This endpoint allows deleting the 'Hello, World!' message. It's a destructive operation and hence restricted to admin users only. After deletion, the GET endpoints will no longer return the message.
    """
    try:
        res = project.deleteHelloWorld_service.deleteHelloWorld(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/helloworld", response_model=project.getHelloWorld_service.HelloWorldResponseModel
)
async def api_get_getHelloWorld(
    request: project.getHelloWorld_service.HelloWorldRequestModel,
) -> project.getHelloWorld_service.HelloWorldResponseModel | Response:
    """
    This endpoint returns a simple 'Hello, World!' message in plain text. It doesn't accept any parameters and is accessible to all users and admins.
    """
    try:
        res = await project.getHelloWorld_service.getHelloWorld(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.put(
    "/health",
    response_model=project.update_health_status_service.HealthCheckUpdateResponse,
)
async def api_put_update_health_status(
    statusMessage: str,
) -> project.update_health_status_service.HealthCheckUpdateResponse | Response:
    """
    This endpoint allows updating the existing health status entry. It would accept relevant health data in the request body and update the current status accordingly. Expected response is a confirmation message that the health status was updated. It is primarily intended for maintenance purposes.
    """
    try:
        res = await project.update_health_status_service.update_health_status(
            statusMessage
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.put(
    "/helloworld",
    response_model=project.updateHelloWorld_service.UpdateHelloWorldResponse,
)
async def api_put_updateHelloWorld(
    message: str,
) -> project.updateHelloWorld_service.UpdateHelloWorldResponse | Response:
    """
    This endpoint allows updating the 'Hello, World!' message. It expects a JSON payload with an updated 'message' field. Like the creation endpoint, this is restricted to admin users.
    """
    try:
        res = await project.updateHelloWorld_service.updateHelloWorld(message)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/helloworld/json",
    response_model=project.getHelloWorldJson_service.HelloWorldResponse,
)
async def api_get_getHelloWorldJson(
    request: project.getHelloWorldJson_service.HelloWorldRequest,
) -> project.getHelloWorldJson_service.HelloWorldResponse | Response:
    """
    This endpoint returns a JSON object containing the 'Hello, World!' message. The response format is {'message': 'Hello, World!'}. This endpoint is also open to all users and admins.
    """
    try:
        res = await project.getHelloWorldJson_service.getHelloWorldJson(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/errors", response_model=project.get_errors_service.ErrorListResponseModel
)
async def api_get_get_errors(
    request: project.get_errors_service.GetErrorsRequestModel,
) -> project.get_errors_service.ErrorListResponseModel | Response:
    """
    This endpoint retrieves a list of all error messages recorded by the ErrorHandlingModule. It is meant for use by administrators to review and manage errors. The expected response is a JSON array of error objects.
    """
    try:
        res = await project.get_errors_service.get_errors(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/health", response_model=project.get_health_status_service.HealthCheckResponseModel
)
async def api_get_get_health_status(
    request: project.get_health_status_service.HealthCheckRequestModel,
) -> project.get_health_status_service.HealthCheckResponseModel | Response:
    """
    This endpoint checks the health status of the API. When called, it returns a simple JSON object that indicates if the API is running correctly. Expected response is a JSON object with a 'status' key set to 'ok'. In case of failure, it interacts with the ErrorHandlingModule to return appropriate status messages.
    """
    try:
        res = await project.get_health_status_service.get_health_status(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post("/api/errors", response_model=project.create_error_service.ErrorResponse)
async def api_post_create_error(
    code: int, message: str
) -> project.create_error_service.ErrorResponse | Response:
    """
    This endpoint allows for the creation of a new error message. It is used internally by other modules to log errors. It accepts a JSON object with 'code' and 'message' fields as input and returns the created error object with a unique ID.
    """
    try:
        res = await project.create_error_service.create_error(code, message)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/errors/{id}",
    response_model=project.get_error_by_id_service.ErrorResponseModel,
)
async def api_get_get_error_by_id(
    id: int,
) -> project.get_error_by_id_service.ErrorResponseModel | Response:
    """
    This endpoint retrieves a specific error message by its ID. It is useful for viewing detailed information about a single error. The expected response is a JSON object containing the error details.
    """
    try:
        res = await project.get_error_by_id_service.get_error_by_id(id)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/api/docs", response_model=project.getDocumentation_service.GetApiDocsResponse
)
async def api_get_getDocumentation(
    request: project.getDocumentation_service.GetApiDocsRequest,
) -> project.getDocumentation_service.GetApiDocsResponse | Response:
    """
    This endpoint provides the documentation for the 'Hello, World!' API. It interacts with the HelloWorldModule to fetch endpoint details and returns them in a structured format. It's designed to be publicly accessible, allowing users and developers to understand how to interact with the API.
    """
    try:
        res = await project.getDocumentation_service.getDocumentation(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.delete(
    "/health",
    response_model=project.delete_health_status_service.HealthCheckDeleteResponse,
)
async def api_delete_delete_health_status(
    request: project.delete_health_status_service.HealthCheckDeleteRequest,
) -> project.delete_health_status_service.HealthCheckDeleteResponse | Response:
    """
    This endpoint allows deletion of the existing health status entry from the logging system. Expected response is a confirmation message that the health status was deleted. It is intended for administrative clean-up purposes.
    """
    try:
        res = await project.delete_health_status_service.delete_health_status(request)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
