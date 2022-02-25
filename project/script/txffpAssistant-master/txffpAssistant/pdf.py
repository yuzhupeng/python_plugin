#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/25 14:53
import io
import os
import zipfile

from PyPDF2 import PdfFileWriter, PdfFileReader


class PDFMerger(object):
    
    def __init__(self):
        self._pdf_writer = PdfFileWriter()
    
    def add_pdf(self, stream):
        """
        Args:
            stream: A File object or an object that supports the standard
            read and seek methods similar to a File object. Could also be
            a string representing a path to a PDF file.
        """
        pdf_reader = PdfFileReader(stream)
        for page_num in range(pdf_reader.getNumPages()):
            self._pdf_writer.addPage(pdf_reader.getPage(page_num))
            
    def write(self, stream):
        """
        Args:
            stream: An object to write the file to. The object must support
            the write method and the tell method, similar to a file object.
        """
        self._pdf_writer.write(stream)


def is_pdf(filename):
    """Check the file extension from the filename."""
    if filename.lower().endswith(".pdf"):
        return True
    else:
        return False


def is_zip(filename):
    """Check the file extension from the filename."""
    if filename.lower().endswith(".zip"):
        return True
    else:
        return False

        
def auto_merger(file, merger_dir, base=True, p_name=None):
    merger_ = None
    myzip = zipfile.ZipFile(file)
    filelist = myzip.infolist()
    
    if base:
        if isinstance(file, str):
            basename = os.path.basename(file)
        else:
            basename = os.path.basename(file.name)
        filename = os.path.splitext(basename)[0]
        merger_dir = os.path.join(merger_dir, filename)
        if not os.path.exists(merger_dir):
            os.mkdir(merger_dir)
            
    pdf_counter = 0
    pdf_name = ""
    for zipinfo in filelist:
        io_file = io.BytesIO(myzip.read(zipinfo))
        io_file.name = zipinfo.filename
        
        if is_pdf(io_file.name):
            if merger_ is None:
                merger_ = PDFMerger()
            merger_.add_pdf(io_file)
            pdf_counter += 1
            pdf_name = io_file.name
        if is_zip(io_file.name):
            if io_file.name.endswith("invoice.zip") or io_file.name.endswith("invoice.zip"):
                auto_merger(io_file, merger_dir, False, io_file.name)
            else:
                auto_merger(io_file, merger_dir, False)
            
    if merger_ is not None:
        if p_name is not None:
            basename = os.path.basename(p_name)
        elif pdf_counter == 1:
            basename = os.path.basename(pdf_name)
        else:
            basename = os.path.basename(myzip.filename)
        filename = os.path.splitext(basename)[0] + ".pdf"
        filepath = os.path.join(merger_dir, filename)
        with open(filepath, "wb") as f:
            merger_.write(f)
