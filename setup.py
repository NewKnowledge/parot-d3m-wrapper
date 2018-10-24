from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Parrot==1.0.0"],
    dependency_links=[
        # must change 
        "git+https://github.com/NewKnowledge/parrot-d3m-wrapper@236044f795948a74f214f391094d2e625bd0032f#egg=Parrot-1.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
