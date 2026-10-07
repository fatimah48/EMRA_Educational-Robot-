# EMRA: Full Model Selection Results

Supplementary results for the EMRA paper. The paper reports the selected model and one headline metric per component; this file holds the complete comparison for every candidate, the datasets, and the ranking weights.

Candidate lists, checkpoint identifiers, quantization settings, and deployment tags are in [model_and_training_details.md](model_and_training_details.md).

---

## 1. Text-emotion datasets and annotation agreement

| | English | Arabic |
|---|---|---|
| **Composition** | | |
| Number of scenarios | 1,000 | 1,000 |
| Scenarios per emotion | 200 | 200 |
| Target age | 6-8 years | 6-8 years |
| Average length | 15.5 words | 6.7 words |
| Language variety | English | Gulf colloquial Arabic |
| General scenarios | 600 | 450 |
| ASD-coded scenarios | 200 | 300 |
| Ambiguous scenarios | 200 | 250 |
| **Inter-rater agreement** | | |
| Overall | 80.9%, κ = 0.757 | 86.6%, κ = 0.825 |
| General | 86.8%, κ = 0.835 | 88.2%, κ = 0.846 |
| ASD-coded | 71.0%, κ = 0.618 | 86.7%, κ = 0.825 |
| Ambiguous | 73.0%, κ = 0.612 | 83.6%, κ = 0.790 |
| **Agreement with construction labels** | | |
| Rater 1 | 78.3% | 82.9% |
| Rater 2 | 83.0% | 84.1% |

---

## 2. Text-emotion classification results

| Lang. | Model | Setting | Accuracy | Precision | Recall | Macro-F1 |
|---|---|---|---|---|---|---|
| English | DistilRoBERTa | Off-the-shelf | 53.6% | 61.4% | 53.6% | 54.5% |
| English | BERT-Emotion | Off-the-shelf | 40.8% | 42.7% | 40.8% | 40.0% |
| English | RoBERTa-large | Off-the-shelf | 68.4% | 72.2% | 68.4% | 68.1% |
| English | DistilRoBERTa | Fine-tuned | 76.4% | 76.7% | 76.4% | 76.5% |
| English | BERT-Emotion | Fine-tuned | 50.8% | 49.2% | 50.8% | 47.2% |
| English | **RoBERTa-large** | Fine-tuned | **86.0%** | **86.4%** | **86.0%** | **86.0%** |
| Arabic | AraBERTv02-Twitter | Fine-tuned | 80.0% | 80.2% | 80.0% | 79.8% |
| Arabic | **MARBERTv2** | Fine-tuned | **84.4%** | **84.4%** | **84.4%** | **84.3%** |
| Arabic | CAMeLBERT-DA | Fine-tuned | 78.0% | 78.0% | 78.0% | 77.8% |

---

## 3. Vision-based emotion detection

| Model | Accuracy (%) | Macro-F1 (%) | Mean latency (ms) | Final score |
|---|---|---|---|---|
| HSEmotion | 50.80 | 50.68 | **12.26** | 0.400 |
| **POSTER++** | **54.60** | **54.45** | 12.87 | **0.984** |
| DDAMFN++ | 51.60 | 50.86 | 27.77 | 0.028 |

---

## 4. Per-class performance of the three selected emotion models

All values are percentages. P = precision, R = recall. The text models were evaluated on 250 test scenarios per language and POSTER++ on 500 images, 100 per class.

| Emotion | RoBERTa-large P | R | F1 | MARBERTv2 P | R | F1 | POSTER++ P | R | F1 |
|---|---|---|---|---|---|---|---|---|---|
| Happy | 93.5 | 86.0 | 89.6 | 88.5 | 92.0 | 90.2 | 83.5 | 71.0 | 76.8 |
| Sad | 80.7 | 92.0 | 86.0 | 77.8 | 70.0 | 73.7 | 52.6 | 50.0 | 51.3 |
| Neutral | 91.3 | 84.0 | 87.5 | 93.8 | 90.0 | 91.8 | 45.0 | 54.0 | 49.1 |
| Angry | 85.1 | 80.0 | 82.5 | 83.7 | 82.0 | 82.8 | 51.6 | 66.0 | 57.9 |
| Fear | 81.5 | 88.0 | 84.6 | 78.6 | 88.0 | 83.0 | 44.4 | 32.0 | 37.2 |
| Macro average | 86.4 | 86.0 | 86.0 | 84.4 | 84.4 | 84.3 | 55.4 | 54.6 | 54.5 |

