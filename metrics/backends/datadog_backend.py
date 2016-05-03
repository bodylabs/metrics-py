import time

class Datadog(object):

    def __init__(self, api_key, app_key=None, **options):
        import datadog

        datadog.initialize(api_key=api_key, app_key=app_key, **options)

        self.client = datadog.api

    def send(self, name, value, metrics_type, tags, timestamp):

        if tags is not None:
            transformed_tags = ['%s:%s' % (k, v) for k, v in tags.iteritems()]
        else:
            transformed_tags = []

        # transform into timestamp and value tuple for datadog
        if timestamp is None:
            # use current timestamp
            timestamp = int(time.time())

        self.client.Metric.send(
            metric=name,
            points=(timestamp, value),
            tags=transformed_tags,
            type=metrics_type)
