import yaml

# Update the paths in the YAML file to match the new directory structure
with open('dataset/data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Set the paths directly to the respective directories
data['train'] = 'dataset/train/images'
data['val'] = 'dataset/valid/images'
# If you have a test set, uncomment the following line
# data['test'] = 'dataset/test/images'

with open('dataset/data.yaml', 'w') as f:
    yaml.dump(data, f)

# Verify the updated data
print(data)