RoBERTa-large is text, English. MARBERTv2 is text, Arabic. POSTER++ is vision, shared.

---

## 5. LLM evaluation results

| Lang. | Model | Empathy | Language app. | Support | Engagement | Safety | Human overall | LLM judgment |
|---|---|---|---|---|---|---|---|---|
| English | **Mistral-7B** | **3.83** | **4.59** | **3.99** | **4.00** | **5.00** | **4.28** | **4.75** |
| English | Qwen2.5-7B | 3.22 | 4.46 | 3.41 | 3.43 | **5.00** | 3.90 | 4.70 |
| English | Llama-3.1-8B | 3.27 | 4.43 | 3.29 | 3.27 | 4.97 | 3.85 | 4.71 |
| Arabic | **ALLaM-7B** | **3.50** | **3.35** | **3.20** | **3.29** | 4.90 | **3.65** | 4.43 |
| Arabic | Command R7B Arabic | 3.13 | 2.85 | 2.82 | 2.86 | **4.92** | 3.31 | **4.54** |
| Arabic | SILMA-9B | 1.46 | 1.44 | 1.36 | 1.42 | 4.68 | 2.07 | 3.76 |

---

## 6. Human overall scores by emotion category

| Lang. | Model | Happy | Sad | Neutral | Angry | Fear |
|---|---|---|---|---|---|---|
| English | **Mistral-7B** | **4.14** | **4.36** | **4.12** | **4.35** | **4.46** |
| English | Qwen2.5-7B | 3.87 | 3.89 | 3.78 | 3.97 | 4.01 |
| English | Llama-3.1-8B | 3.79 | 3.85 | 3.85 | 3.81 | 3.94 |
| Arabic | **ALLaM-7B** | **3.42** | **3.82** | **3.12** | 3.84 | **4.04** |
| Arabic | Command R7B Arabic | 2.98 | 3.11 | 3.05 | **4.16** | 3.28 |
| Arabic | SILMA-9B | 2.15 | 1.88 | 1.81 | 2.36 | 2.16 |

---

## 7. Pairwise Wilcoxon comparisons of human and automated overall scores

Automated Arabic p-values are Holm-adjusted.

| Lang. | Comparison | Human diff. | Human p | Judge p |
|---|---|---|---|---|
| English | Mistral vs. Qwen | 0.38 | 1.9 × 10⁻²⁷ | 3.8 × 10⁻⁵ |
| English | Mistral vs. Llama | 0.44 | 5.7 × 10⁻²⁶ | 0.013 |
| English | Qwen vs. Llama | 0.06 | 0.11 | 0.20 |
| Arabic | ALLaM vs. Command-R | 0.33 | 2.0 × 10⁻⁷ | 1.2 × 10⁻⁵ |
| Arabic | ALLaM vs. SILMA | 1.58 | 2.7 × 10⁻³⁴ | < 10⁻⁵ |
| Arabic | Command-R vs. SILMA | 1.24 | 1.5 × 10⁻³² | < 10⁻⁵ |

---

## 8. Agreement between raters and between humans and LLM judges

Within-one is the proportion of ratings differing by no more than one point. κ is quadratic-weighted Cohen's kappa. r is the Pearson correlation between the human consensus and the judge mean. Gap is the judge score minus the human score.

**(a) Between the two human raters**

| Criterion | English within-one | English κ | Arabic within-one | Arabic κ |
|---|---|---|---|---|
| Empathy | 85.7% | 0.09 | 100% | 0.955 |
| Language appropriateness | 92.0% | 0.00 | 100% | 0.945 |
| Support | 79.2% | 0.07 | 100% | 0.950 |
| Engagement | 80.3% | 0.09 | 100% | 0.940 |
| Safety | 100% | 0.00 | 100% | 0.859 |
| Overall mean difference | 0.61 | | 0.11 | |
| Overall correlation | 0.20 | | 0.98 | |

