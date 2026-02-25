# ComfyUI-SubstringExtractor

🔍 ComfyUI Substring Extractor
This custom node is designed for users who use Large Language Models (like Gemini, GPT, or Claude) to generate complex, structured image prompts.

When an AI returns a long string containing multiple sections (e.g., Face, Eyes, Clothing), this node allows you to isolate and extract just the part you need for specific conditioning or LoRA triggering.

Features
Zero Dependencies: No extra Python libraries required.

LLM Friendly: Handles the "Begin XXX;" and "End XXX;" format perfectly.

Clean Output: Automatically strips leading/trailing whitespace and newlines.
