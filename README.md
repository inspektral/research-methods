
# Testing the efficacy of LLMs in writing Lean4

This repo contains the data and the scripts used for the paper.

## Scripts

In this repo the script __main.py__ is provided. its purpose is to filter lean4_workbook theorems and retrieve them, called without args it returns a list of proven theorems with the associated index (referenced in the data). Called with a theorem index it will return all the details about that specific theorem. 

## Data

Theorems and proofs on which LLMs are tested are in the lean4 workbook, that can by retrieved by git cloning it:
 ```
git clone https://huggingface.co/datasets/internlm/Lean-Workbook
 ```

Results of our testing are contained in __data.csv__ and summarized in __data_summary.csv__.
__livebench.csv__ contains the current (12/11/2024) benchmarks results for the tested LLMs.
## Prompts
The following prompts have been used to test the LLMs.

### Translation
```
translate this statement in lean4, don't prove it and provide only lean4 translation without description

<lean_workbook natural language statement>
```

### Proving
```
proof this in lean4, explain the code in depth step by step and give the complete solution as code at the end

<lean_workbook lean4 statement>
```

### Understanding
```
is this a valid Lean4 proof?

<lean_workbook statement and proof in lean4>
```
