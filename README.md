# Numerical methods

This project implements  algorithms for Newtons method, Lagrange interpolation and Runge-Kutta order 4. 

Furthermore we derivate quadratic convergence for Newtons method, find bounding errors and compare several methods and their computational tradeoffs.


## Installation
Clone the repository and install in editable mode:

```bash
git clone https://github.com/mch-sg/numerical_methods.git
cd pr
pip install -e .
```

This installs the `numerical_methods` package along with its dependencies.


## Project Structure
```
numerical-methods/
├── README.md
├── pyproject.toml
├── requirements.txt
├── numerical_methods/
│   ├── __init__.py
│   ├── newton.py           
│   ├── lagrange.py      
│   ├── rk4.py           
│   └── utils.py  
├── tests/
│   └── test_numerical_methods.py
├── notebooks/
│   └── convergence_analysis.ipynb  
├── data/                      
```


## License

[MIT](https://choosealicense.com/licenses/mit/)