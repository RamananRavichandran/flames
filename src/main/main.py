from src.driver import flames

import sys

def main():
    print("\tFLAMES")
    print("Relationship Predictor ")
    print("Enter a male name")
    male = input()
    print("Enter a female name")
    female = input()
    relation = flames.flames.r_pred(male, female)
    print(relation)