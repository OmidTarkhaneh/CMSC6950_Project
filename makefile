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

.PHONY	:	clean
