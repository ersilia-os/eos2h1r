# Chemical Checker Signaturizer 3D C1-5

Captures the network level of the Chemical Checker, five C spaces positioning a compound by the biological roles, pathways, processes and interactions its targets participate in. Building on a systematic analysis of stereoisomerism across more than a million compounds, where about 40% of isomer pairs showed distinct bioactivity, the descriptors were learned from three-dimensional molecular representations. Because the networks infer signatures for compounds never assayed, output should be read as a prediction of biological context.

This model was incorporated on 2025-06-25.Last packaged on 2025-12-30.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2h1r`
- **Slug:** `cc-signaturizer-3d-c`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Bioactivity profile`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `640`
- **Output Consistency:** `Fixed`
- **Interpretation:** 640 stereochemistry-aware bioactivity features spanning the five network spaces of the Chemical Checker.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| c1_000 | float |  | Dimension 0 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_001 | float |  | Dimension 1 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_002 | float |  | Dimension 2 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_003 | float |  | Dimension 3 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_004 | float |  | Dimension 4 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_005 | float |  | Dimension 5 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_006 | float |  | Dimension 6 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_007 | float |  | Dimension 7 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_008 | float |  | Dimension 8 for Signaturizer3D dataset networks (C) small molecule roles (C1) |
| c1_009 | float |  | Dimension 9 for Signaturizer3D dataset networks (C) small molecule roles (C1) |

_10 of 640 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2h1r](https://hub.docker.com/r/ersiliaos/eos2h1r)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2h1r.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2h1r.zip)

### Resource Consumption
- **Model Size (Mb):** `2728`
- **Environment Size (Mb):** `1302`
- **Image Size (Mb):** `9468.77`

**Computational Performance (seconds):**
- 10 inputs: `32.45`
- 100 inputs: `101.77`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://gitlabsbnb.irbbarcelona.org/packages/signaturizer3d](https://gitlabsbnb.irbbarcelona.org/packages/signaturizer3d)
- **Publication**: [https://doi.org/10.1186/s13321-024-00867-4](https://doi.org/10.1186/s13321-024-00867-4)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2h1r
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2h1r
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
