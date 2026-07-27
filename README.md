# 🧬 DNA Sequence Analyzer

A simple desktop application built with Python's `tkinter` library that performs common bioinformatics operations on a DNA sequence — validation, nucleotide counting, GC/AT content calculation, complement/reverse complement generation, transcription (DNA → RNA), and translation (RNA → Protein).

This project was built as a **Final Semester Project**.

---

## 📋 Features

- ✅ **Sequence Validation** — Ensures the input contains only valid DNA bases (A, T, G, C)
- 🔢 **Nucleotide Counting** — Counts occurrences of Adenine (A), Thymine (T), Guanine (G), and Cytosine (C)
- 📊 **GC & AT Content** — Calculates the percentage of GC and AT bases in the sequence
- 🔄 **Complement Strand** — Generates the complementary DNA strand
- ↩️ **Reverse Complement** — Generates the reverse of the complementary strand
- 🧪 **Transcription** — Converts DNA sequence into RNA (replaces T with U)
- 🧬 **Translation** — Converts RNA into a Protein sequence using a full codon table
- 💾 **Save Report** — Export the complete analysis report as a `.txt` file
- 🖥️ **Simple GUI** — Easy-to-use graphical interface built entirely with `tkinter`

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required — uses only Python's built-in `tkinter` module

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Save the script as `dna_sequence_analyzer.py`.
3. Run the following command in your terminal:

   ```bash
   python dna_sequence_analyzer.py
   ```

4. The application window will open automatically.

---

## 🧭 How to Use

1. **Enter a DNA sequence** in the input box (only letters A, T, G, C are allowed).
2. Click **"Analyze Sequence"** to generate the full report.
3. Click **"Clear"** to reset the input and output fields.
4. Click **"Save Report as .txt"** to export the analysis report to a text file on your computer.

### Example Input
```
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
```

---

## 📄 Sample Output

```
============================================================
 DNA SEQUENCE ANALYSIS REPORT
============================================================
Original Sequence   : ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
Sequence Length     : 39 bases
------------------------------------------------------------
NUCLEOTIDE COUNT
  A (Adenine)  : 9
  T (Thymine)  : 6
  G (Guanine)  : 15
  C (Cytosine) : 9
------------------------------------------------------------
GC Content          : 61.54 %
AT Content          : 38.46 %
------------------------------------------------------------
Complement Strand   : TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC
Reverse Complement  : CTATCGGGCACCCTTTCAGCGGCCCATTACAATGGCCAT
------------------------------------------------------------
Transcribed RNA     : AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
Translated Protein  : MAIVMGR*
============================================================
```

---

## 🧩 Project Structure & Code Overview

| Function | Purpose |
|---|---|
| `clean_sequence()` | Removes spaces/newlines and converts input to uppercase |
| `is_valid_dna()` | Validates that the sequence only contains A, T, G, C |
| `count_nucleotides()` | Counts each base in the sequence |
| `gc_content()` / `at_content()` | Calculates GC% and AT% |
| `get_complement()` | Returns the complementary strand |
| `get_reverse_complement()` | Returns the reversed complementary strand |
| `transcribe_to_rna()` | Converts DNA to RNA |
| `translate_to_protein()` | Converts RNA codons into a protein sequence using `CODON_TABLE` |
| `build_report()` | Combines all analysis results into one formatted report |
| `DNAAnalyzerApp` | The `tkinter` GUI class that ties everything together |

---

## 📚 Concepts Used (Bioinformatics Background)

- **GC Content**: Percentage of Guanine + Cytosine bases; higher GC content generally means a more thermally stable DNA strand.
- **Complement Strand**: In DNA, A always pairs with T, and G always pairs with C.
- **Reverse Complement**: Represents the opposite strand of the DNA double helix, read in the correct 5'→3' direction.
- **Transcription**: The process of converting a DNA sequence into messenger RNA (mRNA) by replacing Thymine (T) with Uracil (U).
- **Translation**: The process of reading RNA codons (groups of 3 bases) to determine the sequence of amino acids that make up a protein, stopping at a STOP codon (`*`).

---

## ⚠️ Limitations

- Only supports the standard 4 DNA bases (A, T, G, C) — does not handle ambiguous IUPAC codes (e.g., N, R, Y).
- Translation always starts from the first base (no reading frame selection).
- No support for reading sequences directly from FASTA files (manual input only).

---

## 👤 Author / Project Info

This project was developed as a **Final Semester Project** to demonstrate practical understanding of DNA sequence analysis and GUI development in Python.

---

## 📜 License

This project is free to use for academic and educational purposes.
