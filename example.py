import argparse

import torch
from transformers import AutoModel, AutoTokenizer

from utils import load_image, split_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example for SenseSI inference")
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/SenseSI-InternVL3-8B",
        help="Model path",
    )
    args = parser.parse_args()

    image_path = "./examples/Q1_1.png"
    question = "<image>\nWhich figure is a top-down view of the given shape?\nOptions:\nA: A\nB: B\nC: C\nD: D"

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

    pixel_values = load_image(image_path, max_num=12).to(torch.bfloat16).cuda()
    generation_config = dict(
        do_sample=False, max_new_tokens=512, top_p=None, num_beams=1
    )

    response = model.chat(tokenizer, pixel_values, question, generation_config)
    print(f"User: {question}\nAssistant: {response}")
