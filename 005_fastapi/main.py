from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World, from FastAPI"
    }


@app.get("/demo")
async def demo():
    return {
        "message": "This is the output from demo function"
    }

@app.post("/post_demo")
async def post_demo():
    return {
        "message": "This is the output from post function"
    }

# @app.post
# @app.put
# @app.delete