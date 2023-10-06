Dataset **Paddy Rice Imagery** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/K/fF/DEuemm4NoZ1t3cQRYWJdNvTxnGrhu2eBCOGHfWX9CEAu5fVsH3i3ZecUxGKAymWzWFNUwxFcqZbvLkoczB2ihWIjxLvExOvTyK99R7hYqjGPdx8DLBKa714qtUCk.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Paddy Rice Imagery', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [128.zip](https://zenodo.org/record/4444741/files/128.zip?download=1)
- [256.zip](https://zenodo.org/record/4444741/files/256.zip?download=1)
- [512.zip](https://zenodo.org/record/4444741/files/512.zip?download=1)
- [basic dataset.zip](https://zenodo.org/record/4444741/files/basic%20dataset.zip?download=1)
- [label_map.txt](https://zenodo.org/record/4444741/files/label_map.txt?download=1)
- [README.txt](https://zenodo.org/record/4444741/files/README.txt?download=1)
- [refined dataset.zip](https://zenodo.org/record/4444741/files/refined%20dataset.zip?download=1)
- [splitting.ipynb](https://zenodo.org/record/4444741/files/splitting.ipynb?download=1)
