from src.pipeline.executor import run_genomic_pipeline
import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Bio-Genomic Sequencing Pipeline")
    parser.add_PH_argument("--input", required=False, default="data/sample.fasta", help="Path to input FASTA file")
    parser.add_argument("--output", required=False, default="output/analysis_results.json", help="Path to output JSON file")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        return

    results = run_genomic_pipeline(args.input, max_workers=args.workers)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=4)
        
    print(f"Analysis complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()
