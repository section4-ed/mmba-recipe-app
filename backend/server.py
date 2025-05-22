from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from main import process_recipes

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_recipe")
async def process_recipe_endpoint(file: UploadFile):
    # Read the contents of the uploaded file
    content = await file.read()
    recipe_text = content.decode('utf-8')
    
    # Process the recipe using imported function
    result = process_recipes(recipe_text)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
