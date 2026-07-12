"""
genpark-aeo-entity-schema-markup-skill: Client SDK
Auto-compiles structured JSON-LD specifications for search engines.
"""
from __future__ import annotations
import json
from typing import Optional


class AEOEntitySchemaMarkupClient:
    """
    SDK for Schema markup generator.
    """

    def generate_schema(
        self,
        product_name: str,
        price_usd: float,
        sku: str,
    ) -> dict:
        schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product_name,
            "sku": sku,
            "offers": {
                "@type": "Offer",
                "price": price_usd,
                "priceCurrency": "USD"
            }
        }

        return {
            "json_ld_schema": json.dumps(schema, indent=2)
        }
