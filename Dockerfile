FROM python:3
COPY calculator.py .
COPY calculatorTests.py .
CMD ["python", "./calculatorTests.py"]