import re
from typing import List, Tuple
import pytesseract
from PIL import Image

def extract_pii(text: str) -> List[str]:
    # Improved regex-based PII detection
    patterns = [
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'\b\d{10}\b',             # Phone number
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        r'\b\d{16}\b',             # Credit card (very naive)
        r'\b\d{2}/\d{2}/\d{4}\b',  # Date (e.g., DOB)
        r'\b\d{5}(?:-\d{4})?\b'    # Zip code
    ]
    
    matches = []
    for pattern in patterns:
        matches.extend(re.findall(pattern, text))
    return matches

def classify_confidentiality(pii_count: int) -> str:
    if pii_count >= 6:
        return 'Highly Confidential'
    elif 3 <= pii_count < 6:
        return 'Medium Confidential'
    else:
        return 'Low Confidential'

def get_confidentiality_from_image(image_path: str) -> Tuple[str, int, List[str]]:
    # OCR Extraction
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    # Extract PII entities
    pii_entities = extract_pii(text)
    pii_count = len(pii_entities)

    # Get Confidentiality Label
    confidentiality_level = classify_confidentiality(pii_count)

    return confidentiality_level, pii_count, pii_entities


# Example test run (optional, for debugging)
if __name__ == "__main__":
    image_path = "data/images/email/0001.tif"
    confidentiality_level, pii_count, pii_entities = get_confidentiality_from_image(image_path)
    print(f"Confidentiality Level: {confidentiality_level}")
    print(f"Number of PII Entities Detected: {pii_count}")
    print(f"Detected PII: {pii_entities}")
