#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SERVEUR MOCK DU WALKING SKELETON SHOPLOC (Port 8082)
Permet d'afficher la reponse JSON du microservice catalogue pour la capture d'ecran.
Appuyez sur Ctrl+C pour arreter le serveur apres avoir pris votre capture.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CatalogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response_data = {
            "id": 1,
            "merchantId": 101,
            "merchantName": "Le Fournil de Suzanne",
            "name": "Baguette Tradition Artisanale",
            "description": "Farine de ble francaise Label Rouge, fermentation lente 24h",
            "priceInCents": 130,
            "stockAvailable": 45,
            "status": "AVAILABLE"
        }
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("X-Correlation-ID", "c9bf9e57-1685-4c89-bafb-ff5af830be8a")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=2, ensure_ascii=False).encode("utf-8"))

    def log_message(self, format, *args):
        print(f"[REQUETE RECUE] {self.address_string()} - {format % args}")

def main():
    port = 8082
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, CatalogHandler)
    print("=" * 65)
    print(f"SERVEUR WALKING SKELETON ACTIF SUR LE PORT {port}")
    print(f"Ouvrez dans votre navigateur : http://localhost:{port}/api/v1/catalog/products/1")
    print("Prenez votre capture d'ecran, puis faites Ctrl+C pour arreter.")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArret du serveur.")

if __name__ == "__main__":
    main()
