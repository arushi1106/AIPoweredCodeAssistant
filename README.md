# AIPoweredCodeAssistant
## Milestone: Data Collection and Preprocessing (april-may.ipynb)

This notebook addresses the **April–May milestone** of the MSc AI project **"AI-Powered Code Review Assistant"**, focusing on the foundational preparation of a vulnerability classification dataset. It includes steps for data cleaning, augmentation, feature engineering, and tokenization — preparing the data for downstream model development.

---
###  Tasks Covered

#### 1. Dataset Sourcing
- Pulled from [CodeXGLUE - Devign Dataset](https://huggingface.co/datasets/code_x_glue_cc_defect_detection)
- C language functions labeled as:
  - `1`: vulnerable
  - `0`: safe

#### 2. Data Cleaning
- Removed:
  - Empty and whitespace-only functions
  - Very short functions (< 5 tokens)
  - Long functions exceeding 512 tokens for LLM compatibility

#### 3. Data Augmentation
Simulates realistic developer variations to improve generalization:
- Variable renaming (e.g., `temp` → `temp_874`)
- Inline comment insertion (`// TODO`)
- Dead code insertion (`int dummy = 0;`)
- Whitespace and formatting changes

#### 4. Feature Engineering
Extracted interpretable, static features from raw code:
- `func_length` (token count)
- `num_loops`, `num_if`, `num_return`
- `has_eval`, `has_system` (flags for dangerous usage)
- `uses_pointer`, `uses_buffer`

#### 5. Tokenization
- Tokenized full dataset using `microsoft/codebert-base`
- Outputs include:
  - `input_ids`
  - `attention_mask`
---

### Storage Notes
- Tokenized files (`.pkl`) are **excluded from GitHub** due to size constraints
- To regenerate them, rerun the notebook locally
---
