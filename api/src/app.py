import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.database.db_init import engine, Base
from src.router import record_router, deleted_router, sentence_router
from src.utils.logging import logger, setup_uvicorn_log_config
from src.utils.config import config, CONFIG_ENV

API_VERSION = config[CONFIG_ENV].VERSION

Base.metadata.create_all(bind=engine)
app = FastAPI(title="SpeechApi", version=API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"]  # Allow all headers
)

app.include_router(record_router.router, prefix=f"/api/{API_VERSION}")
app.include_router(deleted_router.router, prefix=f"/api/{API_VERSION}")
app.include_router(sentence_router.router, prefix=f"/api/{API_VERSION}")


if __name__ == "__main__":
    setup_uvicorn_log_config()
    logger.info("Swagger documentation is accessible at http://{}:{}/docs"
                .format(config[CONFIG_ENV].HOST, config[CONFIG_ENV].PORT))
    uvicorn.run(app, host=config[CONFIG_ENV].HOST, port=config[CONFIG_ENV].PORT)