**(b) Between the human raters and the LLM judges**

| Criterion | English r | English gap | Arabic r | Arabic gap |
|---|---|---|---|---|
| Empathy | 0.31 | +1.16 | 0.58 | +1.07 |
| Language appropriateness | −0.03 | +0.41 | 0.02 | +2.25 |
| Support | 0.18 | +0.76 | 0.54 | +0.92 |
| Engagement | 0.14 | +1.21 | 0.58 | +1.76 |
| Safety | −0.01 | +0.01 | 0.04 | +0.15 |
| Overall | 0.20 | +0.71 | 0.65 | +1.23 |

---

## 9. Arabic dialect and objective measures by model

Dialectness and MSA drift are marker-based measures. SILMA's low MSA-drift rate reflects the absence of MSA markers rather than stronger Gulf dialect use.

| Measure | ALLaM | Command-R | SILMA |
|---|---|---|---|
| Gulf classification (%) | 83.0 | 59.5 | 44.5 |
| MSA classification (%) | 1.0 | 27.0 | 2.0 |
| Marker-based dialectness | 0.75 | 0.43 | 0.20 |
| MSA-drift flag (%) | 5.5 | 38.5 | 1.5 |
| Mean reply length (words) | 20.8 | 28.2 | 7.1 |
| BAREC readability | 11.6 | 12.2 | 7.7 |
| Concrete next step (%) | 86.5 | 91.5 | 71.5 |

---

## 10. LLM generation latency by language and model

| Language | Model | Median TTFT (s) | Median total time (s) |
|---|---|---|---|
| English | Mistral | 2.22 | 3.27 |
| English | Qwen | 2.42 | 3.05 |
| English | Llama | 2.50 | 3.31 |
| Arabic | ALLaM | 2.46 | 2.98 |
| Arabic | SILMA | 3.65 | 5.43 |
| Arabic | Command-R | 4.05 | 9.75 |

---

## 11. Automatic speech recognition results

Raw CER was not recorded for English. English peak GPU memory was measured with the NVML device-memory reading and Arabic with PyTorch's CUDA allocation.

| Lang. | Model | Raw WER (%) ↓ | Raw CER (%) ↓ | Norm. WER (%) ↓ | Norm. CER (%) ↓ | Semantic similarity ↑ | Latency (ms) ↓ | RTF ↓ | VRAM (MB) ↓ | Score ↑ |
|---|---|---|---|---|---|---|---|---|---|---|
| English | **Whisper Large-v3** | 15.16 | – | **8.90** | **4.57** | **0.9398** | 886.0 | 0.123 | **4566** | **0.9443** |
| English | SeamlessM4T-v2 | 18.41 | – | 10.72 | 5.81 | 0.9261 | 2480.9 | 0.338 | 7162 | 0.1918 |
| English | Canary-Qwen-2.5B | **13.96** | – | 11.88 | 6.54 | 0.9290 | **529.3** | **0.072** | 5584 | 0.3621 |
| Arabic | **FastConformer** | **44.4** | **11.7** | **27.9** | **7.9** | 0.843 | 228.83 | 0.053 | **897.2** | **0.940** |
| Arabic | Whisper Large-v2 CV | 46.1 | 12.2 | 32.7 | 8.6 | **0.858** | 738.82 | 0.171 | 6998.5 | 0.150 |
| Arabic | Whisper Large-v3 Turbo | 50.5 | 14.1 | 30.0 | 8.6 | 0.768 | **162.61** | **0.038** | 1597.2 | 0.525 |

---

## 12. Text-to-speech results

NISQA was used for English and SECS for Arabic. The Arabic human rating was provided by one blinded native Saudi listener and was not included in the score. UTMOS is indicative for Arabic. Mean F0 was not scored.

