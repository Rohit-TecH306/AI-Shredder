import os
import torch
from torch.utils.data import DataLoader
from dataset import RVLCDIPDataset, get_transforms
from model import load_model
from utils.confidentiality import get_confidentiality_from_image
from utils.logger import log_to_csv
import torch.nn.functional as F

# Paths (update as needed)
TEST_CSV = 'data/test_labels.csv'
IMG_ROOT = 'data/images/'
CHECKPOINT_PATH = 'models/best_model.pth'
LOG_PATH = 'logs/eval_results.csv'
BATCH_SIZE = 32
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def evaluate():
    test_dataset = RVLCDIPDataset(TEST_CSV, IMG_ROOT, transform=get_transforms())
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=4)
    model = load_model(CHECKPOINT_PATH, num_classes=16, device=DEVICE)
    model.eval()
    results = []
    
    with torch.no_grad():
        for images, labels, doc_ids in test_loader:
            images = images.to(DEVICE)
            outputs = model(images)
            probs = F.softmax(outputs, dim=1)
            top_probs, preds = torch.max(probs, 1)
            
            for doc_id, pred, prob in zip(doc_ids, preds.cpu().numpy(), top_probs.cpu().numpy()):
                image_path = os.path.join(IMG_ROOT, f"{doc_id}.tif")  # Assumed image extension
                confidentiality_level, pii_count, pii_entities = get_confidentiality_from_image(image_path)
                
                print(f"Document ID: {doc_id}")
                print(f"Predicted Class: {pred} (Prob: {prob:.2f})")
                print(f"Confidentiality Level: {confidentiality_level}")
                print(f"PII Count: {pii_count}")
                print(f"Detected PII Entities: {pii_entities}\n")

                log_to_csv(LOG_PATH, [doc_id, pred, confidentiality_level, round(prob * 100, 2)])
                results.append((doc_id, pred, confidentiality_level, round(prob * 100, 2)))

    print(f"Results saved to {LOG_PATH}")
    return results

if __name__ == '__main__':
    evaluate()
