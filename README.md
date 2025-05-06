Part 1: Multilingual PDF Key-Value Extraction & Translation
Objective:
Extract key-value pairs from structured PDFs in different languages and translate the content to English.
Input:
●	~10 PDFs with key-value pairs in various languages (non-image, printed format). The documents will contain only key value pairs. Nothing else. You can generate them in word editor and save them as PDF files.
●	Some values may be multiline.
Tasks:
1.	Read PDFs
2.	Extract structured key-value pairs, handling multi line values properly. Content can contain text, numerical, special characters.
3.	Write output to an Excel sheet (.xlsx).
4.	Translate all keys and values to English using a pretrained translation model.
5.	Automate for a batch of 10 files.
Key Focus:
●	Accuracy of extraction: Preserve associations and structure
●	Translation correctness: Handle multiple languages, mixed text
●	Automation: Should run end-to-end for a folder of PDFs



