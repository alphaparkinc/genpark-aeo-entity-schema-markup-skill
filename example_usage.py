"""
example_usage.py -- Demonstrates AEOEntitySchemaMarkupClient
"""
from client import AEOEntitySchemaMarkupClient

def main():
    client = AEOEntitySchemaMarkupClient()
    result = client.generate_schema(
        product_name="Zenith Earbuds Pro",
        price_usd=89.99,
        sku="EAR-ZEN-01"
    )
    print("[AEO Entity Schema Result]")
    print(result['json_ld_schema'])

if __name__ == "__main__":
    main()
