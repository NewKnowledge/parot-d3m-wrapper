from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.3',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Sloth==2.0.3"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@82a1e08049531270256f38ca838e6cc7d1119223#egg=Sloth-2.0.3"
    ],
    entry_points = {
        'd3m.primitives': [
            'time_series_forecasting.arima.Parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
