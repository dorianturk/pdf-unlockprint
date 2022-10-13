# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:13:16 2022

@author: Doria
"""

from PyPDF2 import PdfMerger

merger = PdfMerger()

for i in range(1,4,1):
    print(i)

    for pdf in [f"file{str(i)}.pdf"]:
        merger.append(pdf)
    
    merger.write(f"file_unlocked{str(i)}.pdf")
    merger.close()
    merger = PdfMerger()
    
merger.close()