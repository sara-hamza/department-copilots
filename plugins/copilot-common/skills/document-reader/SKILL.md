---
name: document-reader
description: This skill should be used when an employee drops in or names a PDF, Word document (.docx), text export, email saved as a file, or a design/standards document and wants it analysed, summarised, reviewed or compared. It explains how to extract the text locally, keep page/section references, and handle scanned or image-only PDFs.
version: 1.0.0
---

# Document Reader

Read employee-supplied documents locally and keep references so findings can be traced back.

## Reading order

1. **PDF**: use the Read tool with the `pages` parameter in chunks of up to 20 pages. For large PDFs, first read pages 1-5 to find the table of contents, then jump to relevant sections. Note the page number beside every finding.
2. **DOCX**: extract text with a local command, no network:
   ```bash
   python3 -c "import zipfile,re,sys;x=zipfile.ZipFile(sys.argv[1]).read('word/document.xml').decode();print(re.sub(r'<[^>]+>',' ',x.replace('</w:p>','\n')))" "FILE.docx"
   ```
   Or `pandoc FILE.docx -t plain` if pandoc is installed.
3. **Text / Markdown / email exports**: Read directly.
4. **Scanned or image-only PDFs**: the Read tool shows the page as an image. Describe what is visible and say explicitly that the text was read visually, not extracted. Flag unreadable regions.

## While reading

- Build a short structure map first (headings, sheets, drawing numbers) before answering questions. This prevents missing a section.
- Quote sparingly: the finding and where it is (`p.12, §4.3`, `Sheet 4, note 7`).
- Separate what the document **says** from what the employee **asked** from what Claude **infers**.
- For comparisons (drawing vs BOM, contract vs policy, invoice vs PO), build a two-column list of items present in one and absent or different in the other.

## Output conventions

```
DOCUMENT MAP
<section list with page refs>

FINDINGS
<numbered, each with a page/section ref>

MISSING INFORMATION
<what the document should contain but does not>
```

## Boundaries

Never fetch documents from SharePoint, email or the web. If a referenced standard or attachment is not supplied, list it under MISSING INFORMATION and ask the employee to drop it in.
