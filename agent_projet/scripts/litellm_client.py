"""Module d'integration client pour la passerelle LiteLLM Proxy locale (ShopLoc).

Permet d'interroger LiteLLM (http://localhost:4000/v1) de maniere standardisee
en s'appuyant sur la cle virtuelle du projet et les alias universels (smart, fast, coding).
"""

import os
import json
import urllib.request
import urllib.error
from typing import Dict, List, Any, Optional

DEFAULT_LITELLM_URL = "http://localhost:4000/v1"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

def load_project_env() -> Dict[str, str]:
    """Charge les variables d'environnement depuis .env et config.local.json."""
    config = {}
    
    # 1. Lecture de config.local.json
    local_cfg_path = os.path.join(PROJECT_ROOT, "config.local.json")
    if os.path.isfile(local_cfg_path):
        try:
            with open(local_cfg_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "litellm_base_url" in data:
                    config["OPENAI_BASE_URL"] = data["litellm_base_url"]
        except Exception:
            pass

    # 2. Lecture de .env
    env_path = os.path.join(PROJECT_ROOT, ".env")
    if os.path.isfile(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        config[k.strip()] = v.strip().strip("\"'")
        except Exception:
            pass

    # 3. Variables systemes prioritaires
    for key in ["OPENAI_BASE_URL", "OPENAI_API_KEY", "LITELLM_BASE_URL"]:
        if os.getenv(key):
            config[key] = os.getenv(key)

    return config

def check_gateway_health(base_url: Optional[str] = None, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Verifie la disponibilite de la passerelle LiteLLM."""
    cfg = load_project_env()
    url = (base_url or cfg.get("OPENAI_BASE_URL") or DEFAULT_LITELLM_URL).rstrip("/")
    if url.endswith("/v1"):
        health_url = url[:-3] + "/health"
        models_url = url[:-3] + "/models"
    else:
        health_url = url + "/health"
        models_url = url + "/models"

    key = api_key or cfg.get("OPENAI_API_KEY", "")
    headers = {"Authorization": f"Bearer {key}"} if key else {}

    result = {
        "status": "offline",
        "url": url,
        "models_count": 0,
        "error": None
    }

    try:
        req = urllib.request.Request(models_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                result["status"] = "online"
                result["models_count"] = len(data.get("data", []))
                return result
    except Exception as e:
        result["error"] = str(e)

    return result

def chat_completion(
    messages: List[Dict[str, str]],
    model: str = "fast",
    temperature: float = 0.2,
    max_tokens: Optional[int] = None,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    user: Optional[str] = "agent_shoploc",
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Envoie une requete de completion a la passerelle LiteLLM locale."""
    cfg = load_project_env()
    url = (base_url or cfg.get("OPENAI_BASE_URL") or DEFAULT_LITELLM_URL).rstrip("/")
    endpoint = f"{url}/chat/completions" if not url.endswith("/chat/completions") else url

    key = api_key or cfg.get("OPENAI_API_KEY", "")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature
    }
    if max_tokens:
        payload["max_tokens"] = max_tokens
    if user:
        payload["user"] = user

    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data_bytes, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as he:
        err_body = he.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Erreur HTTP LiteLLM ({he.code}): {err_body}") from he
    except Exception as exc:
        raise RuntimeError(f"Erreur de communication avec LiteLLM Proxy ({url}): {exc}") from exc

def quick_prompt(prompt: str, model: str = "fast", user: str = "agent_shoploc") -> str:
    """Helper simple pour envoyer un prompt texte et recuperer la reponse brute."""
    resp = chat_completion(messages=[{"role": "user", "content": prompt}], model=model, user=user)
    return resp["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Verification de la connexion LiteLLM Proxy pour ShopLoc...")
    health = check_gateway_health()
    print(f"Statut Passerelle : {health['status'].upper()}")
    print(f"URL Passerelle    : {health['url']}")
    print(f"Modeles exposes   : {health['models_count']}")
    
    if health["status"] == "online":
        print("\nTest de completion avec le modele 'fast'...")
        try:
            ans = quick_prompt("Reponds simplement en 5 mots maximum: pret a servir ShopLoc.")
            print(f"Reponse reçue : {ans.strip()}")
            print("\nSUCCES : La passerelle LiteLLM est pleinement operationnelle.")
        except Exception as err:
            print(f"Erreur lors de la completion : {err}")
    else:
        print(f"\nAvertissement : Passerelle inaccessible ({health['error']})")
