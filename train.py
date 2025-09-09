import os
import torch
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.optim.lr_scheduler import StepLR
import torch.nn as nn
from dataset import get_datasets
from model import load_model
from utils.logger import setup_logger

IMG_ROOT = 'data/images/'
CHECKPOINT_DIR = 'models/'
LOG_PATH = 'logs/train_log.csv'

BATCH_SIZE = 64
FAST_DEV_RUN = False
EPOCHS = 10 if FAST_DEV_RUN else 20
MAX_TRAIN_SAMPLES = 1000  
MAX_VAL_SAMPLES = 1000
LR = 1e-4
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

RESUME = True
ADDITIONAL_EPOCHS = 0

logger = setup_logger(LOG_PATH)

def train():
    train_set, val_set, _ = get_datasets(IMG_ROOT)

    if FAST_DEV_RUN:
        from torch.utils.data import Subset
        gen = torch.Generator().manual_seed(42)
        max_train = min(MAX_TRAIN_SAMPLES, len(train_set))
        max_val = min(MAX_VAL_SAMPLES, len(val_set))
        train_indices = torch.randperm(len(train_set), generator=gen)[:max_train].tolist()
        val_indices = torch.randperm(len(val_set), generator=gen)[:max_val].tolist()
        train_set = Subset(train_set, train_indices)
        val_set = Subset(val_set, val_indices)
        print(f"FAST_DEV_RUN: train={len(train_set)}, val={len(val_set)}, epochs={EPOCHS}")

    train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_set, batch_size=BATCH_SIZE, shuffle=False, num_workers=4)

    model = load_model(num_classes=16, device=DEVICE)
    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=LR)
    scheduler = StepLR(optimizer, step_size=3, gamma=0.5)

    start_epoch = 0
    best_acc = 0.0
    total_epochs_trained = 0
    total_samples_trained = 0
    checkpoint_path = os.path.join(CHECKPOINT_DIR, 'resume_checkpoint.pth')

    if RESUME and os.path.exists(checkpoint_path):
        print(f"Resuming from checkpoint: {checkpoint_path}")
        checkpoint = torch.load(checkpoint_path, map_location=DEVICE)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
        start_epoch = checkpoint['epoch'] + 1
        best_acc = checkpoint.get('best_acc', 0.0)
        total_epochs_trained = checkpoint.get('total_epochs_trained', start_epoch)
        total_samples_trained = checkpoint.get('total_samples_trained', 0)
        print(f"Resumed at epoch {start_epoch} with best_acc={best_acc:.4f}")

    end_epoch = EPOCHS
    if RESUME and ADDITIONAL_EPOCHS > 0 and start_epoch >= EPOCHS:
        end_epoch = start_epoch + ADDITIONAL_EPOCHS

    try:
        for epoch in range(start_epoch, end_epoch):
            print(f"\nEpoch {epoch+1}/{EPOCHS} started...")
            model.train()
            running_loss = 0.0
            correct = 0
            total = 0
            samples_this_epoch = 0

            for batch_idx, (images, labels) in enumerate(train_loader):
                images, labels = images.to(DEVICE), labels.to(DEVICE)
                optimizer.zero_grad()
                outputs = model(images)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                running_loss += loss.item() * images.size(0)
                _, preds = torch.max(outputs, 1)
                correct += (preds == labels).sum().item()
                total += labels.size(0)
                samples_this_epoch += labels.size(0)

                if (batch_idx + 1) % 10 == 0 or (batch_idx + 1) == len(train_loader):
                    print(f"  Batch {batch_idx+1}/{len(train_loader)}: Loss={loss.item():.4f}")

            train_loss = running_loss / total if total > 0 else 0.0
            train_acc = correct / total if total > 0 else 0.0

            print("  Running validation...")
            model.eval()
            val_loss = 0.0
            val_correct = 0
            val_total = 0

            with torch.no_grad():
                for images, labels in val_loader:
                    images, labels = images.to(DEVICE), labels.to(DEVICE)
                    outputs = model(images)
                    loss = criterion(outputs, labels)
                    val_loss += loss.item() * images.size(0)
                    _, preds = torch.max(outputs, 1)
                    val_correct += (preds == labels).sum().item()
                    val_total += labels.size(0)

            val_loss = (val_loss / val_total) if val_total > 0 else 0.0
            val_acc = (val_correct / val_total) if val_total > 0 else 0.0

            logger.info(f"Epoch {epoch+1}/{EPOCHS}, Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
            print(f"Epoch {epoch+1}/{EPOCHS} DONE | Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")

            if val_acc > best_acc:
                best_acc = val_acc
                torch.save(model.state_dict(), os.path.join(CHECKPOINT_DIR, 'best_model.pth'))
                print("  Best model saved!")

            total_epochs_trained += 1
            total_samples_trained += samples_this_epoch

            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'scheduler_state_dict': scheduler.state_dict(),
                'best_acc': best_acc,
                'total_epochs_trained': total_epochs_trained,
                'total_samples_trained': total_samples_trained
            }, checkpoint_path)

            scheduler.step()

    except KeyboardInterrupt:
        interrupted_epoch = epoch if 'epoch' in locals() else start_epoch
        resume_from_epoch = max(interrupted_epoch - 1, 0)

        print(f"\nTraining interrupted. Saving checkpoint for next run...")
        if 'samples_this_epoch' in locals():
            total_samples_trained += samples_this_epoch

        torch.save({
            'epoch': resume_from_epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'scheduler_state_dict': scheduler.state_dict(),
            'best_acc': best_acc,
            'total_epochs_trained': total_epochs_trained,
            'total_samples_trained': total_samples_trained
        }, checkpoint_path)

        print("Checkpoint saved. Exiting...")
        return

    print(f'Training complete. Best Val Acc: {best_acc:.4f}')
