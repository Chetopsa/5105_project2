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

def append_sequentially(corpus_files, output_file):
    with open(output_file, "w") as f_out:
        for file in corpus_files:
            with open(file, "r") as f_in:
                for line in f_in:
                    f_out.write(line)
    print(f"Corpus appended sequentially and saved to {output_file}")

if __name__ == "__main__":
    corpus_dir = "."
    output_file = "corpus_sequential.jsonl"

    corpus_files = load_corpus_files(corpus_dir)
    append_sequentially(corpus_files, output_file)