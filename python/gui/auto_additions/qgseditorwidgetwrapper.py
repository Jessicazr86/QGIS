# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorwidgetwrapper.h
try:
    QgsEditorWidgetWrapper.__attribute_docs__ = {'valueChanged': 'Emit this signal, whenever the value changed.\n\n:param value: The new value\n\n.. deprecated:: QGIS 3.10\n   use valuesChanged signal instead\n', 'valuesChanged': 'Emit this signal, whenever the value changed.\nIt will also return the values for the additional fields handled by the widget\n\n:param value: The new value\n:param additionalFieldValues: A map of additional field names with their corresponding values\n\n.. versionadded:: 3.10\n', 'constraintStatusChanged': 'Emit this signal when the constraint status changed.\nconstraintStatusChanged\n\n:param constraint: represented as a string\n:param desc: is the constraint description\n:param err: the error represented as a string. Empty if none.\n:param status:\n', 'constraintResultVisibleChanged': 'Emit this signal when the constraint result visibility changed.\n'}
except NameError:
    pass
QgsEditorWidgetWrapper.fromWidget = staticmethod(QgsEditorWidgetWrapper.fromWidget)
QgsEditorWidgetWrapper.isInTable = staticmethod(QgsEditorWidgetWrapper.isInTable)
try:
    QgsEditorWidgetWrapper.__group__ = ['editorwidgets', 'core']
except NameError:
    pass
