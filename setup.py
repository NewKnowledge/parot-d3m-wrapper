from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Parrot==1.0.0"],
    dependency_links=[
        # must change 
        "git+https://github.com/NewKnowledge/parrot-d3m-wrapper@abff3b4c6281791ef0fa7319372ae16cc2e198b0#egg=Parrot-1.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
