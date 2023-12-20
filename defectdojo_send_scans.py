#!/usr/bin/python3

import requests
from datetime import datetime
import os

date = datetime.now().strftime('%Y-%m-%d')

class Defectdojo(object):

   def DefectdojoApi():

    # Defectdojo URL API
    url = "http://192.168.1.99:8080/api/v2"

    # API Key
    api_key = "c3f230eb846149d1d7e180dda5215b591f2346d8"

    # Headers
    headers = {
        "Authorization": f"Token {api_key}",
        "Accept": "application/json",
    }

    # Names of Product Type, Product and Engagement
    product_type_name = "Development Team"
    product_name = "Python Product"
    engagement_name = "Python Engagement"

    # Creating Product Type
    product_type_payload = {
        "name": product_type_name,
        "description": "Type of Product",
        "critical_product": "true",
        "key_product": "true",
    }
    product_type_response = requests.post(
        f"{url}/product_types/", headers=headers, json=product_type_payload
    )
    product_type_id = product_type_response.json()["id"]
    print("Product Type ID = " + str(product_type_id))

    # Creating Product
    product_payload = {
        "name": product_name,
        "description": "Product Description",
        "prod_type": product_type_id,
        "business_criticality": "very high",
        "platform": "web service",
        "lifecycle": "construction",
        "origin": "third party library",
        "external_audience": "true",
        "internet_accessible": "true",
        "enable_simple_risk_acceptance": "false",
        "enable_full_risk_acceptance": "true",
        "technical_contact": "2",
        "team_manager": "2",
    }
    product_response = requests.post(
        f"{url}/products/", headers=headers, json=product_payload
    )
    product_id = product_response.json()["id"]
    print("Product ID = " + str(product_id))

    # Creating Engagement
    engagement_payload = {
        "name": engagement_name,
        "description": "Engagement Description",
        "target_start": date,
        "target_end": date,
        "product": product_id,
        "environment": "Pre-prod",
        "engagement_type": "CI/CD",
        "lead": "2",
        "deduplication_on_engagement": "true",
        "close_old_findings": "true",
    }

    engagement_response = requests.post(
        f"{url}/engagements/", headers=headers, json=engagement_payload
    )

    engagement_json = engagement_response.json()
    engagement_id = engagement_json.get("id")
    print("Engagement ID = " + str(engagement_id))

    # Set Engagement to import-scan
    #scan_payload = {
    #    "scan_type": "SARIF",
    #    "file": "./snyk-report.sarif",
    #    "engagement": engagement_id,
    #    "minimum_severity": "Info",
    #    "active": "true",
    #    "verified": "true",
    #}

    scan_payload = {
         "headers": {"Authorization": f"Token {api_key}"},
         "json": {
         "scan_type": "Bandit Scan",
         "engagement": engagement_id,
         "minimum_severity": "Info",
         "active": True,
         "verified": True,
         },
         "files": {"file": open("snyk-report.sarif")}
     }
    # Import to Defectdojo
    #response = requests.post(f"{url}/import-scan/", headers=headers, files=scan_payload)
    response =  requests.post(url_import_scan, files=scan_payload['files'], data=scan_payload['json'], headers=scan_payload['headers'], verify=False)

    # Print result
    print(response.text)
