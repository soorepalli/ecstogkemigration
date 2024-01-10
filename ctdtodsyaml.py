import yaml
import json

def convert_task_definition_to_kubernetes(task_definition_json):
    with open(task_definition_json, 'r') as file:
        task_definition = json.load(file)

    deployment_manifest = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': task_definition['family'],  # Provide a suitable name
            'labels': {
                'app': task_definition['family']  # Adjust labels as needed
            }
        },
        'spec': {
            'replicas': task_definition.get('desiredCount', 1),
            'selector': {
                'matchLabels': {
                    'app': task_definition['family']  # Match the labels from metadata
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': task_definition['family']  # Same labels as above
                    }
                },
                'spec': {
                    # Define containers based on ECS container definitions
                    'containers': [
                        # Sample container, adjust as per ECS containerDefinitions
                        {
                            'name': 'example-container',
                            'image': 'nginx:latest',  # Use ECS container image
                            # Adjust resources and other configurations accordingly
                            'resources': {
                                'requests': {
                                    'cpu': '100m',
                                    'memory': '128Mi'
                                },
                                'limits': {
                                    'cpu': '250m',
                                    'memory': '256Mi'
                                }
                            }
                        }
                    ]
                }
            }
        }
    }

    service_manifest = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': 'example-service',  # Provide a suitable name
            'labels': {
                'app': 'example-app'  # Same label as used in Deployment
            }
        },
        'spec': {
            'selector': {
                'app': 'example-app'  # Same label as used in Deployment
            },
            'ports': [
                # Define ports as required by your application
                {
                    'protocol': 'TCP',
                    'port': 80,
                    'targetPort': 80
                }
            ],
            'type': 'LoadBalancer'  # Adjust service type as needed
        }
    }

    # Writing Deployment and Service YAML files
    with open('deployment2.yaml', 'w') as deployment_file:
        yaml.dump(deployment_manifest, deployment_file, default_flow_style=False)

    with open('service2.yaml', 'w') as service_file:
        yaml.dump(service_manifest, service_file, default_flow_style=False)

    print("Conversion completed. Deployment and Service YAML files generated.")

# Example usage:
    # Update the TaskDefiniton file
input_task_definition = 'TaskDefinition.json'
convert_task_definition_to_kubernetes(input_task_definition)
