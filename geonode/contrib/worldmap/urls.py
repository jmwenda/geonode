from django.conf.urls import patterns, url

urlpatterns = patterns('geonode.contrib.worldmap.views',
                       url(r'^addgeonodelayer/(?P<layertitle>[^/]*)$', 'addLayerJSON', name="addLayerJSON"),
                       url(r'^layerstats/?$', 'ajax_increment_layer_stats', name="ajax_increment_layer_stats"),
                       url(r'^new$', 'new_map', name="new_map"),
                       url(r'^create_pg_layer', 'create_pg_layer', name='create_pg_layer'),
                       url(r'^ajax_lookup_email$', 'ajax_lookup_email', name='ajax_lookup_email'),
                       )
