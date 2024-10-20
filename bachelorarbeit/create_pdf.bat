@REM python3 test.py 
@REM pdflatex test.tex

@REM python3 test_two.py 
@REM pdflatex test_two.tex

@REM python3 test_three.py 
@REM pdflatex test_three.tex

python3 arch_one.py
pdflatex arch_one.tex

python3 arch_two.py
pdflatex arch_two.tex

rm *.aux *.log *.vscodeLog
rm *.tex