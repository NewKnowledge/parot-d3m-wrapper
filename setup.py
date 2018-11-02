from distutils.core import setup

setup(name='ParrotD3MWrapper',
    version='1.0.1',
    description='A thin wrapper for interacting with New Knowledge time series prediction tool Parrot',
    packages=['ParrotD3MWrapper'],
    install_requires=["typing",
        "Sloth>=2.0.2"],
    dependency_links=[
<<<<<<< HEAD
        "git+https://github.com/NewKnowledge/sloth@5ce7132480cdbc7565f9f6c1086f8d10371e94f0#egg=Sloth-2.0.2"
=======
        "git+https://github.com/NewKnowledge/sloth@d48df2844b31f0e08e296b9ba795eab7d8e487fb#egg=Sloth-2.0.1"
>>>>>>> 904ee8c97ebbacb8e0217bc501220fe6abbf58d8
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.parrot = ParrotD3MWrapper:Parrot'
        ],
    },
)
