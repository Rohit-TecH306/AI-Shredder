import torch
from torchvision import datasets, transforms
from torch.utils.data import random_split, DataLoader
from torchvision.datasets.folder import default_loader
import os

def get_transforms():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

def safe_loader(path):
    try:
        return default_loader(path)
    except Exception as e:
        print(f"[Warning] Skipping unreadable image: {path} ({e})")
        return None

class SafeImageFolder(datasets.ImageFolder):
    def __getitem__(self, index):
        path, target = self.samples[index]
        sample = safe_loader(path)
        if sample is None:
            return self.__getitem__((index + 1) % len(self.samples))
        if self.transform is not None:
            sample = self.transform(sample)
        if self.target_transform is not None:
            target = self.target_transform(target)
        return sample, target

def get_datasets(data_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    dataset = SafeImageFolder(data_dir, transform=get_transforms())
    total = len(dataset)
    train_len = int(total * train_ratio)
    val_len = int(total * val_ratio)
    test_len = total - train_len - val_len
    train_set, val_set, test_set = random_split(dataset, [train_len, val_len, test_len], generator=torch.Generator().manual_seed(seed))
    return train_set, val_set, test_set
