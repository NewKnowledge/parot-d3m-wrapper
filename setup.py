from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Sloth==2.0.0"],
    dependency_links=[
        # must change 
        "git+https://github.com/NewKnowledge/sloth@22185ca7bea28b901a14b31edccd1a147734779f#egg=Sloth-2.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
