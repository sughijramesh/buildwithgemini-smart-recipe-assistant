from google.cloud import firestore

# CRITICAL: Hardcode project ID as string for Firestore Client
FIRESTORE_PROJECT = "qwiklabs-gcp-02-aad533fba737"

SAMPLE_RECIPES = [
    {
        "id": "recipe-001",
        "name": "Avocado & Egg Sourdough Toast",
        "category": "Breakfast",
        "prep_time_minutes": 10,
        "ingredients": ["2 slices sourdough bread", "1 ripe avocado", "2 eggs", "salt", "black pepper", "chili flakes"],
        "instructions": "Toast the sourdough bread. Mash the ripe avocado with salt and pepper. Poach or fry the eggs. Spread mashed avocado onto toast, top with eggs and sprinkle chili flakes."
    },
    {
        "id": "recipe-002",
        "name": "Creamy Garlic Parmesan Pasta",
        "category": "Dinner",
        "prep_time_minutes": 20,
        "ingredients": ["8 oz fettuccine", "3 cloves garlic minced", "1 cup heavy cream", "1 cup grated parmesan cheese", "2 tbsp butter", "fresh parsley"],
        "instructions": "Boil fettuccine until al dente. In a skillet, melt butter and sauté garlic for 1 minute. Add heavy cream and bring to simmer. Stir in parmesan until smooth. Toss pasta in sauce and garnish with parsley."
    },
    {
        "id": "recipe-003",
        "name": "Mediterranean Chickpea Salad",
        "category": "Lunch",
        "prep_time_minutes": 15,
        "ingredients": ["1 can chickpeas drained", "1 cucumber diced", "1 cup cherry tomatoes halved", "1/2 cup feta cheese", "2 tbsp olive oil", "1 tbsp lemon juice"],
        "instructions": "Combine chickpeas, diced cucumber, halved cherry tomatoes, and crumbled feta in a salad bowl. Whisk olive oil and lemon juice together, pour over salad, and toss gently."
    }
]

def seed_firestore():
    print(f"Connecting to Firestore with project ID: '{FIRESTORE_PROJECT}'...")
    db = firestore.Client(project=FIRESTORE_PROJECT)
    collection_ref = db.collection("recipes")

    for recipe in SAMPLE_RECIPES:
        doc_ref = collection_ref.document(recipe["id"])
        doc_ref.set(recipe)
        print(f"Seeded recipe: {recipe['name']} (ID: {recipe['id']})")

    print("Firestore seeding complete! ✅")

if __name__ == "__main__":
    seed_firestore()
