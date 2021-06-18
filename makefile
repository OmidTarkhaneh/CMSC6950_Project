Report.pdf: Report.tex createdataset plot_stemperature.png plot_atomospheric.png plot_emission.png
	latexmk -pdf

createdataset: LoadData.py
	python3 LoadData.py


plot_stemperature.png:	Stemperature.py totalrcp_dataset.csv
	python3 Stemperature.py

plot_atomospheric.png: Atomospheric.py totalrcp_dataset.csv
	python3 Atomospheric.py

plot_emission.png: Emission.py rawrcps_dataset.csv
	python3 Emission.py

clean:
	rm *.csv
	rm *.png

.PHONY : clean

deepclean:
	rm *.png
	latexmk -c
	rm *.pdf
	rm *.csv
	rm Report.aux
	rm Report.log
	rm Report.out
	rm Report.bbl

.PHONY : deepclean

