from ruamel.yaml import YAML
yaml = YAML()

metrics_file = 'data/metrics.yml'
publications_file = 'data/publications.yml'
realtimeproducts_file = 'data/realtimeproducts.yml'
collaboration_file = 'data/collaboration.yml'
    
with open(publications_file) as f:
    publications_dict = yaml.load(f)
publications = len(publications_dict['items'])

with open(realtimeproducts_file) as f:
    realtimeproducts_dict = yaml.load(f)
realtimeproducts = len(realtimeproducts_dict['items'])

with open(collaboration_file) as f:
    collaboration_dict = yaml.load(f)
interns = len(collaboration_dict['items'])

with open(metrics_file, 'r+') as f:
    metrics_dict = yaml.load(f)
metrics_dict['counter_item'][0]["number"] = publications
metrics_dict['counter_item'][1]["number"] = realtimeproducts
metrics_dict['counter_item'][2]["number"] = interns
with open(metrics_file, 'w') as f:
    yaml.dump(metrics_dict, f)

