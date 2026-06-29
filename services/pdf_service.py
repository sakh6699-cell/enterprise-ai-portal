# ==========================================================
# PDF_SERVICE.PY
#
# Definition:
#
# Handles PDF storage operations.
#
# Why?
#
# Uploaded files must be saved
# before processing.
#
# PyPDFLoader expects a file path.
#
#
# Interview:
#
# Why save PDF locally?
#
# Answer:
#
# PyPDFLoader works with files
# stored on disk.
#
# Therefore uploaded PDFs
# are first saved in uploads folder.
#
# ==========================================================
# ==========================================================
# IMPORTS
# ==========================================================
import os
# ==========================================================
# UPLOAD DIRECTORY
# ==========================================================
# Folder where PDFs will be stored
UPLOAD_FOLDER = "uploads"
# Creates uploads folder automatically
#
# exist_ok=True prevents errors
# if folder already exists
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)
# ==========================================================
# SAVE PDF
# ==========================================================
# Definition:
#
# Saves uploaded PDF
# into uploads folder.
#
#
# Interview:
#
# Why save_pdf()?
#
# PyPDFLoader needs
# a local file path.
#
#
# Flow:
#
# User Upload
#
# ↓
#
# Streamlit
#
# ↓
#
# FastAPI
#
# ↓
#
# save_pdf()
#
# ↓
#
# uploads/
#
# ↓
#
# resume.pdf
#
#
# Example:
#
# uploads/resume.pdf
#
#
# Returns:
#
# path of saved PDF
def save_pdf(file):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )
    # Write PDF bytes
    with open(
            file_path,
            "wb"
    ) as f:
        f.write(
            file.file.read()
        )
    return file_path
# ==========================================================
# TESTING
# ==========================================================
# Upload PDF
#
# Verify:
#
# uploads/
#
# contains PDF file
#
# Example:
#
# uploads/
#
# └── resume.pdf
#
#
# Interview:
#
# How did you test save_pdf()?
#
# Answer:
#
# Uploaded a PDF through Streamlit
#
# and checked uploads folder.
#
# ==========================================================