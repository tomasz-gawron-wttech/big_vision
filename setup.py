install_requires_core = [
    "absl-py>=1.0.0",  
    "numpy>=1.12",
    "jax>=0.4.3",
    "jaxlib>=0.4.3",
    "flax>=0.4.0",
    "ml-collections>=0.1.1",
    "tensorflow>=2.7",
    "tensorflow-addons>=0.15.0",
    "immutabledict>=2.2.1",
    "clu>=0.0.6",
    "tensorflow-datasets",
    "optax @ git+https://github.com/deepmind/optax.git@master",   
    "flaxformer @ git+https://github.com/google/flaxformer",
    "panopticapi @ git+https://github.com/akolesnikoff/panopticapi.git@mute",
    "overrides",
    "tfds-nightly",
    "tensorflow-addons",
    "tensorflow-text",
    "tensorflow-gan",
    "einops"
]


setup(
    name="big_vision",
    version="0.0.1",
    description=("Google big_vision library"),
    author="Scenic Authors",
    author_email="no-reply@google.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tomasz-gawron-wttech/big_vision/",
    license="Apache 2.0",
    packages=['biv_vision'],
    include_package_data=True,
    install_requires=install_requires_core
)
