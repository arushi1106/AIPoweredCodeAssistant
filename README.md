# AIPoweredCodeAssistant

## Milestone: Data Collection and Preprocessing (april-may.ipynb)

This notebook addresses the **April–May milestone** of the MSc AI project **"AI-Powered Code Review Assistant"**, focusing on the foundational preparation of a vulnerability classification dataset. It includes steps for data cleaning, augmentation, feature engineering, and tokenization — preparing the data for downstream model development.

---

### Tasks Covered

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

## Milestone: Model Fine-Tuning and Evaluation (june-july.ipynb)

Covers **June–July** development of LLM-based vulnerability detectors, benchmarking various models and analyzing performance metrics.

---

### Tasks Covered

#### 1. Model Selection & Preparation

- Initialized LLMs: GPT-4, DeepSeek Coder, Codex, Qwen Coder  
- Prepared Hugging Face training pipelines

#### 2. Fine-Tuning

- Trained on `train_preprocessed.csv` with early stopping and learning rate schedulers  
- Validated on `valid_preprocessed.csv`

#### 3. Benchmarking

- Evaluated on CodeXGLUE-Security test splits  
- Computed precision, recall, F1-score for vulnerability detection

#### 4. Comparative Analysis

- Tabulated and visualized performance across model variants  
- Identified trade-offs: speed vs. accuracy

---

## Milestone: Web App Integration & Feedback (july-august.ipynb)

Focuses on **July–August** integration of the inference pipeline into a Streamlit app and incorporating user feedback.

---

### Tasks Covered

#### 1. Streamlit Interface Prototype

- Developed `app.py` scaffold with code input and analyze button  
- Displayed vulnerability reports and severity scores

#### 2. LLM Inference Hookup

- Connected back-end to selected fine-tuned model  
- Managed API calls, caching, and rate limits

#### 3. User Feedback Loop

- Collected developer annotations via UI forms  
- Updated prompt templates and re-ran evaluations

#### 4. Performance Tuning

- Measured latency, implemented batching and async calls  
- Reduced average response time to <2 seconds

---

## Case Studies & Testing (test.ipynb)

Demonstrates end-to-end functionality through real-world C/C++ code examples and simulated exploits.

---

### Tasks Covered

- Loaded open-source C/C++ projects for vulnerability scanning  
- Simulated attack vectors based on LLM-identified weaknesses  
- Compared model explanations against manual exploit write-ups

---

## Application: Streamlit Interface (app.py)

A user-friendly web UI for on-the-fly code security audits.

### Usage

```bash
streamlit run app.py
