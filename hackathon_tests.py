import unittest
import resource
import time
import pandas as pd

from connected_components import connected_components
from resource_monitor import ResourceManager


class TestConnectedComponents(unittest.TestCase):
    def test_connected_components(self):

        mythread = ResourceManager(connected_components, 'hackathon_dataset_25.csv')
        mythread.start()

        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        max_memory = 0
        memory_usage_refresh = .005  # Seconds

        while (1):
            time.sleep(memory_usage_refresh)
            delta_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem
            if delta_mem > max_memory:
                max_memory = delta_mem
                if max_memory > 104857600:
                    raise MemoryError('Exceeded max memory')

            # Check to see if the library call is complete
            if mythread.isShutdown():
                break;

        # Read output.csv
        data = pd.read_csv('output.csv')
        # Expected number of unique cluster_ids
        self.assertEqual(len(data.cluster_id.value_counts()), 20316767)
