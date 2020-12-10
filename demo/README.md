# Directory Content - Demo

This directory contains the final datasets processed by Spark that are used for visualization and analysis and a notebook for demo purpose.

### the Datasets

`case_final.csv`: 

- the number of new confirmed cases each month by states

`flight_result.csv`: (no header)

- Month|Airport|City|State|Country|Percentage

- the percentage of flights from&to the airport compared to the baseline period (Jan&Feb 2020)

`gz_2010_us_040_00_5m_new.json`:

- source: https://eric.clst.org/tech/usgeojson/
- a JSON file with data about the geo data for the U.S. states boundaries

###  the Notebook

the notebook `demo-notebook.ipynb` contains codes for the final data preprocessing and visualization.

We used Bokeh to build a reactive plot showcasing the trends of flight traffic and the growth of COVID cases. Note that a static plot can be shown by calling the `show()` function, but the plot will not be displayed in the notebook. Instead, a window will pop up with the static plot. To have a fully functioned plot with the reactive components, we will have to run `python -m bokeh serve --show demo-notebook.ipynb` in the terminal with all the dependencies installed. Then a localhost window will be opened in our browser with all the reactive functions like slider, selectors, and hovertools.

![image-20201211054059765](https://github.com/carolcheng98/spark-bokeh-covid-airport-analysis/blob/main/demo/spark-bokeh-covid-airport-analysis/demo/bokeh-plot-demo.png)