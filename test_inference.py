from inference import infer

if __name__ == '__main__':
    image_path = 'data/images/email/0001.tif'  # Adjust the path as needed
    result = infer(image_path)
    
    print("\n===== Inference Result =====")
    print(f"Predicted Class ID     : {result['predicted_class']}")
    print(f"Confidence Score (%)   : {result['confidence_score']}")
    print(f"Confidentiality Level  : {result['confidentiality_level']}")
    print(f"PII Count Detected     : {result['pii_count']}")
    print(f"PII Entities Found     : {result['pii_entities']}")
    print("============================\n")
