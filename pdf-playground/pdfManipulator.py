from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import os

# CURRENT DIRECTORY
pdf_files_path = os.path.join(os.getcwd(), 'pdf_files')
pdf_files = os.listdir(pdf_files_path)


# ROTATE PDF
def rotate_pages(file, filename):
    page = file.getPage(0).rotateClockwise(90)
    writer = PdfFileWriter()
    writer.addPage(page)
    with open(os.path.join(os.getcwd(), 'pdf_files', filename), "wb") as new_file:
        writer.write(new_file)


# ACCESS ALL PDFs & ROTATE FIRST PDF FILE
def open_pdf(files):
    for pdf in files:
        try:
            # ENSURE FILES ARE PDFs
            name, extension = os.path.splitext(pdf)
            if extension == ".pdf":
                # OPEN PDF FILE
                file = PdfFileReader(os.path.join(os.getcwd(), 'pdf_files', pdf))

                # CREATE & ROTATE  FIRST PDFs
                if pdf_files.index(pdf) == 0:
                    rotate_pages(file, "tilt.pdf")
            else:
                print(f"{pdf}'s extension is NOT '.pdf', {name} has a '.ext': {extension}")
        except Exception as err:
            print(f"Error occurred in open_pdf {err}")


# MERGE PDF
def merge_pdf(files, filename):
    try:
        merger = PdfFileMerger()
        for pdf in files:
            merger.append(os.path.join(os.getcwd(), 'pdf_files', pdf))
        with open(os.path.join(os.getcwd(), 'merged_pdf_files', filename), "wb") as new_file:
            merger.write(new_file)
    except Exception as err:
        print(f"Error occurred in merge_pdf {err}")


open_pdf(pdf_files)
merge_pdf(pdf_files, "merged_pdf.pdf")
