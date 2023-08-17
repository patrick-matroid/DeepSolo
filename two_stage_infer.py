
import torch
import torch.nn
from PIL import Image
from strhub.data.module import SceneTextDataModule
import argparse
import PIL


def preprocess(path_or_tensor, mode):
    if isinstance(path_or_tensor, str):
        img = Image.open(path_or_tensor)
    else:
        img = path_or_tensor
    img = torch.Tensor(img)
    


class STD:
    def __init__(self, mode) -> None:
        
        




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inference: STD/GT + Rectifier + STR')
    parser.add_argument('--det', type=str, choices=['gt', 'DPText'])
    parser.add_argument('--aligner', type=str)
    parser.add_argument('--recog', type=str)
    parser.add_argument('--img-path', type=str)
    args = parser.parse_args()
    
    img_tensor = preprocess(args.img_path, 'det')
    detections = STD(args.det)(img_tensor)
    text_crops = warp(args.aligner, args.img_path, detections)
    text_crops_tensor = preprocess(text_crops, 'recog')
    results = recog_crops(args.recog, text_crops_tensor)

    # Load model and image transforms
    parseq = torch.hub.load('baudm/parseq', 'parseq', pretrained=True).eval()
    img_transform = SceneTextDataModule.get_transform(parseq.hparams.img_size)
    
     