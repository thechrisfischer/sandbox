import sys
device = find('prod-memcache01')
template_name = '/Server/Linux/Memcached'
template = device.getRRDTemplateByName(template_name)
source_DS = 'memcached-11211'
for ds in template.getRRDDataSources():
    if ds.id == source_DS:
        source_DS = ds
        all_datapoints = ds.getRRDDataPoints()
        break
else:
    print "Unable to find DS %s in template %s" % (source_DS, template_name)
    sys.exit(1)

available_DS_types = dict(template.getDataSourceOptions())
dsOptionString = available_DS_types[ source_DS.sourcetype ]

new_DS = [ 'memcached-11212', 'memcached-11213','memcached-11214','memcached-11215']
for ds_name in new_DS:
    DS = template.manage_addRRDDataSource(ds_name, dsOptionString)
    # Copy data source information -- specific to template type
    DS.enabled = source_DS.enabled
    DS.usessh = source_DS.usessh
    DS.component = source_DS.component
    DS.eventClass = source_DS.eventClass
    DS.eventKey = source_DS.eventKey
    DS.severity = source_DS.severity
    DS.cycletime = source_DS.cycletime
    DS.parser = source_DS.parser
    DS.commandTemplate = source_DS.commandTemplate
    #
    # Copy datapoint information over
    for dp in all_datapoints:
        new_dp = DS.manage_addRRDDataPoint(dp.id)
        new_dp.rrdtype = dp.rrdtype
        new_dp.rdmin=dp.rrdmin
        new_dp.rdmax=dp.rrdmax
        new_dp.reateCmd=dp.createCmd

#commit()

