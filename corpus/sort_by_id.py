import os
import json

output_files = ['full_corpus_shuffled.jsonl', 'mini_corpus.jsonl', 'corpus_sorted_by_id.jsonl', 'corpus_sorted_by_date.jsonl', 'corpus_sequential.jsonl']

def load_corpus_files(corpus_dir):
    corpus_files = []
    for root, _, files in os.walk(corpus_dir):
        for file in files:
            if file.endswith(".jsonl") and not file in output_files:
                corpus_files.append(os.path.join(root, file))
    return corpus_files

def sort_by_id(corpus_files, output_file):
    all_items = []
    for file in corpus_files:
        with open(file, "r") as f:
            for line in f:
                all_items.append(json.loads(line))

    all_items.sort(key=lambda x: x["id"])

    with open(output_file, "w") as f:
        for item in all_items:
            f.write(json.dumps(item) + "\n")
    print(f"Corpus sorted by id and saved to {output_file}")

if __name__ == "__main__":
    corpus_dir = "."
    output_file = "corpus_sorted_by_id.jsonl"

    corpus_files = load_corpus_files(corpus_dir)
    sort_by_id(corpus_files, output_file)