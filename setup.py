from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Sloth>=2.0.1"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@0524f75a5e72e7db6001ed25eca35a20a46c9d18#egg=Sloth-2.0.1"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
