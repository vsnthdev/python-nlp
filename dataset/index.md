Refer to the docs to know more 👇
[GitHub Repo](https://github.com/snipsco/snips-nlu)
[Docs](https://snips-nlu.readthedocs.io/en/latest)

First you need to generate the dataset from all the YAML files in this directory. To do that run 👇

```bash
snips-nlu generate-dataset en .\dataset\greet.yml > ./dataset/dataset.json
```

Then we need to train the AI with the generated dataset using the following command 👇

```bash
snips-nlu train ./dataset/dataset.json ./engine
```