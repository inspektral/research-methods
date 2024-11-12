import json
import sys

path = "Lean-Workbook\lean_workbook.json"

with_proof = []

with open(path, 'r', encoding='utf-8') as f:
    print("Reading file")
    data = json.load(f)
    print("Loaded")

    for item in data:
        if item["proof"]:
            with_proof.append(item)

with_proof = sorted(with_proof, key=lambda x: len(x["proof"]))

if len(sys.argv) == 2:
    item = with_proof[int(sys.argv[1])]

    print(f"Write this natural mathematical language statement in Lean4:")
    print(item["natural_language_statement"])
    print()
    print("Prove this Lean4 statement:")
    print(item["formal_statement"])
    print()
    print("Proofs")
    for proof in item["proof"]:
        print(proof)

else:
    for index, item in enumerate(with_proof):
        print(index, len(item["proof"]), item["natural_language_statement"])
            