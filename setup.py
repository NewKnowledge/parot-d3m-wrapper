from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.1',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Sloth>=2.0.2"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@7a382ed33a745d6a1205c0bcfe31262332b81e1eegg=Sloth-2.0.2"

    ],
    entry_points = {
        'd3m.primitives': [
            'distil.parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