| Lang. | Model | Human (1-5) | UTMOS ↑ | NISQA MOS ↑ | WER (%) ↓ | CER (%) ↓ | SECS ↑ | Latency (ms) ↓ | RTF ↓ | VRAM (MB) ↓ | Mean F0 (Hz) | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| English | **Kokoro** | – | **4.532** | **4.979** | **0.34** | **0.11** | – | **148.6** | **0.011** | **976.2** | 204.63 | **1.0000** |
| English | XTTS-v2 | – | 3.837 | 4.346 | 0.82 | 0.36 | – | 3826.2 | 0.260 | 2028.7 | 177.59 | 0.1421 |
| English | Chatterbox | – | 4.399 | 4.656 | 0.48 | 0.13 | – | 6059.3 | 0.584 | 3468.1 | 151.14 | 0.4822 |
| Arabic | **SILMA** | 3.3 | 2.625 | – | **10.97** | **3.76** | 0.919 | **2780** | **0.218** | **537.9** | 232.9 | **0.9044** |
| Arabic | NAMAA | **3.9** | **3.231** | – | 13.06 | 3.95 | **0.930** | 11680 | 1.269 | 5820.1 | 241.2 | 0.7201 |
| Arabic | Arabic-F5-v2 | 1.0 | 1.235 | – | 28.02 | 12.22 | 0.690 | 5290 | 0.392 | 936.2 | 235.4 | 0.1980 |

---

## 13. Vision-language model benchmark and deployment results

| Model | POPE acc. | POPE F1 | POPE prec. | POPE rec. | POPE FP | MME acc. | Latency (ms) | Throughput (q/s) | VRAM (MB) | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| **Qwen3-VL-4B** | 0.8767 | 0.8635 | **0.9669** | 0.7800 | **4** | **0.8667** | 3538.9 | 0.283 | 3106.6 | **0.8172** |
| SmolVLM2-2.2B | 0.8267 | 0.8301 | 0.8141 | 0.8467 | 29 | 0.7204 | **1711.9** | **0.584** | **1833.0** | 0.4500 |
| LLaVA-OneVision-7B | **0.9000** | **0.8973** | 0.9225 | **0.8733** | 11 | 0.7767 | 41608.3 | 0.024 | 9327.9 | 0.3347 |

---

## 14. Metrics and weights used for ranking

Used to rank the speech recognition, speech synthesis, and vision-language candidates.

**Automatic speech recognition: recognition 65%, efficiency 35%**

| Metric | What it measures | English | Arabic |
|---|---|---|---|
| WER | Word-level transcription errors against the reference | 0.35 | 0.30 |
| CER | Character-level transcription errors | 0.15 | 0.20 |
| Semantic similarity | Cosine similarity between sentence embeddings of the reference and the transcription, showing whether the meaning was preserved when the wording differed | 0.15 | 0.15 |
| Latency | Mean transcription time across the 200 utterances | 0.20 | 0.20 |
| RTF | Transcription time divided by audio duration; below one is faster than real time | 0.10 | 0.10 |
| VRAM | Peak GPU memory while the model was running | 0.05 | 0.05 |

**Text-to-speech**

| Metric | What it measures | English | Arabic |
|---|---|---|---|
| UTMOS | Predicted MOS-like score for overall speech quality | 0.30 | 0.30 |
| NISQA MOS | Predicted quality with noisiness, coloration, discontinuity, and loudness | 0.20 | – |
| WER | Word errors after transcribing the generated audio with Faster-Whisper Large-v3 | 0.20 | 0.22 |
| CER | Character errors from the same transcription | – | 0.13 |
| SECS | Cosine similarity to the shared reference voice, using a GE2E speaker encoder | – | 0.10 |
| Latency | Mean generation time per response | 0.15 | 0.13 |
| RTF | Generation time divided by the duration of the generated audio | 0.10 | 0.07 |
| VRAM | Peak GPU memory during generation | 0.05 | 0.05 |
| F0 | Mean pitch over voiced frames, probabilistic YIN | descriptive | descriptive |
| Speaking rate | Words per second for English, characters per second for Arabic | descriptive | descriptive |

**Vision-language: answer quality 55%, deployment cost 45%**

| Metric | What it measures | Weight |
|---|---|---|
| MME | Scene understanding, scored as accuracy over a fixed subset of 300 items | 0.35 |
| POPE F1 | Object hallucination, scored over a balanced subset of 300 binary presence questions drawn from MS-COCO, 150 present and 150 absent | 0.20 |
| Latency | Mean response time on the deployment hardware | 0.25 |
| Throughput | Queries processed per second | 0.10 |
| VRAM | Peak GPU memory during inference | 0.10 |
