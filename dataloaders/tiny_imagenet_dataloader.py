import numpy as np
import torch
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
from torch.utils.data import sampler
import torchvision.transforms as transforms

class TinyImagenetDataLoader():
    def __init__(self):
        self.name = 'TinyImgNet'    
        # The numbers are the mean and std provided in PyTorch documentation to be used for models pretrained on ImageNet data
        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        train_root= './dataloaders/datasets/tiny-imagenet/train'
        val_root= './dataloaders/datasets/tiny-imagenet/val'

        train_data = datasets.ImageFolder(train_root,
            transform=transforms.Compose([transforms.Resize(256),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize]))

        validation_data = datasets.ImageFolder(val_root,
            transform=transforms.Compose([transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize]))

        BATCH_SIZE = 20

        self.train= DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True,
                num_workers=4, pin_memory=True)
        self.val = DataLoader(validation_data, batch_size=BATCH_SIZE ,shuffle=False,
                num_workers=4, pin_memory=True)
        self.test = DataLoader(validation_data, batch_size=BATCH_SIZE ,shuffle=False,
                num_workers=4, pin_memory=True)

