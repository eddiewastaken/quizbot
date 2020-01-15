
# Quizbot

A little program I wrote in Python a while ago, to dip my toe into Google's Developer platform and OCR using Tesseract. The code is very blinkered, written as a PoC only. It assumes you have a hypothetic mobile device mirrored to your desktop, and you have a hypothetic **highly** popular mobile-based live quiz game within this mirrored window. The question and (hypothetically) three multiple choice answers will be extracted, converted to greyscale and cleaned up using Python Imaging Library. The question will be searched via Google's API, the results concatenated and the multiple choice answers compared to this result. The more times each answer appears in these results, the higher the 'score' of that answer. This generally gives a solid indication of the answer, which will, on most modern machines, be returned within a hypothetical time limit of, let's say, 10 seconds.

**Note:** This program is for educational purposes only. I accept no liability for use of, or gain from, this program if for anything other than a programming excercise/educational purpose.
