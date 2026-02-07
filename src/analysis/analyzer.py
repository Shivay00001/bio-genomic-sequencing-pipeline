from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, MeltingTemp as mt
from typing import Dict, Any

class GenomicAnalyzer:
    @staticmethod
    def analyze_sequence(sequence_str: str) -> Dict[str, Any]:
        """Performs basic genomic analysis on a sequence string."""
        seq = Seq(sequence_str)
        return {
            "length": len(seq),
            "gc_content": gc_fraction(seq) * 100,
            "melting_temp": mt.Tm_NN(seq),
            "molecular_weight": seq.defined_sequence.molecular_weight() if hasattr(seq, 'defined_sequence') else 0,
            "translation": str(seq.translate(to_stop=True))
        }

    @staticmethod
    def find_motifs(sequence_str: str, motif: str) -> list:
        """Finds all occurrences of a motif in the sequence."""
        import re
        return [m.start() for m in re.finditer(f"(?={motif})", sequence_str)]
