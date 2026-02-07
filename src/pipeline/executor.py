from Bio import SeqIO
from concurrent.futures import ProcessPoolExecutor
from src.analysis.analyzer import GenomicAnalyzer
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_record(record):
    """Processes a single SeqRecord."""
    analysis = GenomicAnalyzer.analyze_sequence(str(record.seq))
    return {
        "id": record.id,
        "description": record.description,
        **analysis
    }

def run_genomic_pipeline(fasta_path: str, max_workers: int = 4):
    """Orchestrates the genomic analysis pipeline."""
    logger.info(f"Loading records from {fasta_path}")
    records = list(SeqIO.parse(fasta_path, "fasta"))
    
    start_time = time.time()
    logger.info(f"Starting parallel processing with {max_workers} workers")
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_record, records))
        
    duration = time.time() - start_time
    logger.info(f"Processed {len(results)} records in {duration:.2f} seconds")
    return results
