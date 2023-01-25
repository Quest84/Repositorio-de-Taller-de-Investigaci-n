calibrar:
	> Medidas.csv
	seq 3 | xargs -Iz python3 merge.py && python3 count.py
	python3 Graficas.py

test:
	> Test.csv
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 merge.py && python3 medir.py
	python3 Promedio_Test.py
	python3 Graficas_Test.py

medir:
	python3 merge.py && python3 count.py
