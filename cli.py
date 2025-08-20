import requests
import webbrowser

def main():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json", "User-Agent": "jokebot/0.1"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        print(data.get("joke", "[sem piada]"))
    except Exception as e:
        print(f"Erro ao buscar piada: {e}")

def abrir_link():
    url = "https://i.imgur.com/4AiXzf8.jpeg"  # link de uma imagem engraçada
    webbrowser.open(url)

if __name__ == "__main__":
    main()
    abrir_link()

