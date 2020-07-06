"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry 
import inspect
from ml.registry import MLRegistry
from ml.income_classifier.random_forest import RandomForest
from ml.income_classifier.extra_trees import ExtraTrees

try:
    registry = MLRegistry() #Creates ML registry
    rf = RandomForest()
    registry.add_algorithm(endpoint_name="income_classifier", algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Gabriel",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForest))
    et = ExtraTrees()
    registry.add_algorithm(endpoint_name="income_classifier", algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Gabriel",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(ExtraTrees))

except Exception as e:
    print("Exception while loading algorithm to registry,", str(e))