from google import genai



def get_car_bio(model,brand,year):

    client = genai.Client(api_key="Sua chave aqui")
    # Definindo o modelo e o prompt

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=[f"Gere uma descrição de venda para um carro {model} da marca {brand}, ano {year}, com no máximo 250 caracteres. Apenas a descrição, sem introduções, explicações ou formatações adicionais."]
    )
    return response.text



# class Llama():
    # def __init__(self,model,brand,year):
    #     self.model = model
    #     self.brand = brand
    #     self.year = year
    #     pass
    
    # # Definindo a URL e os cabeçalhos
    # url = "http://localhost:1234/v1/chat/completions"
    # headers = {"Content-Type": "application/json"}
    
    # data = {
    #     "model": "llama-3.2-1b-instruct",
    #     "messages": [
            
    #         {"role": "user",
    #             "content": "Me mostre uma descriçao de venda para o carro {self.model} da marca {self.brand} do ano {self.year} em apenas 250 caracteres"}
                
    #     ],
    #     "temperature": 0.7,
    #     "max_tokens": -1,
    #     "stream": False
    # }

    # def api_get(self):
    #     # Fazendo a requisição POST
    #     print("Consumindo LLM...")
    #     response = requests.post(
    #         Llama.url, headers=Llama.headers, json=Llama.data)
    #     content = response.json()
    #     content = content.get('choices')[0].get('message').get('content')
    #     # Verificando e exibindo a resposta
    #     if response.status_code == 200:
    #         return content
    #     else:
    #         print("Erro:", response.status_code, response.text)


