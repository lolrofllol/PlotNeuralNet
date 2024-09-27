@REM python3 test.py 
@REM pdflatex test.tex

@REM python3 test_two.py 
@REM pdflatex test_two.tex

python3 test_three.py 
pdflatex test_three.tex

rm *.aux *.log *.vscodeLog
rm *.tex