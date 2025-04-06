from google import genai
from dotenv import load_dotenv



def get_car_bio(model,brand,year):

    load_dotenv()

    api_key = os.getenv('API_KEY')

    client = genai.Client(api_key)
    # Definindo o modelo e o prompt

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=[f"Gere uma descrição de venda para um carro {model} da marca {brand}, ano {year}, com no máximo 250 caracteres. Apenas a descrição, sem introduções, explicações ou formatações adicionais."]
    )
    return response.text



