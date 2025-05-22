from openai import OpenAI
from models import *

client = OpenAI()

def process_recipes(recipes_text: str) -> Recipe:
    """
    Convert recipe text into structured data using OpenAI's format option.
    
    Args:
        recipe_text (str): The text of the recipe to parse
        
    Returns:
        Recipe: A structured Recipe object
    """
    print("executing prompt")
    response = client.responses.parse(
        model="gpt-4o-mini-2024-07-18",
        input=[
            {
                "role": "system",
                "content": "You are a helpful assistant that converts recipe text into structured data. Please convert the following recipes into a structured format."
            },
            {
                "role": "user",
                "content": f"Recipe text: {recipes_text}"
            }
        ],
        text_format=Recipe
    )
    print("finished recipes prompt")
    return response.output_parsed 

if __name__ == "__main__":
    # Example recipe text
    sample_recipe = """
    Classic Chocolate Chip Cookies
    
    Ingredients:
    - 2 1/4 cups flour
    - 1 tsp baking soda
    - 1 tsp salt
    - 1 cup butter, softened
    - 3/4 cup granulated sugar
    - 3/4 cup brown sugar
    - 2 eggs
    - 2 tsp vanilla extract
    - 2 cups chocolate chips
    
    Instructions:
    1. Preheat oven to 375°F
    2. Mix flour, baking soda and salt
    3. Beat butter and sugars until creamy
    4. Add eggs and vanilla
    5. Gradually mix in flour mixture
    6. Stir in chocolate chips
    7. Drop by rounded tablespoon onto ungreased baking sheets
    8. Bake 9-11 minutes until golden brown
    """
    
    # Process the recipe
    result = process_recipes(sample_recipe)
    
    # Print the structured result
    print("\nProcessed Recipe:")
    print(f"Title: {result.title}")
    print("\nIngredients:")
    for ingredient in result.ingredients:
        print(f"- {ingredient.amount} {ingredient.unit} {ingredient.name}")
    print("\nInstructions:")
    for i, instruction in enumerate(result.instructions, 1):
        print(f"{i}. {instruction}")
