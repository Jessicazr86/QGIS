# The following has been generated automatically from src/core/symbology/qgsrulebasedrenderer.h
try:
    QgsRuleBasedRenderer.__attribute_docs__ = {'ftr': 'Feature to render', 'symbol': 'Symbol to render feature with (not owned by this object).', 'jobs': 'List of jobs to render, owned by this object.'}
except NameError:
    pass
QgsRuleBasedRenderer.create = staticmethod(QgsRuleBasedRenderer.create)
QgsRuleBasedRenderer.createFromSld = staticmethod(QgsRuleBasedRenderer.createFromSld)
QgsRuleBasedRenderer.refineRuleCategories = staticmethod(QgsRuleBasedRenderer.refineRuleCategories)
QgsRuleBasedRenderer.refineRuleRanges = staticmethod(QgsRuleBasedRenderer.refineRuleRanges)
QgsRuleBasedRenderer.refineRuleScales = staticmethod(QgsRuleBasedRenderer.refineRuleScales)
QgsRuleBasedRenderer.convertFromRenderer = staticmethod(QgsRuleBasedRenderer.convertFromRenderer)
QgsRuleBasedRenderer.convertToDataDefinedSymbology = staticmethod(QgsRuleBasedRenderer.convertToDataDefinedSymbology)
QgsRuleBasedRenderer.Rule.createFromSld = staticmethod(QgsRuleBasedRenderer.Rule.createFromSld)
QgsRuleBasedRenderer.Rule.create = staticmethod(QgsRuleBasedRenderer.Rule.create)
QgsRuleBasedRenderer.FeatureToRender.__doc__ = """Feature for rendering by a QgsRuleBasedRenderer. Contains a QgsFeature and some flags."""
QgsRuleBasedRenderer.RenderJob.__doc__ = """A QgsRuleBasedRenderer rendering job, consisting of a feature to be rendered with a particular symbol."""
QgsRuleBasedRenderer.RenderLevel.__doc__ = """Render level: a list of jobs to be drawn at particular level for a QgsRuleBasedRenderer."""
try:
    QgsRuleBasedRenderer.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsRuleBasedRenderer.FeatureToRender.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsRuleBasedRenderer.RenderJob.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsRuleBasedRenderer.RenderLevel.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsRuleBasedRenderer.Rule.__group__ = ['symbology']
except NameError:
    pass
