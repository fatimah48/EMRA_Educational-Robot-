# Model and Training Details

Supplementary detail for the EMRA paper. The manuscript points here for the checkpoint
identifiers, the label mappings, and the fine-tuning settings.

---

## Candidate Model Identifiers

All candidates are open-weight and were run offline on the workstation.

### Text-Based Emotion Detection

| Language | Model | Identifier |
|---|---|---|
| English | DistilRoBERTa | `j-hartmann/emotion-english-distilroberta-base` |
| English | BERT-Emotion | `boltuix/bert-emotion` |
| English | RoBERTa-large | `j-hartmann/emotion-english-roberta-large` |
| Arabic | AraBERTv02-Twitter | `aubmindlab/bert-base-arabertv02-twitter` |
| Arabic | MARBERTv2 | `UBC-NLP/MARBERTv2` |
| Arabic | CAMeLBERT-DA | `CAMeL-Lab/bert-base-arabic-camelbert-da` |

### Vision-Based Emotion Detection

| Model | Architecture | Pre-training source |
|---|---|---|
| HSEmotion (`enet_b2_8`) | EfficientNet-B2 facial emotion recognition model | VGGFace2 for face identification, then AffectNet for eight-class expression recognition |
| POSTER++ | Two-stream transformer combining facial image features with landmark information | AffectNet eight-class checkpoint |
| DDAMFN++ | Dual-Direction Attention Mixed Feature Network | AffectNet eight-class checkpoint |

### Large Language Models

| Language | Model | Parameters | Deployment tag |
|---|---|---|---|
| English | Mistral-7B-Instruct-v0.3 | 7B | `mistral:7b` |
| English | Qwen2.5-7B-Instruct | 7B | `qwen2.5:7b` |
| English | Llama-3.1-8B-Instruct | 8B | `llama3.1:8b` |
| Arabic | ALLaM-7B-Instruct-preview | 7B | `iKhalid/ALLaM:7b` |
| Arabic | SILMA-9B-Instruct-v1.0 | 9B | `silma:9b` |
| Arabic | C4AI Command R7B Arabic | approx. 8B | `command-r7b-arabic:latest` |

All six were served through Ollama with four-bit quantization, temperature 0.7 and a fixed
seed. The token limit was 300 new tokens for English and 256 for Arabic.

### Automatic Speech Recognition

| Language | Model | Identifier | Architecture |
|---|---|---|---|
| English | Whisper Large-v3 | `large-v3` | Encoder-decoder transformer trained on large-scale weakly supervised multilingual audio |
| English | SeamlessM4T-v2 | `facebook/seamless-m4t-v2-large` | Multilingual speech-to-text model based on the UnitY2 architecture |
| English | Canary-Qwen-2.5B | `nvidia/canary-qwen-2.5b` | FastConformer encoder combined with a Qwen language model decoder |
| Arabic | FastConformer-Hybrid Large Arabic | `nvidia/stt_ar_fastconformer_hybrid_large_pcd_v1.0` | FastConformer encoder with joint Transducer and CTC decoders, trained on Arabic speech |
| Arabic | Whisper Large-v2 Common Voice Arabic | `speechbrain/asr-whisper-large-v2-commonvoice-ar` | Encoder-decoder Whisper model fine-tuned on Arabic Common Voice |
| Arabic | Whisper Large-v3 Turbo Arabic | `deepdml/whisper-large-v3-turbo-ar-mix-norm` | Whisper Large-v3 Turbo, a reduced-decoder variant, fine-tuned on mixed-domain Arabic data |

### Text-to-Speech

| Language | Model | Identifier | Architecture | Coverage |
|---|---|---|---|---|
| English | Kokoro-82M | `hexgrad/Kokoro-82M` | Compact model based on StyleTTS 2, 82M parameters | Primarily English |
| English | XTTS-v2 | `coqui/XTTS-v2` | Zero-shot model supporting voice cloning | Multilingual |
| English | Chatterbox | — | Provides an emotion-exaggeration parameter | Multilingual |
| Arabic | SILMA-TTS | `silma-ai/silma-tts` | F5-TTS flow matching architecture, roughly 150M parameters | Bilingual Arabic and English |
| Arabic | NAMAA-Saudi-TTS | `NAMAA-Space/NAMAA-Saudi-TTS` | Built on Chatterbox | Saudi dialect Arabic |
| Arabic | Arabic-F5-TTS-v2 | `IbrahimSalah/Arabic-F5-TTS-v2` | F5-TTS, requires diacritised input (*tashkeel*) to guide pronunciation | Modern Standard Arabic |

One voice was fixed per English model and used for all 200 texts. The Arabic candidates are
voice-cloning systems with no built-in speaker, so a single reference clip of a calm adult
voice was used for all three.

### Vision-Language Models

| Model | Identifier | Quantization |
|---|---|---|
| Qwen3-VL-4B | `Qwen/Qwen3-VL-4B-Instruct` | 4-bit |
| SmolVLM2-2.2B | `HuggingFaceTB/SmolVLM2-2.2B-Instruct` | 4-bit |
| LLaVA-OneVision-7B | `llava-hf/llava-onevision-qwen2-7b-ov-hf` | 4-bit |

---

## Label Mappings

The off-the-shelf models were released with their own label schemas. These were mapped onto
the five-class schema used throughout EMRA.

| Target class | English text models | Vision models (AffectNet) |
|---|---|---|
| Happy | joy, happiness, love | Happiness |
| Sad | sadness, shame, guilt | Sadness |
| Angry | anger | Anger, Disgust, Contempt |
| Fear | fear | Fear |
| Neutral | neutral, disgust, surprise, confusion, desire, sarcasm | Neutral, Surprise |

Shame and guilt were mapped to Sad because they are closer to sadness than to the other
target emotions. Labels with no counterpart in the five-class schema were mapped to Neutral
rather than removed, so that every prediction remained included in the evaluation.

No mapping was needed for the Arabic models or for any of the fine-tuned models. The Arabic
candidates carry no emotion labels of their own, and fine-tuning replaces the native schema
with a new five-class head trained directly on the dataset labels.

---

## Fine-Tuning Settings

| Setting | English | Arabic |
|---|---|---|
| Maximum sequence length | 128 tokens | 64 tokens |
| Epochs | Up to 10, early stopping after two epochs without improvement | 5, no early stopping |
| Batch size | 8 | 16 |
| Learning rate | 1e-5 | 2e-5 |
| Weight decay | 0.01 | 0.01 |
| Schedule | Cosine, 10% warmup | Linear |

The 250 test scenarios were kept separate. The remaining 750 were divided using a stratified
90:10 split into 675 training and 75 validation scenarios, with the random seed fixed at 42.
Each model was loaded with its pre-trained weights and its classification layer was replaced
with a new five-class layer initialized from scratch. Macro-averaged F1 on the validation set
selected the best checkpoint, which was then evaluated on the held-out test set.
