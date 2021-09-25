import requests
import requests_cache
import time

requests_cache.install_cache()

url = "https://api.spoonacular.com/recipes/{id}/information"

headers  = {
	"Content-Type": "application/json"
}

payload = {
	"apiKey": "9be7f7b6675e424bb9ee4d7598c9b6dd"
	,"id":  "716429"
	,"includeNutrition": False
}

def spoonacular(payload):
	response = requests.get()

	if not getattr(response, 'from_cache', False):
		time.sleep(0.25)