#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
nlp predict
"""
import ast
import argparse
import paddlehub as hub


parser = argparse.ArgumentParser(__doc__)
parser.add_argument("--model_name", type=str, default=None, help="model name for predict.")
parser.add_argument(
    "--use_gpu", type=ast.literal_eval, default=True, help="Whether use GPU for predict, input should be True or False"
)
parser.add_argument("--batch_size", type=int, default=2, help="predict batch size.")
args = parser.parse_args()

if __name__ == "__main__":
    senta = hub.Module(name=args.model_name)
    test_text = ["这家餐厅很好吃", "这部电影真的很差劲"]
    results0 = senta.sentiment_classify(texts=test_text, use_gpu=args.use_gpu, batch_size=args.batch_size)
    print(results0)
    results1 = senta.get_labels()
    print(results1)
    results2 = senta.get_vocab_path()
    print(results2)
