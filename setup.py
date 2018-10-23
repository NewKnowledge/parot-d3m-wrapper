from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Parot==1.0.0"],
    dependency_links=[
        # must change 
        "git+https://github.com/NewKnowledge/sloth@d38b8892fbefb4425d211d2cd858cfad91a2113e#egg=Sloth-2.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
