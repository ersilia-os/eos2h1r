# imports
import os
import sys
import numpy as np
from signaturizer3d import CCSpace, Signaturizer
from ersilia_pack_utils.core import write_out, read_smiles

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)

# current file directory
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

DATASETS = [i+j for i in "C" for j in "12345"]

def get_model_path(ds):
    return os.path.join(checkpoints_dir, "{}_split3.pt".format(ds))

def predict(smiles_list):
    # For each space, get 3 signatures
    results = {}
    for ds in DATASETS:
        path = get_model_path(ds)
        signaturizer = Signaturizer(space=ds, local_weights_path= path)
        signatures = signaturizer.infer_from_smiles(smiles_list)
        results[ds]=signatures
    # For each space, store the 3 signatures
    output = [[] for _ in range(len(smiles_list))]
    for ds in DATASETS:
        output[0].extend(results[ds][0])
        output[1].extend(results[ds][1])
        output[2].extend(results[ds][2])
    # to numpy array
    output = np.array(output)
    return output

cols,smiles= read_smiles(input_file)

output = predict(smiles)

header = [f"{ds.lower()}_{r:03d}" for ds in DATASETS for r in range(128)]

write_out(output,header,output_file,np.float32)
