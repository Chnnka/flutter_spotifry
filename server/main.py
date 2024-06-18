from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get('/')
def test(): 
    return 'hello world'