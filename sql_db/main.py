from fastapi import FastAPI

from database import database, metadata, engine

from endpoints import router

import uvicorn
app = FastAPI()

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
