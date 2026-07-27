"""
====================================================================
 DNA SEQUENCE ANALYZER
 Final Semester Project
====================================================================

WHAT THIS PROGRAM DOES:
This program takes a DNA sequence as input and performs common
bioinformatics analysis on it:

    1. Validates the sequence (only A, T, G, C allowed)
    2. Counts each nucleotide (A, T, G, C)
    3. Calculates GC content and AT content (%)
    4. Finds the Complement strand
    5. Finds the Reverse Complement strand
    6. Performs Transcription (DNA -> RNA)
    7. Performs Translation (RNA -> Protein) using the codon table
    8. Lets you save the full report as a .txt file

HOW TO RUN:
    python dna_sequence_analyzer.py

Requirements:
    Only uses Python's built-in "tkinter" library - nothing else
    needs to be installed.
====================================================================
"""

import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext

# --------------------------------------------------------------
# STEP 1: THE CODON TABLE
# --------------------------------------------------------------
# This dictionary maps every 3-letter RNA codon to the amino acid
# it codes for. "*" means STOP codon (end of protein).
CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

# Complement of each base (used for complement / reverse complement)
COMPLEMENT_MAP = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


# --------------------------------------------------------------
# STEP 2: CORE ANALYSIS FUNCTIONS
# (Each function does ONE simple job - easy to explain in viva)
# --------------------------------------------------------------

def clean_sequence(seq):
    """Remove spaces/newlines and make everything uppercase."""
    return seq.strip().upper().replace(" ", "").replace("\n", "")


def is_valid_dna(seq):
    """Return True only if the sequence contains just A, T, G, C."""
    return all(base in "ATGC" for base in seq) and len(seq) > 0


def count_nucleotides(seq):
    """Return a dictionary with the count of each base."""
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C"),
    }


def gc_content(seq):
    """Percentage of G and C bases in the sequence."""
    counts = count_nucleotides(seq)
    total = len(seq)
    return round((counts["G"] + counts["C"]) / total * 100, 2)


def at_content(seq):
    """Percentage of A and T bases in the sequence."""
    counts = count_nucleotides(seq)
    total = len(seq)
    return round((counts["A"] + counts["T"]) / total * 100, 2)


def get_complement(seq):
    """Replace each base with its complementary base."""
    return "".join(COMPLEMENT_MAP[base] for base in seq)


def get_reverse_complement(seq):
    """Complement the sequence, then reverse it."""
    return get_complement(seq)[::-1]


def transcribe_to_rna(seq):
    """DNA -> RNA: simply replace every T with U."""
    return seq.replace("T", "U")


def translate_to_protein(rna_seq):
    """
    RNA -> Protein.
    Reads the RNA in groups of 3 letters (codons) and looks up
    each codon in the CODON_TABLE. Stops early if a STOP codon
    ('*') is found.
    """
    protein = ""
    for i in range(0, len(rna_seq) - 2, 3):
        codon = rna_seq[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "?")
        if amino_acid == "*":
            break
        protein += amino_acid
    return protein if protein else "(sequence too short to translate)"


# --------------------------------------------------------------
# STEP 3: BUILD THE FULL REPORT (used by both GUI and save-to-file)
# --------------------------------------------------------------

def build_report(seq):
    seq = clean_sequence(seq)
    counts = count_nucleotides(seq)
    complement = get_complement(seq)
    rev_complement = get_reverse_complement(seq)
    rna = transcribe_to_rna(seq)
    protein = translate_to_protein(rna)

    report = []
    report.append("=" * 60)
    report.append(" DNA SEQUENCE ANALYSIS REPORT")
    report.append("=" * 60)
    report.append(f"Original Sequence   : {seq}")
    report.append(f"Sequence Length     : {len(seq)} bases")
    report.append("-" * 60)
    report.append("NUCLEOTIDE COUNT")
    report.append(f"  A (Adenine)  : {counts['A']}")
    report.append(f"  T (Thymine)  : {counts['T']}")
    report.append(f"  G (Guanine)  : {counts['G']}")
    report.append(f"  C (Cytosine) : {counts['C']}")
    report.append("-" * 60)
    report.append(f"GC Content          : {gc_content(seq)} %")
    report.append(f"AT Content          : {at_content(seq)} %")
    report.append("-" * 60)
    report.append(f"Complement Strand   : {complement}")
    report.append(f"Reverse Complement  : {rev_complement}")
    report.append("-" * 60)
    report.append(f"Transcribed RNA     : {rna}")
    report.append(f"Translated Protein  : {protein}")
    report.append("=" * 60)
    return "\n".join(report)


# --------------------------------------------------------------
# STEP 4: THE GUI (Graphical User Interface)
# --------------------------------------------------------------

class DNAAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Sequence Analyzer")
        self.root.geometry("700x600")
        self.root.configure(bg="#eaf6ec")

        # ---- Title ----
        title = tk.Label(
            root, text="🧬 DNA Sequence Analyzer",
            font=("Arial", 20, "bold"), bg="#eaf6ec", fg="#1b5e20"
        )
        title.pack(pady=15)

        # ---- Input label + entry box ----
        instruction = tk.Label(
            root, text="Enter a DNA sequence (only A, T, G, C):",
            font=("Arial", 12), bg="#eaf6ec"
        )
        instruction.pack()

        self.seq_entry = tk.Entry(root, font=("Consolas", 12), width=60)
        self.seq_entry.pack(pady=8)
        self.seq_entry.insert(0, "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

        # ---- Buttons ----
        button_frame = tk.Frame(root, bg="#eaf6ec")
        button_frame.pack(pady=10)

        analyze_btn = tk.Button(
            button_frame, text="Analyze Sequence", command=self.analyze,
            bg="#2e7d32", fg="white", font=("Arial", 11, "bold"), padx=10
        )
        analyze_btn.grid(row=0, column=0, padx=5)

        clear_btn = tk.Button(
            button_frame, text="Clear", command=self.clear,
            bg="#757575", fg="white", font=("Arial", 11, "bold"), padx=10
        )
        clear_btn.grid(row=0, column=1, padx=5)

        save_btn = tk.Button(
            button_frame, text="Save Report as .txt", command=self.save_report,
            bg="#1565c0", fg="white", font=("Arial", 11, "bold"), padx=10
        )
        save_btn.grid(row=0, column=2, padx=5)

        # ---- Output box (scrollable text area) ----
        self.output_box = scrolledtext.ScrolledText(
            root, width=78, height=25, font=("Consolas", 10)
        )
        self.output_box.pack(padx=15, pady=10)

    def analyze(self):
        raw_seq = self.seq_entry.get()
        seq = clean_sequence(raw_seq)

        if not is_valid_dna(seq):
            messagebox.showerror(
                "Invalid Sequence",
                "Please enter a valid DNA sequence using only the letters A, T, G, C."
            )
            return

        report = build_report(seq)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, report)

    def clear(self):
        self.seq_entry.delete(0, tk.END)
        self.output_box.delete("1.0", tk.END)

    def save_report(self):
        content = self.output_box.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Nothing to Save", "Please analyze a sequence first.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialfile="dna_analysis_report.txt"
        )
        if file_path:
            with open(file_path, "w") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"Report saved successfully to:\n{file_path}")




if __name__ == "__main__":
    root = tk.Tk()
    app = DNAAnalyzerApp(root)
    root.mainloop()
