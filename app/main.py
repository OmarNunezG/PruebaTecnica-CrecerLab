from fastapi import FastAPI

version = "v1"

description = """
A REST API for an event notification web service.

This REST API is able to:
- Create, read, update and delete events.
"""

app = FastAPI(
    title="Prueba Técnica - Omar Núñez",
    description=description,
    version=version,
    contact={
        "name": "Omar Núñez",
        "url": "https://github.com/OmarNunezG/PruebaTecnica-CrecerLab",
        "email": "o.nunez@softwy.com",
    },
    openapi_url="/documentation/schema.json",
    docs_url="/documentation/swagger",
    redoc_url="/documentation/redoc",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
