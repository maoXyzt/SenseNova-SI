import argparse

import torch
from transformers import AutoModel, AutoTokenizer

from utils import load_image, split_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Examples for SenseSI single-run MCQ")
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/SenseSI-InternVL3-8B",
        help="Model path",
    )
    parser.add_argument(
        "--image_paths",
        type=str,
        nargs="+",
        default=["./examples/Q1_1.png"],
        help="Path to image files, can specify multiple",
    )
    parser.add_argument(
        "--question",
        type=str,
        default="<image>\nPlease describe the image in detail.",
        help="Question to ask the model",
    )
    args = parser.parse_args()

    model_path = args.model_path

    device_map = split_model(model_path)
    model = AutoModel.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        load_in_8bit=False,
        low_cpu_mem_usage=True,
        use_flash_attn=True,
        trust_remote_code=True,
        device_map=device_map,
    ).eval()
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=True, use_fast=False
    )

    pixel_values_list = []
    print(f"Load {len(args.image_paths)} images...")
    for path in args.image_paths:
        print(f"Load image {path}...")
        pixel_values_list.append(load_image(path, max_num=12).to(torch.bfloat16).cuda())

    if len(pixel_values_list) > 1:
        pixel_values = torch.cat(pixel_values_list, dim=0)
    else:
        pixel_values = pixel_values_list[0]

    question = args.question

    generation_config = dict(
        do_sample=False, max_new_tokens=512, top_p=None, num_beams=1
    )

    response = model.chat(
        tokenizer, pixel_values, question, generation_config, history=None
    )
    print(f"User: {question}")
    print(f"Assistant: {response}")
