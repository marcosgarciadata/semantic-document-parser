from fastapi import FastAPI, UploadFile, File
from .engine import SemanticParser

app = FastAPI(title="Semantic API")
parser = SemanticParser()

@app.post("/parse")
async def parse_doc(file: UploadFile = File(...)):
    content = await file.read()
    return parser.parse(content.decode(), schema={})
